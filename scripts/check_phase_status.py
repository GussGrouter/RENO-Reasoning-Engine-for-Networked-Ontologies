#!/usr/bin/env python3
"""Validate wiki page location, type, and phase consistency.

Allowed combinations:

- wiki/source/*.md with type: source -> phase must be phase-2-source-built
- wiki/source/*.md with type: summary -> phase must be phase-2-source-built
- wiki/concept/*.md with type: concept -> phase must be phase-3-reasoned
- wiki/insight/*.md with type: insight -> phase must be phase-3-reasoned
- wiki/meta/*.md with type: index -> phase must be not-applicable
- wiki/summary/*.md with type: summary -> phase may be phase-3-reasoned or not-applicable

Uses Python stdlib only and reuses validate_frontmatter.py for the repository's
small frontmatter subset.
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

import validate_chapter_boundaries as CHAPTER_BOUNDARIES

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_ROOT = REPO_ROOT / "wiki"
PROCESSED_ROOT = REPO_ROOT / "processed"
FRONTMATTER_VALIDATOR = REPO_ROOT / "scripts" / "validate_frontmatter.py"


def load_frontmatter_parser():
    spec = importlib.util.spec_from_file_location(
        "validate_frontmatter", FRONTMATTER_VALIDATOR
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {FRONTMATTER_VALIDATOR}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


FM = load_frontmatter_parser()


def collect_markdown_files(root: Path) -> List[Path]:
    if not root.exists():
        return []
    out: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for name in sorted(filenames):
            if name == ".gitkeep" or not name.endswith(".md"):
                continue
            out.append(Path(dirpath) / name)
    return out


def allowed_for(path: Path) -> Tuple[Set[str], Set[str]]:
    try:
        rel = path.relative_to(WIKI_ROOT)
    except ValueError:
        return set(), set()
    parts = rel.parts
    if len(parts) < 2:
        return set(), set()
    area = parts[0]
    if area == "source":
        return {"source", "summary"}, {"phase-2-source-built"}
    if area == "concept":
        return {"concept"}, {"phase-3-reasoned"}
    if area == "insight":
        return {"insight"}, {"phase-3-reasoned"}
    if area == "meta":
        return {"index"}, {"not-applicable"}
    if area == "summary":
        return {"summary"}, {"phase-3-reasoned", "not-applicable"}
    return set(), set()


def validate_one(path: Path) -> List[str]:
    rel = path.relative_to(REPO_ROOT)
    errors: List[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: could not read: {exc}"]

    fm, parse_errors = FM.extract_frontmatter(text)
    for err in parse_errors:
        errors.append(f"{rel}: {err}")
    if fm is None:
        errors.append(f"{rel}: missing leading YAML frontmatter")
        return errors
    if not isinstance(fm, dict):
        errors.append(f"{rel}: frontmatter is not a mapping")
        return errors

    allowed_types, allowed_phases = allowed_for(path)
    page_type = fm.get("type")
    phase = fm.get("phase")

    if not allowed_types:
        errors.append(f"{rel}: wiki location is not recognized for phase/status audit")
        return errors
    if page_type not in allowed_types:
        errors.append(
            f"{rel}: type {page_type!r} is invalid for location; "
            f"expected one of {sorted(allowed_types)}"
        )
    if phase not in allowed_phases:
        errors.append(
            f"{rel}: phase {phase!r} is invalid for location/type; "
            f"expected one of {sorted(allowed_phases)}"
        )

    return errors


def processed_source_dirs(root: Path) -> List[Path]:
    if not root.exists():
        return []
    return sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith("."))


def manifest_requires_boundary(manifest: Dict[str, object]) -> bool:
    if manifest.get("source_kind") == "book-section":
        return True
    slices = manifest.get("slices")
    if not isinstance(slices, list):
        return False
    for slice_rec in slices:
        if isinstance(slice_rec, dict) and CHAPTER_BOUNDARIES.infer_chapter(slice_rec) is not None:
            return True
    return False


def validate_processed_boundaries(source_dir: Path) -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []
    manifest_path = source_dir / "manifest.json"
    boundaries_path = source_dir / "chapter_boundaries.json"

    manifest, manifest_errors = CHAPTER_BOUNDARIES.load_json(manifest_path)
    if manifest_errors:
        # Processed structure is primarily covered by validate_chunk_chain.py.
        return errors, warnings
    if not isinstance(manifest, dict):
        return [f"{manifest_path}: expected top-level JSON object"], warnings

    if not boundaries_path.exists():
        if manifest_requires_boundary(manifest):
            errors.append(
                f"{source_dir.name}: missing chapter_boundaries.json for book/chapter-labeled "
                "processed source"
            )
        return errors, warnings

    boundaries, boundary_load_errors = CHAPTER_BOUNDARIES.load_json(boundaries_path)
    errors.extend(boundary_load_errors)
    if errors:
        return errors, warnings
    if not isinstance(boundaries, dict):
        return [f"{boundaries_path}: expected top-level JSON object"], warnings

    boundary_index, boundary_errors = CHAPTER_BOUNDARIES.build_boundary_index(boundaries)
    errors.extend(boundary_errors)
    if boundary_errors:
        return errors, warnings

    slice_errors, slice_warnings = CHAPTER_BOUNDARIES.validate(manifest, boundary_index)
    errors.extend(f"{source_dir.name}: {e}" for e in slice_errors)
    warnings.extend(f"{source_dir.name}: {w}" for w in slice_warnings)
    return errors, warnings


def main() -> int:
    files = collect_markdown_files(WIKI_ROOT)
    failed = 0
    details: List[str] = []
    warning_details: List[str] = []

    for path in files:
        errs = validate_one(path)
        if errs:
            failed += 1
            details.extend(f"  - {e}" for e in errs)

    boundary_failed = 0
    processed_sources = processed_source_dirs(PROCESSED_ROOT)
    for source_dir in processed_sources:
        errs, warns = validate_processed_boundaries(source_dir)
        if errs:
            boundary_failed += 1
            details.extend(f"  - {e}" for e in errs)
        warning_details.extend(f"  - {w}" for w in warns)

    if details:
        print("check_phase_status: details")
        for line in details:
            print(line)
    if warning_details:
        print("check_phase_status: warnings")
        for line in warning_details:
            print(line)

    total_failed = failed + boundary_failed
    print(
        f"check_phase_status: scanned={len(files)} ok={len(files) - failed} "
        f"failed={failed} processed_sources={len(processed_sources)} "
        f"boundary_failed={boundary_failed}"
    )
    return 0 if total_failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
