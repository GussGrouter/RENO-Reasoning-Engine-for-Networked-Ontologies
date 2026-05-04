# Systems Performance — vmstat for memory (§7.5.1) (PDF scout 320–380)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.5.1** — **vmstat** high-level memory/paging columns (examples retained as **shape**, not endorsement of one layout)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-observability-vmstat-7-5-1.md`
- Chunks: `processed/code/systems-performance-memory-observability-vmstat-7-5-1-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Column semantics dominate interpretation**: **free vs buff/cache**, **si/so** paging, **stolen CPU / wait** columns carry different **scopes** across OS versions—**validate** before comparing hosts ([[measurement-validity]], [[counters-statistics-metrics]]).
- (heuristic) **vmstat is breadth-first triage**, not attribution: pair with **PSI / top / pmap** before allocator traces ([[drill-down-analysis]], [[utilization-and-saturation]]).

## Application validation

- **Dashboard shows high “free” but swap-in churn:** reconcile whether **cache** is folded into “used” on that column layout and whether **si/so** spikes align with **latency** windows—otherwise you tune **cache tuning**, not **heap leaks**.

## Decision clarity

- **Decision:** choose **vmstat + swap/paging columns for “is the VM subsystem moving pages?”** over **heap profilers** when **symptoms are systemic reclaim/swap**, not **single-process RSS creep**.

## Concepts reused / refined / created

- Reused (measurement): [[measurement-validity]], [[counters-statistics-metrics]]
- Reused (heuristic): [[drill-down-analysis]], [[utilization-and-saturation]]
- Reused: [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[counters-statistics-metrics]], [[drill-down-analysis]], [[utilization-and-saturation]], [[systems-performance]]
- Related sources: [[systems-performance-memory-observability-psi-swapon-7-5-2-3]]
