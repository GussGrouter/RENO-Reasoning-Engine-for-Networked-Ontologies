# Bounded recent-history buffer

- Tag: structure

## Definition

A **bounded recent-history buffer** retains only the most recent \(N\) items (or last \(T\) time window) so that decisions made later can still reference recent evidence without unbounded storage growth.

## Scope note

This is a generic structure (often implemented as a ring buffer/queue) used in monitoring, security, tracing, and streaming systems.

## Relation

- Often paired with indexing or deferred processing to make retrieval feasible at decision time.
- Relates to [[time-space-tradeoff]]: retaining more history increases space, but reduces “missed evidence” risk.

## Links

- Source: [[network-algorithmics-3-2-algorithms-vs-algorithmics]]
- Related concepts:
  - [[time-space-tradeoff]]

