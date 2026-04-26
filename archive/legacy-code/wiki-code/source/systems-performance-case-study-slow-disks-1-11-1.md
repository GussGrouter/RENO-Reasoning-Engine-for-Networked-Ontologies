# Systems Performance — case study: slow disks (1.11.1) (PDF pages 55–60)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 1, Section 1.11.1 (case study)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-case-study-slow-disks-1-11-1.md`
- Chunks:
  - `processed/code/systems-performance-case-study-slow-disks-1-11-1-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Start with a problem statement: confirm there is a real issue and how it is measured; treat initial “slow X” hypotheses as provisional.
- (measurement) Monitoring at coarse intervals can hide saturation spikes; higher-resolution measurements can reveal transient 100% utilization and latency increases.
- (diagnosis) A broad first-pass resource check (USE method) helps test hypotheses and avoid tunnel vision on one suspected resource.
- (diagnosis) Workload characterization can distinguish “device malfunction” from “high load” explanations by measuring rates/latencies and ratios.
- (diagnosis) Drill-down analysis is time-consuming; prefer quick checks for plausible causes before deep tracing.
- (measurement) Tracing and off-CPU evidence can connect a symptom (slow queries) to a blocking path (e.g., time waiting for reads) without relying on guesswork.

## Concepts reused / refined / created

- Reused (diagnosis): [[resource-vs-implementation-bottleneck]] (case study emphasizes testing whether disks are “slow” vs just under high load).
- Reused (measurement): [[counters-statistics-metrics]] (monitoring metrics/intervals and derived rates are central).
- Reused (measurement): [[throughput-latency-metrics]] (query latency and disk I/O latency as impact metrics).

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[counters-statistics-metrics]]
  - [[throughput-latency-metrics]]

