# Systems Performance — Memory resource controls (§7.6.5) (PDF scout 381–400)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.6.5** — **ulimit**, cgroup **memory / memsw / kmem / tcp**, **per-cgroup swappiness**, **OOM control**; pointer to cloud chapter

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p381-400.txt`
- Converted slice: `processed/code/systems-performance-memory-tuning-cgroup-limits-7-6-5.md`
- Chunks: `processed/code/systems-performance-memory-tuning-cgroup-limits-7-6-5-chunk-000001.md`

## Extracted ideas (with classification)

- (scope) **`memory.limit_in_bytes` includes file cache charged to the cgroup**—capacity math differs from **RSS-only** process views ([[measurement-validity]]).
- (structure) **memsw limit couples RAM+swap**: changing swap availability **changes failure mode** (reclaim vs OOM) ([[cross-component-interactions]], [[measurement-validity]]).

## Application validation

- **Container killed “for memory” but RSS looks fine:** reconcile **cache charged to cgroup**, ** kmem**, and **tcp** buckets before raising **Java heap**.

## Decision clarity

- **Decision:** choose **cgroup-aware memory pressure signals (PSI + memory.stat breakdown)** over **process RSS dashboards** when **limits include page cache / kernel charges** that RSS-centric tools hide.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[cross-component-interactions]], [[systems-performance]]
- Related sources: [[systems-performance-memory-ch7-exercises-scaffold-7-7]]
