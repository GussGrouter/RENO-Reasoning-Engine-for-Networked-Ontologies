# Metadata, Frontmatter, and Indexes

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

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
