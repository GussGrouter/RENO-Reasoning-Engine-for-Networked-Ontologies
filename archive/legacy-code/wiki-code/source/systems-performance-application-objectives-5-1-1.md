# Systems Performance — application performance objectives (5.1.1) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.1.1 Objectives (latency/throughput/utilization/price goals + quantified examples + Apdex note)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-application-objectives-5-1-1.md`
- Chunks:
  - `processed/code/systems-performance-application-objectives-5-1-1-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Goal-first analysis**: without explicit objectives, work becomes a fishing expedition—same failure mode as skipping [[problem-statement-method]] in incidents.
- (measurement) Goals should be **quantified** from business/QoS needs (averages, tail bounds, outlier elimination, throughput per **bounding resource** such as CPU when host size varies).
- (measurement) Throughput targets need **operation mix**: equal “requests/sec” can hide unequal cost drivers—distribution belongs in the workload spec, not only the headline number.
- (diagnosis) Technique choices (later sections) are **goal-dependent**; the same mechanism can help throughput and hurt latency—tie back to [[throughput-latency-metrics]] trade space.
- (measurement) Composite satisfaction indices (example narrative: Apdex-style buckets) are one way to fold tail pain into a single monitored scalar—still anchored on explicit latency thresholds.

## Concepts reused / refined / created

- Reused (heuristic): [[problem-statement-method]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (measurement): [[latency-percentiles]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[problem-statement-method]]
  - [[throughput-latency-metrics]]
  - [[latency-percentiles]]
  - [[resource-vs-implementation-bottleneck]]
  - [[systems-performance]]
