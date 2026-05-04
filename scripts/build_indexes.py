#!/usr/bin/env python3
"""Build rebuildable JSONL indexes from RENO markdown and processed metadata.

Generated indexes are derived views only. They intentionally omit full markdown
bodies and chunk text; markdown pages, processed chunks, and manifests remain
the source of truth.

Outputs under structured/indexes/:

- files.jsonl
- chunks.jsonl
- sources.jsonl
- concepts.jsonl
- insights.jsonl
- links.jsonl
- manifest_slices.jsonl

Uses Python stdlib only.
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_ROOT = REPO_ROOT / "wiki"
PROCESSED_ROOT = REPO_ROOT / "processed"
INDEX_ROOT = REPO_ROOT / "structured" / "indexes"
FRONTMATTER_VALIDATOR = REPO_ROOT / "scripts" / "validate_frontmatter.py"

GRAPH_DIRS = ("source", "concept", "insight", "summary", "meta")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


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


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


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


def graph_markdown_files() -> List[Path]:
    out: List[Path] = []
    for dirname in GRAPH_DIRS:
        out.extend(collect_markdown_files(WIKI_ROOT / dirname))
    return sorted(out, key=rel)


def all_wiki_markdown_files() -> List[Path]:
    return sorted(collect_markdown_files(WIKI_ROOT), key=rel)


def split_body(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1 :])
    return text


def word_count(text: str) -> int:
    return len([word for word in text.split() if word])


def h1_title(body: str) -> Optional[str]:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# ") and stripped[2:].strip():
            return stripped[2:].strip()
    return None


def page_data(path: Path) -> Tuple[Dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    fm, parse_errors = FM.extract_frontmatter(text)
    if parse_errors:
        raise ValueError(f"{rel(path)}: frontmatter parse errors: {parse_errors}")
    if fm is None or not isinstance(fm, dict):
        raise ValueError(f"{rel(path)}: missing or invalid frontmatter")
    return fm, split_body(text)


def title_for(fm: Dict[str, Any], body: str) -> Optional[str]:
    title = fm.get("title")
    if isinstance(title, str) and title:
        return title
    return h1_title(body)


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


def strip_inline_code(text: str) -> str:
    return INLINE_CODE_RE.sub("", text)


def normalize_target(raw: str) -> str:
    return raw.split("|", 1)[0].split("#", 1)[0].strip()


def wikilinks(text: str) -> List[str]:
    out: List[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in WIKILINK_RE.finditer(strip_inline_code(line)):
            target = normalize_target(match.group(1))
            if target:
                out.append(target)
    return out


def page_keys(path: Path, fm: Dict[str, Any]) -> Set[str]:
    keys = {
        path.stem,
        path.relative_to(WIKI_ROOT).with_suffix("").as_posix(),
    }
    if isinstance(fm.get("id"), str) and fm["id"]:
        keys.add(fm["id"])
    return keys


def build_page_registry(files: Iterable[Path]) -> Tuple[Dict[str, Path], Dict[Path, Dict[str, Any]]]:
    registry: Dict[str, Path] = {}
    metadata: Dict[Path, Dict[str, Any]] = {}
    duplicates: List[str] = []
    for path in files:
        fm, _ = page_data(path)
        metadata[path] = fm
        for key in page_keys(path, fm):
            if key in registry and registry[key] != path:
                duplicates.append(
                    f"registry key {key!r} maps to {rel(registry[key])} and {rel(path)}"
                )
            registry[key] = path
    if duplicates:
        raise ValueError("duplicate page registry keys: " + "; ".join(sorted(duplicates)))
    return registry, metadata


def build_files_records(files: List[Path]) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for path in files:
        fm, body = page_data(path)
        records.append(
            {
                "path": rel(path),
                "id": fm.get("id"),
                "type": fm.get("type"),
                "status": fm.get("status"),
                "phase": fm.get("phase"),
                "title": title_for(fm, body),
                "parent": fm.get("parent"),
                "prev": fm.get("prev"),
                "next": fm.get("next"),
            }
        )
    records.extend(build_processed_file_records())
    return sorted(records, key=lambda r: (str(r.get("path")), str(r.get("id"))))


def manifest_paths() -> List[Path]:
    if not PROCESSED_ROOT.exists():
        return []
    paths: List[Path] = []
    for source_dir in sorted(PROCESSED_ROOT.iterdir()):
        if not source_dir.is_dir() or source_dir.name.startswith("."):
            continue
        path = source_dir / "manifest.json"
        if path.exists():
            paths.append(path)
    return sorted(paths, key=rel)


def parse_paths() -> List[Path]:
    if not PROCESSED_ROOT.exists():
        return []
    paths: List[Path] = []
    for source_dir in sorted(PROCESSED_ROOT.iterdir()):
        if not source_dir.is_dir() or source_dir.name.startswith("."):
            continue
        parses_dir = source_dir / "parses"
        if not parses_dir.exists():
            continue
        paths.extend(sorted(parses_dir.glob("*.json")))
    return sorted(paths, key=rel)


def load_json(path: Path) -> Dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{rel(path)}: could not read JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{rel(path)}: expected JSON object")
    return data


def load_manifests() -> List[Tuple[Path, Dict[str, Any]]]:
    return [(path, load_json(path)) for path in manifest_paths()]


def source_id_from_processed_path(path: Path) -> Optional[str]:
    try:
        rel_parts = path.relative_to(PROCESSED_ROOT).parts
    except ValueError:
        return None
    return rel_parts[0] if rel_parts else None


def manifest_slice_records() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for manifest_path, manifest in load_manifests():
        source_id = source_id_from_processed_path(manifest_path)
        slices = manifest.get("slices", [])
        if not isinstance(slices, list):
            raise ValueError(f"{rel(manifest_path)}: manifest.slices must be a list")
        for slice_entry in slices:
            if not isinstance(slice_entry, dict):
                raise ValueError(f"{rel(manifest_path)}: manifest.slices entry must be an object")
            records.append(
                {
                    "source_id": source_id,
                    "processed_id": manifest.get("processed_id"),
                    "raw_id": manifest.get("raw_id"),
                    "slice_id": slice_entry.get("slice_id"),
                    "page_range": slice_entry.get("page_range"),
                    "section_range": slice_entry.get("section_range"),
                    "parse_path": slice_entry.get("parse_path"),
                    "chunk_ids": slice_entry.get("chunk_ids"),
                    "chunk_count": slice_entry.get("chunk_count"),
                    "page_start": slice_entry.get("page_start"),
                    "page_end": slice_entry.get("page_end"),
                    "parser": slice_entry.get("parser", manifest.get("parser")),
                    "parser_version": slice_entry.get(
                        "parser_version", manifest.get("parser_version")
                    ),
                    "parser_command": slice_entry.get(
                        "parser_command", manifest.get("parser_command")
                    ),
                    "manifest_path": rel(manifest_path),
                }
            )
    return sorted(
        records,
        key=lambda r: (
            str(r.get("source_id")),
            str(r.get("page_start")),
            str(r.get("slice_id")),
        ),
    )


def parse_slice_lookup() -> Dict[str, Dict[str, Any]]:
    lookup: Dict[str, Dict[str, Any]] = {}
    for record in manifest_slice_records():
        parse_path = record.get("parse_path")
        if isinstance(parse_path, str) and parse_path:
            lookup[parse_path] = record
    return lookup


def build_processed_file_records() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    slice_lookup = parse_slice_lookup()

    for manifest_path, manifest in load_manifests():
        source_id = source_id_from_processed_path(manifest_path)
        records.append(
            {
                "path": rel(manifest_path),
                "kind": "manifest",
                "source_id": source_id,
                "processed_id": manifest.get("processed_id"),
                "raw_id": manifest.get("raw_id"),
                "chunk_id": None,
                "slice_id": None,
                "page_start": None,
                "page_end": None,
                "page_range": manifest.get("page_range"),
                "section_range": manifest.get("section_range"),
            }
        )

    for path in chunk_paths():
        data = load_json(path)
        records.append(
            {
                "path": rel(path),
                "kind": "chunk",
                "source_id": data.get("source_id", source_id_from_processed_path(path)),
                "processed_id": data.get("processed_id"),
                "raw_id": data.get("raw_id"),
                "chunk_id": data.get("chunk_id", path.stem),
                "slice_id": None,
                "page_start": data.get("page_start"),
                "page_end": data.get("page_end"),
                "page_range": None,
                "section_range": None,
            }
        )

    for path in parse_paths():
        path_rel = rel(path)
        slice_record = slice_lookup.get(path_rel, {})
        records.append(
            {
                "path": path_rel,
                "kind": "parse",
                "source_id": slice_record.get(
                    "source_id", source_id_from_processed_path(path)
                ),
                "processed_id": slice_record.get("processed_id"),
                "raw_id": slice_record.get("raw_id"),
                "chunk_id": None,
                "slice_id": slice_record.get("slice_id"),
                "page_start": slice_record.get("page_start"),
                "page_end": slice_record.get("page_end"),
                "page_range": slice_record.get("page_range"),
                "section_range": slice_record.get("section_range"),
            }
        )

    return sorted(records, key=lambda r: (str(r.get("path")), str(r.get("kind"))))


def chunk_paths() -> List[Path]:
    if not PROCESSED_ROOT.exists():
        return []
    paths: List[Path] = []
    for source_dir in sorted(PROCESSED_ROOT.iterdir()):
        if not source_dir.is_dir() or source_dir.name.startswith("."):
            continue
        chunks_dir = source_dir / "chunks"
        if not chunks_dir.exists():
            continue
        paths.extend(sorted(chunks_dir.glob("*.json")))
    return sorted(paths, key=rel)


def build_chunks_records() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for path in chunk_paths():
        data = load_json(path)
        records.append(
            {
                "chunk_id": data.get("chunk_id", path.stem),
                "source_id": data.get("source_id"),
                "processed_id": data.get("processed_id"),
                "raw_id": data.get("raw_id"),
                "path": rel(path),
                "page_start": data.get("page_start"),
                "page_end": data.get("page_end"),
                "token_estimate": data.get("token_estimate"),
                "prev_chunk_id": data.get("prev_chunk_id"),
                "next_chunk_id": data.get("next_chunk_id"),
                "content_hash": data.get("content_hash"),
                "review_status": data.get("review_status"),
            }
        )
    return sorted(records, key=lambda r: (str(r.get("path")), str(r.get("chunk_id"))))


def build_sources_records() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for path in collect_markdown_files(WIKI_ROOT / "source"):
        fm, body = page_data(path)
        record = {
            "path": rel(path),
            "id": fm.get("id"),
            "type": fm.get("type"),
            "status": fm.get("status"),
            "phase": fm.get("phase"),
            "source_id": fm.get("source_id"),
            "raw_id": fm.get("raw_id"),
            "processed_ids": fm.get("processed_ids"),
            "chunk_ids": fm.get("chunk_ids"),
            "title": title_for(fm, body),
            "source_kind": fm.get("source_kind"),
            "section_range": fm.get("section_range"),
            "parent": fm.get("parent"),
            "prev": fm.get("prev"),
            "next": fm.get("next"),
            "body_word_count": word_count(body),
        }
        records.append(record)
    return sorted(records, key=lambda r: (str(r.get("path")), str(r.get("id"))))


def build_concepts_records() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for path in collect_markdown_files(WIKI_ROOT / "concept"):
        fm, body = page_data(path)
        records.append(
            {
                "path": rel(path),
                "id": fm.get("id"),
                "status": fm.get("status"),
                "title": title_for(fm, body),
                "related_concepts": wikilinks(section_text(body, "## Related concepts")),
                "source_support": wikilinks(section_text(body, "## Source support")),
                "body_word_count": word_count(body),
            }
        )
    return sorted(records, key=lambda r: (str(r.get("path")), str(r.get("id"))))


def build_insights_records() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for path in collect_markdown_files(WIKI_ROOT / "insight"):
        fm, body = page_data(path)
        records.append(
            {
                "path": rel(path),
                "id": fm.get("id"),
                "status": fm.get("status"),
                "title": title_for(fm, body),
                "concepts_involved": wikilinks(section_text(body, "## Concepts involved")),
                "source_basis": wikilinks(section_text(body, "## Source basis")),
                "body_word_count": word_count(body),
            }
        )
    return sorted(records, key=lambda r: (str(r.get("path")), str(r.get("id"))))


def link_records_for_file(
    path: Path,
    registry: Dict[str, Path],
    metadata: Dict[Path, Dict[str, Any]],
) -> List[Dict[str, Any]]:
    fm, body = page_data(path)
    records: List[Dict[str, Any]] = []
    in_fence = False
    section_context: Optional[str] = None
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped.startswith("#"):
            hashes, _, rest = stripped.partition(" ")
            if hashes and set(hashes) == {"#"} and rest.strip():
                section_context = rest.strip()
        searchable = strip_inline_code(line)
        for match in WIKILINK_RE.finditer(searchable):
            raw_link = match.group(0)
            target = normalize_target(match.group(1))
            target_path = registry.get(target)
            target_fm = metadata.get(target_path, {}) if target_path is not None else {}
            records.append(
                {
                    "source_path": rel(path),
                    "source_id": fm.get("id"),
                    "source_type": fm.get("type"),
                    "target": target,
                    "target_path": rel(target_path) if target_path is not None else None,
                    "target_id": target_fm.get("id") if target_path is not None else None,
                    "target_type": target_fm.get("type") if target_path is not None else None,
                    "section_context": section_context,
                    "raw_link": raw_link,
                }
            )
    return records


def build_links_records(files: List[Path]) -> List[Dict[str, Any]]:
    registry, metadata = build_page_registry(all_wiki_markdown_files())
    records: List[Dict[str, Any]] = []
    for path in files:
        records.extend(link_records_for_file(path, registry, metadata))
    return sorted(
        records,
        key=lambda r: (
            str(r.get("source_path")),
            str(r.get("section_context")),
            str(r.get("target")),
            str(r.get("raw_link")),
        ),
    )


def write_jsonl(path: Path, records: List[Dict[str, Any]]) -> None:
    tmp_path = path.with_name(path.name + ".tmp")
    with tmp_path.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, sort_keys=True, ensure_ascii=False))
            fh.write("\n")
    tmp_path.replace(path)


def main() -> int:
    try:
        INDEX_ROOT.mkdir(parents=True, exist_ok=True)
        files = graph_markdown_files()
        files_records = build_files_records(files)
        chunks_records = build_chunks_records()
        sources_records = build_sources_records()
        concepts_records = build_concepts_records()
        insights_records = build_insights_records()
        links_records = build_links_records(all_wiki_markdown_files())
        manifest_slices_records = manifest_slice_records()

        outputs = {
            "files.jsonl": files_records,
            "chunks.jsonl": chunks_records,
            "sources.jsonl": sources_records,
            "concepts.jsonl": concepts_records,
            "insights.jsonl": insights_records,
            "links.jsonl": links_records,
            "manifest_slices.jsonl": manifest_slices_records,
        }
        for name in sorted(outputs):
            write_jsonl(INDEX_ROOT / name, outputs[name])
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"build_indexes: error: {exc}", file=sys.stderr)
        return 1

    print(
        f"build_indexes: files={len(files_records)} chunks={len(chunks_records)} "
        f"sources={len(sources_records)} concepts={len(concepts_records)} "
        f"insights={len(insights_records)} links={len(links_records)} "
        f"slices={len(manifest_slices_records)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
