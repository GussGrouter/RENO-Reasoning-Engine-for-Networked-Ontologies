#!/usr/bin/env python3
"""Validate processed manifests and chunk chains under processed/.

Scope and rules follow AGENTS.md:

- inspects processed/<source-id>/manifest.json and processed/<source-id>/chunks/*.json
- verifies required chunk fields (chunk_id, prev_chunk_id, next_chunk_id,
  content_hash, token_estimate, processed_id, raw_id, source_id, page_start,
  page_end, title, review_status, text)
- verifies that chunk text is non-empty, content_hash equals SHA-256 of that
  exact text, and token_estimate is a positive integer not exceeding 2000
  (AGENTS.md hard max)
- verifies the prev/next chain has no gaps and no loops:
  - exactly one chunk has prev_chunk_id == null (head)
  - exactly one chunk has next_chunk_id == null (tail)
  - every other chunk's prev_chunk_id points to an existing chunk whose
    next_chunk_id points back to it, and similarly for next_chunk_id
  - all chunks are reachable from the head in a single linear walk
- verifies manifest.slices (multi-slice support):
  - each slice declares slice_id, page_range, section_range, parse_path,
    chunk_ids, chunk_count, page_start, page_end, parser, parser_version,
    parser_command
  - slice_ids are unique within the manifest
  - every slice chunk_id references a real chunk file
  - chunk_ids across slices partition the source-level chain in chain order
    (no overlap; no chunk is missing from the slice partition)
  - slice.chunk_count == len(slice.chunk_ids)
  - slice.page_start matches the first chunk's page_start; slice.page_end
    matches the last chunk's page_end
  - top-level manifest.chunk_count == sum(slice.chunk_count)

Exits 0 if no processed sources exist yet (empty active tree), or if every
processed source passes. Exits 1 on any explicit violation. Prints a one-line
summary on every run.

Uses Python stdlib only.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

TOKEN_HARD_MAX = 2000

REPO_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_ROOT = REPO_ROOT / "processed"

REQUIRED_CHUNK_FIELDS = (
    "chunk_id",
    "processed_id",
    "raw_id",
    "source_id",
    "title",
    "page_start",
    "page_end",
    "token_estimate",
    "prev_chunk_id",
    "next_chunk_id",
    "content_hash",
    "review_status",
    "text",
)

REQUIRED_MANIFEST_FIELDS = (
    "processed_id",
    "raw_id",
    "parser",
    "parser_version",
    "parser_command",
    "source_hash",
    "page_range",
    "section_range",
    "extraction_warnings",
    "chunk_count",
    "generated_files",
    "slices",
)

REQUIRED_SLICE_FIELDS = (
    "slice_id",
    "page_range",
    "section_range",
    "parse_path",
    "chunk_ids",
    "chunk_count",
    "page_start",
    "page_end",
    "parser",
    "parser_version",
    "parser_command",
)


def list_source_dirs(root: Path) -> List[Path]:
    if not root.exists():
        return []
    out: List[Path] = []
    for entry in sorted(root.iterdir()):
        if entry.is_dir() and not entry.name.startswith("."):
            out.append(entry)
    return out


def load_json(path: Path) -> Tuple[Any, List[str]]:
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh), []
    except FileNotFoundError:
        return None, [f"missing file: {path}"]
    except json.JSONDecodeError as exc:
        return None, [f"invalid JSON in {path}: {exc}"]
    except OSError as exc:
        return None, [f"could not read {path}: {exc}"]


def validate_manifest(manifest: Any, source_dir: Path) -> List[str]:
    errors: List[str] = []
    if not isinstance(manifest, dict):
        return [f"{source_dir.name}/manifest.json: not a JSON object"]
    for key in REQUIRED_MANIFEST_FIELDS:
        if key not in manifest:
            errors.append(
                f"{source_dir.name}/manifest.json: missing field '{key}'"
            )
    return errors


def validate_chunk_record(record: Any, label: str) -> List[str]:
    errors: List[str] = []
    if not isinstance(record, dict):
        return [f"{label}: not a JSON object"]
    for key in REQUIRED_CHUNK_FIELDS:
        if key not in record:
            errors.append(f"{label}: missing field '{key}'")
            continue
        if key in {"chunk_id", "content_hash"} and not record[key]:
            errors.append(f"{label}: field '{key}' must be non-empty")

    if "text" in record:
        text = record["text"]
        if not isinstance(text, str) or not text:
            errors.append(f"{label}: field 'text' must be a non-empty string")
        else:
            if "content_hash" in record and isinstance(record["content_hash"], str):
                expected = hashlib.sha256(text.encode("utf-8")).hexdigest()
                if record["content_hash"] != expected:
                    errors.append(
                        f"{label}: content_hash does not match SHA-256(text) "
                        f"(expected {expected[:16]}..., "
                        f"got {record['content_hash'][:16]}...)"
                    )

    if "token_estimate" in record:
        te = record["token_estimate"]
        if not isinstance(te, int) or isinstance(te, bool):
            errors.append(
                f"{label}: token_estimate must be an integer"
            )
        elif te <= 0:
            errors.append(
                f"{label}: token_estimate must be positive (got {te})"
            )
        elif te > TOKEN_HARD_MAX:
            errors.append(
                f"{label}: token_estimate {te} exceeds hard max "
                f"{TOKEN_HARD_MAX}"
            )
    return errors


def chain_order(
    chunks_by_id: Dict[str, Dict[str, Any]],
) -> List[str] | None:
    """Return chunk_ids in chain order starting from head, or None if not walkable."""
    if not chunks_by_id:
        return []
    heads = [c for c in chunks_by_id.values() if c.get("prev_chunk_id") is None]
    if len(heads) != 1:
        return None
    order: List[str] = []
    seen: set = set()
    cursor: Dict[str, Any] | None = heads[0]
    while cursor is not None:
        cid = cursor.get("chunk_id")
        if cid in seen or cid is None:
            return None
        seen.add(cid)
        order.append(cid)
        next_id = cursor.get("next_chunk_id")
        cursor = chunks_by_id.get(next_id) if next_id is not None else None
    if len(order) != len(chunks_by_id):
        return None
    return order


def validate_slices(
    manifest: Dict[str, Any],
    chunks_by_id: Dict[str, Dict[str, Any]],
    label: str,
) -> List[str]:
    """Validate manifest.slices structure against the chunk set and chain order."""
    errors: List[str] = []
    slices = manifest.get("slices")
    if not isinstance(slices, list) or not slices:
        errors.append(f"{label}/manifest.json: slices must be a non-empty array")
        return errors

    order = chain_order(chunks_by_id)

    seen_slice_ids: set = set()
    seen_chunk_ids: set = set()
    chain_walk: List[str] = []
    for idx, slice_rec in enumerate(slices):
        slice_label = f"{label}/manifest.json: slices[{idx}]"
        if not isinstance(slice_rec, dict):
            errors.append(f"{slice_label}: not a JSON object")
            continue

        for key in REQUIRED_SLICE_FIELDS:
            if key not in slice_rec:
                errors.append(f"{slice_label}: missing field '{key}'")
        if any(k not in slice_rec for k in REQUIRED_SLICE_FIELDS):
            continue

        sid = slice_rec["slice_id"]
        if not isinstance(sid, str) or not sid:
            errors.append(f"{slice_label}: slice_id must be a non-empty string")
        elif sid in seen_slice_ids:
            errors.append(f"{slice_label}: duplicate slice_id '{sid}'")
        else:
            seen_slice_ids.add(sid)

        chunk_ids = slice_rec["chunk_ids"]
        if not isinstance(chunk_ids, list) or not chunk_ids:
            errors.append(f"{slice_label}: chunk_ids must be a non-empty array")
            continue

        for cid in chunk_ids:
            if not isinstance(cid, str) or not cid:
                errors.append(f"{slice_label}: chunk_ids contains non-string entry")
                continue
            if cid not in chunks_by_id:
                errors.append(
                    f"{slice_label}: chunk_id '{cid}' is not a real chunk file"
                )
                continue
            if cid in seen_chunk_ids:
                errors.append(
                    f"{slice_label}: chunk_id '{cid}' already appears in an "
                    f"earlier slice; chunk_ids must partition the source chain"
                )
                continue
            seen_chunk_ids.add(cid)
            chain_walk.append(cid)

        cc = slice_rec["chunk_count"]
        if not isinstance(cc, int) or isinstance(cc, bool) or cc != len(chunk_ids):
            errors.append(
                f"{slice_label}: chunk_count {cc!r} does not match "
                f"len(chunk_ids)={len(chunk_ids)}"
            )

        first_id = chunk_ids[0] if isinstance(chunk_ids, list) and chunk_ids else None
        last_id = chunk_ids[-1] if isinstance(chunk_ids, list) and chunk_ids else None
        if first_id in chunks_by_id and last_id in chunks_by_id:
            ps = slice_rec["page_start"]
            pe = slice_rec["page_end"]
            expected_ps = chunks_by_id[first_id].get("page_start")
            expected_pe = chunks_by_id[last_id].get("page_end")
            if ps != expected_ps:
                errors.append(
                    f"{slice_label}: page_start {ps!r} does not match first chunk "
                    f"{first_id!r} page_start={expected_ps!r}"
                )
            if pe != expected_pe:
                errors.append(
                    f"{slice_label}: page_end {pe!r} does not match last chunk "
                    f"{last_id!r} page_end={expected_pe!r}"
                )

    if seen_chunk_ids != set(chunks_by_id.keys()):
        missing = sorted(set(chunks_by_id.keys()) - seen_chunk_ids)
        for cid in missing:
            errors.append(
                f"{label}/manifest.json: chunk '{cid}' exists on disk but is "
                f"not referenced by any slice"
            )

    if order is not None and chain_walk and not errors:
        if chain_walk != order:
            errors.append(
                f"{label}/manifest.json: slice chunk_ids concatenated do not "
                f"match the source-level chain order; slices must record "
                f"contiguous runs in chain order"
            )

    if isinstance(manifest.get("chunk_count"), int):
        slice_total = sum(
            s.get("chunk_count", 0)
            for s in slices
            if isinstance(s, dict) and isinstance(s.get("chunk_count"), int)
        )
        if slice_total != manifest["chunk_count"]:
            errors.append(
                f"{label}/manifest.json: chunk_count={manifest['chunk_count']} "
                f"but sum(slices.chunk_count)={slice_total}"
            )

    return errors


def validate_chain(
    chunks_by_id: Dict[str, Dict[str, Any]],
    label: str,
) -> List[str]:
    errors: List[str] = []
    if not chunks_by_id:
        return errors

    heads = [c for c in chunks_by_id.values() if c.get("prev_chunk_id") is None]
    tails = [c for c in chunks_by_id.values() if c.get("next_chunk_id") is None]
    if len(heads) != 1:
        errors.append(
            f"{label}: expected exactly one head (prev_chunk_id=null), "
            f"got {len(heads)}"
        )
    if len(tails) != 1:
        errors.append(
            f"{label}: expected exactly one tail (next_chunk_id=null), "
            f"got {len(tails)}"
        )

    for cid, rec in chunks_by_id.items():
        prev_id = rec.get("prev_chunk_id")
        next_id = rec.get("next_chunk_id")
        if prev_id is not None:
            if prev_id not in chunks_by_id:
                errors.append(
                    f"{label}: chunk '{cid}' prev_chunk_id '{prev_id}' "
                    f"does not exist"
                )
            elif chunks_by_id[prev_id].get("next_chunk_id") != cid:
                errors.append(
                    f"{label}: chunk '{cid}' prev_chunk_id '{prev_id}' "
                    f"does not point back via next_chunk_id"
                )
        if next_id is not None:
            if next_id not in chunks_by_id:
                errors.append(
                    f"{label}: chunk '{cid}' next_chunk_id '{next_id}' "
                    f"does not exist"
                )
            elif chunks_by_id[next_id].get("prev_chunk_id") != cid:
                errors.append(
                    f"{label}: chunk '{cid}' next_chunk_id '{next_id}' "
                    f"does not point back via prev_chunk_id"
                )

    if errors:
        return errors

    head = heads[0]
    walk_count = 0
    seen: set = set()
    cursor: Dict[str, Any] | None = head
    while cursor is not None:
        cid = cursor.get("chunk_id")
        if cid in seen:
            errors.append(f"{label}: chain loop detected at chunk '{cid}'")
            return errors
        seen.add(cid)
        walk_count += 1
        next_id = cursor.get("next_chunk_id")
        cursor = chunks_by_id.get(next_id) if next_id is not None else None

    if walk_count != len(chunks_by_id):
        errors.append(
            f"{label}: chain reaches {walk_count} of {len(chunks_by_id)} "
            f"chunks (gaps or disconnected segments)"
        )
    return errors


def validate_source(source_dir: Path) -> Tuple[int, int, List[str]]:
    errors: List[str] = []
    manifest_path = source_dir / "manifest.json"
    chunks_dir = source_dir / "chunks"

    if not manifest_path.exists() and not chunks_dir.exists():
        return 0, 0, []

    if manifest_path.exists():
        manifest, m_errors = load_json(manifest_path)
        errors.extend(m_errors)
        if manifest is not None:
            errors.extend(validate_manifest(manifest, source_dir))
    else:
        errors.append(
            f"{source_dir.name}: chunks/ exists but manifest.json is missing"
        )
        manifest = None

    chunks_by_id: Dict[str, Dict[str, Any]] = {}
    chunk_count = 0
    if chunks_dir.exists():
        for chunk_path in sorted(chunks_dir.glob("*.json")):
            record, c_errors = load_json(chunk_path)
            errors.extend(c_errors)
            if record is None:
                continue
            label = f"{source_dir.name}/chunks/{chunk_path.name}"
            field_errors = validate_chunk_record(record, label)
            errors.extend(field_errors)
            if field_errors:
                continue
            cid = record["chunk_id"]
            if cid in chunks_by_id:
                errors.append(
                    f"{source_dir.name}: duplicate chunk_id '{cid}'"
                )
                continue
            chunks_by_id[cid] = record
            chunk_count += 1

    if (
        isinstance(manifest, dict)
        and "chunk_count" in manifest
        and isinstance(manifest["chunk_count"], int)
        and manifest["chunk_count"] != chunk_count
    ):
        errors.append(
            f"{source_dir.name}: manifest.chunk_count="
            f"{manifest['chunk_count']} but found {chunk_count} chunk files"
        )

    errors.extend(validate_chain(chunks_by_id, source_dir.name))

    if isinstance(manifest, dict) and "slices" in manifest:
        errors.extend(validate_slices(manifest, chunks_by_id, source_dir.name))

    return chunk_count, len(errors), errors


def main() -> int:
    sources = list_source_dirs(PROCESSED_ROOT)
    total_sources = 0
    total_chunks = 0
    total_errors = 0
    detail: List[str] = []

    for source_dir in sources:
        manifest_path = source_dir / "manifest.json"
        chunks_dir = source_dir / "chunks"
        if not manifest_path.exists() and not chunks_dir.exists():
            continue
        total_sources += 1
        chunks, errs_count, errs = validate_source(source_dir)
        total_chunks += chunks
        total_errors += errs_count
        for e in errs:
            detail.append(f"  - {e}")

    if detail:
        print("validate_chunk_chain: details")
        for line in detail:
            print(line)

    print(
        f"validate_chunk_chain: sources={total_sources} chunks={total_chunks} "
        f"errors={total_errors} root=processed/"
    )
    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
