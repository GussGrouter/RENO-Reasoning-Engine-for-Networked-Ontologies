## Purpose  

This repository is a persistent LLM wiki.    
Its goal is to **compile knowledge into a structured, interlinked, low-entropy system** that improves over time.  

The wiki covers two domains:  
- **Political Theory**  
- **Code Theory**  

The wiki is the primary output. Chat is temporary.  

---  

## Roles  

**Human**  
- selects sources  
- guides focus  
- reviews outputs  

**LLM (Cursor)**  
- ingests sources  
- extracts and compresses knowledge  
- updates and links pages  
- maintains structure, consistency, and graph integrity  

---  

## Core Principles  

- Prefer **compiled knowledge over raw sources**  
- Prefer **updating existing pages over creating new ones**  
- Keep pages **atomic (one main idea per page)**  
- Prefer **abstraction over quotation**  
- Reduce **duplication and entropy over time**  
- The wiki is a **graph, not a collection of files**  

---  

## Knowledge Hierarchy

```text
summary → concept → insight → source → raw
```

### Definitions

**Summary**: entry point that organizes and links a domain or large concept area  
- not atomic  
- used for navigation and scope  
- should not represent a single mechanism  
- must remain concise (typically <150 words)  
- should include a brief orientation layer:  
  - what the domain is used for  
  - what type of decisions it supports  
- should link out instead of explaining in detail  

**Concept**: atomic, reusable idea (mechanism, structure, or tradeoff)  
- must represent one core concept  
- should be applicable across contexts  
- should represent a reusable idea beyond the specific source  
- may originate from a single source if clearly generalizable  
- must NOT be tied only to a specific example or implementation  

Clarification (for method-type concepts):
- method: structured approach or checklist
- cycle: iterative loop
- technique: specific procedure or decomposition strategy
- framework: high-level reasoning structure

When creating a concept of type method/cycle/technique/framework:
- clarify its role relative to existing concepts in the Relation section
- do NOT merge or rename existing concepts
- do NOT retroactively rewrite existing pages

**Insight**: synthesis or decision rule derived from multiple concepts  
- expresses a relationship, boundary, or implication  
- not a standalone mechanism  
- must involve at least two concepts  

**Source**: structured extraction of a specific part of a source  
- supports concepts and insights  
- not authoritative on its own  

**Raw**: original, unmodified material  
- never edited  
- used only as fallback  

---  

## Retrieval Priority

When answering queries:

1. summary  
2. concept  
3. insight  
4. source  
5. raw (fallback only)  

Do not default to raw material.  

---  

## Folder Structure

/  
├── AGENTS.md  
├── raw/  
│   ├── political/  
│   └── code/  
│  
├── processed/  
│   ├── political/  
│   └── code/  
│  
├── wiki/  
│   ├── political/  
│   │   ├── summary/  
│   │   ├── concept/  
│   │   ├── insight/  
│   │   ├── source/  
│   │   └── indexes/  
│   │  
│   ├── code/  
│   │   ├── summary/  
│   │   ├── concept/  
│   │   ├── insight/  
│   │   ├── source/  
│   │   └── indexes/  
│   │  
│   ├── shared/  
│   │   ├── concept/  
│   │   └── insight/  
│   │  
│   └── meta/  
│       ├── index.md  
│       ├── log.md  
│  
└── scripts/

---  

## Domain Rules  

### Political Theory  

- governance, ideology, institutions, political economy, strategy  

### Code Theory  

- programming, systems, architecture, cryptography, tooling  

### Shared  

- only for genuinely cross-domain concepts  

---  

## Naming Rules  

Naming must optimize for stability, reuse, and low duplication.  

### General Rules  

- use lowercase kebab-case  
- keep names stable and descriptive  
- name by the reusable idea, not the source phrasing  
- prefer short, precise names (usually 2–4 words)  
- prefer canonical technical terms when they exist  
- prefer nouns or noun phrases over sentence-like names  
- do not encode source names in concept or insight page names  
- do not encode chapter numbers in concept or insight page names  
- add qualifiers only when necessary for disambiguation  

### Concept Naming  

