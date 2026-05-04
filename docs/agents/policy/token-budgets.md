# Token Budgets

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

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
