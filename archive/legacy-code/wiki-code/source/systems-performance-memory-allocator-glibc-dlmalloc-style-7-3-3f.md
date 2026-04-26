# Systems Performance — glibc / dlmalloc-style multi-policy user heap (7.3.3) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.3** — **glibc** allocator sketch: **bins**, **mmap for large**, mixed policies (book-level, not a how-to)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-allocator-glibc-dlmalloc-style-7-3-3f.md`
- Chunks:
  - `processed/code/systems-performance-memory-allocator-glibc-dlmalloc-style-7-3-3f-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Size-class branching** means **different code paths and OS interactions** by allocation size—**p99** can be dominated by **rare huge allocations** even if **median** is tiny ([[resource-vs-implementation-bottleneck]], [[throughput-latency-metrics]]).
- (measurement) **Attributing RSS to “malloc”** without **large-allocation vs small-bin** split is a **representation** error ([[measurement-validity]]).

## Application validation

- **Latency spikes when moving from KB to MB allocations**: suspect **mmap path + VMA management**, not **CPU cache misses**—validate with **allocation-size histogram**.

## Decision clarity

- **Decision**: choose **size-aware allocation strategy (pools / arenas for large objects)** over **uniform malloc** when **tail alloc latency** tracks **infrequent multi-page** requests.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-allocator-design-tradeoffs-7-3-3c]]
  - [[systems-performance-memory-allocator-tcmalloc-thread-cache-7-3-3g]]