Prefer:  
- canonical term names  
- reusable mechanism names  
- structure or tradeoff names  

### Insight Naming  

Name insights by:  
- a decision rule  
- a tradeoff  
- a boundary  
- a synthesis pattern  

### Source Naming  

Source pages may remain source-shaped and may include:  
- book/source name  
- section/topic  
- section numbering if useful  

---  

## Ingestion Rules  

### Concept Creation Rule (IMPORTANT)

A new concept SHOULD be created when:

- it represents a reusable mechanism, structure, or tradeoff  
- it appears in multiple contexts or is likely to reappear  
- it cannot be cleanly represented as a refinement of an existing concept  

Do NOT be overly conservative.

Prefer:
- creating a reusable concept early  
over:
- waiting for confirmation across multiple sources  

Avoid creating a concept when:
- it is only a specific example of an existing concept  
- it does not introduce a new mechanism, structure, or tradeoff  

Limit:
- max 1–2 new concepts per section  

If a page represents a domain, discipline, or field:

- DO NOT create it as a concept  
- create it as a summary  

When ingesting a source:

- normalize format (e.g. PDF → markdown)  
- chunk by meaning (small batches only)  
- extract:
    - concepts  
    - principles  
    - mechanisms  
- update existing pages first  
- create new pages only when necessary  
- link all relevant knowledge  

Raw sources are never modified.  

### Classification Test (use during ingestion)

Ask:

- Can this be applied directly? → Concept  
- Does it describe a relationship between concepts? → Insight  
- Is it just explaining part of a source? → Source  
- Is it an entry point to a domain? → Summary  

---  

## Page Rules  

- one main idea per page  
- avoid multi-topic pages  
- prefer explanation over copying  
- maintain consistent structure  

---  

## Linking Rules (CRITICAL)  

The wiki is a **graph**. Every page must be connected.  

### Concept pages MUST:

- link to at least one source  
- link to at least one related concept (if applicable)  
- be reachable from a summary or index  

### Source pages MUST:

- link to all supported concepts  
- not exist without concept references  

### Insight pages MUST:

- link to all contributing concepts  
- not exist without concept references  

### Summary pages MUST:

- act as entry points  
- link to core concepts and insights  

---  

## Concept Importance  

Concepts may be:

- core: widely reused, foundational  
- supporting: context-specific or secondary  

Prefer linking and reasoning with core concepts.  

---  

## Query Behavior  

- answer using the wiki, not raw files  
- synthesize across pages  
- prioritize clarity over coverage  
- prefer using a small number of highly relevant concepts (3–6)  
- avoid listing many concepts without synthesis  

---  

## Application Rule  

When possible:

- translate concepts and insights into actionable system design decisions  
- map abstract ideas to:
  - architecture  
  - tradeoffs  
  - constraints  

---  

## Indexing Rules  

- All concept, insight, and source pages MUST be listed in `wiki/meta/index.md`  
- The index is the primary navigation layer  
- The LLM must update the index on every ingest  

---  

## Graph Health Rules  

Periodically:

- detect orphan pages  
- detect weakly connected nodes  
- ensure concepts form connected clusters  

---  

## Linting  

Periodically:

- remove duplication  
- detect contradictions  
- fix orphan pages  
- suggest missing concepts  
- improve linking  

---  

## Working Mode (Cursor)  

- think in terms of repository state  
- prefer structured multi-file updates  
- keep changes minimal and precise  
- maintain graph integrity  

---  

## Concept Evolution Rules  

Concepts evolve over time and must remain stable.  

### Merge Rules  

- merge overlapping concepts  
- update all links  

### Split Rules  

- split concepts that become too broad  

### Stability Priority  

Prefer:
- refining existing concepts  
over:
- creating new ones  

---  

## Anti-Patterns  

Do not:

- duplicate knowledge  
- rely on raw sources by default  
- create unstructured pages  
- modify `/raw/`  
- collapse domains  
- create unlinked pages  

---  

## Success Condition  

The system is working when:

- most queries are answered without raw sources  
- knowledge becomes more compressed over time  
- pages are well-linked and non-duplicative  
- the graph is navigable and meaningful  
- new inputs improve structure instead of adding noise  
