# RENO

RENO is a work-in-progress system for turning technical books, papers, standards, and explicitly requested implementation snapshots into a structured, source-grounded LLM wiki for later reasoning. It is intended to make technical knowledge durable, auditable, and reusable across coding, architecture, debugging, performance, security, and systems-design work. In practice, RENO is meant to let an LLM answer engineering questions by retrieving source-supported concepts and insights instead of re-reading entire books from scratch.

RENO stands for **Reasoning Engine for Networked Ontologies**. The current repository is a technical deep-knowledge vault plus ingestion/policy scaffolding. It is not a generic PKM app, a vector-memory product, or a database-first knowledge system.

Implementation snapshots are in scope only when explicitly requested as stable source artifacts. The live codebase is not mirrored into RENO by default.

## Status

- WIP / experimental.
- Actively being developed.
- Current focus: stabilizing the ingestion pipeline and the source / concept / insight workflow.
- Not yet a polished package, hosted service, or one-command product.
- Existing prompts, validators, source pages, concepts, and insights should be treated as evolving project artifacts.

## Why RENO Exists

LLMs can summarize technical documents in chat, but chat output is temporary, hard to audit, easy to lose, and difficult to reuse across later decisions. RENO tries to make technical knowledge durable by converting selected sources into a structured wiki with provenance, graph links, validation scripts, and strict phase boundaries.

The goal is not to replace source review. The goal is to reduce repeated low-level re-reading while preserving enough source support to ask better questions and make better decisions later.

RENO is meant to support:

- reuse of technical knowledge across tasks and chats;
- source-grounded concept creation;
- auditable support for insights and decision rules;
- better architecture, coding, debugging, performance, and systems-design reasoning;
- cross-source retrieval without turning parser output or indexes into truth.

## Core Idea

The durable output is the wiki. Chat is temporary.

```text
raw -> processed chunks -> source pages -> concepts -> insights -> summaries/indexes
```

Each layer has a different authority:

- `raw/`: immutable original artifacts on your machine (PDFs, standards, papers, or explicitly requested snapshots). This directory is **gitignored** so private or copyrighted sources are not committed; manifests and wiki provenance may still reference paths and hashes.
- `processed/`: parser output, manifests, chunk JSON, hashes, page spans, section spans, and chunk-chain evidence. Processed data is evidence, not reasoning.
- `wiki/source/`: bounded source-shaped memory tied to explicit chunk ranges.
- `wiki/concept/`: reusable technical ideas created or refined only in Phase 3.
- `wiki/insight/`: relationships, tradeoffs, contradictions, boundaries, and decision rules created only in Phase 3.
- `wiki/meta/`: logs and navigation pages.
- `structured/indexes/`: generated, rebuildable JSONL query and audit views. These are not reasoning truth.
- `scripts/`: validators, index builders, and maintenance tooling.
- `prompts/`: execution prompts for phase-specific runs.
- `docs/agents/`: policy files for LLM/agent behavior.

Markdown body content is the main reasoning layer. YAML frontmatter is for identity, navigation, status, and provenance. JSONL indexes are rebuildable views over the wiki and processed evidence.

Concrete examples in this repository include `wiki/source/systems-performance-ch5-applications-p210-224.md`, `wiki/concept/observability-source-interface.md`, and `wiki/insight/choose-observability-source-by-question-risk.md`.

## Ingestion Pipeline

RENO ingestion is deliberately phased. The phase boundaries are part of the system, not administrative overhead.

### Phase 0 — Boundary Map

Phase 0 maps source boundaries before body ingestion, especially for book-length sources and chapter-based slices.

Typical output:

- `processed/<source-id>/chapter_boundaries.json`
- front-matter or contents parse evidence
- printed-page to PDF-page mapping
- boundary confidence and notes

Phase 0 does **not** create chunks, source pages, concepts, insights, or graph-visible reasoning pages.

### Phase 1 — Parse, Chunk, and Spine Build

Phase 1 registers raw artifacts, runs parsing, creates processed manifests, promotes parse files, creates chunk JSON files, and maintains a single linear chunk chain.

Typical output:

