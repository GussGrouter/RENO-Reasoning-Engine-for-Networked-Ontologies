# Phase 2 — Source Extraction

Use `AGENTS.md` as the active policy file. Run **Phase 2 only**.

This prompt converts a validated Phase 1 chunk chain into bounded source-shaped memory: one source hub per major source plus one or more bounded source pages tied to specific chunk ranges. A single Phase 2 run may produce **one or several** bounded pages from the **requested** contiguous chunk range when split planning (below) warrants it. It must not produce concept pages, insight pages, generalized summaries, or ontology reasoning. Source hubs are navigation summaries only. It must not parse, re-parse, or re-chunk any raw artifact.

---

## Activation prerequisites

Before invoking this prompt, all of the following must already exist for the target `<source-id>`:

- `processed/<source-id>/manifest.json` (validates against `structured/schema/processed-manifest.schema.json`)
- `processed/<source-id>/chunks/*.json` (validate against `structured/schema/chunk.schema.json`)
- `structured/schema/source.schema.json`
- `scripts/validate_source_provenance.py`
- `scripts/check_token_budgets.py`

Run, in order, before extracting anything:

```text
python3 scripts/validate_frontmatter.py
python3 scripts/validate_chunk_chain.py
python3 scripts/check_token_budgets.py
```

All three must exit `0` against the current tree before Phase 2 may write any source page. If any validator fails, stop and report.

---

## Architecture

For major sources (books, multi-section standards, multi-chapter docs):

- **One source hub** at `wiki/source/<source-id>.md` with frontmatter `type: summary` and `id: <source-id>-hub`. The hub is a navigation node that lists bounded child source pages, ingestion status, extraction hazards, and per-section phase status. The hub does **not** contain extracted source memory.
- **One or more bounded source pages**, each tied to a specific section or chunk **sub**range, e.g. `wiki/source/<source-id>-<section>-<scope>.md` with frontmatter `type: source`. A bounded source page **must** be limited to the chunks it declares (usually a contiguous subrange of one Phase 1 slice). One Phase 2 invocation may create **multiple** such pages from **one** user-requested chunk range when split planning shows distinct subsections or density pressure. Do not create a single giant source page covering the whole book.
- **Chronological prev/next links** between bounded source pages whose underlying chunks are contiguous along the chunk chain. Use Obsidian wikilinks. The first bounded page has `prev: null`; the last has `next: null` for now and is updated when later pages are added.
- **Chunks remain JSON-only** under `processed/<source-id>/chunks/`. Phase 2 cites their `chunk_id`s in source-page frontmatter and body. Phase 2 must not create markdown chunk cards (`chunks/*.md`, `wiki/chunk/*.md`, etc.) and must not turn chunk JSON into graph-visible nodes.

For small single-section sources (one paper, one technical note, one ADR), the hub may be omitted: a single bounded source page with `parent: null` is acceptable. The default still produces a hub when more than one bounded page is anticipated.

---

## Naming conventions

- **Hub file:** `wiki/source/<source-id>.md`. Hub `id`: `<source-id>-hub`.
- **Bounded source page file:** `wiki/source/<source-id>-<section-tag>-<scope-tag>.md`. The bounded page `id` equals its filename without the `.md` suffix.
- `<section-tag>` is a short kebab-case label for the section (e.g. `ch1-introduction`, `ch10-network`, `sec10-6-13`). Prefer the same section-range label used in `manifest.section_range` whenever it is short enough; otherwise abbreviate.
- `<scope-tag>` is a short bound for what the page covers (`p40-55`, `chunks-0001-0007`, `subsec-10-6-13`). Page-range scope is preferred when the underlying chunks are contiguous by page; chunk-id scope is preferred when section boundaries cut across pages. When several bounded pages are carved from one Phase 1 slice, use distinct scope tags (e.g. different page spans or chunk ordinals) so filenames and ids stay unique and navigable.

Example for the current Systems Performance Chapter 1 slice:

```text
wiki/source/systems-performance.md                              ← hub
wiki/source/systems-performance-ch1-introduction-p40-55.md      ← bounded page
```

with bounded-page id `systems-performance-ch1-introduction-p40-55`.

---

## Inputs

