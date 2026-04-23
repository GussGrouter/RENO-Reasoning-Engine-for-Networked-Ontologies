# Systems Performance — User vs kernel allocators and fragmentation (7.2.8) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.2.8** — **allocator role** in virtual address spaces; **per-thread caching** upside vs **fragmentation** downside; points forward to **§7.3** detail

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-concepts-allocators-7-2-8.md`
- Chunks:
  - `processed/code/systems-performance-memory-concepts-allocators-7-2-8-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Allocator choice** is often an **implementation bottleneck** masquerading as “need more RAM”: fragmentation and hot-path locks inflate **CPU + metadata** cost without raising **RSS** much ([[resource-vs-implementation-bottleneck]], [[throughput-latency-metrics]]).
- (abstraction) **Measurement validity**: comparing two allocators on **peak throughput** alone misses **tail fragmentation** and **multi-thread layout** effects—define **workload shape + duration** first ([[measurement-validity]], [[process-abstraction]]).

## Application validation

- **CPU regression after dependency bump** (no RSS change): profile for **allocator hot paths / mmap churn** before assuming **GC or application logic** changed.

## Decision clarity

- **Decision**: choose **allocator A/B under realistic fragmentation + concurrency** over **micro-benchmark malloc/free loops** when the production pain is **tail latency under long-lived heaps**.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[process-abstraction]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[process-abstraction]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-concepts-demand-paging-7-2-3]]
