# RENO: Reasoning Engine for Networked Ontologies

## Purpose and Scope

RENO is a persistent ingest-time LLM wiki for technical reasoning. Its goal is to compile technical sources into a structured, interlinked, low-entropy reasoning system that improves coding, architecture, debugging, security, performance, and system-design decisions over time.

The wiki is the primary output. Chat is temporary.

This vault is technical-only by project boundary, not by folder names or `domain` tags. Business, political, ideological, personal, or broad PKM material belongs in separate vaults with separate policies.

Folders outside the active structure in this file are out of scope for normal ingestion, graph health, concept promotion, and retrieval unless the user explicitly names them in a task prompt.

The live codebase and external project filesystem are outside RENO by default. They may be inspected as read-only implementation evidence when a task explicitly asks for coding/build validation, but they must not be ingested, indexed, summarized, or mirrored into RENO unless the user explicitly requests a stable artifact or snapshot.

---

## Authority Model

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

Do not let parser output dictate concepts. Do not let JSONL indexes or YAML frontmatter become reasoning truth. Do not rewrite RENO into a database-first system.

---

## Roles

**Human**
- selects sources and focus
- reviews outputs
- approves ambiguous ontology changes
- decides what should be promoted, refined, contradicted, deprecated, or preserved

**LLM / Cursor**
- follows this file as policy
- executes only the requested phase/mode
- preserves provenance across `raw → processed → source → concept/insight/summary`
- treats frontmatter as navigation/provenance, not evidence
- updates links, indexes, and graph integrity
- keeps RENO separate from the live codebase unless the task explicitly asks for implementation validation

---

## Support Files

This file is the policy. Execution details should live in prompts, schemas, and scripts.

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

## Phase Workflow

Ingestion must keep parsing/source construction separate from ontology reasoning.

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
- `parse.json` exists or extraction exception is logged
- `manifest.json` exists
- chunks exist with stable IDs, hashes, spans, and token estimates
- chunk chain has no gaps or loops
- book/chapter slice boundaries validate against `chapter_boundaries.json`
- `scripts/validate_chapter_boundaries.py` has been run after every Phase 1 append when a boundary map exists or the slice is chapter-labeled
- indexes/logs are updated or marked `manual/pending`

### Phase 2 — Source Extraction

Purpose: convert processed chunks/spines into bounded source-shaped memory.

Allowed outputs:
- completed source hubs
- chapter/section source spines
- source pages tied to bounded chunk/section ranges
- compressed extracted source memory
- decision-relevant ideas
- short candidate concept names/IDs
- candidate contradictions and candidate insights in the page body

Forbidden outputs:
- new concept pages
- concept merges/splits
- concept refinements
- generalized ontology reasoning

Completion gate:
- source hub/page spine exists
- each source page links to processed chunks
- each source page has clear source scope
- source memory is compressed and close to the source
- candidates are recorded without promotion
- provenance audits back to chunks and raw

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

### Standard validator sequence

Run the validators that exist for the phase being executed. For Phase 1 appends on sources with `processed/<source-id>/chapter_boundaries.json`, or any chapter-labeled slice, include:

```text
python3 scripts/validate_chapter_boundaries.py --source-id <source-id>
```

If chapter-boundary validation fails, stop before Phase 2 or Phase 3 and repair the boundary map or slice plan. Generated indexes are rebuildable views; rebuild them with `scripts/build_indexes.py` and verify them with `scripts/check_indexes.py` after successful writes when those scripts exist.

---

## Knowledge Layers

```text
summary → concept → insight → source → processed → raw
```

The hierarchy is primary, but not every source must produce every layer.

Required for ingestion:
- raw
- processed
- source

Required for reusable reasoning:
- concept, when a reusable abstraction exists

Conditional:
- insight, only for real cross-concept synthesis, contradiction, boundary, or decision rule
- summary, only as navigation/index/routing layer

### Raw

Original, unmodified material. Never edit raw. Raw may include books, papers, transcripts, standards, docs, logs, architecture docs, protocol docs, first-party technical artifacts, internal notes, and explicit snapshots requested by the user.

Raw metadata should include at minimum: source type, title/origin, original path, content hash, license/copyright status when known, and ingestion status.

### Processed

Normalized parser and chunk material used for auditability. Includes LiteParse JSON, extracted text, layout data, page/section records, chunks, manifests, hashes, review views, and extraction warnings. Processed is evidence, not reasoning.