- `<source-id>`: the kebab-case source identifier (e.g. `systems-performance`).
- `<bounded-page-id>`: filename stem / frontmatter `id` for **each** bounded source page **created** after split planning (one id per file). A user may supply a provisional label for a single-page extraction; if the plan splits the range, derive distinct ids per contiguous chunk subrange.
- `<chunk-id-range>`: the contiguous list of `chunk_id`s requested for this Phase 2 run (one unbroken segment of the chunk chain, in chain order). Split planning partitions this list into subranges per bounded page without gaps or reordering.
- `<section-range>`: matches `manifest.section_range` for the underlying chunks when available.
- `<page-range>`: derived from `chunk.page_start`/`chunk.page_end` of the included chunks.
- `<source-kind>`: copied from `manifest.source_kind`.

If any input is missing or ambiguous, stop and report. Do not invent inputs. The requested `<chunk-id-range>` is validated as one contiguous chain segment; **bounded page split planning** (next section) then decides whether it becomes one bounded source page or multiple, each with its own `<bounded-page-id>` and contiguous chunk subrange.

---

## Bounded page split planning

Before writing any source pages, inspect the requested `<chunk-id-range>` (text and structure implied by chunk boundaries / headings in chunk `text`) and write a short **bounded page split plan** for the completion report: either one page or an ordered list of planned pages with contiguous chunk subranges and brief rationale.

**Prefer a single bounded source page** when:

- the requested chunk range is one coherent source unit;
- the page can preserve useful mechanisms, caveats, and decision-relevant detail without harmful over-compression;
- the page can stay reasonably near the soft word target (~600 words).

**Split into multiple bounded source pages** when:

- the chunk range spans multiple distinct source subsections;
- candidate concepts would become too diverse for one page (~6 cap per page still applies per page);
- decision-relevant ideas clearly belong to different mechanisms or themes;
- one page would force dropping important technical detail solely for length;
- one page would likely exceed the soft target by a large margin while dense material remains.

**Rules:**

1. Split by **source structure** (headings, subsection boundaries visible in chunk text) **first**, then assign **contiguous chunk subranges**—never skip or reorder chunks across pages.
2. Each bounded page **must**: cover a **contiguous** chunk subrange; stay within one coherent subsection or a tightly related group of subsections; cite **only** chunk IDs listed in **that** page’s own `chunk_ids` frontmatter; use correct `parent` / `prev` / `next` with neighbours and any newly inserted siblings; keep body ≤ **1,000** words hard max; **prefer ~300–700 words** when the source material is dense.
3. **Do not** create one markdown page per chunk by default; chunks remain JSON-only. Splitting is for readability and fidelity, not mechanical chunk fan-out.

If this Phase 2 run creates **multiple** bounded pages from one requested range: update the hub’s bounded-page list in chunk-chain order; refresh `prev` / `next` across **all** new pages **and** neighbouring existing pages (only navigation fields on neighbours unless an explicit repair scope says otherwise); append **all** created `<bounded-page-id>` values and chunk subranges to `wiki/meta/log.md` and to the completion report.

---

## Steps

### 1. Validate inputs against processed evidence

- Read `processed/<source-id>/manifest.json` and confirm it parses, has `ingestion_status` of `phase-1-parsed` or later, and lists `chunk_count` matching the number of chunk JSONs under `processed/<source-id>/chunks/`.
- Load every chunk JSON under `processed/<source-id>/chunks/` and verify they form a single linear chain with no gaps or loops.
- Confirm the requested `<chunk-id-range>` is contiguous in chain order. Stop and report if it is not.
- Produce the **bounded page split plan** (see § Bounded page split planning) before creating files; adjust planned `<bounded-page-id>` and per-page chunk subranges accordingly.
- Use `manifest.json` and `chunks/*.json` directly. Do not re-mine promoted parser output under `processed/<source-id>/parses/` except for explicit audit/repair tasks.
- Do not re-parse the raw PDF.

### 2. Create or update the source hub (when needed)

If `wiki/source/<source-id>.md` does not exist or is still a Phase 1 skeleton:

- Create or update it with frontmatter:

  ```yaml
  ---
  id: <source-id>-hub
  type: summary
  status: active
  phase: phase-2-source-built
  parent: null
  prev: null
  next: null
  source_id: <source-id>
  ---
  ```

- Body sections (terse, navigation only):

  - `# <human-readable title>`
  - `## Scope` — one or two lines describing what the source is and what is in scope for ingestion.
  - `## Ingestion status` — bullets for raw registration, parser/version, current `ingestion_status`, and outstanding extraction hazards.
  - `## Bounded source pages` — wikilinks to every bounded source page that exists for this source, in chunk-chain order, plus their page/section span.
  - `## Provenance` — `processed/<source-id>/manifest.json` link/path, raw artifact path under `raw/<source-id>/`, parser version.

