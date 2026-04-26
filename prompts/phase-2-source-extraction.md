# Phase 2 — Source Extraction (PLACEHOLDER)

This prompt is a **placeholder**. Do not use it yet.

Use `AGENTS.md` as the active policy file. Run only the phase the user explicitly requests.

## Activation prerequisites

Do not invoke this prompt until all of the following exist:

- `structured/schema/source.schema.json`
- `scripts/validate_source_provenance.py`
- a Phase 1 run has produced at least one source's `processed/<source-id>/manifest.json` and chunk chain that pass `validate_chunk_chain.py`

When this prompt is filled in, it must:

- consume only Phase 1 outputs (raw, processed manifest, chunks)
- produce source hubs and source pages tied to bounded chunk/section ranges
- record candidate concepts and candidate insights only as suggestions
- preserve provenance from source pages back to chunks and raw

## Forbidden in Phase 2

- creating, refining, merging, splitting, or deprecating concept pages
- creating insight pages
- generalized ontology reasoning
- crossing into Phase 3 work in the same run

## Boundary rule

If a step would require reasoning beyond the source itself, stop and report. Do not cross phase boundaries.

Follow `AGENTS.md` for all behavior not specified here.
