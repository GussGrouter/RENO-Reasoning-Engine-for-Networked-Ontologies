#!/usr/bin/env python3
"""Generic Phase 1 chunk + manifest builder for RENO ingestion.

Reads a LiteParse parse.json and writes:

  <output-dir>/manifest.json
  <output-dir>/parses/<slice-id>.json   (promoted parse copy)
  <output-dir>/chunks/<chunk-id>.json

Schemas enforced by validate_chunk_chain.py:

  structured/schema/processed-manifest.schema.json
  structured/schema/chunk.schema.json

Phase 1 only. This script never creates source pages, concept pages,
markdown chunk cards, or anything under wiki/. It does not invoke LiteParse;
it only consumes existing parser output. Raw bytes are not modified.

Modes:

  - default (initial slice on a new source): writes a fresh manifest with a
    single slice record and the new chunk files. Refuses to overwrite any
    existing manifest, parse, or chunk file unless --force is passed.

  - --append (continuation slice on an existing source): refuses to start
    if the manifest is missing. Loads the existing manifest and chunk files,
    assigns new chunk ordinals after the current source-level maximum, sets
    the first new chunk's prev_chunk_id to the existing tail and updates the
    existing tail's next_chunk_id to the first new chunk, and appends a new
    slice record to manifest.slices. Refuses to write if --slice-id collides
    with an existing slice unless --force is passed. Refuses to overwrite
    any pre-existing chunk file or promoted parse path under any flag.

Chunking algorithm (deterministic):

  - skip pages whose stripped text is empty
  - join page text with "[page N]\\n<text>" markers, separated by "\\n\\n"
  - estimate tokens as round(words * 1.33), where words = len(text.split())
  - greedily group consecutive pages until adding the next page would push
    the cumulative token estimate above the soft target high (1500); the
    final chunk may be shorter
  - if a single page exceeds the hard max (2000 tokens), abort

Stable identifiers:

  - chunk_id = "<source-id>[-<section-slug>]-chunk-<NNNN>" with NNNN = the
    source-level ordinal (zero-padded, four digits). For initial slices the
    ordinal starts at 0001; in --append mode it continues from one past the
    current source-level maximum so older chunk IDs are never reissued. The
    section component is omitted when --section-range is "null" or "unknown".
  - processed_id = "<source-id>-processed-001"
  - raw_id       = "<source-id>-raw-001"
  - slice_id is supplied via --slice-id and stored in manifest.slices.

Usage example (initial slice):

  python3 scripts/build_phase1_chunks.py \\
      --source-id systems-performance \\
      --slice-id chapter-1-introduction-p40-55 \\
      --raw-path raw/systems-performance/Systems.Performance.Enterprise.and.the.Cloud.pdf \\
      --parse-json /tmp/parse.candidate.json \\
      --output-dir processed/systems-performance/ \\
      --source-kind book-section \\
      --title-or-origin "Systems Performance: Enterprise and the Cloud, Second Edition (Brendan Gregg)" \\
      --original-path "raw/Systems.Performance.Enterprise.and.the.Cloud.pdf" \\
      --page-range "40-55" \\
      --section-range "chapter-1-introduction" \\
      --license-copyright-status "unknown; copyrighted commercial book; not redistributed" \\
      --parser liteparse \\
      --parser-version 1.5.2 \\
      --parser-command "liteparse parse ... -o ... --format json --target-pages 40-55 --no-ocr -q" \\
      --dry-run

Usage example (continuation slice):

  python3 scripts/build_phase1_chunks.py \\
      --source-id systems-performance \\
      --slice-id chapter-2-methodologies-p72-130 \\
      --raw-path raw/systems-performance/Systems.Performance.Enterprise.and.the.Cloud.pdf \\
      --parse-json /tmp/parse.candidate.json \\
      --output-dir processed/systems-performance/ \\
      --source-kind book-section \\
      --title-or-origin "Systems Performance: Enterprise and the Cloud, Second Edition (Brendan Gregg)" \\
      --original-path "raw/Systems.Performance.Enterprise.and.the.Cloud.pdf" \\
      --page-range "72-130" \\
      --section-range "chapter-2-methodologies" \\
      --license-copyright-status "unknown; copyrighted commercial book; not redistributed" \\
      --parser liteparse \\
      --parser-version 1.5.2 \\
      --parser-command "liteparse parse ... -o ... --format json --target-pages 72-130 --no-ocr -q" \\
      --append \\
      --dry-run
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import validate_chapter_boundaries as chapter_boundaries

REPO_ROOT = Path(__file__).resolve().parent.parent

ALLOWED_SOURCE_KINDS = (
    "book-section",
    "paper-section",
    "standard-section",
    "technical-doc",
    "first-party-artifact",
    "explicit-snapshot",
)
ALLOWED_PARSERS = ("liteparse",)

TARGET_LO = 800
TARGET_HI = 1500
HARD_MAX = 2000

NULL_LITERALS = {"", "null", "none", "unknown"}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def estimate_tokens(text: str) -> int:
    """Whitespace-words * 1.33, rounded. Deterministic English-prose heuristic."""
    words = len(text.split())
    return int(round(words * 1.33))


def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\-]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def short_title(title_or_origin: str) -> str:
    """First clause of title_or_origin, used as the human-readable title prefix."""
    head = title_or_origin
    for sep in (":", " — ", " – ", " (", "("):
        if sep in head:
            head = head.split(sep, 1)[0]
    return head.strip()


def normalize_optional(value: str | None) -> str | None:
    if value is None:
        return None
    if value.strip().lower() in NULL_LITERALS:
        return None
    return value


def page_text(page: Dict[str, Any]) -> str:
    return (page.get("text") or "").strip()


def build_chunks(pages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Group consecutive non-empty pages into chunks within the token budget."""
    chunks: List[Dict[str, Any]] = []
    pending_pages: List[Dict[str, Any]] = []
    pending_parts: List[str] = []
    pending_tokens = 0

    for page in pages:
        text = page_text(page)
        if not text:
            continue
        ptokens = estimate_tokens(text)
        if ptokens > HARD_MAX:
            raise SystemExit(
                f"page {page['page']} alone has {ptokens} tokens, "
                f"exceeds hard max {HARD_MAX}; abort."
            )
        if pending_pages and pending_tokens + ptokens > TARGET_HI:
            chunks.append(
                {
                    "pages": list(pending_pages),
                    "text": "\n\n".join(pending_parts),
                    "token_estimate": pending_tokens,
                }
            )
            pending_pages = []
            pending_parts = []
            pending_tokens = 0
        pending_pages.append(page)
        pending_parts.append(f"[page {page['page']}]\n{text}")
        pending_tokens += ptokens

    if pending_pages:
        chunks.append(
            {
                "pages": list(pending_pages),
                "text": "\n\n".join(pending_parts),
                "token_estimate": pending_tokens,
            }
        )

    return chunks


