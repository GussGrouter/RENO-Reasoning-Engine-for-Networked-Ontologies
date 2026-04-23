# Systems Performance — queueing theory (2.6.5) (PDF pages 98–114)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.6.5 Queueing Theory

## Processed artifacts

- Converted slice: `processed/code/systems-performance-queueing-theory-2-6-5.md`
- Chunks:
  - `processed/code/systems-performance-queueing-theory-2-6-5-chunk-000001.md`

## Extracted ideas (with classification)

- (framework) Queueing theory studies queued systems to analyze queue length, wait time (latency), and utilization; multiple queues form queueing networks.
- (framework) Little’s law: \(L = \\lambda W\) relates average jobs in system \(L\), arrival rate \(\\lambda\), and average time in system \(W\).
- (diagnosis) Queueing models answer “what happens if load doubles?” / “what if we add a processor?” and can reason about percentile response-time targets.
- (abstraction) Queueing systems are categorized by arrival process, service time distribution, and number of service centers (Kendall notation \(A/S/m\)).
- (diagnosis) Simple models (e.g., M/D/1) show response time rising rapidly beyond moderate utilization; disk I/O can become problematic well before 100% utilization.

## Concepts reused / refined / created

- Created (framework): [[queueing-theory]]
- Reused (diagnosis): [[utilization-and-saturation]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[queueing-theory]]
  - [[utilization-and-saturation]]
  - [[throughput-latency-metrics]]
  - [[model-classify-intervene]]

