# Graph and Retrieval

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

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