CHUNK_ORDINAL_RE = re.compile(r"-chunk-(\d{4,})$")


def parse_chunk_ordinal(chunk_id: str) -> int | None:
    m = CHUNK_ORDINAL_RE.search(chunk_id)
    if not m:
        return None
    return int(m.group(1))


def load_existing_chunks(chunks_dir: Path) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    if not chunks_dir.exists():
        return out
    for path in sorted(chunks_dir.glob("*.json")):
        with path.open("r", encoding="utf-8") as fh:
            rec = json.load(fh)
        out[rec["chunk_id"]] = rec
    return out


def find_tail(chunks_by_id: Dict[str, Dict[str, Any]]) -> Dict[str, Any] | None:
    tails = [c for c in chunks_by_id.values() if c.get("next_chunk_id") is None]
    if len(tails) != 1:
        return None
    return tails[0]


def build_slice_record(
    args: argparse.Namespace,
    chunk_records: List[Dict[str, Any]],
    output_dir: Path,
) -> Dict[str, Any]:
    parse_dest = output_dir / "parses" / f"{args.slice_id}.json"
    return {
        "slice_id": args.slice_id,
        "page_range": normalize_optional(args.page_range)
        if args.page_range is not None
        else None,
        "section_range": normalize_optional(args.section_range),
        "parse_path": relative_to_repo(parse_dest),
        "chunk_ids": [r["chunk_id"] for r in chunk_records],
        "chunk_count": len(chunk_records),
        "page_start": chunk_records[0]["page_start"],
        "page_end": chunk_records[-1]["page_end"],
        "parser": args.parser,
        "parser_version": args.parser_version,
        "parser_command": args.parser_command,
    }


