# Source Repair (PLACEHOLDER)

This prompt is a **placeholder**. Do not use it yet.

Use `AGENTS.md` as the active policy file.

## Activation prerequisites

Do not invoke this prompt until all of the following exist:

- `structured/schema/source.schema.json`
- `scripts/validate_source_provenance.py`
- a Phase 2 source corpus with at least one detected provenance defect

When this prompt is filled in, it must:

- target a single named provenance defect (mismatched chunk/section ranges, broken `chunk_ids`, drifted `processed_ids`, stale `raw_id`, off-by-one page spans, fabricated section keys)
- repair the defect in source pages or processed manifests only
- preserve markdown body reasoning verbatim unless the user explicitly approves rewording
- log the repair in `wiki/meta/log.md` with date, source-id, defect kind, and remediation

## Forbidden during source repair

- reinterpreting source memory
- creating or refining concepts
- modifying raw bytes
- silent merges/splits

## Boundary rule

If a defect requires re-parsing, route the work back to Phase 1 instead of patching the source page.

Follow `AGENTS.md` for all behavior not specified here.
