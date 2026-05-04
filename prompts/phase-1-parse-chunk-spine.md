# Phase 1 — Parse, Chunk, and Spine Build

Use `AGENTS.md` as the active policy file. Inspect current repo state directly. Do not rely on prior chat memory. Run **Phase 1 only**.

This prompt is the execution layer for Phase 1. It governs raw registration, LiteParse invocation, processed manifest construction, and chunk spine creation. It must not produce any reasoning artifacts.

---

## Scope

Allowed in this run:

- raw registration and raw metadata
- LiteParse parser output promoted to `processed/<source-id>/parses/<slice-id>.json` per bounded slice
- processed manifest at `processed/<source-id>/manifest.json` (one manifest per source, with a `slices` array recording each promoted slice)
- chunk JSON files under `processed/<source-id>/chunks/` with stable IDs, content hashes, token estimates, and page/section spans (all chunks for the source share this directory)
- previous/next chunk links forming a single non-branching source-level chain across all slices
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
- `<slice-id>`: stable kebab-case id for this bounded slice (e.g. `chapter-1-introduction-p40-55`). Slices are append-only within a source.
- `<raw-path>`: absolute or repo-relative path to the raw artifact (PDF, DOCX, etc.).
- `<source-kind>`: one of `book-section`, `paper-section`, `standard-section`, `technical-doc`, `first-party-artifact`, `explicit-snapshot`.
- Optional: `<page-range>` or `<target-pages>` to bound the parse.
- For book-length or chapter-labeled sources, `processed/<source-id>/chapter_boundaries.json` must already exist before body chunking.

## Initial vs continuation slice

- An **initial slice** is the first Phase 1 slice for a `<source-id>` that has no `processed/<source-id>/manifest.json` yet. Run `scripts/build_phase1_chunks.py` without `--append`. The script writes a fresh manifest, promotes the parse into `processed/<source-id>/parses/<slice-id>.json`, and writes new chunk files starting at ordinal `0001`.
- A **continuation slice** appends to an existing source. Run `scripts/build_phase1_chunks.py --append --slice-id <slice-id>`. The script:
  - refuses to start without an existing manifest;
  - assigns new chunk ordinals continuing past the current source-level maximum (existing chunk IDs stay frozen);
  - sets the first new chunk's `prev_chunk_id` to the existing tail and updates that tail's `next_chunk_id` to the first new chunk so the source-level chain stays linear;
  - appends a new slice record to `manifest.slices`;
  - **never overwrites existing chunk files or promoted parses**, with or without `--force`. `--force` only allows replacing a slice record that already has the same `slice_id` (explicit repair).
- Source pages depend on stable chunk IDs. Continuing a source must not change any previously promoted chunk's `chunk_id`, `text`, `content_hash`, or `prev_chunk_id` (only the previous tail's `next_chunk_id` is allowed to change to point at the new slice's first chunk).
- Phase 1 must not overwrite existing chunks for a source unless the task is an explicit repair invoked with `--force`.

---

## Steps

### 1. Register raw

- Confirm `<raw-path>` lives under `raw/<source-id>/` (move only if the user explicitly asked; otherwise stop and report).
- Compute and record SHA-256 of the raw file as `source_hash`.
- Record raw-registration metadata **inside `processed/<source-id>/manifest.json`** (see step 3 for the field list). Do not create a separate raw metadata file unless the user explicitly asks for one.
- Do not modify raw bytes. Raw is immutable.

### 1a. Load chapter boundaries

- For book-length sources and any slice whose `slice_id` or `section_range` is chapter-labeled, load `processed/<source-id>/chapter_boundaries.json` before choosing or validating a body slice.
- Confirm the planned `<page-range>` lies inside the inferred chapter boundary.
- Hard-stop if `<page-range>` violates the chapter boundary, or if the relevant chapter boundary is missing or low-confidence.
- Do not rely only on local heading strings or grep matches; later chapters may repeat terms.

### 2. Invoke LiteParse

- Run LiteParse into a temporary candidate path, e.g. `processed/<source-id>/parse.candidate-<slice-id>.json`. The candidate path lets the dry-run gate inspect output before promotion.
- Use `liteparse parse <raw-path> -o <candidate-path> --format json` (alias `lit`).
- For bounded slices, pass `--target-pages` or `--max-pages`.
- Capture parser version (`liteparse --version`) and the exact command line as `parser_version` and `parser_command`.
- Persist any extraction warnings emitted by LiteParse.
- If LiteParse fails, write an extraction exception note to `processed/<source-id>/extraction-exception.md` and stop.
- After the dry-run gate passes, `scripts/build_phase1_chunks.py` promotes the candidate to `processed/<source-id>/parses/<slice-id>.json`. Do not write directly to `processed/<source-id>/parse.json`; that path is no longer the canonical promoted location. Delete the candidate file after promotion.

### 3. Write processed manifest