def validate_planned_chapter_boundary(
    args: argparse.Namespace,
    slice_record: Dict[str, Any],
    output_dir: Path,
) -> None:
    """Fail fast when a book/chapter slice lacks or violates boundary evidence."""
    boundary_path = output_dir / "chapter_boundaries.json"
    inferred_chapter = chapter_boundaries.infer_chapter(slice_record)
    boundary_required = args.source_kind == "book-section" or inferred_chapter is not None

    if not boundary_path.exists():
        if boundary_required:
            raise SystemExit(
                "chapter boundary validation required before Phase 1 body chunking: "
                f"missing {chapter_boundaries.relative_to_repo(boundary_path)}"
            )
        return

    boundary_map, load_errors = chapter_boundaries.load_json(boundary_path)
    if load_errors:
        raise SystemExit("; ".join(load_errors))
    if not isinstance(boundary_map, dict):
        raise SystemExit(f"{chapter_boundaries.relative_to_repo(boundary_path)}: expected JSON object")

    boundary_index, boundary_errors = chapter_boundaries.build_boundary_index(boundary_map)
    if boundary_errors:
        raise SystemExit("; ".join(boundary_errors))

    if inferred_chapter is None:
        print(
            "warning: chapter boundary map exists, but this slice does not "
            "infer a chapter from slice_id/section_range; boundary range not enforced.",
            file=sys.stderr,
        )
        return

    boundary = boundary_index.get(inferred_chapter)
    if boundary is None:
        raise SystemExit(
            f"{slice_record['slice_id']}: no boundary record for inferred "
            f"chapter {inferred_chapter}; aborting Phase 1 chunk build."
        )
    if boundary.get("confidence") == "low":
        raise SystemExit(
            f"{slice_record['slice_id']}: inferred chapter {inferred_chapter} "
            "boundary is low confidence; resolve boundary evidence before body chunking."
        )

    errors, warnings = chapter_boundaries.validate_slice(slice_record, boundary_index)
    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    if errors:
        raise SystemExit("; ".join(errors))


