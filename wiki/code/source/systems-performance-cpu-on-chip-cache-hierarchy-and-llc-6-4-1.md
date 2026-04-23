# Systems Performance — On-chip cache ladder and “last-level cache” naming (6.4.1) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.4.1 — **CPU Caches** through **LLC** definition (stops before vendor-specific historical Table 6.3)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-on-chip-cache-hierarchy-and-llc-6-4-1.md`
- Chunks:
  - `processed/code/systems-performance-cpu-on-chip-cache-hierarchy-and-llc-6-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) **Multi-level caches** are the default **latency ladder** between cores and DRAM—performance work routes “memory slow” through **which level misses** and **which sharing pattern** applies ([[caching]], [[throughput-latency-metrics]]).
- (abstraction) **LLC (last-level / longest-latency cache)** names the **last fast tier before DRAM**, which may or may not be “L3” on a given SKU—treat **level numbers** as **vendor shorthand**, not a universal topology law ([[measurement-validity]], [[caching]]).
- (structure) **Historical growth of cache sizes** is evidence for **pressure moving up the memory hierarchy** over product generations—useful for capacity planning, not as a memorization table ([[universal-scalability-law]], [[resource-vs-implementation-bottleneck]]).

## Application validation

- **Large in-memory index**: if DRAM bandwidth is flat but **LLC MPKI** drops after a topology change, suspect **socket migration** or **shared LLC interference**, not “more GB RAM.”

## Decision clarity

- **Decision**: choose **LLC-aware placement / object layout work** over **raw RAM upgrades** when misses concentrate at the **last on-chip tier** and DRAM bandwidth is not the limiter.

## Concepts reused / refined / created

- Reused (mechanism): [[caching]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[universal-scalability-law]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[caching]]
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[universal-scalability-law]]
  - [[resource-vs-implementation-bottleneck]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-p-states-and-c-states-6-4-1]]
  - [[systems-performance-cpu-models-architecture-and-caches-6-2-1-2]]
  - [[systems-performance-cpu-cache-coherency-latency-mmu-tlb-6-4-1]]