### Source

Bounded source-shaped memory tied to a specific source, section, chunk range, first-party artifact, or explicit snapshot. Source pages preserve source interpretation and provenance. They may contain candidates during Phase 2 but are not generalized concepts unless Phase 3 promotes the idea.

### Concept

Atomic reusable technical idea: mechanism, structure, tradeoff, method, policy lens, or general principle. A concept must be applicable beyond one source and must not be a tool/vendor/taxonomy item.

### Insight

A relationship between concepts: decision rule, contradiction, boundary, implication, or synthesis. Insights must link contributing concepts and source support where possible.

### Summary

A concise routing/index page. Summaries orient the agent to source hubs, concept clusters, and decision areas. They should link out rather than explain deeply.

Major sources should have a source hub that lists child source pages, ingestion status, extraction hazards, and phase status.

### Structured indexes

Generated JSONL support layer for metadata, filtering, links, contradictions, decisions, and audits. This layer supports the wiki; it does not replace it.

---

## Obsidian Graph Semantics

The Obsidian graph is the human visual/navigation graph. It is not the full provenance graph.

Default visible graph nodes:
- source hubs
- source pages
- concepts
- insights
- summaries/indexes

Excluded from the visible graph by default:
- raw files
- processed JSON
- chunk JSON
- parser output
- generated JSONL indexes

Chunks are canonical processed evidence, but they are not markdown graph nodes by default. Do not create markdown chunk cards during normal ingestion. Reference processed chunks from source pages through frontmatter `chunk_ids`, provenance sections, and generated indexes.

Source pages are the default graph-visible evidence layer. They should link with Obsidian wikilinks to:
- parent source hub
- previous/next source page when chronological order exists
- candidate or linked concepts

Source pages should reference processed chunk IDs/paths for audit, but should not create Obsidian chunk nodes unless the user explicitly requests a review/debug graph.

Concept pages are abstractions. Do not rewrite concept pages just to add every new supporting source. Concepts should primarily link to related concepts and high-signal insights. Source support should normally be maintained through incoming links from source pages, generated indexes, and audit scripts. Direct source links in concept pages should be reserved for foundational or defining sources.

Insights build on concepts. Summaries route to source hubs, concepts, and high-signal insights.

---

## Token Budgets

Token budgets are part of system correctness.

- **Chunk target:** 800–1,500 tokens; hard max 2,000
- **Source page target:** 200–600 words; hard max 1,000 unless hub/index
- **Concept page target:** 300–700 words; hard max 1,000
- **Insight page target:** 150–400 words; hard max 600
- **Top-level summary target:** <150 words
- **Book/source hub target:** 300–800 words, longer only for navigation lists
- **YAML frontmatter target:** 8–20 lines; hard max 30

Retrieval budget for coding-reasoning prompts:
- 1 summary maximum
- 3–6 concepts
- 1–3 insights
- 2–5 source pages only when evidence is needed
- processed/raw only for audit or missing context

Batch targets:
- Phase 1: 20–50 chunks or one coherent source/chapter slice
- Phase 2: 5–12 source pages
- Phase 3: 5–12 source pages or one conceptual cluster

Stop early if extracted ideas become repetitive or shallow.

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
- store full parser output as `processed/<source-id>/parse.json`
- preserve page numbers, text items, table/figure markers, bounding boxes if available, parser version, source hash, and extraction warnings
- derive chunks from parser output, not ad hoc copied text
- create markdown review files only as views over parser output
- log parser/layout disagreements and mark affected chunks/sources for review

Raw remains immutable.

---

## Metadata Rules

RENO uses small YAML frontmatter plus generated JSONL indexes.

### Frontmatter

Every maintained markdown page under `wiki/` should begin with small YAML frontmatter.

Base fields:

```yaml
---
id: stable-id
type: summary|concept|insight|source|index|decision|contradiction
status: active|draft|candidate|deprecated|needs-review
phase: phase-1-parsed|phase-2-source-built|phase-3-reasoned|not-applicable
parent: null
prev: null
next: null
source_id: null
---
```

Do not include `domain: technical`. This vault is technical by boundary; a domain tag is redundant noise.

Use optional fields only when useful and stable. Avoid `created_at`, `updated_at`, `last_reviewed`, `confidence`, and long `source_ids` lists unless scripts maintain them or they answer a real query.

### Metadata reasoning rule

