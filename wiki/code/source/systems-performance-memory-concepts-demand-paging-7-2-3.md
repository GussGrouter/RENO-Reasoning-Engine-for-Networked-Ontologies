# Systems Performance — Demand paging, fault classes, RSS vs VSZ (7.2.3) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.2.3** — **demand mapping**, **minor vs major faults**, **virtual memory states (A–D)**, **RSS vs virtual size**

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-concepts-demand-paging-7-2-3.md`
- Chunks:
  - `processed/code/systems-performance-memory-concepts-demand-paging-7-2-3-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) **Demand paging** shifts cost to **first access**—profiling “allocation sites” without **fault attribution** can miss where **DRAM/time** actually went ([[demand-paging]], [[sampling-based-profiling]]).
- (measurement) **Minor vs major faults** is a **representation + semantics** split: same word “fault,” different **I/O and latency implications**—dashboards that sum them blur decisions ([[measurement-validity]]).
- (abstraction) **RSS vs VSZ** operationalizes **resident vs committed footprint**—capacity and noisy-neighbor questions should default to **RSS-shaped views** for **DRAM**, not **VSZ** alone ([[virtual-memory-abstraction]], [[time-space-tradeoff]]).

## Application validation

- **malloc-heavy service**: if CPU is in **kernel page fault paths**, treat **major fault rate** as a **first-class SLO input**, not only **user-space profile hot spots**.

## Decision clarity

- **Decision**: choose **major-fault / swap-in witnesses + RSS derivative** over **aggregate CPU%** when deciding whether **memory subsystem** (not **user code**) owns **p99 latency**.

## Concepts reused / refined / created

- Reused (mechanism): [[demand-paging]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (abstraction): [[time-space-tradeoff]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[demand-paging]]
  - [[sampling-based-profiling]]
  - [[measurement-validity]]
  - [[virtual-memory-abstraction]]
  - [[time-space-tradeoff]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-concepts-paging-7-2-2]]
