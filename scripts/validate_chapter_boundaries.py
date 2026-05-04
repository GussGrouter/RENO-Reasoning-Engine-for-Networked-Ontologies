#!/usr/bin/env python3
"""Validate that manifest slices stay within chapter boundaries.

Reads processed truth directly:
- processed/<source-id>/manifest.json
- processed/<source-id>/chapter_boundaries.json

Rules:
- infer intended chapter from slice_id and/or section_range (chapter-N-...)
- warn (not fail) when chapter cannot be inferred
- warn (not fail) when chapter boundary confidence is low
- fail when an inferable slice page range is outside the chapter boundary
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent

CHAPTER_RE = re.compile(r"(?:^|-)chapter-(\d+)(?:-|$)")


def load_json(path: Path) -> Tuple[Optional[Any], List[str]]:
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh), []
    except FileNotFoundError:
        return None, [f"missing file: {path}"]
    except json.JSONDecodeError as exc:
        return None, [f"invalid JSON in {path}: {exc}"]
    except OSError as exc:
        return None, [f"could not read {path}: {exc}"]


def infer_chapter(slice_rec: Dict[str, Any]) -> Optional[int]:
    for key in ("slice_id", "section_range"):
        value = slice_rec.get(key)
        if not isinstance(value, str):
            continue
        m = CHAPTER_RE.search(value)
        if m:
            return int(m.group(1))
    return None


def parse_slice_range(slice_rec: Dict[str, Any]) -> Optional[Tuple[int, int]]:
    ps = slice_rec.get("page_start")
    pe = slice_rec.get("page_end")
    if isinstance(ps, int) and isinstance(pe, int):
        return ps, pe

    pr = slice_rec.get("page_range")
    if isinstance(pr, str) and "-" in pr:
        left, right = pr.split("-", 1)
        if left.strip().isdigit() and right.strip().isdigit():
            return int(left.strip()), int(right.strip())
    return None


def build_boundary_index(boundaries: Dict[str, Any]) -> Tuple[Dict[int, Dict[str, Any]], List[str]]:
    errors: List[str] = []
    out: Dict[int, Dict[str, Any]] = {}
    entries = boundaries.get("chapter_boundaries")
    if not isinstance(entries, list):
        return {}, ["chapter_boundaries.json: 'chapter_boundaries' must be an array"]

    for idx, entry in enumerate(entries):
        label = f"chapter_boundaries.json: chapter_boundaries[{idx}]"
        if not isinstance(entry, dict):
            errors.append(f"{label} must be an object")
            continue

        n = entry.get("chapter_number")
        start = entry.get("start_pdf_page")
        end = entry.get("end_pdf_page")
        confidence = entry.get("confidence")

        if not isinstance(n, int):
            errors.append(f"{label}: chapter_number must be an integer")
            continue
        if not isinstance(start, int):
            errors.append(f"{label}: start_pdf_page must be an integer")
            continue
        if end is not None and not isinstance(end, int):
            errors.append(f"{label}: end_pdf_page must be an integer or null")
            continue
        if confidence not in {"high", "medium", "low"}:
            errors.append(f"{label}: confidence must be one of high/medium/low")
            continue
        if end is not None and end < start:
            errors.append(f"{label}: end_pdf_page {end} is before start_pdf_page {start}")
            continue
        if n in out:
            errors.append(f"{label}: duplicate chapter_number {n}")
            continue

        out[n] = entry
    return out, errors


def format_range(start: int, end: Optional[int]) -> str:
    if end is None:
        return f"{start}+"
    return f"{start}-{end}"


def relative_to_repo(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path)


def validate_slice(
    slice_rec: Dict[str, Any],
    boundary_index: Dict[int, Dict[str, Any]],
) -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []

    sid = slice_rec.get("slice_id", "<unknown>")
    sr = parse_slice_range(slice_rec)
    if sr is None:
        warnings.append(f"{sid}: could not parse page range; skipping boundary validation")
        return errors, warnings
    page_start, page_end = sr

    chapter = infer_chapter(slice_rec)
    if chapter is None:
        warnings.append(
            f"{sid}: could not infer intended chapter from slice_id/section_range; "
            "boundary check skipped"
        )
        return errors, warnings

    boundary = boundary_index.get(chapter)
    if boundary is None:
        warnings.append(f"{sid}: no boundary record for inferred chapter {chapter}; check skipped")
        return errors, warnings

    b_start = boundary["start_pdf_page"]
    b_end = boundary.get("end_pdf_page")
    confidence = boundary["confidence"]
    chapter_title = boundary.get("chapter_title", f"chapter {chapter}")

    if confidence == "low":
        warnings.append(
            f"{sid}: inferred chapter {chapter} boundary is low confidence "
            f"({format_range(b_start, b_end)}); not enforced as hard failure"
        )
        return errors, warnings

    out_of_range = page_start < b_start or (b_end is not None and page_end > b_end)
    if out_of_range:
        errors.append(
            f"{sid}: labeled chapter {chapter} ({chapter_title}) but page_range "
            f"{page_start}-{page_end} is outside expected boundary "
            f"{format_range(b_start, b_end)}; suggested action: relabel/split/rollback this slice "
            "to fit chapter boundaries"
        )

    return errors, warnings


def validate(manifest: Dict[str, Any], boundary_index: Dict[int, Dict[str, Any]]) -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []

    slices = manifest.get("slices")
    if not isinstance(slices, list):
        return ["manifest.json: 'slices' must be an array"], warnings

    for idx, slice_rec in enumerate(slices):
        label = f"manifest.json:slices[{idx}]"
        if not isinstance(slice_rec, dict):
            errors.append(f"{label}: slice entry is not an object")
            continue

        e2, w2 = validate_slice(slice_rec, boundary_index)
        errors.extend(e2)
        warnings.extend(w2)

    return errors, warnings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-id", default="systems-performance")
    parser.add_argument("--manifest-path", default=None)
    parser.add_argument("--boundaries-path", default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest_path) if args.manifest_path else (
        REPO_ROOT / "processed" / args.source_id / "manifest.json"
    )
    boundaries_path = Path(args.boundaries_path) if args.boundaries_path else (
        REPO_ROOT / "processed" / args.source_id / "chapter_boundaries.json"
    )

    manifest, manifest_load_errors = load_json(manifest_path)
    boundaries, boundaries_load_errors = load_json(boundaries_path)
    errors: List[str] = []
    warnings: List[str] = []
    errors.extend(manifest_load_errors)
    errors.extend(boundaries_load_errors)

    if not errors:
        if not isinstance(manifest, dict):
            errors.append(f"{manifest_path}: expected top-level JSON object")
        if not isinstance(boundaries, dict):
            errors.append(f"{boundaries_path}: expected top-level JSON object")

    if not errors:
        boundary_index, boundary_errors = build_boundary_index(boundaries)
        errors.extend(boundary_errors)
        if not boundary_errors:
            e2, w2 = validate(manifest, boundary_index)
            errors.extend(e2)
            warnings.extend(w2)

    if warnings:
        print("validate_chapter_boundaries: warnings")
        for line in warnings:
            print(f"  - {line}")

    if errors:
        print("validate_chapter_boundaries: errors")
        for line in errors:
            print(f"  - {line}")

    total_slices = 0
    if isinstance(manifest, dict) and isinstance(manifest.get("slices"), list):
        total_slices = len(manifest["slices"])

    print(
        f"validate_chapter_boundaries: source_id={args.source_id} "
        f"slices={total_slices} warnings={len(warnings)} errors={len(errors)}"
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
