# Authority Model

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

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
