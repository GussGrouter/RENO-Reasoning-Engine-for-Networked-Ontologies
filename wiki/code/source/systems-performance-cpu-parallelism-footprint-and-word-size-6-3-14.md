# Systems Performance — Parallelism width vs locality, and word-size footprint (6.3.14 + architecture bridge) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6 — misplaced “6.4 Architecture” bridge on **CPU span** (fewer vs more CPUs) plus Section **6.3.14 Word Size** (pointer/data footprint and performance tradeoffs)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-parallelism-footprint-and-word-size-6-3-14.md`
- Chunks:
  - `processed/code/systems-performance-cpu-parallelism-footprint-and-word-size-6-3-14-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Width is not free**: “use all CPUs” can lose to **running on fewer CPUs** when **synchronization + NUMA locality penalties** dominate extra parallelism—this is a **composition** decision, not a moral imperative to fill sockets ([[universal-scalability-law]], [[cross-component-interactions]]).
- (mechanism) **Word size couples** integer/register width, often **address space / pointer width**, and therefore **data footprint and memory traffic**—larger pointers can increase **DRAM traffic** even when arithmetic is “wider” ([[resource-vs-implementation-bottleneck]], [[throughput-latency-metrics]]).
- (measurement) **ABI / build choice changes semantics of “fast”**: running a **narrow build on a wide CPU** may work but can be **relatively poor** if it leaves registers/conventions on the table—treat as a **measurement validity** question for apples-to-apples comparisons ([[measurement-validity]]).

## Application validation

- **Go GC pressure**: moving to **64-bit pointers** on large heaps → measure **RSS + cache misses**, not only CPU%; the **footprint** term can dominate.

## Decision clarity

- **Decision**: choose **fewer active CPUs / stronger pinning** over **maximum parallelism** when **remote NUMA access + lock traffic** exceeds **compute parallelism gains**.

## Concepts reused / refined / created

- Reused (abstraction): [[universal-scalability-law]]
- Reused (structure): [[cross-component-interactions]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[universal-scalability-law]]
  - [[cross-component-interactions]]
  - [[resource-vs-implementation-bottleneck]]
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-multiprocess-multithreading-tradeoffs-6-3-13]]
  - [[systems-performance-cpu-compiler-optimization-pointer-6-3-15]]
