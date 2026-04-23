# Systems Performance — observability foundations (1.7) (PDF pages 46–54)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: PDF pages 46–54 (Chapter 1, Section 1.7 Observability + 1.7.1 counters/statistics/metrics; profiling/tracing overview)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-observability-1-7-p46-54.md`
- Chunks:
  - `processed/code/systems-performance-observability-1-7-chunk-000001.md`
  - `processed/code/systems-performance-observability-1-7-chunk-000002.md`
  - `processed/code/systems-performance-observability-1-7-chunk-000003.md`

## Extracted ideas (with classification)

- (diagnosis) Complex performance issues may have multiple causes and interacting resources; resolving one bottleneck can shift the bottleneck elsewhere, so diagnosis must consider whole-system interactions.
- (measurement) Latency is a central metric for quantifying impact; when latency can be decomposed into contributing waits, it supports estimating potential speedup (upper bound).
- (measurement) Latency requires qualifiers (what interval/operation is being timed) to avoid ambiguous interpretations across domains.
- (measurement) Observability tools (counters, profiling, tracing) are distinct from experimental/benchmark tools; in production, prefer observability first because experiments can perturb workloads.
- (measurement) Counter → statistic → metric hierarchy: counters record state/activity; statistics are computed from counters over time; metrics are selected statistics used for monitoring and alerting; industry usage is not rigid.
- (measurement) Metrics can resolve some issues (correlating start time with changes) but often only point to a direction; profiling/tracing provide deeper causal detail when metrics are insufficient.
- (measurement) Profiling is sampling-based measurement to form a coarse picture; tracing is event-based recording consumed live or analyzed later.
- (measurement) Static vs dynamic instrumentation differs in how observation points are provided (hard-coded vs inserted at runtime), affecting what can be measured and how flexible the measurement is.

## Concepts reused / refined / created

- Reused (measurement): [[throughput-latency-metrics]] (this section adds structure on why latency is actionable and how ambiguity arises).
- Created (measurement): [[counters-statistics-metrics]]

## Links

- Concepts:
  - [[counters-statistics-metrics]]
  - [[throughput-latency-metrics]]

