# Systems Performance — CPU concepts: pipeline, width, and SMT (6.3.3–6.3.6) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Sections 6.3.3–6.3.6 (pipelining, branch prediction costs, superscalar width, instruction size/CISC vs RISC, SMT behavior and contention)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-concepts-pipeline-width-and-smt-6-3-3-6.md`
- Chunks:
  - `processed/code/systems-performance-cpu-concepts-pipeline-width-and-smt-6-3-3-6-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) **Pipelining + superscalar width** raise **best-case IPC ceiling**; **branch mispredicts** discard speculative work—control-flow stability affects throughput like any other **implementation** constraint ([[resource-vs-implementation-bottleneck]]).
- (abstraction) **Instruction encoding width** (CISC vs RISC footprints) feeds **I-fetch pressure**—ties binary size and alignment to front-end behavior without naming a vendor as the lesson ([[throughput-latency-metrics]]).
- (structure) **SMT siblings share a core’s execution resources**—kernel spreading load across cores to **avoid sibling contention** is a capacity policy, not “anti-parallelism” ([[utilization-and-saturation]], [[cross-component-interactions]]).

## Application validation

- **HT off vs on**: when p99 improves with only one thread per core busy, treat SMT as **shared-core contention** for latency-sensitive tiers, not as “free cores.”

## Decision clarity

- **Decision**: choose **SMT-aware packing (one busy sibling per core)** over **maximal logical CPU packing** when workloads are IPC-high and latency-sensitive.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (structure): [[cross-component-interactions]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[throughput-latency-metrics]]
  - [[utilization-and-saturation]]
  - [[cross-component-interactions]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-concepts-instruction-lifecycle-and-stall-cycles-6-3-2]]
  - [[systems-performance-cpu-concepts-ipc-utilization-and-user-kernel-time-6-3-7-9]]
