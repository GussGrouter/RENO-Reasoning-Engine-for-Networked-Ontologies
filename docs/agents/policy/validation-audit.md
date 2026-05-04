# Validation and Audit

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

## Support Files

This file defines validation/audit policy. Execution details should live in prompts, schemas, and scripts.

### Prompt templates

Recommended:

```text
prompts/phase-0-boundary-map.md
prompts/phase-1-parse-chunk-spine.md
prompts/phase-2-source-extraction.md
prompts/phase-3-reasoning-pass.md
prompts/graph-audit.md
prompts/source-repair.md
prompts/coding-retrieval.md
```

### Schema files

Start with the minimum useful set:

```text
structured/schema/frontmatter.schema.json
structured/schema/processed-manifest.schema.json
structured/schema/chunk.schema.json
structured/schema/source.schema.json
structured/schema/concept.schema.json
structured/schema/insight.schema.json
structured/schema/summary.schema.json
structured/schema/index-record.schema.json
structured/schema/contradiction.schema.json
structured/schema/decision.schema.json
```

### Validation scripts

Start with the minimum useful set:

```text
scripts/validate_frontmatter.py
scripts/validate_chunk_chain.py
scripts/validate_chapter_boundaries.py
scripts/validate_source_provenance.py
scripts/build_indexes.py
scripts/check_indexes.py
scripts/check_token_budgets.py
scripts/check_orphans.py
scripts/check_broken_links.py
scripts/check_concept_source_support.py
scripts/check_phase_status.py
```

If referenced prompts, schemas, or scripts do not exist, do not claim automated validation passed. Either create them when explicitly asked, or mark validation as `manual/pending`.

Once `build_indexes.py` exists, JSONL indexes should be regenerated from markdown frontmatter, markdown links, and processed metadata instead of hand-maintained.

---

### Standard validator sequence

Run the validators that exist for the phase being executed. For Phase 1 appends on sources with `processed/<source-id>/chapter_boundaries.json`, or any chapter-labeled slice, include:

```text
python3 scripts/validate_chapter_boundaries.py --source-id <source-id>
```

If chapter-boundary validation fails, stop before Phase 2 or Phase 3 and repair the boundary map or slice plan. Generated indexes are rebuildable views; rebuild them with `scripts/build_indexes.py` and verify them with `scripts/check_indexes.py` after successful writes when those scripts exist.

---

## Audit Rules

Audit rules combine indexing, graph health, and linting.

Check periodically or at phase gates:
- every maintained page has valid frontmatter
- all maintained concept, insight, summary, source, and source-hub pages are listed in `wiki/meta/index.md` or a generated index referenced from it
- concept, insight, summary, and source pages are reachable
- source pages reference processed chunk IDs/paths for provenance
- chunk JSON records form valid previous/next chains
- book/source hubs list their children
- concepts have support through incoming source links, generated indexes, audits, or a few foundational direct links
- insights link contributing concepts
- contradictions affecting decisions are surfaced
- generated JSONL indexes are rebuilt or marked `manual/pending`
- duplicate pages and broken links are corrected
- token budgets are respected

---

## Success Conditions

RENO works when:
- most reasoning queries are answered without raw sources
- source provenance audits through processed chunks to raw
- chunk JSON records and source pages form stable spines
- concepts are reusable and source-supported without becoming source bibliographies
- insights exist only where they preserve real synthesis, contradiction, or decision rules
- summaries/hubs improve navigation without becoming essays
- the graph is connected and low-duplication
- generated JSONL indexes are rebuildable
- validation catches drift before it affects reasoning
- RENO supports coding decisions without becoming a stale shadow codebase
