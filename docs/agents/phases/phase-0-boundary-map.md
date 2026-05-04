# Phase 0 - Boundary Map

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

## Use With

- `docs/agents/policy/scope-boundaries.md`
- `docs/agents/policy/validation-audit.md`
- `docs/agents/policy/token-budgets.md`

### Phase 0 — Boundary Map

Purpose: establish chapter/page boundaries for book-length sources before body chunking.

Required for any new book-length source before Phase 1 body ingestion:
- parse the front matter / table of contents into processed parser evidence, usually `processed/<source-id>/parse.candidate-frontmatter-contents-<pages>.json`
- create `processed/<source-id>/chapter_boundaries.json`
- record the mapping between printed pages and PDF pages, including Roman-numeral front matter
- derive chapter end pages from the next chapter's start page minus one when the contents supports it
- mark ambiguous boundaries with `confidence: low` and do not enforce them as hard failures until resolved
- record the parse path, parser command, evidence basis, chapter starts/ends, printed-page starts/ends when available, evidence text, confidence, and notes

Boundary maps are processed evidence / planning truth, not wiki reasoning memory. Do not create source pages, concepts, insights, or graph-visible markdown from Phase 0 evidence alone.

Phase 0 gate:
- body chunking for a chapter must not start until the relevant boundary is known with sufficient confidence
- Phase 1 slice boundaries must be checked against `chapter_boundaries.json` when it exists
- a slice must not cross a chapter boundary unless it is explicitly labeled as a boundary/transition slice and approved by policy for that task
- do not rely only on local heading strings or grep matches, because later chapters may repeat terms
- if `scripts/validate_chapter_boundaries.py` fails, stop and repair the boundary/slice problem before Phase 2 or Phase 3
