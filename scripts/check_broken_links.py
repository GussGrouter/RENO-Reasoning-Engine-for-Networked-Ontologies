#!/usr/bin/env python3
"""Validate Obsidian wikilinks across wiki/.

Rules:

- scan all .md files under wiki/
- build a page registry from filename stems, frontmatter ids, and paths relative
  to wiki/ without the .md suffix
- resolve [[target]], [[target|alias]], [[target#heading]], and
  [[target#heading|alias]] by stripping alias and heading
- ignore links inside code spans and fenced code blocks
- fail on duplicate registry keys and unresolved wikilinks

Uses Python stdlib only and reuses the lightweight frontmatter parser from
validate_frontmatter.py so id parsing stays consistent with other validators.
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


def strip_code(text: str) -> str:
    text = FENCED_CODE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def normalize_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return target.strip()


def page_keys(path: Path, text: str) -> Set[str]:
    keys = {path.stem}
    rel_no_suffix = path.relative_to(WIKI_ROOT).with_suffix("").as_posix()
    keys.add(rel_no_suffix)

    fm, _ = FM.extract_frontmatter(text)
    if isinstance(fm, dict) and isinstance(fm.get("id"), str) and fm["id"]:
        keys.add(fm["id"])
    return keys


def build_registry(files: List[Path]) -> Tuple[Set[str], Dict[str, List[Path]]]:
    registry: Set[str] = set()
    aliases: Dict[str, List[Path]] = {}
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        for key in page_keys(path, text):
            registry.add(key)
            aliases.setdefault(key, []).append(path)
    return registry, aliases


def duplicate_details(aliases: Dict[str, List[Path]]) -> List[str]:
    details: List[str] = []
    for key in sorted(aliases):
        unique_paths = sorted(set(aliases[key]))
        if len(unique_paths) <= 1:
            continue
        rels = ", ".join(str(path.relative_to(REPO_ROOT)) for path in unique_paths)
        details.append(f"registry key {key!r} maps to multiple files: {rels}")
    return details


def main() -> int:
    files = collect_markdown_files(WIKI_ROOT)
    registry, aliases = build_registry(files)
    duplicates = duplicate_details(aliases)

    total_links = 0
    unresolved: List[str] = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            unresolved.append(f"{path.relative_to(REPO_ROOT)}: could not read: {exc}")
            continue

        for match in WIKILINK_RE.finditer(strip_code(text)):
            total_links += 1
            target = normalize_target(match.group(1))
            if not target:
                unresolved.append(f"{path.relative_to(REPO_ROOT)}: empty wikilink target")
            elif target not in registry:
                unresolved.append(
                    f"{path.relative_to(REPO_ROOT)}: unresolved wikilink [[{target}]]"
                )

    if unresolved:
        print("check_broken_links: details")
        for line in unresolved:
            print(f"  - {line}")
    if duplicates:
        print("check_broken_links: duplicate-key details")
        for line in duplicates:
            print(f"  - {line}")

    print(
        f"check_broken_links: files={len(files)} links={total_links} "
        f"unresolved={len(unresolved)}"
    )
    return 0 if not unresolved and not duplicates else 1


if __name__ == "__main__":
    sys.exit(main())
