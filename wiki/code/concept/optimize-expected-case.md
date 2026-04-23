# Optimize the expected case

- Tag: heuristic

## Definition

To **optimize the expected case** is to make the common/typical behavior fast, even if uncommon behaviors become slower, provided overall performance improves under realistic workloads.

## Scope note

This relies on identifying (or learning) what “expected” means; it can drift over time.

## Relation

- Often implemented via caching and prediction; relates to [[performance-hints]] when a likely-correct hint enables fast handling.
- Can change bottleneck classification by moving cost from the fast path to rare paths (see [[fast-path-slow-path]] and [[resource-vs-implementation-bottleneck]]).

## Links

- Source: [[network-algorithmics-3-3-3-speeding-up-routines]]
- Source: [[systems-performance-pgo-kernels-3-5-1]]
- Source: [[systems-performance-optimize-common-case-5-1-2]]
- Source: [[systems-performance-thread-pool-and-seda-patterns-5-2-5]]
- Source: [[systems-performance-hash-lock-striping-and-chains-5-2-5]]
- Related concepts:
  - [[fast-path-slow-path]]
  - [[performance-hints]]
  - [[resource-vs-implementation-bottleneck]]

