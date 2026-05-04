## Purpose  

This repository is a persistent LLM wiki.  
Its goal is to **compile knowledge into a structured, interlinked, low-entropy system** that improves over time.  

The system is best understood as:  

**a technical reasoning compiler with retained source memory**  

The wiki is the primary output. Chat is temporary.  

This repository uses a **hybrid architecture**:  
- **LLM wiki = compiled reasoning layer**  
- **minimal structured backend = operational/query support layer**  

The wiki remains the primary reasoning substrate.  
The structured backend exists to support metadata, filtering, contradictions, decision tracking, and operational queries. It must not replace the wiki or become the primary reasoning layer.  

The repository covers three domains:  
- **Code**  
- **Business**  
- **Political**  

---  

## Roles  

**Human**  
- selects sources  
- guides focus  
- reviews outputs  
- decides what should be promoted, refined, or contradicted  

**LLM (Cursor)**  
- ingests sources  
- extracts and compresses knowledge  
- updates and links pages  
- maintains structure, consistency, and graph integrity  
- preserves provenance across raw → processed → source → concept/insight/summary  

---  

## Core Principles  

- Prefer **compiled knowledge over raw sources**  
- Prefer **updating existing pages over creating new ones**  
- Keep pages **atomic (one main idea per page)**  
- Prefer **abstraction over quotation**  
- Reduce **duplication and entropy over time**  
- The wiki is a **graph, not a collection of files**  
- Preserve **provenance and auditability** through intermediate layers  
- The wiki is optimized for **technical understanding, architecture reasoning, system design, debugging, security reasoning, tradeoff analysis, and reusable decision primitives**  
- The structured backend is optimized for **metadata, filtering, contradiction surfacing, decision history, codebase-linked operational facts, and lightweight structured querying**  
- Do **not** rewrite this repository into a database-first system  
- Do **not** collapse the hierarchy into a generic PKM vault  

---  

## Architectural Recommendation  

This repository should remain a **disciplined ingest-time LLM wiki with provenance**.  

The recommended architecture is:  

- **raw** = immutable originals  
- **processed** = normalized slices/chunks for auditability  
- **source** = source-shaped extracted memory tied to specific materials or subsystems  
- **concept / insight / summary** = compiled reusable reasoning  
- **structured backend** = thin metadata/index/query support layer  
- **wiki** = primary reasoning interface  
- **codebase** = first-class technical substrate inside the code domain  
- **separate build/project instructions may consume the wiki during implementation**  

This design exists because:  
- pure LLM wikis are high leverage but vulnerable to silent synthesis drift  
- retained source memory improves auditability and recovery  
- technical work benefits from precompiled concepts, insights, and summaries  
- operational queries benefit from lightweight structured support  
- a thin structured backend solves query weakness without sacrificing the strengths of the wiki  

The current system is closer to **Karpathy's ingest-time wiki** than to **OpenBrain's query-time database**, but it is stronger than a plain LLM wiki because it preserves intermediate layers. It is **not** a full operational memory/database system.  

---  

## Knowledge Hierarchy

```text
summary → concept → insight → source → raw
```

The hierarchy remains primary.  
Do **not** replace it with a database-first model.  
The structured backend is auxiliary and minimal.  

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

**Concept**: atomic, reusable idea (mechanism, structure, tradeoff, policy lens, or domain-general principle)  
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
- expresses a relationship, boundary, contradiction, implication, or operating rule  
- not a standalone mechanism  
- must involve at least two concepts  

**Source**: structured extraction of a specific part of a source  
- supports concepts and insights  
- preserves source-shaped memory and provenance  
- should stay close to the source or subsystem it came from  
- not authoritative on its own  

**Processed**: normalized / chunked / sliced materials used for ingestion and auditability  
- derivative of raw material  
- may be transformed for readability, chunking, or extraction  
- exists to support ingestion, review, and traceability  

**Raw**: original, unmodified material  
- never edited  
- may include books, papers, transcripts, codebase exports, docs, notes, logs, architecture docs, protocol docs, first-party technical materials, and internal artifacts  
- used only as fallback and audit root  

**Structured backend**: minimal metadata/query support, not the main reasoning layer  
- stores metadata, timestamps, tags, entities, project names, codebase links, contradiction markers, decision records, and operational facts that benefit from precise filtering  
- supports lightweight structured querying and multi-agent/automation workflows  
- must support the wiki, not replace it  

---  

