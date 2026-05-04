# Implementation Boundary

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

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
