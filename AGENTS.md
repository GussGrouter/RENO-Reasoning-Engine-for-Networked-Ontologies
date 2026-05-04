# RENO: Reasoning Engine for Networked Ontologies

## Purpose

RENO is a persistent ingest-time LLM wiki for technical reasoning. It compiles technical sources into a structured, interlinked, low-entropy reasoning system that improves coding, architecture, debugging, security, performance, and system-design decisions over time. The wiki is the primary output; chat is temporary.

This vault is technical-only by project boundary, not by folder names or `domain` tags. Business, political, ideological, personal, or broad PKM material belongs in separate vaults with separate policies.

## Non-Negotiable Invariants

- RENO is a technical-only deep-knowledge vault, not a generic PKM system.
- Raw artifacts are immutable.
- Processed data is parser/chunk evidence, not reasoning.
- Source pages are bounded source-shaped memory tied to provenance.
- Markdown body is authoritative reasoning content.
- YAML frontmatter is only identity, status, navigation, and minimal provenance.
- Generated JSONL indexes are rebuildable query/audit views, not reasoning truth.
- Concepts and insights are created only in Phase 3.
- Phase 0/1/2/3 boundaries must stay strict.
- Validation, provenance, token budgets, graph hygiene, and implementation-boundary rules must not be weakened.
- Do not turn RENO into a database-first system.
- Do not make the live codebase part of RENO by default.

## Authority and Precedence

Use one authority per layer:

- **raw** = immutable original artifact
- **processed** = LiteParse/normalized parser output, chunks, hashes, page/section spans, manifests, and extraction warnings
- **source** = bounded source-shaped memory tied to chunks/sections/artifacts
- **concept / insight / summary** = compiled reusable reasoning
- **markdown body** = authoritative reasoning content
- **YAML frontmatter** = local identity, phase/status, navigation, and minimal provenance only
- **generated JSONL indexes** = rebuildable query/audit views
- **schemas + validation scripts** = enforcement layer
- **prompt templates** = execution layer
- **external codebase/filesystem** = implementation truth when explicitly inspected

Instruction precedence inside RENO:

1. User task prompt for the current run selects task scope, phase, source, and any explicit allowed exception.
2. Root `AGENTS.md` defines non-negotiable project invariants, authority, routing, and boundaries.
3. Relevant phase file defines phase permissions and procedure.
4. Relevant policy file defines cross-phase rules.
5. Relevant template file defines page shape.
6. Generated indexes, schemas, and scripts act as enforcement and audit artifacts.
7. Existing wiki content provides current project state.

Conflict rules:

- If the user task conflicts with root non-negotiables, stop and report the conflict instead of silently overriding RENO doctrine.
- `docs/agents/README.md` is navigational only; if README conflicts with root, phase, policy, or template files, README loses.
- `docs/agents/archive/AGENTS.monolith.before-split.md` is audit-only; it is not active policy after the split.
- The user may explicitly request allowed exceptions already described by root policy, such as implementation inspection or creating a stable snapshot.
- The user prompt does not automatically permit database-first reasoning, phase-boundary collapse, YAML/JSONL-as-truth, or generic PKM ingestion.
- If a subfile conflicts with root `AGENTS.md`, root wins.
- If a phase file conflicts with a policy file, the stricter rule wins unless root says otherwise.
- If generated indexes conflict with markdown body reasoning, markdown body wins.
- If YAML/frontmatter conflicts with markdown body reasoning, markdown body wins.
- If RENO reasoning conflicts with explicitly inspected live implementation truth, implementation truth wins for implementation facts only.

## Roles

**Human**
- selects sources and focus
- reviews outputs
- approves ambiguous ontology changes
- decides what should be promoted, refined, contradicted, deprecated, or preserved

**LLM / Cursor**
- follows this file as policy
- executes only the requested phase/mode
- preserves provenance across `raw -> processed -> source -> concept/insight/summary`
- treats frontmatter as navigation/provenance, not evidence
- updates links, indexes, and graph integrity
- keeps RENO separate from the live codebase unless the task explicitly asks for implementation validation

## Task Routing

Read root first, then only the subfiles relevant to the current task. If task scope or phase is ambiguous, ask or stop before crossing a phase boundary.