The hub does not contain extracted source memory, candidate concepts, decision-relevant ideas, or contradictions. Those belong in bounded source pages.

If the hub already exists and the only change is "add the new bounded page link(s) to the index", limit edits to the `## Bounded source pages` list and `## Ingestion status` if it has shifted.

### 3. Create bounded source page(s)

For **each** planned bounded page in the split plan, create `wiki/source/<bounded-page-id>.md` with the following template. Frontmatter must match `structured/schema/source.schema.json`. Frontmatter is flat: scalars or inline arrays only. No nested YAML.

```yaml
---
id: <bounded-page-id>
type: source
status: active
phase: phase-2-source-built
parent: <source-id>-hub
prev: <previous-bounded-page-id-or-null>
next: <next-bounded-page-id-or-null>
source_id: <source-id>
raw_id: <raw-id-from-manifest>
processed_ids: ["<processed-id-from-manifest>"]
chunk_ids: ["<chunk-id-1>", "<chunk-id-2>", "..."]
title: "<human-readable title for this bounded slice>"
source_kind: <source_kind copied from manifest>
section_range: <section_range copied from manifest, when available>
---
```

Body sections (in this order, all required unless noted; keep total under ~600 words soft target where feasible, **prefer ~300–700 words when the slice is dense**, hard max 1,000 per page):

- `# <Title>` — the human title.
- `## Source scope` — one bullet for the source name, one bullet for the section/chunk span (page range and chunk-id range), one bullet stating why this slice matters for technical reasoning.
- `## Graph navigation` — Obsidian wikilinks: `Hub: [[<source-id>-hub]]`, `Previous: [[<prev-bounded-page-id>]]` or `null`, `Next: [[<next-bounded-page-id>]]` or `null`. Concept links go in `## Candidate concepts` only — do **not** link to concept pages from this section.
- `## Section outline` — short list of the source's own section/subsection headings covered by this bounded page, in source order. Use the source's own headings; do not invent headings.
- `## Extracted source memory` — compressed bulleted notes faithful to the source, grouped by the headings in `## Section outline`. Each bullet group must reference its supporting `chunk_id`(s) inline, e.g. `_chunks: chunk-0003, chunk-0004_`. Stay close to the source's own language; do not generalize.
- `## Decision-relevant ideas` — short bullets with explicit substructure when present:
  - `**Decision pressure:**`
  - `**Tradeoff / mechanism:**`
  - `**Failure mode:**`
  - Skip subfields that are not warranted by the slice. Do not invent decisions the source did not raise.
- `## Candidate concepts` — kebab-case candidate concept names only (one per line, no definitions, no decision rules). These are suggestions for Phase 3, not concept pages. Cap the list at ~6 candidates per bounded page; if a slice generates more, prioritise the highest-signal ideas.
- `## Candidate insights` — one-line candidate insight statements citing involved candidate concept names. Mark clearly as candidate. Do not write full insight reasoning.
- `## Contradictions / caveats` — explicit contradictions or boundaries the source itself raises within this slice, or `None observed.` Do not synthesize cross-source contradictions.
- `## Provenance` — explicit `processed_id`, every `chunk_id` in the slice, raw artifact path, page range, and a one-line audit pointer back to `processed/<source-id>/manifest.json`.

Every claim group in `## Extracted source memory` and `## Decision-relevant ideas` must cite at least one `chunk_id` from **that page’s** `chunk_ids:` frontmatter (the slice for that file only). Body claim citations must use chunk IDs that appear in that frontmatter; `validate_source_provenance.py` enforces this.

Do **not**:

- create concept pages, insight pages, or summary pages
- merge, split, refine, or deprecate existing concepts
- create markdown chunk cards
- write generalized cross-source synthesis
- exceed the 1,000-word hard max for the body
- copy long verbatim quotes when a compressed bullet would do

### 4. Link bounded page(s) from the hub and from neighbours

- Add **every** new bounded page to the hub's `## Bounded source pages` list, in chunk-chain order.
- Update the hub's `## Ingestion status` if Phase-2 coverage of the source has changed.
- Repair the source’s bounded-page chain: if multiple pages are inserted, set `prev`/`next` (and graph navigation sections) so order matches chunk-chain order end-to-end—including links **between** the new pages and links from/to existing neighbours. Update only navigation fields on neighbours unless an explicit repair scope says otherwise; do not re-extract neighbour bodies.

