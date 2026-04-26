# Systems Performance — Characterizing usage: advanced checklist (7.4.3 continued) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.4.3** — concrete **measurement checklist** + **micro-benchmarking traps** + **allocator policy** sanity (book names tools; retained as checklist **categories**)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-methodology-usage-checklist-7-4-3b.md`
- Chunks:
  - `processed/code/systems-performance-memory-methodology-usage-checklist-7-4-3b-chunk-000001.md`

## Extracted ideas (with classification)

- (heuristic) **Checklist is adversarial**: ask **not only who allocates** but **whether counters measure resident vs virtual vs allocator heap** ([[measurement-validity]], [[resource-analysis-vs-workload-analysis]]).
- (measurement) **Benchmarking allocator choice** requires **representative fragmentation + thread count**—**toy micro-benches** invert rankings ([[micro-benchmarking]]).

## Application validation

- **Perf shows malloc dominates**: verify **whether RSS growth tracks mallocs** or **metadata/page-table inflation** before swapping allocators.

## Decision clarity

- **Decision**: choose **allocator experiments on production-shaped fragmentation + concurrency** over **single-thread synthetic malloc/free loops** when **decisions target tail latency under parallel load**.

## Concepts reused / refined / created

- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (measurement): [[micro-benchmarking]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[measurement-validity]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[micro-benchmarking]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-methodology-characterizing-usage-7-4-3a]]
