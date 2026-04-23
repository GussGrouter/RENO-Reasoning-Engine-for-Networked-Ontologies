# Handle as index

- Tag: mechanism

## Definition

**Handle as index** is an interface pattern where a caller passes back a compact identifier (a handle) that can be used as a direct index into a service’s internal table, avoiding associative lookup on the full key.

## Scope note

The handle must be validated (bounds/checks, generation counters, etc.) so correctness and protection do not depend on untrusted caller behavior.

## Relation

- A concrete instance of [[performance-hints]]: the handle accelerates lookup but must be checked.
- Often enables a fast path by replacing expensive hashing/search with constant-time validation (see [[fast-path-slow-path]]).

## Links

- Source: [[network-algorithmics-4-1-buffer-validation]]
- Related concepts:
  - [[performance-hints]]
  - [[fast-path-slow-path]]

