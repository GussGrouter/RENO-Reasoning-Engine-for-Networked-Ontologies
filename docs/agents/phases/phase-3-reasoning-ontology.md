# Phase 3 - Reasoning and Ontology Construction

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

## Use With

- `docs/agents/policy/authority-model.md`
- `docs/agents/policy/graph-retrieval.md`
- `docs/agents/policy/validation-audit.md`
- `docs/agents/policy/token-budgets.md`
- `docs/agents/templates/concept-page-template.md`

### Phase 3 — Reasoning and Ontology Construction

Purpose: compile source memory into reusable reasoning.

Allowed outputs:
- concept creation/refinement
- insight creation
- contradiction surfacing
- cross-source synthesis
- concise summaries/navigation maps
- decision rules
- graph consolidation

Reason from:
1. source pages
2. processed chunk metadata when needed
3. raw only as fallback/audit root

Completion gate:
- candidate concepts are mapped, rejected, or promoted
- concept pages have source support
- insights link contributing concepts
- summaries/hubs are updated only where useful
- graph/index updates are complete or marked `manual/pending`
- concept/source support audit passes or is marked `manual/pending`

---

## Concept and Insight Rules

Create concepts only in Phase 3.

A concept should be created when:
- it represents a reusable mechanism, structure, tradeoff, method, or policy lens
- it can apply across contexts
- it cannot be cleanly represented by refining an existing concept

Do not create concepts for:
- tools
- vendors
- implementation details
- taxonomies
- source-specific examples

Limit new concepts to 1–2 per source cluster unless explicitly doing concept-maintenance.

Create insights only when there is:
- a contradiction that affects a decision
- a reusable cross-concept decision rule
- a boundary between concepts
- a multi-source synthesis worth preserving

Do not force insights or summaries.

---

## Concept Maintenance

Concept merges, splits, renames, and deprecations should happen only during explicit concept-maintenance or Phase 3 tasks.

When merging or splitting concepts:
- update links and generated indexes
- preserve aliases where useful
- preserve source support
- log the change

---

## Contradictions

Contradictions should not remain buried across sources.

Surface them through:
- insight pages when they create a reusable decision issue
- source body caveats when local
- `structured/indexes/contradictions.jsonl` when filtering/audit is useful

Do not smooth important tension into false consensus.
