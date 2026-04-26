# Graph Audit (PLACEHOLDER)

This prompt is a **placeholder**. Do not use it yet.

Use `AGENTS.md` as the active policy file.

## Activation prerequisites

Do not invoke this prompt until all of the following exist:

- `scripts/check_orphans.py`
- `scripts/check_broken_links.py`
- `scripts/check_concept_source_support.py`
- `scripts/check_phase_status.py`
- `scripts/build_indexes.py`
- a non-empty `wiki/` corpus produced by Phase 1 / Phase 2 / Phase 3

When this prompt is filled in, it must:

- audit frontmatter validity, reachability, source-to-chunk provenance, chunk chains, hub child listings, concept support, insight links, contradiction surfacing, JSONL index freshness, duplicates, broken links, and token budgets
- never mutate raw, processed, or archive material
- emit a single audit report and update `wiki/meta/log.md`

## Boundary rule

The graph audit is read-mostly. Only repair-grade edits (fix frontmatter typos, repair broken wiki links, regenerate JSONL indexes) are allowed, and only when the user explicitly requests audit-with-repair. Otherwise the audit only reports.

Follow `AGENTS.md` for all behavior not specified here.
