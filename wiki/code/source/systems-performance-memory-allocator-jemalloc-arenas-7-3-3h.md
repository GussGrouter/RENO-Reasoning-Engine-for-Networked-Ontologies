# Systems Performance — Arenas + slabs user allocator pattern (jemalloc, book) (7.3.3) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.3** — **arenas**, **per-thread caching**, **mmap preference** (textbook summary; cites vendor usage as context)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-allocator-jemalloc-arenas-7-3-3h.md`
- Chunks:
  - `processed/code/systems-performance-memory-allocator-jemalloc-arenas-7-3-3h-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Multiple arenas** partition **heap metadata contention**—the decision is **how many arenas** vs **cross-arena fragmentation** under your **thread topology** ([[resource-vs-implementation-bottleneck]], [[cross-component-interactions]]).
- (measurement) **Preferring mmap** changes **RSS vs VMA** semantics and **reclaim** behavior—compare **host-level** and **cgroup-level** views ([[measurement-validity]], [[utilization-and-saturation]]).

## Application validation

- **Container limit is VMA count not bytes**: **jemalloc mmap-heavy** configs can **fail** before **DRAM** saturates—watch **max_map_count**-class limits, not only **MiB RSS**.

## Decision clarity

- **Decision**: choose **arena-heavy / mmap-biased allocators** over **sbrk-only heaps** when **heap lock contention** is proven, after checking **VMA and cgroup accounting** headroom.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (structure): [[cross-component-interactions]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[utilization-and-saturation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[cross-component-interactions]]
  - [[measurement-validity]]
  - [[utilization-and-saturation]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-allocator-tcmalloc-thread-cache-7-3-3g]]
