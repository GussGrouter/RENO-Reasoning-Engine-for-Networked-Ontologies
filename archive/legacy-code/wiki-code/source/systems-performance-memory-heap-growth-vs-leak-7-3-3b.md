# Systems Performance — Heap growth vs leak, returning pages to OS (7.3.3) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.3** — **allocator-retained RSS** after `free`, **mmap/munmap**, **malloc_trim** class behaviors

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-heap-growth-vs-leak-7-3-3b.md`
- Chunks:
  - `processed/code/systems-performance-memory-heap-growth-vs-leak-7-3-3b-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Monotonic RSS after frees** is often **allocator policy**, not proof of **leak**—the decision needs **allocation-age / heap delta** semantics ([[measurement-validity]], [[utilization-and-saturation]]).
- (abstraction) **Returning pages to the OS** is a **different API path** (`mmap`/`munmap`, trim) than **heap freelists**—capacity planning must not conflate them ([[virtual-memory-abstraction]], [[demand-paging]]).

## Application validation

- **Alert on RSS slope after traffic returned to baseline**: compare **jemalloc stats / heap profile** before weeks-long **leak hunt**—you may be seeing **retained arena**, not **lost objects**.

## Decision clarity

- **Decision**: choose **allocator-aware instrumentation + epoch comparison** over **raw RSS derivative alone** when classifying **leak vs retention** after load drops.

## Concepts reused / refined / created

- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (mechanism): [[demand-paging]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[measurement-validity]]
  - [[utilization-and-saturation]]
  - [[virtual-memory-abstraction]]
  - [[demand-paging]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-process-address-space-segments-7-3-3a]]
  - [[systems-performance-memory-allocator-design-tradeoffs-7-3-3c]]
