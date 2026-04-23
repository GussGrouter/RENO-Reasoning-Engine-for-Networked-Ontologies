# Systems Performance — Ch.9 §9.3.12–§9.3.13 (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **sync vs async** disk vs app; **why disk rate ≠ app rate**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-concepts-async-mismatch-9-3-12-13.md`
- Chunks: `systems-performance-disks-ch9-concepts-async-mismatch-9-3-12-13-chunk-000001.md`

## Extracted ideas

- **Write-back**, **prefetch**, **worker threads** decouple **app completion** from **media completion** (**[[throughput-latency-metrics]]**, [[caching]]).
- **Mismatch list** ties disk metrics back to **FS inflation**, **paging**, **RAID**, **drivers**—classic [[cross-component-interactions]] + [[measurement-validity]] framing.

## Application validation

High **disk throughput** but calm **app threads:** validate whether work is **async / buffered** before chasing **device upgrades**.

## Decision clarity

**Decision:** choose **end-to-end request latency tracing** over **disk-only dashboards** when **symptoms are user-visible stalls** but **disk util looks healthy**.

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[caching]], [[cross-component-interactions]], [[measurement-validity]], [[latency-analysis]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[caching]], [[cross-component-interactions]], [[measurement-validity]], [[latency-analysis]], [[systems-performance]]
