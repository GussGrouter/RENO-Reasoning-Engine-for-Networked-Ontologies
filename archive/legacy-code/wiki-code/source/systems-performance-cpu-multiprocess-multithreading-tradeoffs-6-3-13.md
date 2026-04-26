# Systems Performance — Multiprocess vs multithreading as a scalability packaging choice (6.3.13) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.3.13 (software parallelism models; scalability framing; Table 6.1 attributes summarized as tradeoffs, not as taxonomy to memorize)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-multiprocess-multithreading-tradeoffs-6-3-13.md`
- Chunks:
  - `processed/code/systems-performance-cpu-multiprocess-multithreading-tradeoffs-6-3-13-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Parallelism packaging**: “use all CPUs” requires **multiple schedulable contexts**; **how** you package work (process boundaries vs shared-address threads) changes **isolation, communication cost, and coherency pressure**—not just peak FLOPS ([[process-abstraction]], [[universal-scalability-law]]).
- (mechanism) **Process model** trades **MMU / address-space lifecycle costs** and **IPC** for **stronger fault containment**; **threads** reduce creation/communication overhead but **amplify shared-state coupling** ([[context-switching]], [[resource-vs-implementation-bottleneck]]).
- (measurement) **Scalability is an empirical curve**, not the CPU count: effective speedup depends on **serialization, synchronization, and memory behavior** as width grows ([[universal-scalability-law]], [[measurement-validity]]).

## Application validation

- **Edge service**: need blast-radius isolation → **worker processes + bounded IPC**; accept higher baseline CPU for **fork/IPC** vs a single giant threaded binary.

## Decision clarity

- **Decision**: choose **multiprocess** over **threads** when **failure isolation / upgrade granularity** dominates **shared-memory micro-latency** needs (and budget the **IPC + address-space** tax explicitly).

## Concepts reused / refined / created

- Reused (abstraction): [[process-abstraction]]
- Reused (abstraction): [[universal-scalability-law]]
- Reused (mechanism): [[context-switching]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[process-abstraction]]
  - [[universal-scalability-law]]
  - [[context-switching]]
  - [[resource-vs-implementation-bottleneck]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-priority-inversion-and-inheritance-6-3-12]]
  - [[systems-performance-cpu-parallelism-footprint-and-word-size-6-3-14]]
