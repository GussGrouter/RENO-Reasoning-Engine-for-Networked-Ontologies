# Systems Performance — Characterizing usage: problem statement (7.4.3 opening) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.4.3** — define **who allocates**, **allocation rate**, **lifetime**, **caller paths**, **growth vs steady-state**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-methodology-characterizing-usage-7-4-3a.md`
- Chunks:
  - `processed/code/systems-performance-memory-methodology-characterizing-usage-7-4-3a-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Characterization spans workload + implementation**: **RSS vs heap vs anon vs page cache** split catches **mis-cache-config** masquerading as “memory leak” ([[resource-analysis-vs-workload-analysis]], [[throughput-latency-metrics]], [[caching]]).

## Application validation

- **RSS climbs but heap stable**: investigate **mmap/file-backed + cache sizing** before rewriting allocators.

## Decision clarity

- **Decision**: choose **usage attribution by memory class (anon vs file vs cache)** over **single RSS trend** when **swap pressure tracks cache growth**, not heap.

## Concepts reused / refined / created

- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (mechanism): [[caching]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-analysis-vs-workload-analysis]]
  - [[throughput-latency-metrics]]
  - [[caching]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-methodology-usage-checklist-7-4-3b]]
