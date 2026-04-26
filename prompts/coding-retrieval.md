# Coding Retrieval (PLACEHOLDER)

This prompt is a **placeholder**. Do not use it yet.

Use `AGENTS.md` as the active policy file.

## Activation prerequisites

Do not invoke this prompt until all of the following exist:

- a Phase 3 corpus with concept and insight pages
- generated JSONL indexes maintained by `scripts/build_indexes.py`
- the user has stated a coding-reasoning task that explicitly permits filesystem inspection if implementation evidence is needed

When this prompt is filled in, it must enforce the retrieval budget from `AGENTS.md`:

- 1 summary maximum
- 3–6 concepts
- 1–3 insights
- 2–5 source pages only when evidence is needed
- processed/raw only for audit or missing context

It must also:

- prefer reasoning frames, invariants, risks, and tradeoffs from RENO
- verify exact implementation details against the live repository when allowed
- never let RENO override implementation truth

## Forbidden during coding retrieval

- ingesting filesystem findings into RENO without an explicit snapshot request
- creating or refining concepts during a retrieval run
- using frontmatter or JSONL indexes as reasoning evidence

Follow `AGENTS.md` for all behavior not specified here.
