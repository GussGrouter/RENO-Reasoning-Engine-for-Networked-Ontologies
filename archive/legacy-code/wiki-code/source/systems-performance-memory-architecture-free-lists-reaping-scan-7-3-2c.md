# Systems Performance — Free lists, buddy NUMA hierarchy, reaping, kswapd scanning (7.3.2) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.2** — **free list / buddy** hierarchy (**per-node**), **reaping** slabs, **kswapd** LRU **inactive/active**, **direct reclaim**, **watermarks** (forward ref tuning), **“scanning”** term ambiguity vs historical Unix

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-architecture-free-lists-reaping-scan-7-3-2c.md`
- Chunks:
  - `processed/code/systems-performance-memory-architecture-free-lists-reaping-scan-7-3-2c-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Per-CPU single-page freelists** reduce **lock contention** but tie **allocation locality** to **scheduler placement**—another **composition** surface ([[cross-component-interactions]], [[resource-vs-implementation-bottleneck]]).
- (measurement) **“Scanning”** in **kswapd** means **LRU walk eligibility**, not **full-memory sweep**—comparing to **1980s textbooks** is a **semantics** trap ([[measurement-validity]]).
- (structure) **Direct reclaim** is **synchronous reclaim on allocation path**—shows up as **latency** under **allocation bursts**, not only as **background kswapd CPU** ([[utilization-and-saturation]], [[throughput-latency-metrics]]).

## Application validation

- **p99 spikes correlate with allocation storms** but **kswapd looks idle**: check **direct reclaim** / **watermark breach** path, not only **swap I/O**.

## Decision clarity

- **Decision**: choose **burst-aware reclaim tuning (watermarks / scale factor)** over **blind swapfile growth** when **latency collapses under allocation spikes** but **swap bytes** stay flat.

## Concepts reused / refined / created

- Reused (structure): [[cross-component-interactions]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (mechanism): [[caching]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[cross-component-interactions]]
  - [[resource-vs-implementation-bottleneck]]
  - [[measurement-validity]]
  - [[utilization-and-saturation]]
  - [[throughput-latency-metrics]]
  - [[virtual-memory-abstraction]]
  - [[caching]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-architecture-swappiness-swap-cgroups-7-3-2b]]
