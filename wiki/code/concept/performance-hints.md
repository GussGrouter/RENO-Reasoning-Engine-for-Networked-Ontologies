# Performance hints

- Tag: mechanism

## Definition

A **performance hint** is information passed from a caller to a service that can avoid expensive work by the service if the hint is correct; the service must validate the hint so correctness does not depend on it.

## Scope note

This contrasts with “tips” (guaranteed-correct information) which require stronger correctness guarantees and may avoid validation cost.

## Relation

- A mechanism for recovering efficiency while retaining modularity by reducing associative lookup or dispatch overhead.
- Related to [[fast-path-slow-path]] when a validated hint enables a fast path and incorrect hints fall back to a slower path.

## Links

- Source: [[network-algorithmics-3-3-2-modularity-with-efficiency]]
- Source: [[systems-performance-filesystems-ch8-application-calls-fadvise-madvise-8-8-1]]
- Related concepts:
  - [[fast-path-slow-path]]

