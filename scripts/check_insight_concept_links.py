#!/usr/bin/env python3
"""Check that insight pages link contributing concepts and source pages.

Rules:

- scan wiki/insight/*.md recursively
- require ## Concepts involved with at least two wikilinks
- every Concepts involved wikilink must resolve to wiki/concept/*.md
- require ## Source basis with at least one wikilink
- every Source basis wikilink must resolve to wiki/source/*.md

Uses Python stdlib only and reuses validate_frontmatter.py for frontmatter ids.
"""

from __future__ import annotations

import importlib.util
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_ROOT = REPO_ROOT / "wiki"
CONCEPT_ROOT = WIKI_ROOT / "concept"
INSIGHT_ROOT = WIKI_ROOT / "insight"
SOURCE_ROOT = WIKI_ROOT / "source"
FRONTMATTER_VALIDATOR = REPO_ROOT / "scripts" / "validate_frontmatter.py"

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
    out: List[str] = []
    for match in WIKILINK_RE.finditer(strip_code(text)):
        target = normalize_target(match.group(1))
        if target:
            out.append(target)
    return out


def build_registry(root: Path) -> Dict[str, Path]:
    registry: Dict[str, Path] = {}
    for path in collect_markdown_files(root):
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


def validate_one(
    path: Path,
    concept_registry: Dict[str, Path],
    source_registry: Dict[str, Path],
) -> List[str]:
    rel = path.relative_to(REPO_ROOT)
    errors: List[str] = []

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: could not read: {exc}"]

    body = split_body(text)
    concepts_section = section_text(body, "## Concepts involved")
    if not concepts_section:
        errors.append(f"{rel}: missing required section '## Concepts involved'")
    concept_links = wikilinks(concepts_section)
    if len(concept_links) < 2:
        errors.append(
            f"{rel}: Concepts involved must contain at least two wikilinks"
        )
    for target in concept_links:
        if target not in concept_registry:
            errors.append(
                f"{rel}: Concepts involved wikilink [[{target}]] does not "
                "resolve to wiki/concept/*.md"
            )

    source_section = section_text(body, "## Source basis")
    if not source_section:
        errors.append(f"{rel}: missing required section '## Source basis'")
    source_links = wikilinks(source_section)
    if not source_links:
        errors.append(f"{rel}: Source basis must contain at least one wikilink")
    for target in source_links:
        if target not in source_registry:
            errors.append(
                f"{rel}: Source basis wikilink [[{target}]] does not resolve "
                "to wiki/source/*.md"
            )

    return errors


def main() -> int:
    insights = collect_markdown_files(INSIGHT_ROOT)
    concept_registry = build_registry(CONCEPT_ROOT)
    source_registry = build_registry(SOURCE_ROOT)

    failed = 0
    details: List[str] = []
    for path in insights:
        errs = validate_one(path, concept_registry, source_registry)
        if errs:
            failed += 1
            details.extend(f"  - {e}" for e in errs)

    if details:
        print("check_insight_concept_links: details")
        for line in details:
            print(line)

    print(
        f"check_insight_concept_links: insights={len(insights)} "
        f"ok={len(insights) - failed} failed={failed}"
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
