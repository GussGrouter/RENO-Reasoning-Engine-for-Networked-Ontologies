# Systems Performance — Ch.9 §9.3.1 Measuring time (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.3.1** — kernel vs disk time vocabulary; **`iostat` caveat**; tracing

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-concepts-measuring-time-9-3-1.md`
- Chunks: `systems-performance-disks-ch9-concepts-measuring-time-9-3-1-chunk-000001.md`

## Extracted ideas

- **Named intervals** prevent mixing **queue wait**, **transport**, **device service**, **on-disk queue** (**measurement-validity**: **scope/semantics**).
- **Utilization/IOPS-derived service time** assumes **single-server flavor** behavior—breaks under **parallelism / deep queues**; **tracing** timestamps ground truth.

## Application validation

When **`iostat`** “svctm” style thinking disagrees with **BPF/trace** histograms, trust **timestamp pairs** after validating **probe placement**.

## Decision clarity

**Decision:** choose **event/trace latency from defined issue→completion probes** over **derived averages from counter ratios** when **responses are multimodal or highly parallel**.

## Concepts reused / refined / created

- Reused: [[latency-analysis]], [[measurement-validity]], [[throughput-latency-metrics]], [[event-tracing]], [[counters-statistics-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[latency-analysis]], [[measurement-validity]], [[throughput-latency-metrics]], [[event-tracing]], [[counters-statistics-metrics]], [[systems-performance]]
