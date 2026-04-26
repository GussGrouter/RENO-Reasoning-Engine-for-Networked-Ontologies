#!/usr/bin/env python3
"""Validate processed manifests and chunk chains under processed/.

Scope and rules follow AGENTS.md:

- inspects processed/<source-id>/manifest.json and processed/<source-id>/chunks/*.json
- verifies required chunk fields (chunk_id, prev_chunk_id, next_chunk_id,
  content_hash, token_estimate, processed_id, raw_id, source_id, page_start,
  page_end, title, review_status)
- verifies the prev/next chain has no gaps and no loops:
  - exactly one chunk has prev_chunk_id == null (head)
  - exactly one chunk has next_chunk_id == null (tail)
  - every other chunk's prev_chunk_id points to an existing chunk whose
    next_chunk_id points back to it, and similarly for next_chunk_id
  - all chunks are reachable from the head in a single linear walk

Exits 0 if no processed sources exist yet (empty active tree), or if every
processed source passes. Exits 1 on any explicit violation. Prints a one-line
summary on every run.

Uses Python stdlib only.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

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
