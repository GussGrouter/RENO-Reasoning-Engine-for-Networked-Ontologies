# Systems Performance — MMU, page sizes, TLB reach (7.3.1) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.1** — **MMU** translation model; **huge pages**; **TLB** as translation cache; **Table 7.2** vendor grid **omitted** from processed extract

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-architecture-mmu-tlb-7-3-1e.md`
- Chunks:
  - `processed/code/systems-performance-memory-architecture-mmu-tlb-7-3-1e-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Larger pages increase TLB reach**—a **capacity knob** for **translation**, not a free win: it trades **internal fragmentation / pinning** for fewer **TLB miss walks** ([[virtual-memory-abstraction]], [[throughput-latency-metrics]]).
- (measurement) **“TLB miss rate” claims** without **page-size mix + SKU table** are **representation-incomplete**—vendor tables differ by **generation** ([[measurement-validity]], [[caching]] as translation-cache analogy).

## Application validation

- **Huge-page experiment for DB**: if CPU drops but **RSS fragmentation** rises, you traded **translation misses** for **allocator / compaction** work—re-evaluate **page size policy** per workload.

## Decision clarity

- **Decision**: choose **huge pages + pinned mappings** over **4K-only defaults** when **profiles show translation walk + fault storm** dominating **DRAM bandwidth** on a **wide mapped heap**.

## Concepts reused / refined / created

- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (mechanism): [[caching]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[virtual-memory-abstraction]]
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[caching]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-architecture-cpu-caches-ch7-7-3-1d]]