def assemble(
    args: argparse.Namespace,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]], Dict[str, Any], Dict[str, Any]]:
    """Return (manifest, new_chunk_records, slice_record, plan).

    plan keys:
      mode:             "initial" | "append"
      parse_src:        absolute Path of input parse.json
      parse_dest:       absolute Path of promoted parses/<slice-id>.json
      tail_update:      None | {chunk_id, prev_next_value} when append updates the prior tail
    """
    parse_path = Path(args.parse_json).resolve()
    raw_path = Path(args.raw_path).resolve()
    output_dir = Path(args.output_dir).resolve()
    chunks_dir = output_dir / "chunks"
    parses_dir = output_dir / "parses"
    manifest_path = output_dir / "manifest.json"
    parse_dest = parses_dir / f"{args.slice_id}.json"

    if not parse_path.exists():
        raise SystemExit(f"missing parse.json: {parse_path}")
    if not raw_path.exists():
        raise SystemExit(f"missing raw artifact: {raw_path}")

    with parse_path.open("r", encoding="utf-8") as fh:
        parsed = json.load(fh)
    pages = parsed.get("pages") or []
    if not pages:
        raise SystemExit(f"{parse_path}: no pages")

    grouped = build_chunks(pages)
    if not grouped:
        raise SystemExit(f"{parse_path}: no chunks produced (all pages empty)")

    section_norm = normalize_optional(args.section_range)
    section_slug = slugify(section_norm) if section_norm else ""
    section_display = section_norm.replace("-", " ") if section_norm else "section"
    title_prefix = short_title(args.title_or_origin)

    mode: str = "append" if args.append else "initial"
    existing_manifest: Dict[str, Any] | None = None
    existing_chunks: Dict[str, Dict[str, Any]] = {}
    start_ordinal = 1
    tail_update: Dict[str, Any] | None = None

    if mode == "append":
        if not manifest_path.exists():
            raise SystemExit(
                f"--append requires existing manifest at {manifest_path}; "
                "run without --append for the initial slice."
            )
        with manifest_path.open("r", encoding="utf-8") as fh:
            existing_manifest = json.load(fh)
        existing_slices = existing_manifest.get("slices") or []
        for s in existing_slices:
            if s.get("slice_id") == args.slice_id:
                if not args.force:
                    raise SystemExit(
                        f"--append refused: slice_id {args.slice_id!r} already "
                        f"exists in manifest.slices; pass --force to override."
                    )
        existing_chunks = load_existing_chunks(chunks_dir)
        if not existing_chunks:
            raise SystemExit(
                "--append requires existing chunks under "
                f"{chunks_dir}; none found."
            )
        ordinals = [
            parse_chunk_ordinal(cid)
            for cid in existing_chunks
        ]
        ordinals = [o for o in ordinals if o is not None]
        if not ordinals:
            raise SystemExit(
                "--append could not parse any source-level chunk ordinals "
                "from existing chunk_ids; aborting."
            )
        start_ordinal = max(ordinals) + 1
        prior_tail = find_tail(existing_chunks)
        if prior_tail is None:
            raise SystemExit(
                "--append requires exactly one tail chunk "
                "(next_chunk_id=null) in the existing chain; aborting."
            )
        tail_update = {
            "chunk_id": prior_tail["chunk_id"],
            "old_next": prior_tail.get("next_chunk_id"),
        }
    else:
        if manifest_path.exists() and not args.force:
            raise SystemExit(
                f"manifest already exists at {manifest_path}; pass --append "
                "to add a new slice or --force to rewrite the source from "
                "scratch (repair only)."
            )

    chunk_records: List[Dict[str, Any]] = []
    for offset, group in enumerate(grouped):
        ordinal = start_ordinal + offset
        page_numbers = [p["page"] for p in group["pages"]]
        if section_slug:
            chunk_id = f"{args.source_id}-{section_slug}-chunk-{ordinal:04d}"
        else:
            chunk_id = f"{args.source_id}-chunk-{ordinal:04d}"
        if mode == "append" and chunk_id in existing_chunks:
            raise SystemExit(
                f"--append would produce chunk_id {chunk_id!r}, which already "
                f"exists; aborting to protect existing chunks."
            )
        rec: Dict[str, Any] = {
            "chunk_id": chunk_id,
            "processed_id": f"{args.source_id}-processed-001",
            "raw_id": f"{args.source_id}-raw-001",
            "source_id": args.source_id,
            "title": (
                f"{title_prefix} — {section_display} pages "
                f"{page_numbers[0]}-{page_numbers[-1]}"
            ),
            "page_start": page_numbers[0],
            "page_end": page_numbers[-1],
            "token_estimate": group["token_estimate"],
            "prev_chunk_id": None,
            "next_chunk_id": None,
            "content_hash": sha256_text(group["text"]),
            "review_status": "unreviewed",
            "text": group["text"],
        }
        chunk_records.append(rec)

    for i, rec in enumerate(chunk_records):
        if i > 0:
            rec["prev_chunk_id"] = chunk_records[i - 1]["chunk_id"]
        if i < len(chunk_records) - 1:
            rec["next_chunk_id"] = chunk_records[i + 1]["chunk_id"]

    if mode == "append" and tail_update is not None:
        first_new_id = chunk_records[0]["chunk_id"]
        chunk_records[0]["prev_chunk_id"] = tail_update["chunk_id"]
        tail_update["new_next"] = first_new_id

    slice_record = build_slice_record(args, chunk_records, output_dir)
    validate_planned_chapter_boundary(args, slice_record, output_dir)

    if mode == "append":
        assert existing_manifest is not None
        manifest = dict(existing_manifest)
        slices = list(existing_manifest.get("slices") or [])
        if args.force:
            slices = [s for s in slices if s.get("slice_id") != args.slice_id]
        slices.append(slice_record)
        manifest["slices"] = slices
        manifest["chunk_count"] = sum(s["chunk_count"] for s in slices)
        manifest["page_range"] = slice_record["page_range"]
        manifest["section_range"] = slice_record["section_range"]
        manifest["parser"] = args.parser
        manifest["parser_version"] = args.parser_version
        manifest["parser_command"] = args.parser_command
        manifest["ingestion_status"] = "phase-1-parsed"
        all_chunk_ids: List[str] = []
        for s in slices:
            all_chunk_ids.extend(s["chunk_ids"])
        manifest["generated_files"] = [
            *(s["parse_path"] for s in slices),
            *(
                f"{relative_to_repo(chunks_dir)}/{cid}.json"
                for cid in all_chunk_ids
            ),
        ]
    else:
        chunks_rel_dir = relative_to_repo(chunks_dir)
        chunk_rels = [
            f"{chunks_rel_dir}/{r['chunk_id']}.json" for r in chunk_records
        ]
        manifest = {
            "processed_id": f"{args.source_id}-processed-001",
            "raw_id": f"{args.source_id}-raw-001",
            "parser": args.parser,
            "parser_version": args.parser_version,
            "parser_command": args.parser_command,
            "source_hash": sha256_file(raw_path),
            "page_range": slice_record["page_range"],
            "section_range": slice_record["section_range"],
            "extraction_warnings": [],
            "chunk_count": len(chunk_records),
            "generated_files": [slice_record["parse_path"], *chunk_rels],
            "source_kind": args.source_kind,
            "title_or_origin": args.title_or_origin,
            "raw_path": relative_to_repo(raw_path),
            "original_path": normalize_optional(args.original_path),
            "file_size_bytes": raw_path.stat().st_size,
            "license_copyright_status": normalize_optional(
                args.license_copyright_status
            ),
            "ingestion_status": "phase-1-parsed",
            "slices": [slice_record],
        }
        if manifest["page_range"] is None and args.page_range is not None:
            manifest["page_range"] = args.page_range

    plan = {
        "mode": mode,
        "parse_src": parse_path,
        "parse_dest": parse_dest,
        "tail_update": tail_update,
    }
    return manifest, chunk_records, slice_record, plan


