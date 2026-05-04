#!/usr/bin/env python3
"""Check token and word-count budgets across processed chunks and wiki/source/.

Scope and rules follow AGENTS.md "Token Budgets":

- chunk target: 800-1500 tokens; hard max 2000
- bounded source page (type: source) target: 200-600 words; hard max 1000
- source hub (type: summary under wiki/source/) is navigation only;
  warn if the body exceeds 1200 words but never hard-fail

This script:

- inspects every chunk JSON under processed/*/chunks/
  * warns if chunk.token_estimate > CHUNK_SOFT_MAX (1500)
  * fails if chunk.token_estimate > CHUNK_HARD_MAX (2000)
  * fails if chunk.token_estimate is missing or not a positive integer
- inspects every wiki/source/*.md file
  * if frontmatter type is 'source':
    - warns if the body exceeds SOURCE_BODY_SOFT_WORD_MAX (600) words
    - fails if the body exceeds SOURCE_BODY_HARD_WORD_MAX (1000) words
  * if frontmatter type is 'summary':
    - warns if the body exceeds HUB_BODY_SOFT_WORD_MAX (1200) words
    - never hard-fails on body length
  * other types under wiki/source/ are skipped (not enforced here)
- prints a one-line summary including source_body_soft_word_max,
  source_body_hard_word_max, and hub_body_soft_word_max
- exits 0 when there are no hard failures (no chunk over the hard max, no
  malformed chunk records, no source body over the word hard max)
- exits 1 when at least one hard failure is recorded

Word counting is intentionally simple: split the body on whitespace after
stripping fenced code blocks. Markdown formatting characters are kept (the
threshold has slack for that).

Uses Python stdlib only.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_ROOT = REPO_ROOT / "processed"
WIKI_SOURCE = REPO_ROOT / "wiki" / "source"

CHUNK_SOFT_MAX = 1500
CHUNK_HARD_MAX = 2000
SOURCE_BODY_SOFT_WORD_MAX = 600
SOURCE_BODY_HARD_WORD_MAX = 1000
HUB_BODY_SOFT_WORD_MAX = 1200

FENCE_PATTERN = re.compile(r"^\s*```", re.MULTILINE)
TYPE_LINE_PATTERN = re.compile(r"^\s*type\s*:\s*(.+?)\s*$")


def list_chunk_paths() -> List[Path]:
    if not PROCESSED_ROOT.exists():
        return []
    out: List[Path] = []
    for entry in sorted(PROCESSED_ROOT.iterdir()):
        if not entry.is_dir() or entry.name.startswith("."):
            continue
        chunks_dir = entry / "chunks"
        if not chunks_dir.exists():
            continue
        for path in sorted(chunks_dir.glob("*.json")):
            out.append(path)
    return out


def list_source_md_paths() -> List[Path]:
    if not WIKI_SOURCE.exists():
        return []
    out: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(WIKI_SOURCE):
        dirnames.sort()
        for name in sorted(filenames):
            if name == ".gitkeep":
                continue
            if not name.endswith(".md"):
                continue
            out.append(Path(dirpath) / name)
    return out


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1 :])
    return text


def extract_frontmatter_type(text: str) -> str | None:
    """Return the value of the top-level frontmatter `type:` field, or None."""
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == "---":
            return None
        m = TYPE_LINE_PATTERN.match(line)
        if not m:
            continue
        raw = m.group(1).strip()
        if (raw.startswith('"') and raw.endswith('"')) or (
            raw.startswith("'") and raw.endswith("'")
        ):
            raw = raw[1:-1]
        return raw or None
    return None


def strip_code_fences(text: str) -> str:
    """Remove fenced code blocks (```...```) from markdown body."""
    out: List[str] = []
    in_fence = False
    for line in text.splitlines():
        if FENCE_PATTERN.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        out.append(line)
    return "\n".join(out)


def word_count(text: str) -> int:
    return len([w for w in text.split() if w])


def check_chunks() -> Tuple[int, List[str], List[str]]:
    """Return (hard_failure_count, warnings, hard_failures)."""
    warnings: List[str] = []
    failures: List[str] = []
    for path in list_chunk_paths():
        rel = path.relative_to(REPO_ROOT)
        try:
            with path.open("r", encoding="utf-8") as fh:
                record = json.load(fh)
        except json.JSONDecodeError as exc:
            failures.append(f"{rel}: invalid JSON: {exc}")
            continue
        except OSError as exc:
            failures.append(f"{rel}: could not read: {exc}")
            continue

        if not isinstance(record, dict):
            failures.append(f"{rel}: not a JSON object")
            continue

        te = record.get("token_estimate")
        if not isinstance(te, int) or isinstance(te, bool):
            failures.append(
                f"{rel}: token_estimate must be an integer (got {te!r})"
            )
            continue
        if te <= 0:
            failures.append(
                f"{rel}: token_estimate must be positive (got {te})"
            )
            continue
        if te > CHUNK_HARD_MAX:
            failures.append(
                f"{rel}: token_estimate {te} exceeds hard max {CHUNK_HARD_MAX}"
            )
            continue
        if te > CHUNK_SOFT_MAX:
            warnings.append(
                f"{rel}: token_estimate {te} exceeds soft max {CHUNK_SOFT_MAX}"
            )

    return len(failures), warnings, failures


def check_source_pages() -> Tuple[List[str], List[str]]:
    """Return (warnings, hard_failures) for wiki/source/*.md bodies.

    Word-count rules apply by frontmatter type:

    - type: source   -> warn >SOURCE_BODY_SOFT_WORD_MAX, fail >SOURCE_BODY_HARD_WORD_MAX
    - type: summary  -> warn >HUB_BODY_SOFT_WORD_MAX, never fail
    - other types    -> not enforced by this check
    """
    warnings: List[str] = []
    failures: List[str] = []
    for path in list_source_md_paths():
        rel = path.relative_to(REPO_ROOT)
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            failures.append(f"{rel}: could not read: {exc}")
            continue
        ftype = extract_frontmatter_type(text)
        body = strip_code_fences(strip_frontmatter(text))
        wc = word_count(body)
        if ftype == "source":
            if wc > SOURCE_BODY_HARD_WORD_MAX:
                failures.append(
                    f"{rel}: type=source body word count {wc} exceeds hard max "
                    f"{SOURCE_BODY_HARD_WORD_MAX}"
                )
                continue
            if wc > SOURCE_BODY_SOFT_WORD_MAX:
                warnings.append(
                    f"{rel}: type=source body word count {wc} exceeds soft max "
                    f"{SOURCE_BODY_SOFT_WORD_MAX}"
                )
        elif ftype == "summary":
            if wc > HUB_BODY_SOFT_WORD_MAX:
                warnings.append(
                    f"{rel}: type=summary hub body word count {wc} exceeds "
                    f"soft max {HUB_BODY_SOFT_WORD_MAX} (no hard fail)"
                )
    return warnings, failures


def main() -> int:
    chunk_paths = list_chunk_paths()
    source_paths = list_source_md_paths()
    chunk_hard_count, chunk_warnings, chunk_failures = check_chunks()
    source_warnings, source_failures = check_source_pages()
    hard_count = chunk_hard_count + len(source_failures)

    detail: List[str] = []
    if chunk_failures or source_failures:
        detail.append("check_token_budgets: hard failures")
        for f in chunk_failures + source_failures:
            detail.append(f"  - {f}")
    if chunk_warnings:
        detail.append("check_token_budgets: chunk warnings")
        for w in chunk_warnings:
            detail.append(f"  - {w}")
    if source_warnings:
        detail.append("check_token_budgets: source page warnings")
        for w in source_warnings:
            detail.append(f"  - {w}")

    for line in detail:
        print(line)

    print(
        f"check_token_budgets: chunks={len(chunk_paths)} "
        f"source_pages={len(source_paths)} "
        f"hard_failures={hard_count} "
        f"chunk_warnings={len(chunk_warnings)} "
        f"source_page_warnings={len(source_warnings)} "
        f"chunk_soft_max={CHUNK_SOFT_MAX} chunk_hard_max={CHUNK_HARD_MAX} "
        f"source_body_soft_word_max={SOURCE_BODY_SOFT_WORD_MAX} "
        f"source_body_hard_word_max={SOURCE_BODY_HARD_WORD_MAX} "
        f"hub_body_soft_word_max={HUB_BODY_SOFT_WORD_MAX}"
    )
    return 0 if hard_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
