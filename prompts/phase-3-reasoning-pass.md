# Phase 3 — Reasoning and Ontology Construction

Use `AGENTS.md` as the active policy file. Run **Phase 3 only**.

Phase 3 compiles bounded source memory into reusable reasoning. It may create or refine concepts and insights only when the user explicitly requests a Phase 3 reasoning run. If the user asks for prerequisites or scaffolding only, do not create reasoning pages.

---

## Scope

Allowed in this run when explicitly requested:

- concept creation or refinement
- insight creation
- contradiction or boundary surfacing
- small cross-source synthesis
- concise navigation updates where useful
- graph consolidation for pages touched in the run
- log/index updates, or `manual/pending` markers when index tooling is absent

Forbidden in this run:

- Phase 1 parsing, chunking, or raw registration
- Phase 2 source extraction or rewriting source memory
- markdown chunk cards
- broad summaries unless explicitly requested and justified as navigation
- treating frontmatter, JSONL indexes, or processed JSON as reasoning truth
- creating concepts for tools, vendors, taxonomies, implementation details, or source-specific examples
- creating a large ontology pass when the user asked for a small test set

If parsing or source extraction is required, stop and route the work to Phase 1 or Phase 2.

---

## Evidence Order

Reason from:

1. **Source page bodies** under `wiki/source/` (primary evidence for Phase 3).
2. **Processed chunks** only as audit fallback when a source page claim is unclear, suspect, or needs chunk-level verification.
3. **Raw** only as final audit root when processed evidence is insufficient.

Do not reason from:

- YAML frontmatter alone
- generated JSONL indexes as truth
- chunk metadata without reading source memory, except for audit/provenance repair

Frontmatter is identity, navigation, status, and provenance. It is not technical evidence.

---

## Candidate Triage

Before creating pages:

1. Read the relevant bounded source pages in full.
2. Extract candidate concept names already recorded in Phase 2 source pages.
3. Merge duplicate or near-duplicate candidates.
4. Rename source phrasing into reusable idea names when appropriate.
5. Reject or defer weak candidates and report them.

Create a concept only when it is a reusable decision primitive:

- reusable mechanism, structure, tradeoff, method, policy lens, or general principle
- applicable outside one source page and outside one anecdote
- useful for future coding, architecture, debugging, performance, security, or systems decisions
- not cleanly represented by an existing or better-named concept

Reject concepts that are:

- source-specific examples or story characters
- tool-specific commands or products
- vendor names
- taxonomies with no decision use
- chapter/section labels
- routine bibliography items
- synonyms of a stronger candidate

Prefer merging/renaming candidates over creating many small concepts. For a small test, create only the requested number of pages and keep rejected/deferred candidates in the report.

---

## Concept Page Rules

Concept pages live under `wiki/concept/` and use flat frontmatter:

```yaml
---
id: <concept-id>
type: concept
status: active|draft|candidate|deprecated|needs-review
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Optional title"
---
```

Required body sections:

- H1 title
- `## Definition`
- `## Use when`
- `## Do not use when`
- `## Related concepts`
- `## Source support`

Keep concept pages as reusable reasoning, not source recap. Do not turn concept pages into source bibliographies. Cite source pages only as limited supporting evidence under `## Source support`; use at most a few foundational source links, not every source that mentions the idea. Routine support should come from incoming source links, generated indexes, and audits.

Do not encode source names, chapter numbers, tool names, or vendor names into concept IDs unless the concept is genuinely about a general mechanism with no better reusable name.

---

## Insight Page Rules

Insight pages live under `wiki/insight/` and use flat frontmatter:

```yaml
---
id: <insight-id>
type: insight
status: active|draft|candidate|deprecated|needs-review
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Optional title"
---
```

Required body sections:

- H1 title
- `## Claim`
- `## Concepts involved`
- `## Source basis`
- `## Decision use`

Create insights only for reusable cross-concept decision rules, contradictions, boundaries, implications, or synthesis. Do not force insights for every concept.

---

## Process

1. Run source/provenance validators before reasoning:

```text
python3 scripts/validate_frontmatter.py
python3 scripts/validate_chunk_chain.py
python3 scripts/validate_source_provenance.py
python3 scripts/check_token_budgets.py
```

2. Read the source pages requested by the user. Prefer their markdown bodies over frontmatter.
3. Build a candidate map:
   - candidate name
   - source pages that support it
   - reason to promote, merge, rename, reject, or defer
4. If the user asked for a small test set, create only that small set.
5. Create or update concept/insight pages only after candidate triage.
6. Do **not** rewrite source pages during concept creation unless a validator identifies a minimal navigation/provenance repair required for the current run.
7. Update source hubs, summaries, or indexes only when useful and within the requested scope. If `scripts/build_indexes.py` does not exist, mark JSONL index updates `manual/pending` in `wiki/meta/log.md`.
8. Run post-write validators:

```text
python3 scripts/validate_frontmatter.py
python3 scripts/validate_source_provenance.py
python3 scripts/validate_concepts.py
python3 scripts/validate_insights.py
```

Run additional graph or support audits when those scripts exist. If they do not exist, report them as `manual/pending`; do not claim those audits passed.

---

## Completion Report

Report:

- concepts or insights created/modified
- candidates promoted, merged/renamed, rejected, and deferred
- source pages read
- any processed chunks consulted as audit fallback
- validator output
- JSONL/index or graph audits still `manual/pending`
- confirmation that Phase 1 and Phase 2 work was not performed
