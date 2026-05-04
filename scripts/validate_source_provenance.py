#!/usr/bin/env python3
"""Validate source-page provenance under wiki/source/.

Scope and rules follow AGENTS.md and structured/schema/source.schema.json:

- scans wiki/source/*.md recursively
- ignores .gitkeep and non-.md files
- exits 0 if there are no source pages yet (empty active tree)
- a "source page" is a markdown file under wiki/source/ whose frontmatter has
  type == "source"; pages with type == "summary" (source hubs) are counted as
  scanned but skipped here -- their base validation is handled by
  validate_frontmatter.py
- for each source page, verifies:
    * required source frontmatter fields are present and well-typed
    * status, phase, type values are within their AGENTS.md enums
    * processed/<source-id>/manifest.json exists
    * raw_id matches manifest.raw_id
    * every processed_id matches manifest.processed_id (single processed run
      per source for now)
    * source_kind, when present, equals manifest.source_kind
    * every chunk_id in frontmatter exists as a real chunk JSON under
      processed/<source-id>/chunks/
    * every Obsidian-style chunk-id token mentioned in the body
      (matched by  '<source>-...-chunk-NNNN' pattern) exists as a real chunk
      JSON file somewhere under processed/*/chunks/
    * every body-referenced chunk id is also listed in frontmatter chunk_ids
      (if a chunk exists globally but is not declared in chunk_ids, fail)
- prints a one-line summary
- exits 0 when nothing fails, 1 otherwise (with per-file detail lines)

Uses Python stdlib only. Frontmatter is parsed by reusing the lightweight YAML
subset parser from validate_frontmatter.py via dynamic import; this avoids
duplicating the parser and guarantees the two scripts agree on what counts as
valid frontmatter.
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_SOURCE = REPO_ROOT / "wiki" / "source"
PROCESSED_ROOT = REPO_ROOT / "processed"

REQUIRED_FIELDS = (
    "id",
    "type",
    "status",
    "phase",
    "parent",
    "prev",
    "next",
    "source_id",
    "raw_id",
    "processed_ids",
    "chunk_ids",
)
ALLOWED_TYPE = "source"
ALLOWED_STATUSES = {
    "active",
    "draft",
    "candidate",
    "deprecated",
    "needs-review",
}
ALLOWED_PHASES = {
    "phase-2-source-built",
    "phase-3-reasoned",
    "not-applicable",
}
ALLOWED_SOURCE_KINDS = {
    "book-section",
    "paper-section",
    "standard-section",
    "technical-doc",
    "first-party-artifact",
    "explicit-snapshot",
}

CHUNK_ID_PATTERN = re.compile(r"(?<![A-Za-z0-9_])([a-z0-9]+(?:-[a-z0-9]+)*-chunk-\d{4,})(?![A-Za-z0-9_])")


def _load_frontmatter_module():
    spec = importlib.util.spec_from_file_location(
        "_reno_frontmatter",
        Path(__file__).resolve().parent / "validate_frontmatter.py",
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load validate_frontmatter.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_FM = _load_frontmatter_module()


def split_body(text: str) -> Tuple[str, str]:
    """Return (frontmatter_text_or_empty, body_text)."""
    if not text.startswith("---"):
        return "", text
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return "", text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fm_text = "\n".join(lines[: i + 1]) + "\n"
            body = "\n".join(lines[i + 1 :])
            return fm_text, body
    return "", text


def collect_source_md_files(root: Path) -> List[Path]:
    if not root.exists():
        return []
    out: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for name in sorted(filenames):
            if name == ".gitkeep":
                continue
            if not name.endswith(".md"):
                continue
            out.append(Path(dirpath) / name)
    return out


def list_processed_chunk_ids() -> Dict[str, Set[str]]:
    """Return {source_id: {chunk_id, ...}} based on chunk JSON filenames."""
    out: Dict[str, Set[str]] = {}
    if not PROCESSED_ROOT.exists():
        return out
    for entry in sorted(PROCESSED_ROOT.iterdir()):
        if not entry.is_dir() or entry.name.startswith("."):
            continue
        chunks_dir = entry / "chunks"
        if not chunks_dir.exists():
            continue
        ids: Set[str] = set()
        for path in sorted(chunks_dir.glob("*.json")):
            ids.add(path.stem)
        out[entry.name] = ids
    return out


def load_manifest(source_id: str) -> Tuple[Dict[str, Any] | None, str]:
    path = PROCESSED_ROOT / source_id / "manifest.json"
    if not path.exists():
        return None, f"missing processed/{source_id}/manifest.json"
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh), ""
    except json.JSONDecodeError as exc:
        return None, f"invalid JSON in {path}: {exc}"
    except OSError as exc:
        return None, f"could not read {path}: {exc}"


def validate_source_page(
    path: Path,
    chunk_index: Dict[str, Set[str]],
) -> List[str]:
    rel = path.relative_to(REPO_ROOT)
    errors: List[str] = []

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: could not read file: {exc}"]

    fm, fm_errors = _FM.extract_frontmatter(text)
    for e in fm_errors:
        errors.append(f"{rel}: {e}")

    if fm is None:
        errors.append(f"{rel}: missing leading YAML frontmatter")
        return errors

    page_type = fm.get("type")
    if page_type != ALLOWED_TYPE:
        return errors

    for key in REQUIRED_FIELDS:
        if key not in fm:
            errors.append(f"{rel}: missing required field '{key}'")

    if "status" in fm and fm["status"] not in ALLOWED_STATUSES:
        errors.append(
            f"{rel}: status {fm['status']!r} not in "
            f"{sorted(ALLOWED_STATUSES)}"
        )
    if "phase" in fm and fm["phase"] not in ALLOWED_PHASES:
        errors.append(
            f"{rel}: phase {fm['phase']!r} not in {sorted(ALLOWED_PHASES)}"
        )

    for nav in ("parent", "prev", "next"):
        if nav in fm and fm[nav] is not None and not isinstance(fm[nav], str):
            errors.append(
                f"{rel}: field '{nav}' must be a string or null, "
                f"got {type(fm[nav]).__name__}"
            )

    for ident in ("id", "source_id", "raw_id"):
        v = fm.get(ident)
        if v is not None and (not isinstance(v, str) or not v):
            errors.append(
                f"{rel}: field '{ident}' must be a non-empty string"
            )

    if (
        isinstance(fm.get("id"), str)
        and isinstance(path.stem, str)
        and fm["id"] != path.stem
    ):
        errors.append(
            f"{rel}: id {fm['id']!r} does not match filename stem "
            f"{path.stem!r}"
        )

    processed_ids = fm.get("processed_ids")
    if processed_ids is None or not isinstance(processed_ids, list):
        errors.append(
            f"{rel}: field 'processed_ids' must be a list (use [] when empty)"
        )
        processed_ids = []
    else:
        for v in processed_ids:
            if not isinstance(v, str) or not v:
                errors.append(
                    f"{rel}: processed_ids entry must be a non-empty string, "
                    f"got {v!r}"
                )

    chunk_ids_fm = fm.get("chunk_ids")
    if chunk_ids_fm is None or not isinstance(chunk_ids_fm, list):
        errors.append(
            f"{rel}: field 'chunk_ids' must be a list (use [] when empty)"
        )
        chunk_ids_fm = []
    else:
        for v in chunk_ids_fm:
            if not isinstance(v, str) or not v:
                errors.append(
                    f"{rel}: chunk_ids entry must be a non-empty string, "
                    f"got {v!r}"
                )

    if "source_kind" in fm and fm["source_kind"] not in ALLOWED_SOURCE_KINDS:
        errors.append(
            f"{rel}: source_kind {fm['source_kind']!r} not in "
            f"{sorted(ALLOWED_SOURCE_KINDS)}"
        )

    source_id = fm.get("source_id")
    if not isinstance(source_id, str) or not source_id:
        return errors

    manifest, manifest_err = load_manifest(source_id)
    if manifest is None:
        errors.append(f"{rel}: {manifest_err}")
        return errors

    raw_id_fm = fm.get("raw_id")
    raw_id_manifest = manifest.get("raw_id")
    if isinstance(raw_id_fm, str) and raw_id_fm and raw_id_manifest != raw_id_fm:
        errors.append(
            f"{rel}: raw_id {raw_id_fm!r} does not match manifest raw_id "
            f"{raw_id_manifest!r}"
        )

    processed_id_manifest = manifest.get("processed_id")
    for pid in processed_ids:
        if pid != processed_id_manifest:
            errors.append(
                f"{rel}: processed_ids entry {pid!r} does not match manifest "
                f"processed_id {processed_id_manifest!r}"
            )

    if (
        "source_kind" in fm
        and isinstance(fm["source_kind"], str)
        and manifest.get("source_kind") not in (None, fm["source_kind"])
    ):
        errors.append(
            f"{rel}: source_kind {fm['source_kind']!r} does not match "
            f"manifest source_kind {manifest.get('source_kind')!r}"
        )

    available = chunk_index.get(source_id, set())
    for cid in chunk_ids_fm:
        if cid not in available:
            errors.append(
                f"{rel}: chunk_ids entry {cid!r} does not exist as "
                f"processed/{source_id}/chunks/{cid}.json"
            )

    _, body = split_body(text)
    body_chunk_ids: Set[str] = set()
    for match in CHUNK_ID_PATTERN.finditer(body):
        body_chunk_ids.add(match.group(1))

    declared_chunk_ids: Set[str] = set()
    if isinstance(chunk_ids_fm, list):
        for v in chunk_ids_fm:
            if isinstance(v, str) and v:
                declared_chunk_ids.add(v)

    all_known: Set[str] = set()
    for ids in chunk_index.values():
        all_known |= ids
    for cid in sorted(body_chunk_ids):
        if cid not in all_known:
            errors.append(
                f"{rel}: body references chunk id {cid!r} but no chunk JSON "
                f"file exists under processed/*/chunks/"
            )
        elif cid not in declared_chunk_ids:
            errors.append(
                f"{rel}: body references chunk id {cid!r} that exists under "
                f"processed/*/chunks/ but is not listed in frontmatter "
                f"chunk_ids; add {cid!r} to chunk_ids for this page"
            )

    return errors


def main() -> int:
    files = collect_source_md_files(WIKI_SOURCE)
    chunk_index = list_processed_chunk_ids()

    total_scanned = 0
    total_source_pages = 0
    total_failed_files = 0
    detail: List[str] = []

    for path in files:
        total_scanned += 1
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            detail.append(f"  - {path.relative_to(REPO_ROOT)}: could not read: {exc}")
            total_failed_files += 1
            continue
        fm, _ = _FM.extract_frontmatter(text)
        if isinstance(fm, dict) and fm.get("type") == ALLOWED_TYPE:
            total_source_pages += 1

        errs = validate_source_page(path, chunk_index)
        if errs:
            total_failed_files += 1
            for e in errs:
                detail.append(f"  - {e}")

    if detail:
        print("validate_source_provenance: details")
        for line in detail:
            print(line)

    print(
        f"validate_source_provenance: scanned={total_scanned} "
        f"source_pages={total_source_pages} failed={total_failed_files} "
        f"root=wiki/source/"
    )
    return 0 if total_failed_files == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
