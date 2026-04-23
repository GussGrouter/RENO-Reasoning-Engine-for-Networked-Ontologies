# Systems Performance — garbage collection: footprint, CPU, and tail latency (5.3.4) (PDF ~182–230)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.3.4 Garbage Collection

## Processed artifacts

- Converted slice: `processed/code/systems-performance-garbage-collection-performance-5-3-4.md`
- Chunks:
  - `processed/code/systems-performance-garbage-collection-performance-5-3-4-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Heap growth** without reclamation drives paging and hard limits—GC is not only CPU, it is **capacity** ([[throughput-latency-metrics]] + memory pressure).
- (measurement) **GC CPU ramps with live set / allocation rate**—can monopolize a core; tuning knobs shift **who pays** (mutator vs collector) rather than deleting work.
- (measurement) **Pause-type collectors** create tail latency spikes—classification (stop-the-world vs incremental vs concurrent) predicts which SLO story breaks first ([[latency-percentiles]]).

## Application validation

- **Tail SLO services**: if p99 spikes correlate with GC logs, first quantify **allocation churn** per request before sweeping JVM flag matrices—often the fix is fewer short-lived objects, not a different collector.

## Concepts reused / refined / created

- Reused (measurement): [[throughput-latency-metrics]]
- Reused (measurement): [[latency-percentiles]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (diagnosis): [[latency-analysis]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[latency-percentiles]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[latency-analysis]]
  - [[systems-performance]]
