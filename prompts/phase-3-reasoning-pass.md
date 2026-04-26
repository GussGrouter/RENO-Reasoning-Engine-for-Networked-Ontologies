# Phase 3 — Reasoning and Ontology Construction (PLACEHOLDER)

This prompt is a **placeholder**. Do not use it yet.

Use `AGENTS.md` as the active policy file. Run only the phase the user explicitly requests.

## Activation prerequisites

Do not invoke this prompt until all of the following exist:

- `structured/schema/concept.schema.json`
- `structured/schema/insight.schema.json`
- `structured/schema/summary.schema.json`
- `structured/schema/contradiction.schema.json`
- `structured/schema/decision.schema.json`
- `scripts/build_indexes.py`
- `scripts/check_orphans.py`
- `scripts/check_broken_links.py`
- `scripts/check_concept_source_support.py`
- a Phase 2 source corpus that passes `validate_source_provenance.py`

When this prompt is filled in, it must:

- reason from source pages first, processed chunk metadata when needed, raw only as fallback
- produce concept creation/refinement, insights, contradictions, summaries, and decision rules
- update graph links and generated indexes
- respect concept and insight creation rules and token budgets

## Forbidden in Phase 3

- treating frontmatter or JSONL indexes as reasoning truth
- rewriting concept pages only to add routine source backlinks
- creating concepts for tools, vendors, taxonomies, or source-specific examples
- crossing back into Phase 1 or Phase 2 ingestion in the same run

## Boundary rule

If parsing or source extraction is required, stop and route the work to Phase 1 or Phase 2 instead.

Follow `AGENTS.md` for all behavior not specified here.