## Layer Responsibilities  

### A. Compiled reasoning layer  

This is the existing wiki system. It remains responsible for:  
- summaries  
- concepts  
- insights  
- source pages  
- compression of knowledge into reusable abstractions  
- technical worldview formation  
- architecture reasoning  
- tradeoff reasoning  
- provenance-aware synthesis  

This layer is optimized for questions like:  
- how should I think about this?  
- what reusable concept applies here?  
- what design tradeoff is present?  
- what does this imply for system architecture?  
- what abstractions should guide implementation?  

### B. Minimal structured backend  

This is **not** the main wiki. It is a thin support layer.  

It should be responsible for:  
- source metadata  
- timestamps  
- tags  
- entities  
- project names  
- codebase links  
- contradiction markers  
- decision records  
- operational facts that benefit from precise filtering  
- lightweight support for structured querying  
- better support for multi-agent or automation workflows  

This layer is optimized for questions like:  
- show all auth decisions after a date  
- find all records tied to a project  
- list contradictions related to one subsystem  
- retrieve all sources linked to one entity  
- track decision changes over time  

The structured backend exists to **support** the wiki, not replace it.  

---  

## Retrieval Priority

When answering queries:

1. summary  
2. concept  
3. insight  
4. source  
5. raw (fallback only)  

Use the structured backend when the question is fundamentally about filtering, metadata, contradiction lookup, or operational facts rather than reusable reasoning.  

Do not default to raw material.  
Do not default to the structured backend for reasoning questions.  

---  

## Folder Structure

/  
├── AGENTS.md  
├── raw/  
│   ├── political/  
│   ├── business/  
│   └── code/  
│  
├── processed/  
│   ├── political/  
│   ├── business/  
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
│   ├── business/  
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
├── structured/  
│   ├── schema/  
│   ├── exports/  
│   └── indexes/  
│  
└── scripts/

---  

## Domain Rules  

### Classification Rule

Classify by the **main decision the material helps make**.

- If it primarily helps decide **how the system should be built or how the code works** → `code`  
- If it primarily helps decide **how the company should be packaged, sold, adopted, or monetized** → `business`  
- If it primarily helps explain **institutional meaning, power structure, governance, or ideological grounding** → `political`  

### Code  

Use for:  
- programming  
- systems  
- architecture  
- cryptography  
- security engineering  
- protocols  
- tooling  
- implementation  
- project technical docs  
- the actual codebase  

This domain represents:  
**how the system works**  

The code domain includes both **technical theory** and the **actual first-party project codebase**.  

First-party project materials are especially important inputs. Treat as high-priority source material:  
- the codebase itself  
- architecture docs  
- protocol docs  
- internal technical notes  
- design notes  
- incident/debugging notes  
- first-party implementation docs  

When external abstraction conflicts with implementation truth, **implementation truth takes priority**.  

### Business  

Use for:  
- marketing  
- sales  
- positioning  
- pricing  
- distribution  
- market structure  
- customer acquisition  
- go-to-market reasoning  
- business operations  
- startup/operator reasoning  
- market trend analysis  
- relevant transcripts/books/videos about company growth and adoption  

This domain represents:  
**how the company wins**  

### Political  

Use for:  
- governance  
- ideology  
- institutions  
- political economy  
- monopoly / power analysis  
- trust infrastructure critique  
- pirate grounding  
- institutional framing  

This domain represents:  
**why the system matters**  

### Shared  

- only for genuinely cross-domain concepts  
- keep strict and minimal  

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
- a contradiction made legible  

### Source Naming  

Source pages may remain source-shaped and may include:  
- book/source name  
- section/topic  
- section numbering if useful  
- subsystem or codebase area if useful  

---  

## Ingestion Rules  

### Concept Creation Rule (IMPORTANT)

A new concept SHOULD be created when:

- it represents a reusable mechanism, structure, tradeoff, or policy lens  
- it appears in multiple contexts or is likely to reappear  
- it cannot be cleanly represented as a refinement of an existing concept  

Do NOT be overly conservative.

Prefer:
- creating a reusable concept early  
over:
- waiting for confirmation across multiple sources  

Avoid creating a concept when:
- it is only a specific example of an existing concept  
- it does not introduce a new mechanism, structure, tradeoff, or policy lens  

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
    - contradictions  
    - decision rules  