- `processed/<source-id>/manifest.json`
- `processed/<source-id>/parses/<slice-id>.json`
- `processed/<source-id>/chunks/<chunk-id>.json`
- chunk `prev_chunk_id` / `next_chunk_id` links
- validation and index updates

Phase 1 does **not** create source memory, concept pages, insight pages, markdown chunk cards, or high-level synthesis.

### Phase 2 — Source Extraction

Phase 2 turns validated chunk ranges into bounded source pages under `wiki/source/`.

Source pages preserve source-shaped memory, decision-relevant ideas, candidate concept names, candidate insight statements, caveats, and provenance. They stay close to the source's structure and language.

One Phase 2 run may create one or multiple bounded source pages from one requested chunk range when the source structure warrants it. Each bounded source page must cite chunk IDs from its own `chunk_ids` frontmatter and remain under the 1,000-word hard limit.

Phase 2 does **not** create concept pages, insight pages, generalized summaries, ontology decisions, or Phase 3 reasoning.

### Phase 3 — Reasoning and Ontology Construction

Phase 3 promotes high-signal candidates into reusable concepts and insights. This is the only phase that creates or refines concept and insight pages.

Phase 3 handles:

- reusable concept creation and refinement;
- cross-concept insights;
- contradiction surfacing;
- decision rules;
- ontology maintenance;
- graph consolidation for touched pages.

Phase 3 should reason from source page bodies first. Processed chunks and raw artifacts are audit fallback, not the normal reasoning substrate.

## Example: From Source to Concept to Insight

This example is illustrative. Actual RENO concepts and insights must be source-supported.

A source page from a performance engineering book might extract source memory about:

- I/O size versus latency and throughput;
- observability versus narrow benchmark wins;
- compiler frame pointer flags versus profiling quality;
- application performance objectives and Apdex.

Candidate or promoted concepts might include:

- `io-size-throughput-latency-tradeoff`
- `observability-over-narrow-benchmark-wins`
- `compiler-frame-pointer-vs-profiling-tradeoff`
- `quantified-performance-objectives-and-apdex`

An insight might connect concepts into a decision rule:

> When optimizing an application, a faster opaque stack can be worse than a slightly slower observable stack if the observable stack exposes removable work and supports better diagnosis.

The value is not the phrasing alone. The value is that the idea can point back to source pages and chunk provenance.

## How Concepts and Insights Are Useful

In practical use, a **concept** is a named, reusable technical idea. It should be source-supported, small enough to apply across tasks, and useful as a lens, checklist, or question generator. A concept is not just a summary of one source page. It is a compact abstraction that helps an agent recognize a mechanism or tradeoff again later.

An **insight** is a relationship between concepts. It often captures a tradeoff, contradiction, boundary, implication, or decision rule. Insights are useful when an LLM or developer must choose between approaches rather than merely recall facts.

Concepts and insights help an LLM or developer:

- retrieve source-grounded patterns relevant to a task;
- inspect linked source support before applying a general idea;
- compare implementation and architecture tradeoffs;
- avoid repeating low-level source review when the source support is already captured;
- ask better implementation, debugging, and review questions;
- produce a source-grounded recommendation, checklist, or caveat list;
- connect knowledge across multiple technical sources without treating YAML, JSONL, or parser output as reasoning truth.

### Reasoning flow

```text
task/question
  -> retrieve relevant concepts
  -> inspect linked source pages
  -> apply insights/tradeoffs
  -> produce decision checklist or recommendation
  -> cite/trace back to source support
```

### Reasoning example

Suppose a developer asks whether to optimize a service by changing async I/O, increasing I/O size, adding thread pools, or improving observability.

RENO might retrieve concepts such as:

- `io-size-throughput-latency-tradeoff`
- `observability-over-narrow-benchmark-wins`
- `quantified-performance-objectives-and-apdex`
- `compiler-frame-pointer-vs-profiling-tradeoff`

Then it would inspect the linked source pages and use insights to frame the decision:

- define the performance objective before tuning;
- optimize the common case rather than random code paths;
- beware opaque benchmark wins that make later diagnosis harder;
- preserve observability and profiling quality if future debugging matters.

Final recommendations should trace back to supporting source pages and provenance rather than treating concepts as free-floating advice.