def relative_to_repo(path: Path) -> str:
    try:
        rel = path.resolve().relative_to(REPO_ROOT)
    except ValueError:
        return str(path)
    return rel.as_posix()


def serialize(obj: Dict[str, Any]) -> str:
    return json.dumps(obj, indent=2, sort_keys=True) + "\n"


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generic Phase 1 chunk + manifest builder.",
    )
    p.add_argument("--source-id", required=True)
    p.add_argument(
        "--slice-id",
        required=True,
        help="Stable kebab-case slice id, e.g. chapter-1-introduction-p40-55.",
    )
    p.add_argument("--raw-path", required=True)
    p.add_argument("--parse-json", required=True)
    p.add_argument("--output-dir", required=True)
    p.add_argument("--source-kind", required=True, choices=ALLOWED_SOURCE_KINDS)
    p.add_argument("--title-or-origin", required=True)
    p.add_argument("--original-path", required=True)
    p.add_argument("--page-range", required=True)
    p.add_argument("--section-range", required=True)
    p.add_argument("--license-copyright-status", required=True)
    p.add_argument("--parser", default="liteparse", choices=ALLOWED_PARSERS)
    p.add_argument("--parser-version", required=True)
    p.add_argument("--parser-command", required=True)
    p.add_argument(
        "--append",
        action="store_true",
        help=(
            "Add a new slice to an existing source manifest. Requires the "
            "manifest and chunks/ directory to already exist; new chunk "
            "ordinals continue past the current source-level maximum."
        ),
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned manifest/chunks; do not write files.",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help=(
            "Required to overwrite an existing slice_id in append mode, or "
            "to rewrite an existing source manifest from scratch (repair)."
        ),
    )
    return p.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv)

    manifest, chunk_records, slice_record, plan = assemble(args)
    output_dir = Path(args.output_dir).resolve()
    chunks_dir = output_dir / "chunks"
    parses_dir = output_dir / "parses"
    manifest_path = output_dir / "manifest.json"
    parse_dest: Path = plan["parse_dest"]
    parse_src: Path = plan["parse_src"]
    tail_update = plan["tail_update"]

    serialized_manifest = serialize(manifest)
    serialized_new_chunks: Dict[str, str] = {
        r["chunk_id"]: serialize(r) for r in chunk_records
    }

    serialized_tail_update: Tuple[Path, str] | None = None
    if tail_update is not None:
        tail_path = chunks_dir / f"{tail_update['chunk_id']}.json"
        with tail_path.open("r", encoding="utf-8") as fh:
            tail_rec = json.load(fh)
        tail_rec["next_chunk_id"] = tail_update["new_next"]
        serialized_tail_update = (tail_path, serialize(tail_rec))

    if args.dry_run:
        print("=== DRY RUN ===")
        print(f"mode:        {plan['mode']}")
        print(f"source-id:   {args.source_id}")
        print(f"slice-id:    {args.slice_id}")
        print(f"output-dir:  {relative_to_repo(output_dir)}")
        print(f"new chunks:  {len(chunk_records)}")
        for r in chunk_records:
            print(
                f"  {r['chunk_id']}  pages {r['page_start']}-{r['page_end']}  "
                f"tokens={r['token_estimate']}  "
                f"hash={r['content_hash'][:16]}..."
            )
        print(
            f"manifest.slices total slices after write: "
            f"{len(manifest['slices'])} "
            f"(this slice: chunks {len(chunk_records)}, "
            f"pages {slice_record['page_start']}-{slice_record['page_end']})"
        )
        print(
            f"promoted parse: {relative_to_repo(parse_src)} "
            f"-> {relative_to_repo(parse_dest)} "
            f"(exists: {parse_dest.exists()})"
        )
        if tail_update is not None:
            print(
                f"chain link: update existing tail "
                f"{tail_update['chunk_id']!r} next_chunk_id "
                f"{tail_update['old_next']!r} -> {tail_update['new_next']!r}"
            )

        diffs = 0
        present_files = 0
        if manifest_path.exists():
            present_files += 1
            existing = manifest_path.read_text(encoding="utf-8")
            same = existing == serialized_manifest
            print(f"manifest.json exists; would-be-identical: {str(same).lower()}")
            if not same:
                diffs += 1
        else:
            print("manifest.json does not exist; would create.")

        for cid, body in serialized_new_chunks.items():
            cp = chunks_dir / f"{cid}.json"
            if cp.exists():
                present_files += 1
                existing = cp.read_text(encoding="utf-8")
                same = existing == body
                print(
                    f"  chunks/{cid}.json exists; "
                    f"would-be-identical: {str(same).lower()}"
                )
                if not same:
                    diffs += 1
            else:
                print(f"  chunks/{cid}.json does not exist; would create.")

        if serialized_tail_update is not None:
            tp, body = serialized_tail_update
            existing = tp.read_text(encoding="utf-8")
            same = existing == body
            print(
                f"  chunks/{tp.name} (existing tail update) "
                f"would-be-identical: {str(same).lower()}"
            )
            if not same:
                diffs += 1
            present_files += 1

        if parse_dest.exists():
            present_files += 1
            try:
                existing = parse_dest.read_text(encoding="utf-8")
                same = existing == parse_src.read_text(encoding="utf-8")
            except OSError:
                same = False
            print(
                f"  parses/{parse_dest.name} exists; "
                f"would-be-identical: {str(same).lower()}"
            )
            if not same:
                diffs += 1
        else:
            print(f"  parses/{parse_dest.name} does not exist; would create.")

        if present_files == 0:
            print("summary: no existing files to compare against.")
        else:
            print(
                f"summary: {present_files} existing file(s) compared, "
                f"{diffs} would differ; "
                f"would-be-identical-overall: "
                f"{'yes' if diffs == 0 else 'no'}"
            )
        return 0

    refuse_existing: List[Path] = []
    if plan["mode"] == "initial":
        if manifest_path.exists() and not args.force:
            refuse_existing.append(manifest_path)
        for cid in serialized_new_chunks:
            cp = chunks_dir / f"{cid}.json"
            if cp.exists() and not args.force:
                refuse_existing.append(cp)
        if parse_dest.exists() and not args.force:
            refuse_existing.append(parse_dest)
    else:
        for cid in serialized_new_chunks:
            cp = chunks_dir / f"{cid}.json"
            if cp.exists():
                refuse_existing.append(cp)
        if parse_dest.exists():
            refuse_existing.append(parse_dest)

    if refuse_existing:
        if plan["mode"] == "append":
            print(
                "--append refused: would overwrite existing chunk(s) or "
                "promoted parse. Append never overwrites existing chunks.",
                file=sys.stderr,
            )
        else:
            print(
                "refusing to overwrite existing files (use --force for "
                "explicit repair):",
                file=sys.stderr,
            )
        for f in refuse_existing:
            print(f"  - {relative_to_repo(f)}", file=sys.stderr)
        return 2

    chunks_dir.mkdir(parents=True, exist_ok=True)
    parses_dir.mkdir(parents=True, exist_ok=True)

    if not parse_dest.exists() or args.force:
        shutil.copyfile(parse_src, parse_dest)

    if serialized_tail_update is not None:
        tp, body = serialized_tail_update
        tp.write_text(body, encoding="utf-8")

    for cid, body in serialized_new_chunks.items():
        (chunks_dir / f"{cid}.json").write_text(body, encoding="utf-8")

    manifest_path.write_text(serialized_manifest, encoding="utf-8")

    print(
        f"wrote {relative_to_repo(manifest_path)} and "
        f"{len(chunk_records)} new chunk(s); slice={args.slice_id}; "
        f"mode={plan['mode']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