Use frontmatter to:
- identify the page
- locate parent/previous/next pages
- locate chunks/source hubs
- track phase/status
- support indexing, audits, and graph repair

Do not use frontmatter to:
- infer technical truth
- define concept meaning
- support architecture decisions
- replace source body text
- replace processed/raw evidence
- replace implementation evidence from the live codebase

When reasoning, read markdown body and supporting source/chunk evidence. Ignore frontmatter unless the task is metadata, navigation, provenance repair, or audit.

### Minimal frontmatter by page type

Source page:

```yaml
---
id: <stable-source-id>
type: source
status: active|candidate|needs-review
phase: phase-2-source-built
source_kind: book-section|paper-section|standard-section|technical-doc|first-party-artifact|explicit-snapshot
source_id: <source-id>
raw_id: <raw-id>
processed_ids: []
chunk_ids: []
parent: null
prev: null
next: null
candidate_concepts: []
linked_concepts: []
---
```

Concept page:

```yaml
---
id: <concept-id>
type: concept
status: active|candidate|needs-review|deprecated
phase: phase-3-reasoned
importance: core|supporting
aliases: []
related_concepts: []
---
```

Insight page:

```yaml
---
id: <insight-id>
type: insight
status: active|candidate|needs-review|deprecated
phase: phase-3-reasoned
contributing_concepts: []
source_ids: []
---
```

Summary or source hub:

```yaml
---
id: <summary-or-source-id>
type: summary
status: active|draft|needs-review
phase: phase-1-parsed|phase-2-source-built|phase-3-reasoned|not-applicable
source_id: null
---
```

Keep candidate lists short. Store only stable IDs or concise names in frontmatter. Put explanations, uncertainty, and evidence in the markdown body or generated indexes.

### Processed and chunk metadata

Processed/chunk metadata belongs in `processed/<source-id>/` JSON/manifests, not wiki frontmatter.

Important processed fields:
- `processed_id`
- `raw_id`
- `parser`
- `parser_version`
- `parser_command`
- `source_hash`
- `page_range`
- `section_range`
- `extraction_warnings`
- `chunk_count`
- `generated_files`

Important chunk fields:
- `chunk_id`
- `processed_id`
- `raw_id`
- `source_id`
- `title`
- `page_start`
- `page_end`
- `token_estimate`
- `prev_chunk_id`
- `next_chunk_id`
- `content_hash`
- `review_status`

### Generated JSONL indexes

Start with:

```text
structured/indexes/files.jsonl
structured/indexes/chunks.jsonl
structured/indexes/sources.jsonl
structured/indexes/links.jsonl
structured/indexes/concepts.jsonl
structured/indexes/contradictions.jsonl
structured/indexes/decisions.jsonl
```

Optional later:
- `insights.jsonl`
- `entities.jsonl`
- `projects.jsonl`

Indexes are generated/rebuildable views. They do not replace markdown reasoning content.

### Sidecars

Do not create `.md.json` sidecars by default. Use sidecars only for exceptional audit reports, large migration reports, complex contradiction maps, or layout/bounding-box metadata that would clutter markdown.

---

## Page Templates

### Source Page Template

```markdown
---
id: <stable-source-id>
type: source
status: active|candidate|needs-review
phase: phase-2-source-built
source_kind: book-section|paper-section|standard-section|technical-doc|first-party-artifact|explicit-snapshot
source_id: <source-id>
raw_id: <raw-id>
processed_ids: []
chunk_ids: []
parent: null
prev: null
next: null
candidate_concepts: []
linked_concepts: []
---

# Source scope

- Source:
- Section / chunk span:
- Why this source matters:

# Graph navigation

- Hub:
- Previous source:
- Next source:
- Related concepts:

# Extracted source memory

-

# Decision-relevant ideas

- **Decision pressure:**
- **Tradeoff / mechanism:**
- **Failure mode:**

# Candidate concepts

-

# Contradictions / caveats

-

# Provenance

- Processed chunk IDs/paths:
- Raw audit root:
```

Rules:
- stay close to the source
- use Obsidian links for hub, previous/next source pages, and related concepts
- reference chunk IDs/paths for audit without creating markdown chunk cards by default
- do not create/redefine concepts
- keep candidate concepts as suggestions only
- prefer compressed bullets over prose essays

### Concept Page Template

