# Systems Performance — CPUs chapter intro and structure (Chapter 6) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6 CPUs (chapter purpose, depth ladder from utilization → cycles, six-part roadmap)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpus-chapter-intro-and-parts-6.md`
- Chunks:
  - `processed/code/systems-performance-cpus-chapter-intro-and-parts-6-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) CPU work is diagnosed at **stacked depths** (system/thread → code path → cycles), so tool choice follows **which layer currently owns uncertainty** ([[drill-down-analysis]], [[observability-vs-experimentation]]).
- (diagnosis) **Scheduler latency** is named as a first-class CPU degradation mode alongside utilization shape—capacity is not only “GHz busy” ([[utilization-and-saturation]], [[context-switching]]).
- (abstraction) **Memory-side stalls** on CPUs are explicitly deferred to Chapter 7—CPU chapter decisions should not pretend DRAM/NUMA is absent when IPC or utilization looks odd ([[throughput-latency-metrics]], [[caching]]).

## Application validation

- **SLO triage template**: if user-visible latency is bad but “CPU% is fine,” still walk the chapter ladder through **scheduler wait** and **instruction/memory efficiency** before closing the CPU chapter.

## Concepts reused / refined / created

- Reused (heuristic): [[drill-down-analysis]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (mechanism): [[context-switching]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (mechanism): [[caching]]
- Reused (abstraction): [[universal-scalability-law]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[drill-down-analysis]]
  - [[observability-vs-experimentation]]
  - [[utilization-and-saturation]]
  - [[context-switching]]
  - [[throughput-latency-metrics]]
  - [[caching]]
  - [[universal-scalability-law]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-chapter-5-exercises-under-load-lab-b-5-7]]
  - [[systems-performance-cpu-terminology-6-1]]
