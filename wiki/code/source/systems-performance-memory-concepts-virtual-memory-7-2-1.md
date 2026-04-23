# Systems Performance — Virtual memory as oversubscription mechanism (7.2.1) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.2.1** — **virtual memory goals** (private linear spaces, **oversubscription**), **swap-backed mapping**, and **virtual limit** vs **overcommit** teaser

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-concepts-virtual-memory-7-2-1.md`
- Chunks:
  - `processed/code/systems-performance-memory-concepts-virtual-memory-7-2-1-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Oversubscription** is a deliberate **time–space split**: more **committed virtual** than **DRAM+swap** can hold, relying on **sparse use** and **reclaim**—performance depends on how often reality contradicts that bet ([[virtual-memory-abstraction]], [[throughput-latency-metrics]]).
- (measurement) **“Out of virtual memory” vs “OOM killer”** are different failure semantics—both are **validity** traps if you conflate them with “leak” without checking **limits and policies** ([[measurement-validity]]).
- (mechanism) **Demand mapping** is the enabling mechanism for **deferred costs**—latency shows up at **first touch** and under **pressure**, not at `malloc` return ([[demand-paging]]).

## Application validation

- **malloc succeeds, later jobs die**: classify whether you hit **commit accounting**, **reclaim thrash**, or **true leak** by pairing **fault rates + reclaim + RSS slope**, not peak **VSZ** alone.

## Decision clarity

- **Decision**: choose **pressure-aware capacity limits (RSS + reclaim + swap)** over **virtual bytes ceilings** when protecting **SLO latency**, because **virtual success** can still produce **fault storms**.

## Concepts reused / refined / created

- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (mechanism): [[demand-paging]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[virtual-memory-abstraction]]
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[demand-paging]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-terminology-7-1]]
  - [[systems-performance-memory-concepts-paging-7-2-2]]
