# Systems Performance — File system cache growth vs “free memory” (7.2.6) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.2.6** — **page cache** uses spare DRAM by design; **low “free”** can be healthy **reuse-ready cache**, not automatic pressure

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-concepts-filesystem-cache-usage-7-2-6.md`
- Chunks:
  - `processed/code/systems-performance-memory-concepts-filesystem-cache-usage-7-2-6-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Cache-as-freeable memory** means **utilization** of DRAM is high while **application saturation** may still be low—dashboard “free” is a **representation hazard** ([[caching]], [[measurement-validity]], [[utilization-and-saturation]]).
- (abstraction) Treating warm cache as waste triggers **bad decisions** (premature DRAM buys, aggressive cache dropping) when the real risk is **reclaim latency under concurrent fault load** ([[throughput-latency-metrics]]).

## Application validation

- **Post-boot “memory leak” alert with flat RSS**: first split **page cache growth** vs **anonymous RSS**—often no leak, only **working set warming**.

## Decision clarity

- **Decision**: choose **pressure/reclaim/swap/OOM witnesses** over **low free-memory panic** when **application latency** is still flat and **RSS** is stable.

## Concepts reused / refined / created

- Reused (mechanism): [[caching]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[caching]]
  - [[measurement-validity]]
  - [[utilization-and-saturation]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-concepts-utilization-saturation-7-2-7]]
  - [[systems-performance-memory-concepts-paging-7-2-2]]