That should produce better questions before recommending an implementation:

- What metric is being optimized: latency, throughput, utilization, price/performance, or Apdex?
- Is the workload latency-bound, throughput-bound, or utilization-bound?
- Is the common case known from profiling, tracing, logs, or application metrics?
- Would larger I/O reduce fixed overhead or add latency/cache waste for this workload?
- Would async I/O or thread pools reduce blocking, or just move the bottleneck?
- Will the change reduce observability, stack quality, or future profiling fidelity?
- Does the source support this as a general rule, or only as a context-specific caveat?

Concepts and insights should not be treated as magic truth. They are reusable reasoning aids that remain subordinate to source page bodies, explicit provenance, and current implementation facts when implementation has been inspected.

Example questions RENO should help answer:

- "What concepts should I consider when choosing between async I/O and thread pools?"
- "What source support do we have for keeping frame pointers enabled in production?"
- "What insights connect observability, profiling, and application performance goals?"

## How an LLM/Agent Should Use This Repo

Start with `AGENTS.md`. It is the root policy file and defines non-negotiable invariants, authority layers, task routing, phase boundaries, validation expectations, and stop conditions.

Then:

1. Follow the task routing in `AGENTS.md`.
2. Read only the relevant phase and companion policy files under `docs/agents/`.
3. Use `prompts/` for execution-layer instructions.
4. Never skip phase boundaries.
5. Do not treat YAML frontmatter, JSONL indexes, or parser output as reasoning truth.
6. Do not create concepts or insights outside Phase 3.
7. Run validators when modifying artifacts.

Example for Phase 2 source extraction:

1. Read `AGENTS.md`.
2. Read `docs/agents/phases/phase-2-source-extraction.md`.
3. Read required companion policy/template files, especially metadata, graph retrieval, validation, token budgets, and the source page template.
4. Execute `prompts/phase-2-source-extraction.md`.
5. Validate source provenance and token budgets before reporting completion.

## Repository Map

```text
AGENTS.md          Root policy and task routing for humans/agents.
docs/agents/       Split phase, policy, and template guidance for agents.
prompts/           Execution prompts for Phase 0/1/2/3 and repair/audit tasks.
raw/               Local/private originals (gitignored; do not commit copyrighted PDFs).
processed/         Parser output, manifests, chunk JSON, and chunk chains.
wiki/              Durable Markdown knowledge graph.
wiki/source/       Bounded source memory tied to chunks.
wiki/concept/      Reusable technical ideas.
wiki/insight/      Cross-concept relationships and decision rules.
wiki/meta/         Index and log pages.
structured/        Schemas, generated JSONL indexes, and export space.
scripts/           Validators, index builders, and maintenance tooling.
```

## Current Limitations / WIP

- RENO is evolving and should not be treated as a finished product.
- `raw/` is expected to exist locally for ingestion but is **ignored by git**; do not commit raw source bytes to public repos (copyrighted books, private material).
- Processed manifests and wiki pages may reference raw paths and content hashes; those artifacts can be shared without storing the raw files themselves.
- It is not yet a generic CLI/app or packaged workflow.
- Ingestion prompts and validators are still being refined.
- Source repair and graph audit workflows are present or under development as prompts/scripts in this repo, and should be treated as WIP unless validated for a specific task.
- Concepts and insights may need periodic review as source pages are repaired, split, or extended.
- Multi-domain knowledge should live in separate RENO-style vaults with separate policy, not in this technical vault by default.

## Non-Goals

RENO is not:

- a generic PKM system;
- a vector database;
- an automatic full-book summarizer;
- a replacement for source review;
- a live-codebase mirror;
- a database-first memory system;
- a place to ingest non-technical material into this vault.

## Suggested Next Steps for Contributors and Agents

- Inspect `AGENTS.md` before changing anything.
- Run existing validators before and after artifact changes.
- Work phase-by-phase.
- Keep changes small, bounded, and auditable.
- Prefer repair and audit before ontology rewrites.
- Preserve provenance from wiki pages back to processed chunks and raw artifacts.
- Treat generated indexes as rebuildable views, not as the source of truth.
