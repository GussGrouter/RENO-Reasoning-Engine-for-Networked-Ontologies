# Phase 1 — Parse, Chunk, and Spine Build

Use `AGENTS.md` as the active policy file. Run **Phase 1 only**.

This prompt is the execution layer for Phase 1. It governs raw registration, LiteParse invocation, processed manifest construction, and chunk spine creation. It must not produce any reasoning artifacts.

---

## Scope

Allowed in this run:

- raw registration and raw metadata
- LiteParse parser output stored as `processed/<source-id>/parse.json`
- processed manifest at `processed/<source-id>/manifest.json`
- chunk JSON files under `processed/<source-id>/chunks/` with stable IDs, content hashes, token estimates, and page/section spans
- previous/next chunk links forming a single non-branching chain
- optional empty source-hub skeleton at `wiki/source/<source-id>.md` for navigation only
- updates to `wiki/meta/log.md` and any generated index/log entries for raw/processed/chunk artifacts

Forbidden in this run:

- source pages with extracted source memory
- concept pages, insight pages, summary pages
- concept refinements, merges, splits, deprecations
- markdown chunk cards (`processed/<source-id>/chunks/*.md` or graph-visible chunk nodes)
- modifications to `archive/`, existing `raw/` artifacts, or `AGENTS.md`
- ingestion of non-technical material
- ingestion of live codebase or external filesystem state

If reasoning would be required to satisfy a step, stop and report instead of continuing.

---

## Inputs

- `<source-id>`: lowercase kebab-case stable id (e.g. `systems-performance`, `network-algorithmics`).
- `<raw-path>`: absolute or repo-relative path to the raw artifact (PDF, DOCX, etc.).
- `<source-kind>`: one of `book-section`, `paper-section`, `standard-section`, `technical-doc`, `first-party-artifact`, `explicit-snapshot`.
- Optional: `<page-range>` or `<target-pages>` to bound the parse.

---

## Steps

### 1. Register raw

- Confirm `<raw-path>` lives under `raw/<source-id>/` (move only if the user explicitly asked; otherwise stop and report).
- Compute and record SHA-256 of the raw file as `source_hash`.
- Record `source_kind`, `title/origin`, `original_path`, `license/copyright_status` (if known), and `ingestion_status: phase-1-in-progress`.
- Do not modify raw bytes. Raw is immutable.

### 2. Invoke LiteParse

- Use `liteparse parse <raw-path> -o processed/<source-id>/parse.json --format json` (alias `lit`).
- For bounded slices, pass `--target-pages` or `--max-pages`.
- Capture parser version (`liteparse --version`) and the exact command line as `parser_version` and `parser_command`.
- Persist any extraction warnings emitted by LiteParse.
- If LiteParse fails, write an extraction exception note to `processed/<source-id>/extraction-exception.md` and stop.

### 3. Write processed manifest

`processed/<source-id>/manifest.json` must validate against `structured/schema/processed-manifest.schema.json` and include:

- `processed_id`
- `raw_id`
- `parser` (`liteparse`)
- `parser_version`
- `parser_command`
- `source_hash`
- `page_range`
- `section_range`
- `extraction_warnings` (list)
- `chunk_count`
- `generated_files` (list of relative paths)

### 4. Build chunks

- Derive chunks from LiteParse output. Do not copy ad hoc text.
- Target 800–1,500 tokens per chunk; hard max 2,000.
- Each chunk lives at `processed/<source-id>/chunks/<chunk-id>.json` and must validate against `structured/schema/chunk.schema.json` with:
  - `chunk_id` (stable, kebab-case, includes `<source-id>`, optional section path, and a zero-padded ordinal)
  - `processed_id`
  - `raw_id`
  - `source_id`
  - `title`
  - `page_start`, `page_end`
  - `token_estimate`
  - `content_hash` (SHA-256 of the chunk text)
  - `prev_chunk_id` (or `null` for the first chunk)
  - `next_chunk_id` (or `null` for the last chunk)
  - `review_status` (`unreviewed` by default)
- The chain must be a single linear sequence with no gaps and no loops.
- Do **not** create `chunks/*.md` files. Chunks are JSON-only by default.

### 5. Optional source-hub skeleton

If a hub is useful for navigation, create `wiki/source/<source-id>.md` with:

```yaml
---
id: <source-id>-hub
type: summary
status: draft
phase: phase-1-parsed
source_id: <source-id>
parent: null
prev: null
next: null
---
```

Body: a single H1, a one-line scope statement, and a link to `wiki/meta/index.md`. No extracted memory, no candidate concepts, no insights.

### 6. Update meta and indexes

- Append a one-line entry to `wiki/meta/log.md` describing this Phase 1 run (date, source-id, page range, chunk count).
- If `structured/indexes/files.jsonl` and `structured/indexes/chunks.jsonl` do not yet exist or are not maintained by `scripts/build_indexes.py`, mark the index update as `manual/pending` in the log entry.

### 7. Validation

Run, in order:

```text
python3 scripts/validate_frontmatter.py
python3 scripts/validate_chunk_chain.py
```

Both must exit 0. Other checks (token budgets, orphans, broken links, source provenance) remain `manual/pending` until their scripts exist.

---

## Completion gate

Phase 1 is complete only when all of the following hold:

- raw is registered with `source_hash` and metadata
- `processed/<source-id>/parse.json` exists, or an extraction exception is logged
- `processed/<source-id>/manifest.json` exists and validates
- chunk JSON files exist with stable IDs, content hashes, token estimates, and page/section spans
- `prev_chunk_id` / `next_chunk_id` form a chain with no gaps or loops
- `wiki/meta/log.md` has been updated
- index updates are either complete or explicitly marked `manual/pending`
- both validators exited 0

If any item fails, stop and report instead of continuing into Phase 2.

---

## Reminders

- Frontmatter is identity / navigation / provenance. It is not reasoning evidence.
- Do not promote anything. Phase 1 produces evidence, not interpretation.
- Archive material remains read-only and is not migrated by this prompt.
- The live codebase is out of scope unless the user explicitly requests filesystem inspection for a coding-reasoning task.
