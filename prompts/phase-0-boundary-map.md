# Phase 0 — Boundary Map

Use `AGENTS.md` as the active policy file. Inspect current repo state directly. Do not rely on prior chat memory. Run **Phase 0 only**.

This prompt creates processed boundary evidence for a book-length source before Phase 1 body ingestion. It must not create chunks, source pages, concepts, insights, or graph-visible reasoning pages.

---

## Scope

Allowed in this run:

- parse front matter / table of contents pages from the raw artifact
- create `processed/<source-id>/parse.candidate-frontmatter-contents-<pages>.json`
- create or update `processed/<source-id>/chapter_boundaries.json`
- record printed-page to PDF-page mapping, including Roman-numeral front matter
- record parser command, evidence basis, chapter starts/ends, evidence excerpts, confidence, and notes
- run boundary validation against any existing manifest for the source

Forbidden in this run:

- Phase 1 body chunking
- source pages
- concepts or insights
- chunk repair, deletion, rename, or relabeling
- edits to `raw/` or `archive/`

---

## Steps

1. Read `AGENTS.md` and inspect the raw source under `raw/<source-id>/`.
2. Parse the front matter / contents pages with LiteParse into a candidate parse file. Start conservatively if the exact contents pages are unknown.
3. Find the table of contents / chapter listing in the parse output.
4. Derive chapter start PDF pages from contents evidence and the printed-page to PDF-page offset.
5. Derive chapter end PDF pages from the next chapter start minus one when supported by the contents.
6. Mark ambiguous or unsupported boundaries with `confidence: low`; do not invent boundaries.
7. Write `processed/<source-id>/chapter_boundaries.json`.
8. Run:

```text
python3 scripts/validate_chapter_boundaries.py --source-id <source-id>
```

If validation fails or boundary evidence is ambiguous, stop and report. Do not continue into Phase 1.

---

## Completion Report

Report:

- raw path inspected
- parse command and output path
- pages parsed
- contents evidence found
- chapter boundaries created, including confidence
- printed-page/PDF-page mapping
- validator result
- confirmation that no chunks, source pages, concepts, or insights were created
