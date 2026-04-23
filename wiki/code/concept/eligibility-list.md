# Eligibility list

- Tag: structure

## Definition

An **eligibility list** is an auxiliary structure that maintains the set of currently eligible items (ready tasks, active flows, runnable VCs), allowing selection without scanning ineligible entries.

## Scope note

This is redundant state: it must be maintained as eligibility changes (items become eligible/ineligible).

## Relation

- A concrete instance of “add/exploit state to gain speed” (see [[incremental-computation]] for a related “update instead of recompute” pattern).
- Often supports fair selection policies (e.g., round-robin) without paying linear scan overhead.

## Links

- Source: [[network-algorithmics-4-2-atm-flow-control-scheduler]]
- Related concepts:
  - [[incremental-computation]]