- New book-length source before body ingestion: `docs/agents/phases/phase-0-boundary-map.md`, `docs/agents/policy/scope-boundaries.md`, `docs/agents/policy/validation-audit.md`, `docs/agents/policy/token-budgets.md`.
- Parse/chunk/spine work: `docs/agents/phases/phase-1-parse-chunk-spine.md`, `docs/agents/policy/metadata-frontmatter-indexes.md`, `docs/agents/policy/validation-audit.md`, `docs/agents/policy/token-budgets.md`.
- Source page extraction: `docs/agents/phases/phase-2-source-extraction.md`, `docs/agents/policy/metadata-frontmatter-indexes.md`, `docs/agents/policy/graph-retrieval.md`, `docs/agents/policy/validation-audit.md`, `docs/agents/policy/token-budgets.md`, `docs/agents/templates/source-page-template.md`.
- Concept/insight creation: `docs/agents/phases/phase-3-reasoning-ontology.md`, `docs/agents/policy/authority-model.md`, `docs/agents/policy/graph-retrieval.md`, `docs/agents/policy/validation-audit.md`, `docs/agents/policy/token-budgets.md`, `docs/agents/templates/concept-page-template.md`.
- Coding support/retrieval task: `docs/agents/policy/implementation-boundary.md`, `docs/agents/policy/graph-retrieval.md`, and relevant phase/policy files only if the task also modifies RENO.
- Graph/index/audit repair: `docs/agents/policy/graph-retrieval.md`, `docs/agents/policy/metadata-frontmatter-indexes.md`, `docs/agents/policy/validation-audit.md`, `docs/agents/policy/anti-patterns.md`.

Use `docs/agents/README.md` only as navigation for the split instruction files.

## Phase Boundary Summary

Ingestion must keep parsing/source construction separate from ontology reasoning.

- Phase 0 creates boundary maps only; no source pages, concepts, insights, or graph-visible markdown from Phase 0 evidence alone.
- Phase 1 creates raw/processed/chunks/spines, generated index/log updates, and optional minimal source-hub skeletons for navigation only; no interpreted source essays, concepts, insights, or high-level synthesis.
- Phase 2 creates bounded source-shaped memory and candidates only; no concept pages, merges/splits, refinements, or generalized ontology reasoning.
- Phase 3 is the only phase for concepts, insights, contradiction synthesis, ontology decisions, and concept maintenance.
- If a task crosses a boundary, stop or split the task explicitly.

## Validation Summary

Run the validators that exist for the phase being executed. If referenced prompts, schemas, or scripts do not exist, do not claim automated validation passed; either create them when explicitly asked, or mark validation as `manual/pending`.

For Phase 1 appends on sources with `processed/<source-id>/chapter_boundaries.json`, or any chapter-labeled slice, run:

```text
python3 scripts/validate_chapter_boundaries.py --source-id <source-id>
```

If chapter-boundary validation fails, stop before Phase 2 or Phase 3 and repair the boundary map or slice plan. Generated indexes are rebuildable views; rebuild them with `scripts/build_indexes.py` and verify them with `scripts/check_indexes.py` after successful writes when those scripts exist.

## Implementation Boundary Summary

RENO is not the build playbook and does not mirror the live codebase. External filesystem inspection is allowed only when explicitly requested for a coding-reasoning task. Do not convert filesystem findings into RENO source pages, concepts, summaries, indexes, or raw/processed artifacts unless the user explicitly asks to create a stable source artifact or snapshot.

If RENO reasoning conflicts with implementation truth, implementation truth wins for implementation facts only.

## Anti-Pattern Summary

Do not:

- modify `raw/`
- create unlinked pages
- create concepts during Phase 1 or Phase 2
- let parsed chunks masquerade as reasoning
- use YAML frontmatter as evidence
- rely only on brittle line numbers
- create `.md.json` sidecars by default
- duplicate full metadata across frontmatter, sidecars, and indexes
- treat generated JSONL indexes as reasoning truth
- ingest non-technical material into this vault
- mirror the live codebase
- exceed token budgets without reason
- turn RENO into a generic PKM vault or database-first system

## Stop Conditions

Stop and ask or report the conflict when:

- the requested task crosses phase boundaries without explicit split/approval
- a user request conflicts with root non-negotiables
- validation fails at a phase gate
- provenance back to processed chunks/raw cannot be established where required
- a task would make YAML, JSONL, or parser output authoritative reasoning truth
- a task would ingest or mirror the live codebase by default
