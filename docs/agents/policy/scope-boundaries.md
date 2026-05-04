# Scope Boundaries

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

## Purpose and Scope

RENO is a persistent ingest-time LLM wiki for technical reasoning. Its goal is to compile technical sources into a structured, interlinked, low-entropy reasoning system that improves coding, architecture, debugging, security, performance, and system-design decisions over time.

The wiki is the primary output. Chat is temporary.

This vault is technical-only by project boundary, not by folder names or `domain` tags. Business, political, ideological, personal, or broad PKM material belongs in separate vaults with separate policies.

Folders outside the active structure in this file are out of scope for normal ingestion, graph health, concept promotion, and retrieval unless the user explicitly names them in a task prompt.

The live codebase and external project filesystem are outside RENO by default. They may be inspected as read-only implementation evidence when a task explicitly asks for coding/build validation, but they must not be ingested, indexed, summarized, or mirrored into RENO unless the user explicitly requests a stable artifact or snapshot.

---

## Folder Structure

```text
/
├── AGENTS.md
├── SKILLS.md
│
├── prompts/
│   ├── phase-0-boundary-map.md
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
