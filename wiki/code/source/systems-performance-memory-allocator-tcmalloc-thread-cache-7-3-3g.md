# Systems Performance — Thread-cached malloc pattern (TCMalloc, book) (7.3.3) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.3** — **per-thread cache** + **central heap GC** pattern (textbook summary)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-allocator-tcmalloc-thread-cache-7-3-3g.md`
- Chunks:
  - `processed/code/systems-performance-memory-allocator-tcmalloc-thread-cache-7-3-3g-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Thread-local freelists** buy **contention reduction** at the cost of **RSS scatter** and **rebalance latency** when threads die or go idle ([[resource-vs-implementation-bottleneck]], [[throughput-latency-metrics]]).
- (measurement) **Microbench “malloc is fast”** often uses **steady threads**; production **churn** triggers **central heap / GC phases** absent from the benchmark ([[measurement-validity]], [[scientific-method]]).

## Application validation

- **High core count + allocator-bound**: if **lock profiles** disappear after **TCMalloc-class** switch but **RSS grows**, you traded **mutex** for **cached bytes**—check **fleet memory headroom**.

## Decision clarity

- **Decision**: choose **thread-caching allocators** over **single-heap locks** when **mutex contention** dominates **alloc CPU**, accepting **possible RSS inflation** under **thread churn**.

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
  - [[systems-performance-memory-allocator-glibc-dlmalloc-style-7-3-3f]]
  - [[systems-performance-memory-allocator-jemalloc-arenas-7-3-3h]]