```markdown
---
id: <concept-id>
type: concept
status: active|candidate|needs-review|deprecated
phase: phase-3-reasoned
importance: core|supporting
aliases: []
related_concepts: []
---

# Definition

One concise definition.

# Decision rule

Use this concept when <condition> because <reason>.

# Use when

-

# Do not use when

-

# Coding relevance

- Architecture:
- Debugging:
- Security / correctness:
- Performance:

# Failure modes

-

# Related concepts

-

# Source support

Do not list every supporting source. Use incoming source links, generated indexes, and audits for routine support. Add only foundational or defining sources here.

-
```

Rules:
- concepts are reusable reasoning, not source recap
- `Decision rule` is mandatory
- `Do not use when` is mandatory when over-application is plausible
- do not rewrite concept pages only to add routine source backlinks
- keep any direct source support high-signal

---

## Retrieval Rules

For reasoning queries, prefer:

1. summary/source hub
2. concepts
3. insights
4. source pages
5. processed chunks for audit/detail
6. raw only as fallback

Do not default to raw or structured indexes for reasoning. Use JSONL indexes when the question is about filtering, metadata, contradictions, chronology, link structure, or decisions.

For coding support:
- use RENO for reasoning frames, invariants, risks, and tradeoffs
- verify exact implementation details against the live repository/build workflow when the task explicitly permits filesystem inspection
- never let RENO override the live codebase

---

## Folder Structure

```text
/
├── AGENTS.md
├── SKILLS.md
│
├── prompts/
│   ├── phase-1-parse-chunk-spine.md
│   ├── phase-2-source-extraction.md
│   ├── phase-3-reasoning-pass.md
│   ├── graph-audit.md
│   ├── source-repair.md
│   └── coding-retrieval.md
│
├── raw/
│
├── processed/
│   └── <source-id>/
│       ├── parse.json
│       ├── manifest.json
│       ├── pages/
│       ├── sections/
│       ├── chunks/
│       └── review-md/
│
├── wiki/
│   ├── summary/
│   ├── concept/
│   ├── insight/
│   ├── source/
│   ├── indexes/
│   └── meta/
│       ├── index.md
│       └── log.md
│
├── structured/
│   ├── schema/
│   ├── exports/
│   └── indexes/
│
└── scripts/
```

No `technical/` folder or `domain: technical` tag is used. This vault is technical by policy and scope.

---

## Naming Rules

- use lowercase kebab-case
- keep names stable and descriptive
- name by reusable idea, not source phrasing
- prefer short canonical terms
- do not encode source names or chapter numbers in concept/insight names
- source/chunk files may include source name, chapter/section ID, section title, and chunk number
- prefer stable IDs over brittle line numbers

Example:

```text
systems-performance__ch10__sec10-6-13__chunk0001.json
systems-performance-network-ch10-observability-tcpdump-10-6-13.md
```

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

## Contradictions

Contradictions should not remain buried across sources.

Surface them through:
- insight pages when they create a reusable decision issue
- source body caveats when local
- `structured/indexes/contradictions.jsonl` when filtering/audit is useful

Do not smooth important tension into false consensus.

---

## Implementation Boundary

RENO is not the build playbook and does not mirror the live codebase.

Use RENO to support coding by ingesting stable first-party technical artifacts, such as:
- architecture docs
- protocol docs
- ADRs/design notes
- API contracts
- incident/debugging notes
- explicit implementation snapshots requested by the user
- first-party technical writeups

External filesystem inspection is allowed only when explicitly requested for a coding-reasoning task. Use it to verify current implementation facts, paths, APIs, configuration, build/test outputs, or repository state.

Do not convert filesystem findings into RENO source pages, concepts, summaries, indexes, or raw/processed artifacts unless the user explicitly asks to create a stable source artifact or snapshot.

If RENO reasoning conflicts with implementation truth, implementation truth wins.

A separate build/project instruction file may reference RENO as a reasoning substrate but should govern normal coding behavior.

---

## Working Mode

Cursor should:
- execute the requested phase/mode only
- keep changes minimal and precise
- preserve provenance and graph integrity
- keep frontmatter small
- reason from markdown body/source pages and processed chunks when needed, not frontmatter
- keep Obsidian graph links focused on hubs, source pages, concepts, insights, and summaries
- treat structured indexes as support, not reasoning truth
- respect token budgets and templates
- run or mark validation at phase gates
- avoid raw unless auditing or missing context
- avoid filesystem inspection unless explicitly requested

---

## Anti-Patterns

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
