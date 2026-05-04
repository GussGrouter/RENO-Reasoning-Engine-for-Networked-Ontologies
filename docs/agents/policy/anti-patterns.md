# Anti-Patterns

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

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
