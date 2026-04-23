# Systems Performance — DDR standards narrative and multichannel bandwidth (7.3.1) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.1** — **DDR SDRAM** mechanism narrative; **Table 7.1** vendor grid **omitted** from processed extract; **multichannel** bandwidth stacking

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-architecture-ddr-multichannel-7-3-1c.md`
- Chunks:
  - `processed/code/systems-performance-memory-architecture-ddr-multichannel-7-3-1c-chunk-000001.md`

## Extracted ideas (with classification)

- (tradeoff) **Peak MB/s from a standard name** is a **SKU ceiling**, not **achieved bandwidth under contention**—capacity planning needs **sustained + parallel channel use** ([[memory-technology-tradeoff]], [[throughput-latency-metrics]]).
- (structure) **Multichannel** is a **parallelism-of-wires** decision: more **bandwidth headroom** for the same **DRAM technology generation** ([[cross-component-interactions]]).
- (measurement) **Marketing “PC-####”** vs **what your DIMM layout actually runs** is a **representation** gap—validate with **independent bandwidth probes** under your **channel population** ([[measurement-validity]]).

## Application validation

- **Streaming kernel still “memory bound” after DDR5 upgrade**: confirm **channels populated** and **interleave** match the SKU assumption behind the **expected peak**.

## Decision clarity

- **Decision**: choose **DIMM population / channel symmetry upgrades** over **faster per-DIMM grade alone** when **measured bandwidth** plateaus below **datasheet peak** due to **single-channel** operation.

## Concepts reused / refined / created

- Reused (tradeoff): [[memory-technology-tradeoff]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[cross-component-interactions]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[memory-technology-tradeoff]]
  - [[throughput-latency-metrics]]
  - [[cross-component-interactions]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-architecture-uma-numa-buses-7-3-1b]]
