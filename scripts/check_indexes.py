#!/usr/bin/env python3
"""Validate structured/indexes/*.jsonl against current repository state.

This script checks existing generated indexes only. It does not rebuild or
repair them; stale or malformed rows fail the run so scripts/build_indexes.py
can be run explicitly.

Uses Python stdlib only and reuses validate_frontmatter.py for the repository's
small frontmatter subset.
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_ROOT = REPO_ROOT / "wiki"
PROCESSED_ROOT = REPO_ROOT / "processed"
INDEX_ROOT = REPO_ROOT / "structured" / "indexes"
FRONTMATTER_VALIDATOR = REPO_ROOT / "scripts" / "validate_frontmatter.py"

GRAPH_DIRS = ("source", "concept", "insight", "summary", "meta")
REQUIRED_INDEXES = (
    "files.jsonl",
    "chunks.jsonl",
    "sources.jsonl",
    "concepts.jsonl",
    "insights.jsonl",
    "links.jsonl",
    "manifest_slices.jsonl",
)
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


def repo_path(path_string: str) -> Path:
    return REPO_ROOT / path_string


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
    paths: List[Path] = []
    for dirname in GRAPH_DIRS:
        paths.extend(collect_markdown_files(WIKI_ROOT / dirname))
    return sorted(paths, key=rel)


def all_wiki_markdown_files() -> List[Path]:
    return sorted(collect_markdown_files(WIKI_ROOT), key=rel)


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


def chunk_paths() -> List[Path]:
    if not PROCESSED_ROOT.exists():
        return []
    paths: List[Path] = []
    for source_dir in sorted(PROCESSED_ROOT.iterdir()):
        if not source_dir.is_dir() or source_dir.name.startswith("."):
            continue
        chunks_dir = source_dir / "chunks"
        if chunks_dir.exists():
            paths.extend(sorted(chunks_dir.glob("*.json")))
    return sorted(paths, key=rel)


def parse_paths() -> List[Path]:
    if not PROCESSED_ROOT.exists():
        return []
    paths: List[Path] = []
    for source_dir in sorted(PROCESSED_ROOT.iterdir()):
        if not source_dir.is_dir() or source_dir.name.startswith("."):
            continue
        parses_dir = source_dir / "parses"
        if parses_dir.exists():
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


def read_jsonl(name: str, errors: List[str]) -> List[Dict[str, Any]]:
    path = INDEX_ROOT / name
    if not path.exists():
        errors.append(f"missing required index {rel(path)}")
        return []
    records: List[Dict[str, Any]] = []
    try:
        with path.open("r", encoding="utf-8") as fh:
            for line_no, line in enumerate(fh, start=1):
                if not line.strip():
                    errors.append(f"{rel(path)}:{line_no}: blank JSONL line")
                    continue
                try:
                    value = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(f"{rel(path)}:{line_no}: malformed JSON: {exc}")
                    continue
                if not isinstance(value, dict):
                    errors.append(f"{rel(path)}:{line_no}: row is not a JSON object")
                    continue
                records.append(value)
    except OSError as exc:
        errors.append(f"{rel(path)}: could not read: {exc}")
    return records


def split_body(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1 :])
    return text


def page_data(path: Path) -> Tuple[Dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    fm, parse_errors = FM.extract_frontmatter(text)
    if parse_errors:
        raise ValueError(f"{rel(path)}: frontmatter parse errors: {parse_errors}")
    if fm is None or not isinstance(fm, dict):
        raise ValueError(f"{rel(path)}: missing or invalid frontmatter")
    return fm, split_body(text)


def h1_title(body: str) -> Optional[str]:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# ") and stripped[2:].strip():
            return stripped[2:].strip()
    return None


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


def word_count(text: str) -> int:
    return len([word for word in text.split() if word])


def source_id_from_processed_path(path: Path) -> Optional[str]:
    try:
        parts = path.relative_to(PROCESSED_ROOT).parts
    except ValueError:
        return None
    return parts[0] if parts else None


def index_by_path(
    records: List[Dict[str, Any]],
    index_name: str,
    errors: List[str],
) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    counts = Counter(str(record.get("path")) for record in records)
    for path, count in sorted(counts.items()):
        if count > 1:
            errors.append(f"{index_name}: duplicate path record {path!r} count={count}")
    for record in records:
        path = record.get("path")
        if not isinstance(path, str) or not path:
            errors.append(f"{index_name}: record missing non-empty string path")
            continue
        out[path] = record
    return out


def compare_field(
    errors: List[str],
    context: str,
    record: Dict[str, Any],
    expected: Dict[str, Any],
    key: str,
) -> None:
    if record.get(key) != expected.get(key):
        errors.append(
            f"{context}: field {key!r} stale: "
            f"index={record.get(key)!r} expected={expected.get(key)!r}"
        )


def check_files_index(records: List[Dict[str, Any]], errors: List[str]) -> None:
    by_path = index_by_path(records, "files.jsonl", errors)
    expected_paths = {rel(path) for path in graph_markdown_files()}
    expected_paths |= {rel(path) for path in manifest_paths()}
    expected_paths |= {rel(path) for path in chunk_paths()}
    expected_paths |= {rel(path) for path in parse_paths()}
    actual_paths = set(by_path)

    for path in sorted(expected_paths - actual_paths):
        errors.append(f"files.jsonl: missing expected path {path}")
    for path in sorted(actual_paths - expected_paths):
        errors.append(f"files.jsonl: unexpected path {path}")
    for path in sorted(actual_paths):
        if not repo_path(path).exists():
            errors.append(f"files.jsonl: path no longer exists: {path}")


def check_chunks_index(records: List[Dict[str, Any]], errors: List[str]) -> None:
    by_path = index_by_path(records, "chunks.jsonl", errors)
    expected_paths = {rel(path) for path in chunk_paths()}
    actual_paths = set(by_path)
    for path in sorted(expected_paths - actual_paths):
        errors.append(f"chunks.jsonl: missing chunk record for {path}")
    for path in sorted(actual_paths - expected_paths):
        errors.append(f"chunks.jsonl: unexpected chunk record for {path}")

    fields = (
        "chunk_id",
        "source_id",
        "processed_id",
        "raw_id",
        "page_start",
        "page_end",
        "prev_chunk_id",
        "next_chunk_id",
        "content_hash",
        "token_estimate",
    )
    for path in sorted(actual_paths & expected_paths):
        chunk_path = repo_path(path)
        if not chunk_path.exists():
            errors.append(f"chunks.jsonl: path no longer exists: {path}")
            continue
        data = load_json(chunk_path)
        record = by_path[path]
        for key in fields:
            compare_field(errors, f"chunks.jsonl:{path}", record, data, key)


def expected_manifest_slice_records() -> Dict[Tuple[str, str], Dict[str, Any]]:
    expected: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for manifest_path in manifest_paths():
        manifest = load_json(manifest_path)
        source_id = source_id_from_processed_path(manifest_path)
        slices = manifest.get("slices", [])
        if not isinstance(slices, list):
            raise ValueError(f"{rel(manifest_path)}: manifest.slices must be a list")
        for slice_entry in slices:
            if not isinstance(slice_entry, dict):
                raise ValueError(f"{rel(manifest_path)}: manifest.slices entry is not an object")
            record = {
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
            expected[(record["manifest_path"], str(record["slice_id"]))] = record
    return expected


def check_manifest_slices_index(records: List[Dict[str, Any]], errors: List[str]) -> None:
    expected = expected_manifest_slice_records()
    actual: Dict[Tuple[str, str], Dict[str, Any]] = {}
    counts: Counter[Tuple[str, str]] = Counter()
    for record in records:
        key = (str(record.get("manifest_path")), str(record.get("slice_id")))
        counts[key] += 1
        actual[key] = record
    for key, count in sorted(counts.items()):
        if count > 1:
            errors.append(f"manifest_slices.jsonl: duplicate slice record {key} count={count}")
    for key in sorted(set(expected) - set(actual)):
        errors.append(f"manifest_slices.jsonl: missing slice record {key}")
    for key in sorted(set(actual) - set(expected)):
        errors.append(f"manifest_slices.jsonl: unexpected slice record {key}")

    fields = (
        "source_id",
        "processed_id",
        "raw_id",
        "slice_id",
        "page_range",
        "section_range",
        "parse_path",
        "chunk_ids",
        "chunk_count",
        "page_start",
        "page_end",
        "parser",
        "parser_version",
        "parser_command",
        "manifest_path",
    )
    for key in sorted(set(expected) & set(actual)):
        record = actual[key]
        exp = expected[key]
        manifest_path = record.get("manifest_path")
        if not isinstance(manifest_path, str) or not repo_path(manifest_path).exists():
            errors.append(f"manifest_slices.jsonl:{key}: manifest_path does not exist")
        parse_path = record.get("parse_path")
        if not isinstance(parse_path, str) or not repo_path(parse_path).exists():
            errors.append(f"manifest_slices.jsonl:{key}: parse_path does not exist")
        for chunk_id in record.get("chunk_ids") or []:
            source_id = record.get("source_id")
            if not isinstance(source_id, str) or not isinstance(chunk_id, str):
                errors.append(f"manifest_slices.jsonl:{key}: invalid chunk_ids/source_id")
                continue
            chunk_path = PROCESSED_ROOT / source_id / "chunks" / f"{chunk_id}.json"
            if not chunk_path.exists():
                errors.append(
                    f"manifest_slices.jsonl:{key}: chunk_id {chunk_id!r} "
                    f"does not exist at {rel(chunk_path)}"
                )
        for field in fields:
            compare_field(errors, f"manifest_slices.jsonl:{key}", record, exp, field)


def check_sources_index(records: List[Dict[str, Any]], errors: List[str]) -> None:
    by_path = index_by_path(records, "sources.jsonl", errors)
    expected_paths = {rel(path) for path in collect_markdown_files(WIKI_ROOT / "source")}
    actual_paths = set(by_path)
    for path in sorted(expected_paths - actual_paths):
        errors.append(f"sources.jsonl: missing source record for {path}")
    for path in sorted(actual_paths - expected_paths):
        errors.append(f"sources.jsonl: unexpected source record for {path}")

    fields = ("id", "type", "status", "phase", "source_id", "parent", "prev", "next", "title")
    for path in sorted(actual_paths & expected_paths):
        page_path = repo_path(path)
        if not page_path.exists():
            errors.append(f"sources.jsonl: path no longer exists: {path}")
            continue
        fm, body = page_data(page_path)
        expected = {key: fm.get(key) for key in fields if key != "title"}
        expected["title"] = title_for(fm, body)
        if "chunk_ids" in fm:
            expected["chunk_ids"] = fm.get("chunk_ids")
        record = by_path[path]
        for field in fields:
            compare_field(errors, f"sources.jsonl:{path}", record, expected, field)
        if "chunk_ids" in fm:
            compare_field(errors, f"sources.jsonl:{path}", record, expected, "chunk_ids")


def check_concepts_index(records: List[Dict[str, Any]], errors: List[str]) -> None:
    by_path = index_by_path(records, "concepts.jsonl", errors)
    expected_paths = {rel(path) for path in collect_markdown_files(WIKI_ROOT / "concept")}
    actual_paths = set(by_path)
    for path in sorted(expected_paths - actual_paths):
        errors.append(f"concepts.jsonl: missing concept record for {path}")
    for path in sorted(actual_paths - expected_paths):
        errors.append(f"concepts.jsonl: unexpected concept record for {path}")

    for path in sorted(actual_paths & expected_paths):
        page_path = repo_path(path)
        if not page_path.exists():
            errors.append(f"concepts.jsonl: path no longer exists: {path}")
            continue
        fm, body = page_data(page_path)
        expected = {
            "id": fm.get("id"),
            "status": fm.get("status"),
            "title": title_for(fm, body),
            "related_concepts": wikilinks(section_text(body, "## Related concepts")),
            "source_support": wikilinks(section_text(body, "## Source support")),
        }
        for field in expected:
            compare_field(errors, f"concepts.jsonl:{path}", by_path[path], expected, field)


def check_insights_index(records: List[Dict[str, Any]], errors: List[str]) -> None:
    by_path = index_by_path(records, "insights.jsonl", errors)
    expected_paths = {rel(path) for path in collect_markdown_files(WIKI_ROOT / "insight")}
    actual_paths = set(by_path)
    for path in sorted(expected_paths - actual_paths):
        errors.append(f"insights.jsonl: missing insight record for {path}")
    for path in sorted(actual_paths - expected_paths):
        errors.append(f"insights.jsonl: unexpected insight record for {path}")

    for path in sorted(actual_paths & expected_paths):
        page_path = repo_path(path)
        if not page_path.exists():
            errors.append(f"insights.jsonl: path no longer exists: {path}")
            continue
        fm, body = page_data(page_path)
        expected = {
            "id": fm.get("id"),
            "status": fm.get("status"),
            "title": title_for(fm, body),
            "concepts_involved": wikilinks(section_text(body, "## Concepts involved")),
            "source_basis": wikilinks(section_text(body, "## Source basis")),
        }
        for field in expected:
            compare_field(errors, f"insights.jsonl:{path}", by_path[path], expected, field)


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
    for path in files:
        fm, _ = page_data(path)
        metadata[path] = fm
        for key in page_keys(path, fm):
            registry[key] = path
    return registry, metadata


def fresh_link_records() -> List[Dict[str, Any]]:
    registry, metadata = build_page_registry(all_wiki_markdown_files())
    records: List[Dict[str, Any]] = []
    for path in all_wiki_markdown_files():
        fm, body = page_data(path)
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
            for match in WIKILINK_RE.finditer(strip_inline_code(line)):
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
    return sorted(
        records,
        key=lambda row: (
            str(row.get("source_path")),
            str(row.get("section_context")),
            str(row.get("target")),
            str(row.get("raw_link")),
        ),
    )


def comparable_rows(rows: List[Dict[str, Any]]) -> List[str]:
    return sorted(json.dumps(row, sort_keys=True, ensure_ascii=False) for row in rows)


def check_links_index(records: List[Dict[str, Any]], errors: List[str]) -> None:
    for i, record in enumerate(records, start=1):
        source_path = record.get("source_path")
        if not isinstance(source_path, str) or not repo_path(source_path).exists():
            errors.append(f"links.jsonl:{i}: source_path does not exist: {source_path!r}")
        target_path = record.get("target_path") or record.get("target_resolved_path")
        if target_path is None:
            errors.append(f"links.jsonl:{i}: unresolved target_path for {record.get('raw_link')!r}")
        elif not isinstance(target_path, str) or not repo_path(target_path).exists():
            errors.append(f"links.jsonl:{i}: target_path does not exist: {target_path!r}")

    expected = fresh_link_records()
    if len(records) != len(expected):
        errors.append(
            f"links.jsonl: link count stale: index={len(records)} expected={len(expected)}"
        )
    if comparable_rows(records) != comparable_rows(expected):
        errors.append("links.jsonl: records do not match fresh wiki wikilink scan")


def main() -> int:
    errors: List[str] = []
    indexes = {name: read_jsonl(name, errors) for name in REQUIRED_INDEXES}

    try:
        check_files_index(indexes["files.jsonl"], errors)
        check_chunks_index(indexes["chunks.jsonl"], errors)
        check_manifest_slices_index(indexes["manifest_slices.jsonl"], errors)
        check_sources_index(indexes["sources.jsonl"], errors)
        check_concepts_index(indexes["concepts.jsonl"], errors)
        check_insights_index(indexes["insights.jsonl"], errors)
        check_links_index(indexes["links.jsonl"], errors)
    except (OSError, ValueError, RuntimeError) as exc:
        errors.append(str(exc))

    if errors:
        print("check_indexes: details")
        for error in errors:
            print(f"  - {error}")

    print(
        f"check_indexes: files={len(indexes['files.jsonl'])} "
        f"chunks={len(indexes['chunks.jsonl'])} "
        f"sources={len(indexes['sources.jsonl'])} "
        f"concepts={len(indexes['concepts.jsonl'])} "
        f"insights={len(indexes['insights.jsonl'])} "
        f"links={len(indexes['links.jsonl'])} "
        f"slices={len(indexes['manifest_slices.jsonl'])} "
        f"errors={len(errors)}"
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
