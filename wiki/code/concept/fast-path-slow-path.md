# Fast path vs slow path

- Tag: structure

## Definition

**Fast path vs slow path** is an implementation structure where the common, time-critical case is handled by a constrained, optimized pipeline (fast path), while uncommon or complex cases are diverted to a more flexible mechanism (slow path).

## Scope note

This is an architectural separation (not specific to routers): it appears in kernels, runtimes, storage systems, and network devices.

## Relation

- A recurring way to manage [[resource-vs-implementation-bottleneck]] by constraining worst-case work in the critical path.
- Supports [[network-algorithmics]] by making “where work runs” (pipeline vs general code) a first-class design decision.

## Links

- Source: [[network-algorithmics-2-3-2-router-architecture]]
- Source: [[systems-performance-buffering-polling-scalability-5-2-3-4]]
- Source: [[systems-performance-lock-fastpath-midpath-slowpath-rcu-5-2-5]]
- Related concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[network-algorithmics]]

