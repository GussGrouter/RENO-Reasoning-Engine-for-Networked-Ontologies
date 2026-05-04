#!/usr/bin/env python3
"""Check concept pages for bounded source support.

Rules:

- scan wiki/concept/*.md recursively
- require ## Source support with at least one wikilink
- every Source support wikilink must resolve to an existing wiki/source/*.md page
- fail if Source support has more than five source links
- warn if ## Related concepts has zero wikilinks

Uses Python stdlib only and reuses validate_frontmatter.py for the repository's
small frontmatter subset.
"""

from __future__ import annotations

import importlib.util
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_ROOT = REPO_ROOT / "wiki"
CONCEPT_ROOT = WIKI_ROOT / "concept"
SOURCE_ROOT = WIKI_ROOT / "source"
FRONTMATTER_VALIDATOR = REPO_ROOT / "scripts" / "validate_frontmatter.py"

SOURCE_LINK_MAX = 5
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
FENCED_CODE_RE = re.compile(r"(?ms)^```.*?^```")


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


def split_body(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1 :])
    return text


def section_text(body: str, heading: str) -> str:
    lines = body.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == heading:
            start = i + 1
            break
    if start is None:
        return ""
    end = len(lines)
    for i in range(start, len(lines)):
        if lines[i].startswith("## "):
            end = i
            break
    return "\n".join(lines[start:end])


def strip_code(text: str) -> str:
    text = FENCED_CODE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def normalize_target(raw: str) -> str:
    return raw.split("|", 1)[0].split("#", 1)[0].strip()


def wikilinks(text: str) -> List[str]:
    return [
        normalize_target(match.group(1))
        for match in WIKILINK_RE.finditer(strip_code(text))
        if normalize_target(match.group(1))
    ]


def build_source_registry() -> Dict[str, Path]:
    registry: Dict[str, Path] = {}
    for path in collect_markdown_files(SOURCE_ROOT):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        keys = {
            path.stem,
            path.relative_to(WIKI_ROOT).with_suffix("").as_posix(),
        }
        fm, _ = FM.extract_frontmatter(text)
        if isinstance(fm, dict) and isinstance(fm.get("id"), str) and fm["id"]:
            keys.add(fm["id"])
        for key in keys:
            registry[key] = path
    return registry


def validate_one(path: Path, source_registry: Dict[str, Path]) -> Tuple[List[str], List[str]]:
    rel = path.relative_to(REPO_ROOT)
    errors: List[str] = []
    warnings: List[str] = []

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: could not read: {exc}"], warnings

    body = split_body(text)
    support = section_text(body, "## Source support")
    if not support:
        errors.append(f"{rel}: missing required section '## Source support'")
    support_links = wikilinks(support)
    if not support_links:
        errors.append(f"{rel}: Source support must contain at least one wikilink")
    if len(support_links) > SOURCE_LINK_MAX:
        errors.append(
            f"{rel}: Source support has {len(support_links)} source links; "
            f"max {SOURCE_LINK_MAX}"
        )
    for target in support_links:
        if target not in source_registry:
            errors.append(
                f"{rel}: Source support wikilink [[{target}]] does not resolve "
                "to wiki/source/*.md"
            )

    related = section_text(body, "## Related concepts")
    if related and not wikilinks(related):
        warnings.append(f"{rel}: Related concepts has zero wikilinks")

    return errors, warnings


def main() -> int:
    concepts = collect_markdown_files(CONCEPT_ROOT)
    source_registry = build_source_registry()
    failed = 0
    warnings: List[str] = []
    details: List[str] = []

    for path in concepts:
        errs, warns = validate_one(path, source_registry)
        warnings.extend(warns)
        if errs:
            failed += 1
            details.extend(f"  - {e}" for e in errs)

    if details:
        print("check_concept_source_support: details")
        for line in details:
            print(line)
    if warnings:
        print("check_concept_source_support: warnings")
        for line in warnings:
            print(f"  - {line}")

    print(
        f"check_concept_source_support: concepts={len(concepts)} "
        f"ok={len(concepts) - failed} failed={failed} warnings={len(warnings)}"
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