### 5. Update meta and indexes

- Append to `wiki/meta/log.md` for this Phase 2 run: date, source-id, **bounded page split plan summary**, every **bounded-page-id** created with its chunk subrange, validation status, and JSONL index status.
- Update `wiki/meta/index.md` so the new bounded page is reachable through the hub. The index page should not list every bounded page; one link to the hub is enough.
- If `scripts/build_indexes.py` exists, run it and report status. If it is unavailable or explicitly out of scope for the run, mark `structured/indexes/sources.jsonl`, `structured/indexes/chunks.jsonl`, and `structured/indexes/links.jsonl` as `manual/pending`. Do not hand-write generated indexes.

### 6. Validation

Run, in order:

```text
python3 scripts/validate_frontmatter.py
python3 scripts/validate_chunk_chain.py
python3 scripts/validate_source_provenance.py
python3 scripts/check_token_budgets.py
```

All four must exit `0`. Other audits (`check_orphans.py`, `check_broken_links.py`, `check_concept_source_support.py`, `check_phase_status.py`) remain `manual/pending` until their scripts exist; note that fact in the log entry.

---

## Completion report

When finishing the run, report at least:

- The **bounded page split plan** (one page vs several; brief rationale tied to source structure / density).
- Whether the source hub was created or updated.
- Every **bounded-page-id** file created or materially updated, each with its **chunk subrange**, PDF/page span if known, and `prev` / `next` relationship when multiple pages were created from one requested range.
- Validator outcomes and index status as elsewhere in this prompt.
- Confirmation that no Phase 1 parsing/chunking or Phase 3 concept/insight work was performed.

If only one bounded page was created, state that explicitly.

---

## Completion gate

Phase 2 is complete for this requested chunk range only when all of the following hold:

- The **bounded page split plan** has been stated (completion report or equivalent).
- The source hub exists, has valid frontmatter, lists **all** new bounded page(s), and is reachable from `wiki/meta/index.md`.
- **Each** bounded source page created for this run exists, has valid frontmatter, and validates against `structured/schema/source.schema.json`.
- Every `chunk_id` in each bounded page's `chunk_ids:` frontmatter exists as a real chunk JSON file under `processed/<source-id>/chunks/`.
- Every Obsidian-style chunk ID mentioned in a bounded page body exists as a real chunk JSON file and is listed in **that** page’s `chunk_ids`.
- Every claim group in each bounded body cites at least one `chunk_id` from **that** page’s `chunk_ids:` frontmatter.
- `prev` / `next` between bounded pages of the same source form a single non-branching chain in chunk-chain order (including across multiple pages produced in one run).
- `wiki/meta/log.md` has been appended.
- All four validators exited `0`.
- Token budgets respected: **each** source body ≤ 1,000 words; no chunk in the underlying chain exceeds 2,000 tokens.

If any item fails, stop and report. Do not start Phase 3.

---

## Forbidden in Phase 2

- creating, refining, merging, splitting, or deprecating concept pages
- creating insight pages
- creating new summary pages outside the source hub
- generalized ontology reasoning, cross-source synthesis, or cross-source contradiction surfacing
- markdown chunk cards or graph-visible chunk nodes
- modifications to `archive/`, existing `raw/` artifacts, or `AGENTS.md`
- modifications to `processed/<source-id>/chunks/*.json` (chunk JSON is immutable in Phase 2; if a chunk is wrong, run a Phase 1 repair task instead)
- re-parsing or re-chunking the raw artifact
- crossing into Phase 3 work in the same run
- using YAML frontmatter as evidence

If a step would require any of the above, stop and report. Do not cross phase boundaries.

---

## Reminders

- Frontmatter is identity / navigation / provenance. It is not reasoning evidence.
- Source pages stay close to the source's own language and structure.
- Candidate concept names go in the bounded page; concept pages are a Phase 3 deliverable.
- Split planning may yield multiple bounded pages from one requested `<chunk-id-range>`; each page stays chunk-backed, JSON-only chunks, ≤1,000 words, with chain-correct `prev`/`next`.
- Archive material is read-only and is not migrated by this prompt.
- The live codebase is out of scope unless the user explicitly requests filesystem inspection for a coding-reasoning task.
