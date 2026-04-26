# Systems Performance — Allocator design axes (fragmentation, contention, observability) (7.3.3) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.3** — **allocator feature checklist**: API, **fragmentation/coalesce**, **lock / per-thread caches**, **stats & debug**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-allocator-design-tradeoffs-7-3-3c.md`
- Chunks:
  - `processed/code/systems-performance-memory-allocator-design-tradeoffs-7-3-3c-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Allocator choice** is multi-objective: **throughput**, **RSS shape**, **tail latency under contention**, and **debuggability** trade off—no single “fastest malloc” ([[resource-vs-implementation-bottleneck]], [[throughput-latency-metrics]]).
- (measurement) **Observability as a first-class feature** changes what evidence is **cheap vs impossible**—benchmark without stats can **mis-rank** production fitness ([[measurement-validity]], [[scientific-method]]).

## Application validation

- **Picking jemalloc vs tcmalloc for a service**: weight **production allocation stats + fragmentation** alongside **microbench QPS**, or you optimize the wrong objective.

## Decision clarity

- **Decision**: choose **allocators with operational introspection** over **opaque winners on synthetic malloc loops** when **incident time** must answer **which call sites grow**.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[scientific-method]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[scientific-method]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-kernel-slab-and-magazines-7-3-3d]]
