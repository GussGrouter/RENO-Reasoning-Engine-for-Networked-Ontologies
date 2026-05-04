# Systems Performance — Word size, addressable range, and kernel reservations (7.2.11) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.2.11** — **32 vs 64-bit** address spaces, **>4G process** requirement, **kernel VA reservations**, **PAE** footnote (not per-process expansion)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-concepts-word-size-7-2-11.md`
- Chunks:
  - `processed/code/systems-performance-memory-concepts-word-size-7-2-11-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Addressable range** caps **single-process footprint** independent of **installed DRAM**—large in-memory workloads are a **build/target architecture** decision, not only **hardware** ([[virtual-memory-abstraction]], [[process-abstraction]]).
- (measurement) **Kernel reservation splits user VA**—“2G usable on 32-bit Windows” is a **semantics** fact for **capacity planning**, not visible in naive “64-bit app” assumptions ([[measurement-validity]], [[throughput-latency-metrics]]).

## Application validation

- **Legacy 32-bit service near “2G heap”**: treat as **hard architecture ceiling**—fix is **64-bit build or process sharding**, not **tuning swappiness**.

## Decision clarity

- **Decision**: choose **64-bit (or multi-process shard)** over **PAE / bigger machine** when a **single address space** must exceed **safe user VA** under your OS’s **kernel reservation rules**.

## Concepts reused / refined / created

- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (abstraction): [[process-abstraction]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[virtual-memory-abstraction]]
  - [[process-abstraction]]
  - [[measurement-validity]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-parallelism-footprint-and-word-size-6-3-14]]
  - [[systems-performance-memory-concepts-working-set-size-7-2-10]]
