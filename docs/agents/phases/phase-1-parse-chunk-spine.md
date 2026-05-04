# Phase 1 - Parse, Chunk, and Spine Build

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

## Use With

- `docs/agents/policy/metadata-frontmatter-indexes.md`
- `docs/agents/policy/validation-audit.md`
- `docs/agents/policy/token-budgets.md`

### Phase 1 — Parse, Chunk, and Spine Build

Purpose: deterministic provenance and chunk construction.

Allowed outputs:
- raw registration and raw metadata
- LiteParse/normalized parser output
- processed manifest
- chunk files with stable IDs, content hashes, token estimates, and page/section spans
- previous/next chunk links
- optional minimal source-hub skeleton for navigation
- generated index/log updates for raw/processed/chunk artifacts

Forbidden outputs:
- interpreted source memory
- source-page essays
- graph-visible markdown chunk cards by default
- concepts
- concept refinements
- insights
- high-level synthesis

Completion gate:
- raw is registered
- a promoted parse exists at `processed/<source-id>/parses/<slice-id>.json` and is referenced from `manifest.slices[]` / `generated_files`, or an extraction exception is logged
- `manifest.json` exists
- chunks exist with stable IDs, hashes, spans, and token estimates
- chunk chain has no gaps or loops
- book/chapter slice boundaries validate against `chapter_boundaries.json`
- `scripts/validate_chapter_boundaries.py` has been run after every Phase 1 append when a boundary map exists or the slice is chapter-labeled
- indexes/logs are updated or marked `manual/pending`

---

## LiteParse and Parsing

LiteParse is preferred for PDF ingestion when layout, tables, page structure, figures, or auditability matter.

Use LiteParse for:
- technical books
- standards/specifications
- papers with tables/figures
- multi-column PDFs
- PDFs where simpler extraction produces unstable boundaries
- sources where page/layout provenance matters

Use simpler extraction only when source text is already clean or LiteParse adds no value.

When using LiteParse:
- store promoted parser output as `processed/<source-id>/parses/<slice-id>.json`
- record promoted parse paths in `processed/<source-id>/manifest.json` through `manifest.slices[]` and `generated_files`
- preserve page numbers, text items, table/figure markers, bounding boxes if available, parser version, source hash, and extraction warnings
- derive chunks from parser output, not ad hoc copied text
- create markdown review files only as views over parser output
- log parser/layout disagreements and mark affected chunks/sources for review

Raw remains immutable.
