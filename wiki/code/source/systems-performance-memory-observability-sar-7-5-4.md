# Systems Performance — sar memory statistics (§7.5.4) (PDF scout 320–380)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.5.4** — **sar** memory/paging/huge/swap options; **reclaim-efficiency** and **direct-reclaim** rate signals (book names fields; treat as **interpretation patterns**)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-observability-sar-7-5-4.md`
- Chunks: `processed/code/systems-performance-memory-observability-sar-7-5-4-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Statistic names embed units** (`pg`, `kb`, `%`, `/s`)—misreading **population** (global vs per-device) breaks trends ([[counters-statistics-metrics]], [[measurement-validity]]).
- (heuristic) **%vmeff / pgscand-style signals** separate **healthy reclaim** from ** allocator path blocking**; **high pgscand** points to **follow-up tracing** (not micro-optimizing app code first) ([[resource-vs-implementation-bottleneck]], [[drill-down-analysis]]).
- (method) **Historical sar** answers “when did pressure start?” for incidents that **current-only tools** miss ([[time-series-monitoring]]).

## Application validation

- **Intermittent stalls:** pull **sar paging + vmscan / pgscand** around the incident window; if **pgscand rises** before latency, schedule **direct-reclaim tracing** instead of **SQL query tuning first**.

## Decision clarity

- **Decision:** choose **archived sar (or equivalent metrics store) for timeline correlation** over **live vmstat alone** when **customer impact is rare** and you need **start time + trend shape**, not a point sample.

## Concepts reused / refined / created

- Reused (measurement): [[counters-statistics-metrics]], [[measurement-validity]]
- Reused (heuristic): [[resource-vs-implementation-bottleneck]], [[drill-down-analysis]]
- Reused (structure): [[time-series-monitoring]]
- Reused: [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[counters-statistics-metrics]], [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[drill-down-analysis]], [[time-series-monitoring]], [[systems-performance]]
- Related sources: [[systems-performance-memory-observability-psi-swapon-7-5-2-3]], [[systems-performance-memory-observability-slab-numa-7-5-5-6]]
