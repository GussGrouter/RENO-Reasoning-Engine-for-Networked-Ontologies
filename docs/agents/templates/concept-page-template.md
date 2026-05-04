# Concept Page Template

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

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
