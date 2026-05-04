#!/usr/bin/env python3
"""Validate Phase 3 insight pages under wiki/insight/.

Rules:

- scan wiki/insight/*.md only (ignore .gitkeep and non-markdown files)
- exit 0 if no insight pages exist
- validate flat frontmatter against structured/schema/insight.schema.json
- require body sections:
  - H1 title
  - ## Claim
  - ## Concepts involved
  - ## Source basis
  - ## Decision use
- warn if body exceeds 700 words
- fail if body exceeds 1,000 words
- print a one-line summary

Uses Python stdlib only. The schema is intentionally minimal and this script
implements just the schema subset used by structured/schema/insight.schema.json.
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
INSIGHT_ROOT = REPO_ROOT / "wiki" / "insight"
SCHEMA_PATH = REPO_ROOT / "structured" / "schema" / "insight.schema.json"
FRONTMATTER_VALIDATOR = REPO_ROOT / "scripts" / "validate_frontmatter.py"

SOFT_WORD_MAX = 700
HARD_WORD_MAX = 1000

REQUIRED_SECTIONS = (
    "## Claim",
    "## Concepts involved",
    "## Source basis",
    "## Decision use",
)


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


def list_insight_paths() -> List[Path]:
    if not INSIGHT_ROOT.exists():
        return []
    out: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(INSIGHT_ROOT):
        dirnames.sort()
        for name in sorted(filenames):
            if name == ".gitkeep" or not name.endswith(".md"):
                continue
            out.append(Path(dirpath) / name)
    return out


def split_body(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1 :])
    return text


def word_count(text: str) -> int:
    return len([w for w in text.split() if w])


def validate_schema(fm: Dict[str, Any], rel: Path, schema: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    required = schema.get("required", [])
    props = schema.get("properties", {})
    if schema.get("additionalProperties") is False:
        for key in sorted(fm):
            if key not in props:
                errors.append(f"{rel}: unexpected frontmatter field {key!r}")
    for key in required:
        if key not in fm:
            errors.append(f"{rel}: missing required frontmatter field {key!r}")
    for key, spec in props.items():
        if key not in fm:
            continue
        value = fm[key]
        allowed = spec.get("enum")
        if allowed is not None and value not in allowed:
            errors.append(
                f"{rel}: frontmatter {key!r}={value!r} not in {allowed!r}"
            )
        typ = spec.get("type")
        if typ == "string" and not isinstance(value, str):
            errors.append(f"{rel}: frontmatter {key!r} must be a string")
        if typ == ["string", "null"] and value is not None and not isinstance(value, str):
            errors.append(f"{rel}: frontmatter {key!r} must be string or null")
        if spec.get("minLength", 0) > 0 and isinstance(value, str) and not value:
            errors.append(f"{rel}: frontmatter {key!r} must be non-empty")
    return errors


def validate_one(path: Path, schema: Dict[str, Any]) -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []
    rel = path.relative_to(REPO_ROOT)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: could not read: {exc}"], warnings

    fm, parse_errors = FM.extract_frontmatter(text)
    for e in parse_errors:
        errors.append(f"{rel}: {e}")
    if fm is None:
        errors.append(f"{rel}: missing leading YAML frontmatter")
        return errors, warnings
    if not isinstance(fm, dict):
        errors.append(f"{rel}: frontmatter is not a mapping")
        return errors, warnings

    errors.extend(validate_schema(fm, rel, schema))

    if fm.get("id") != path.stem:
        errors.append(
            f"{rel}: frontmatter id {fm.get('id')!r} must equal filename stem {path.stem!r}"
        )

    body = split_body(text)
    if not re.search(r"(?m)^#\s+\S", body):
        errors.append(f"{rel}: missing H1 title")
    for heading in REQUIRED_SECTIONS:
        if heading not in body:
            errors.append(f"{rel}: missing required section {heading!r}")

    wc = word_count(body)
    if wc > HARD_WORD_MAX:
        errors.append(
            f"{rel}: body word count {wc} exceeds hard max {HARD_WORD_MAX}"
        )
    elif wc > SOFT_WORD_MAX:
        warnings.append(
            f"{rel}: body word count {wc} exceeds soft max {SOFT_WORD_MAX}"
        )

    return errors, warnings


def main() -> int:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except OSError as exc:
        print(f"validate_insights: could not read schema: {exc}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"validate_insights: invalid schema JSON: {exc}", file=sys.stderr)
        return 1

    paths = list_insight_paths()
    failures = 0
    warnings: List[str] = []
    details: List[str] = []
    for path in paths:
        errs, warns = validate_one(path, schema)
        warnings.extend(warns)
        if errs:
            failures += 1
            details.extend(f"  - {e}" for e in errs)

    if details:
        print("validate_insights: details")
        for line in details:
            print(line)
    if warnings:
        print("validate_insights: warnings")
        for line in warnings:
            print(f"  - {line}")

    print(
        f"validate_insights: scanned={len(paths)} ok={len(paths) - failures} "
        f"failed={failures} warnings={len(warnings)} root=wiki/insight/"
    )
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
