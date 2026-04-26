# Shift computation in time

- Tag: heuristic

## Definition

To **shift computation in time** is to move work away from a time-critical point of use to another time (earlier, later, or amortized), improving the critical-path cost.

## Scope note

This includes tactics such as precomputation, lazy evaluation, and batching/expense sharing.

When an operation has a large fixed “setup” cost (privilege checks, metadata allocation, boundary crossings), batching/coalescing larger units of useful work onto the same setup amortizes that overhead—often the driver behind larger I/O or RPC batches.

## Specific tactic: lazy processing at eviction

**Lazy processing at eviction** defers expensive per-key work until an item naturally leaves a bounded buffer/window (eviction time), instead of doing the full work immediately when a key is flagged or detected.

Often used in streaming/online settings: it trades “immediate completeness” for reduced peak work on the critical path.

- Often used together with a [[bounded-recent-history-buffer]].
- A way to reduce implementation overhead in the fast path, relating to [[resource-vs-implementation-bottleneck]].
- Support: [[network-algorithmics-3-2-algorithms-vs-algorithmics]].

## Relation

- Often trades latency, memory, or staleness for throughput (related to [[time-space-tradeoff]] and [[throughput-latency-metrics]]).

Batching and “initialization tax” amortization are the same **shift work off the critical path** pattern; the product tradeoff (bigger batches vs per-unit latency) is already expressed under [[throughput-latency-metrics]], not a separate “batching concept.”

## Links

- Source:
  - [[network-algorithmics-3-3-1-systems-principles]]
  - [[network-algorithmics-3-2-algorithms-vs-algorithmics]]
  - [[systems-performance-linux-kernel-developments-3-4-1]]
  - [[systems-performance-io-size-tradeoffs-5-2-1]]
  - [[systems-performance-buffering-polling-scalability-5-2-3-4]]
  - [[systems-performance-nonblocking-io-async-models-5-2-6]]
  - [[systems-performance-cpu-profiling-methodology-sampling-vs-instrumentation-6-5-4]]
  - [[systems-performance-cpu-interrupt-gpu-tools-and-distribution-visualizations-6-6-19-6-7-4]]
- Related concepts:
  - [[time-space-tradeoff]]
  - [[throughput-latency-metrics]]
  - [[bounded-recent-history-buffer]]
  - [[resource-vs-implementation-bottleneck]]