`processed/<source-id>/manifest.json` must validate against `structured/schema/processed-manifest.schema.json` and include:

Parser/processed fields:

- `processed_id`
- `raw_id`
- `parser` (`liteparse`; reflects the most recently appended slice)
- `parser_version` (most recently appended slice)
- `parser_command` (most recently appended slice)
- `source_hash`
- `page_range` (most recently appended slice; per-slice authoritative values live in `slices[]`)
- `section_range` (most recently appended slice)
- `extraction_warnings` (list)
- `chunk_count` (total across all slices)
- `generated_files` (list of repo-relative paths covering every promoted parse and every chunk file)
- `slices` (append-only list of slice records; see below)

Slice records (`manifest.slices[]`, one per bounded Phase 1 slice):

- `slice_id`
- `page_range`
- `section_range`
- `parse_path` (repo-relative path to `processed/<source-id>/parses/<slice-id>.json`)
- `chunk_ids` (in chain order)
- `chunk_count`
- `page_start`, `page_end` (must equal the first/last referenced chunk's page span)
- `parser`, `parser_version`, `parser_command`

Raw-registration fields (kept here by default; only split into a separate raw metadata file on explicit user request):

- `source_kind` (one of the enum values listed under Inputs above)
- `title_or_origin` (book title, paper citation, doc URL, etc.)
- `raw_path` (repo-relative, under `raw/<source-id>/`)
- `original_path` (where the raw artifact came from before registration, or `null`)
- `file_size_bytes`
- `license_copyright_status` (free-form string or `null` when unknown)
- `ingestion_status` (start at `phase-1-in-progress`; flip to `phase-1-parsed` once the completion gate is satisfied)

### 4. Build chunks

- Derive chunks from LiteParse output. Do not copy ad hoc text.
- Target 800–1,500 tokens per chunk; hard max 2,000.
- Each chunk lives at `processed/<source-id>/chunks/<chunk-id>.json` and must validate against `structured/schema/chunk.schema.json` with:
  - `chunk_id` (stable, kebab-case, includes `<source-id>`, optional section path, and a zero-padded source-level ordinal that never restarts across slices)
  - `processed_id`
  - `raw_id`
  - `source_id`
  - `title`
  - `page_start`, `page_end`
  - `token_estimate` (integer, positive, ≤ 2000)
  - `text` (the **exact** chunk text used for `token_estimate` and `content_hash`)
  - `content_hash` (SHA-256 of the `text` field, hex-encoded; `validate_chunk_chain.py` recomputes this and rejects mismatches)
  - `prev_chunk_id` (or `null` for the source-level head)
  - `next_chunk_id` (or `null` for the source-level tail)
  - `review_status` (`unreviewed` by default)
- Phase 2 must be able to consume chunk JSON directly from `processed/<source-id>/chunks/`. Do not require Phase 2 to mine the per-slice `parses/<slice-id>.json`. The `text` field is the source of truth for that consumption.
- The chain must be a single linear sequence across all slices with no gaps and no loops.
- Do **not** create `chunks/*.md` files. Chunks are JSON-only by default.

Use the generic helper `scripts/build_phase1_chunks.py`. Per-source ad hoc helpers are forbidden. Run it without `--append` for the initial slice on a new source and with `--append --slice-id <slice-id>` for every continuation slice. Always dry-run first. Append mode never overwrites existing chunk files or promoted parses.

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
python3 scripts/validate_chapter_boundaries.py --source-id <source-id>
```

All applicable validators must exit 0. Run `validate_chapter_boundaries.py` after every append when a boundary map exists or the slice is chapter-labeled. Other checks (token budgets, orphans, broken links, source provenance) remain `manual/pending` until their scripts exist.

---

## Completion gate

Phase 1 is complete only when all of the following hold:

- raw is registered with `source_hash` and metadata
- a promoted parse exists at `processed/<source-id>/parses/<slice-id>.json` and is referenced from `manifest.slices[]` / `generated_files`, or an extraction exception is logged
- `processed/<source-id>/manifest.json` exists and validates
- chunk JSON files exist with stable IDs, content hashes, token estimates, and page/section spans
- `prev_chunk_id` / `next_chunk_id` form a chain with no gaps or loops
- book/chapter slice page ranges validate against `processed/<source-id>/chapter_boundaries.json`
- `wiki/meta/log.md` has been updated
- index updates are either complete or explicitly marked `manual/pending`
- applicable validators exited 0, including chapter-boundary validation when required

If any item fails, stop and report instead of continuing into Phase 2.

---

## Reminders

- Frontmatter is identity / navigation / provenance. It is not reasoning evidence.
- Do not promote anything. Phase 1 produces evidence, not interpretation.
- Archive material remains read-only and is not migrated by this prompt.
- The live codebase is out of scope unless the user explicitly requests filesystem inspection for a coding-reasoning task.
