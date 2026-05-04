#!/usr/bin/env python3
"""Warn about graph-visible pages with no incoming wikilinks.

Graph-visible pages are:

- wiki/source/*.md
- wiki/concept/*.md
- wiki/insight/*.md
- wiki/summary/*.md

The script warns, but does not fail, for zero incoming graph-visible links.
It fails only when a bounded source page has no incoming link from its source
hub, previous/next source page, or wiki/meta/index.md.
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
GRAPH_DIRS = ("source", "concept", "insight", "summary")
META_INDEX = WIKI_ROOT / "meta" / "index.md"
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


def collect_graph_pages() -> List[Path]:
    out: List[Path] = []
    for dirname in GRAPH_DIRS:
        out.extend(collect_markdown_files(WIKI_ROOT / dirname))
    return sorted(out)


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


def page_frontmatter(path: Path) -> Dict[str, object]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    fm, _ = FM.extract_frontmatter(text)
    return fm if isinstance(fm, dict) else {}


def page_keys(path: Path, fm: Dict[str, object]) -> Set[str]:
    keys = {
        path.stem,
        path.relative_to(WIKI_ROOT).with_suffix("").as_posix(),
    }
    if isinstance(fm.get("id"), str) and fm["id"]:
        keys.add(str(fm["id"]))
    return keys


def build_registry(pages: List[Path]) -> Tuple[Dict[str, Path], Dict[Path, Dict[str, object]]]:
    registry: Dict[str, Path] = {}
    metadata: Dict[Path, Dict[str, object]] = {}
    for path in pages:
        fm = page_frontmatter(path)
        metadata[path] = fm
        for key in page_keys(path, fm):
            registry[key] = path
    return registry, metadata


def build_incoming(
    link_sources: List[Path],
    registry: Dict[str, Path],
) -> Dict[Path, Set[Path]]:
    incoming: Dict[Path, Set[Path]] = {path: set() for path in set(registry.values())}
    for source in link_sources:
        try:
            text = source.read_text(encoding="utf-8")
        except OSError:
            continue
        for target in wikilinks(text):
            dest = registry.get(target)
            if dest is not None and dest != source:
                incoming.setdefault(dest, set()).add(source)
    return incoming


def is_source_hub(path: Path, fm: Dict[str, object]) -> bool:
    return path.parent == WIKI_ROOT / "source" and fm.get("type") == "summary"


def is_bounded_source(path: Path, fm: Dict[str, object]) -> bool:
    return path.parent == WIKI_ROOT / "source" and fm.get("type") == "source"


def is_allowed_source_incoming(path: Path, fm: Dict[str, object]) -> bool:
    if path == META_INDEX:
        return True
    if path.parent != WIKI_ROOT / "source":
        return False
    page_type = fm.get("type")
    return page_type in {"summary", "source"}


def main() -> int:
    pages = collect_graph_pages()
    registry, metadata = build_registry(pages)

    graph_incoming = build_incoming(pages, registry)
    hard_sources = pages + ([META_INDEX] if META_INDEX.exists() else [])
    hard_incoming = build_incoming(hard_sources, registry)
    source_metadata = {path: page_frontmatter(path) for path in hard_sources}

    warnings: List[str] = []
    hard_failures: List[str] = []

    for path in pages:
        rel = path.relative_to(REPO_ROOT)
        fm = metadata.get(path, {})
        graph_count = len(graph_incoming.get(path, set()))
        if graph_count == 0:
            meta_index_links = META_INDEX in hard_incoming.get(path, set())
            if not (is_source_hub(path, fm) and meta_index_links):
                warnings.append(f"{rel}: zero incoming graph-visible wikilinks")

        if is_bounded_source(path, fm):
            allowed = [
                src
                for src in hard_incoming.get(path, set())
                if is_allowed_source_incoming(src, source_metadata.get(src, {}))
            ]
            if not allowed:
                hard_failures.append(
                    f"{rel}: bounded source page has no incoming link from "
                    "source hub, adjacent source page, or wiki/meta/index.md"
                )

    if warnings:
        print("check_orphans: warnings")
        for line in warnings:
            print(f"  - {line}")
    if hard_failures:
        print("check_orphans: details")
        for line in hard_failures:
            print(f"  - {line}")

    print(
        f"check_orphans: pages={len(pages)} warnings={len(warnings)} "
        f"hard_failures={len(hard_failures)}"
    )
    return 0 if not hard_failures else 1


if __name__ == "__main__":
    sys.exit(main())
