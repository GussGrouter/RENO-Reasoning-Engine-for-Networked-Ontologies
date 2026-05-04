# Source Page Template

> This file specializes root `AGENTS.md`; it may not weaken root scope, authority, phase, provenance, or anti-pattern rules.

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