- update existing pages first  
- create new pages only when necessary  
- link all relevant knowledge  
- preserve provenance through processed and source layers  
- where useful, record metadata for the structured backend (timestamps, tags, entities, project names, codebase links, contradictions, decision records)  

Raw sources are never modified.  

### Classification Test (use during ingestion)

Ask:

- Can this be applied directly? → Concept  
- Does it describe a relationship between concepts? → Insight  
- Is it just explaining part of a source or subsystem? → Source  
- Is it an entry point to a domain? → Summary  
- Is it metadata, chronology, contradiction state, entity linking, or an operational fact that benefits from precise filtering? → Structured backend  

---  

## Page Rules  

- one main idea per page  
- avoid multi-topic pages  
- prefer explanation over copying  
- maintain consistent structure  
- keep contradiction visible when it matters  

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
- preserve enough specificity that a concept can be challenged or refined later  

### Insight pages MUST:

- link to all contributing concepts  
- not exist without concept references  
- make contradictions explicit when those contradictions matter for decisions  

### Summary pages MUST:

- act as entry points  
- link to core concepts and insights  

---  

## Contradictions  

Contradictions should not remain buried across sources.  

When detected, contradictions should be surfaced explicitly through:  
- insight pages  
- contradiction markers  
- structured backend metadata if appropriate  

The system should not only preserve contradiction; it should also make contradiction **legible**.  

Do not smooth important tension away into false consensus.  
If two views matter for a real decision, preserve the gap.  

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
- use the structured backend when the user needs precise filtering, chronology, contradiction lookup, or project/entity-level operational facts  

---  

## Application Rule  

When possible:

- translate concepts and insights into actionable system design decisions  
- map abstract ideas to:  
  - architecture  
  - tradeoffs  
  - constraints  
  - implementation choices  
  - business packaging / GTM / pricing / positioning decisions  
  - political / institutional framing when relevant  

---  

## Indexing Rules  

- All concept, insight, and source pages MUST be listed in `wiki/meta/index.md`  
- The index is the primary navigation layer  
- The LLM must update the index on every ingest  
- Structured backend schemas/exports/indexes should be documented separately and must not replace the wiki index as the main reasoning navigation layer  

---  

## Graph Health Rules  

Periodically:

- detect orphan pages  
- detect weakly connected nodes  
- ensure concepts form connected clusters  
- ensure contradictions that affect decisions are surfaced, not merely stored  

---  

## Linting  

Periodically:

- remove duplication  
- detect contradictions  
- fix orphan pages  
- suggest missing concepts  
- improve linking  
- review whether structured metadata would make recurring operational queries easier without moving reasoning out of the wiki  

---  

## Working Mode (Cursor)  

- think in terms of repository state  
- prefer structured multi-file updates  
- keep changes minimal and precise  
- maintain graph integrity  
- preserve the hierarchy and provenance logic  
- treat the wiki as the primary reasoning substrate  
- treat the structured backend as a thin support layer  

---  

## Codebase Priority  

The codebase is a first-class project substrate inside the code domain.  

Use first-party project materials aggressively.  
If there is a conflict between external theory and the actual implementation, give priority to the implementation, then explain the conflict.  

Architecture docs, protocol docs, code comments, internal design notes, and project-specific technical writeups should be treated as high-value source material because they describe how the system actually works.  

---  

## Future Build / Project Workflow  

This repository governs **knowledge ingestion and compiled reasoning**.  
It is not the build playbook.  

A separate future build/project MD may govern implementation workflows. That build/project file should:  
- reference this wiki  
- use the wiki as a reasoning substrate  
- prefer `wiki/code` for architecture / security / technical decisions  
- prefer `wiki/business` for market / positioning / pricing / GTM reasoning  
- prefer `wiki/political` for framing / worldview / institutional justification  

The build/project workflow may consume the wiki during implementation, but it must not replace the wiki as the repository's knowledge system.  

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
- let the structured backend become the primary reasoning layer  
- rewrite the project into an OpenBrain-style database system  
- turn the repository into a generic PKM vault  

---  

## Success Condition  

The system is working when:

- most reasoning queries are answered without raw sources  
- knowledge becomes more compressed over time  
- pages are well-linked and non-duplicative  
- the graph is navigable and meaningful  
- new inputs improve structure instead of adding noise  
- the wiki remains the primary reasoning substrate  
- the structured backend improves filtering, contradiction surfacing, and operational querying without replacing the wiki  
- the codebase is treated as a first-class technical substrate in the code domain  
