# Systems Performance — On-chip cache levels (Ch.7 pointer to Ch.6) (7.3.1) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.1** — **L1/L2/L3** recap; **virtual vs physical** indexing note; pointer back to **Chapter 6** for depth; introduces **TLB** as additional hardware cache in this chapter

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-architecture-cpu-caches-ch7-7-3-1d.md`
- Chunks:
  - `processed/code/systems-performance-memory-architecture-cpu-caches-ch7-7-3-1d-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) **Hierarchy depth** is the decision lever: **miss cost** escalates by **tier**, so “memory tuning” without **cache tier awareness** misallocates effort ([[caching]], [[resource-vs-implementation-bottleneck]]).
- (abstraction) **L1 virtual vs L2+ physical** indexing changes **where translation and coherency costs** appear in profiles—**Ch.6** remains canonical for drill-down ([[virtual-memory-abstraction]] as bridge).

## Application validation

- **Ch.7 memory chapter investigation**: when stacks show **cache-heavy** behavior, **borrow Ch.6 PMC / stall framing** instead of inventing parallel “memory-only” theories.

## Decision clarity

- **Decision**: choose **Ch.6 cache + stall evidence** over **DRAM sizing alone** when **hot working set** clearly fits **on-chip tiers** but **p99** still tracks **miss storms**.

## Concepts reused / refined / created

- Reused (mechanism): [[caching]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[caching]]
  - [[resource-vs-implementation-bottleneck]]
  - [[virtual-memory-abstraction]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-on-chip-cache-hierarchy-and-llc-6-4-1]]
  - [[systems-performance-memory-architecture-mmu-tlb-7-3-1e]]
