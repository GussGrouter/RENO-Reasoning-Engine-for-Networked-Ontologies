#!/usr/bin/env python3
"""Validate YAML frontmatter on maintained markdown pages under wiki/.

Scope and rules follow AGENTS.md:

- only validates files under wiki/
- ignores .gitkeep, archive/, prompts/, raw/, processed/, structured/, scripts/, AGENTS.md
- requires leading YAML frontmatter delimited by '---' lines
- requires id, type, status, phase
- type values must be one of:
  summary | concept | insight | source | index | decision | contradiction
- status values must be one of:
  active | draft | candidate | deprecated | needs-review
- phase values must be one of:
  phase-1-parsed | phase-2-source-built | phase-3-reasoned | not-applicable

The script exits 0 on an empty or minimal active tree (no markdown files under
wiki/) and prints a one-line summary in all cases. Exit code is non-zero only
when at least one explicit violation is detected.

Uses Python stdlib only. If a leading YAML block is present, only a small
subset of YAML used for RENO frontmatter is recognized: scalar key: value pairs
with strings, numbers, booleans, null, inline empty lists ([]), and flat inline
non-empty lists ([item, "item with spaces", ...]). Complex YAML constructs
(nested mappings, multi-line lists, anchors, aliases, etc.) are rejected with a
clear error rather than silently parsed.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_ROOT = REPO_ROOT / "wiki"

ALLOWED_TYPES = {
    "summary",
    "concept",
    "insight",
    "source",
    "index",
    "decision",
    "contradiction",
}
ALLOWED_STATUSES = {
    "active",
    "draft",
    "candidate",
    "deprecated",
    "needs-review",
}
ALLOWED_PHASES = {
    "phase-1-parsed",
    "phase-2-source-built",
    "phase-3-reasoned",
    "not-applicable",
}
REQUIRED_FIELDS = ("id", "type", "status", "phase")


def split_inline_list(inner: str) -> List[str]:
    """Split the inside of an inline YAML list on top-level commas.

    Respects single- and double-quoted strings. Brackets/braces inside quoted
    strings are not treated as nesting. Nested unquoted brackets/braces are
    rejected by the caller via parse_scalar (which forbids '[' or '{' inside an
    item after this split).
    """
    parts: List[str] = []
    buf: List[str] = []
    quote: str | None = None
    for ch in inner:
        if quote is not None:
            buf.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in ('"', "'"):
            quote = ch
            buf.append(ch)
            continue
        if ch == ",":
            parts.append("".join(buf).strip())
            buf = []
            continue
        buf.append(ch)
    if quote is not None:
        raise ValueError("unterminated quoted string in inline list")
    tail = "".join(buf).strip()
    if tail or parts:
        parts.append(tail)
    return parts


def parse_scalar(raw: str) -> Any:
    raw = raw.strip()
    if raw == "" or raw.lower() == "null" or raw == "~":
        return None
    if raw == "[]":
        return []
    if raw == "{}":
        return {}
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        try:
            parts = split_inline_list(inner)
        except ValueError as exc:
            raise ValueError(f"malformed inline list {raw!r}: {exc}") from exc
        items: List[Any] = []
        for part in parts:
            if "[" in part or "]" in part or "{" in part or "}" in part:
                raise ValueError(
                    f"nested or malformed item in inline list {raw!r}: {part!r}"
                )
            items.append(parse_scalar(part))
        return items
    if raw.startswith("[") or raw.startswith("{"):
        raise ValueError(f"unsupported nested or unclosed YAML value: {raw!r}")
    if raw.lower() == "true":
        return True
    if raw.lower() == "false":
        return False
    if (raw.startswith('"') and raw.endswith('"')) or (
        raw.startswith("'") and raw.endswith("'")
    ):
        return raw[1:-1]
    try:
        if raw.startswith("-") or raw.isdigit():
            return int(raw)
    except ValueError:
        pass
    return raw


def extract_frontmatter(text: str) -> Tuple[Dict[str, Any] | None, List[str]]:
    """Return (frontmatter_dict_or_None, errors).

    A None dict means "no frontmatter detected at all".
    """
    errors: List[str] = []
    if not text.startswith("---"):
        return None, errors

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, errors

    end_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx == -1:
        errors.append("frontmatter opens with --- but is not closed by a matching ---")
        return {}, errors

    body_lines = lines[1:end_idx]
    fm: Dict[str, Any] = {}
    for raw_line in body_lines:
        line = raw_line.rstrip()
        if line.strip() == "" or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            errors.append(
                f"unsupported indented YAML in frontmatter: {raw_line!r}"
            )
            continue
        if ":" not in line:
            errors.append(f"unparseable frontmatter line: {raw_line!r}")
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        if not key:
            errors.append(f"empty key in frontmatter line: {raw_line!r}")
            continue
        try:
            fm[key] = parse_scalar(value)
        except ValueError as exc:
            errors.append(
                f"could not parse value for key '{key}' in frontmatter line "
                f"{raw_line!r}: {exc}"
            )
    return fm, errors


def is_ignored(path: Path) -> bool:
    if path.name == ".gitkeep":
        return True
    if path.suffix.lower() != ".md":
        return True
    return False


def collect_markdown_files(root: Path) -> List[Path]:
    if not root.exists():
        return []
    out: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for name in sorted(filenames):
            p = Path(dirpath) / name
            if not is_ignored(p):
                out.append(p)
    return out


def validate_one(path: Path) -> List[str]:
    errors: List[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"could not read file: {exc}"]

    fm, parse_errors = extract_frontmatter(text)
    errors.extend(parse_errors)

    if fm is None:
        errors.append("missing leading YAML frontmatter")
        return errors

    for key in REQUIRED_FIELDS:
        if key not in fm:
            errors.append(f"missing required field '{key}'")
        elif fm[key] in (None, ""):
            errors.append(f"required field '{key}' is empty")

    if "type" in fm and fm["type"] not in ALLOWED_TYPES:
        errors.append(
            f"type '{fm['type']!r}' not in allowed set {sorted(ALLOWED_TYPES)}"
        )
    if "status" in fm and fm["status"] not in ALLOWED_STATUSES:
        errors.append(
            f"status '{fm['status']!r}' not in allowed set "
            f"{sorted(ALLOWED_STATUSES)}"
        )
    if "phase" in fm and fm["phase"] not in ALLOWED_PHASES:
        errors.append(
            f"phase '{fm['phase']!r}' not in allowed set {sorted(ALLOWED_PHASES)}"
        )
    return errors


def main() -> int:
    files = collect_markdown_files(WIKI_ROOT)
    total = len(files)
    failed = 0
    detail: List[str] = []
    for path in files:
        errs = validate_one(path)
        if errs:
            failed += 1
            rel = path.relative_to(REPO_ROOT)
            for e in errs:
                detail.append(f"  - {rel}: {e}")

    if detail:
        print("validate_frontmatter: details")
        for line in detail:
            print(line)

    print(
        f"validate_frontmatter: scanned={total} ok={total - failed} "
        f"failed={failed} root=wiki/"
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
