# Systems Performance — random change anti-method (2.5.2) (PDF pages 78–84)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.5.2 Random Change Anti-Method

## Processed artifacts

- Converted slice: `processed/code/systems-performance-random-change-anti-method-2-5-2.md`
- Chunks:
  - `processed/code/systems-performance-random-change-anti-method-2-5-2-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Randomly change something (e.g., a tunable), measure a chosen performance metric, and keep changes that look better than baseline; repeat.
- (measurement) Improvement is judged via runtime/latency/throughput/operation rate metrics, but the method itself does not establish causality.
- (diagnosis) Risks: time-consuming; leaves behind changes that are not understood; changes may become obsolete later; may cause worse problems at peak load.

## Concepts reused / refined / created

- Created (heuristic): [[random-change-anti-method]]
- Reused (measurement): [[throughput-latency-metrics]] (typical evaluation metrics).
- Reused (diagnosis): [[cross-component-interactions]] (changing multiple factors obscures which mattered).
- Reused (diagnosis): [[resource-vs-implementation-bottleneck]] (tuning without understanding the bottleneck type).

## Links

- Concepts:
  - [[random-change-anti-method]]
  - [[throughput-latency-metrics]]
  - [[cross-component-interactions]]
  - [[resource-vs-implementation-bottleneck]]

