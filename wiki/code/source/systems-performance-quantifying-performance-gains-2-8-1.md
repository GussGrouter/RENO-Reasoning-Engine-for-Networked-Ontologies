# Systems Performance — quantifying performance gains (2.8.1) (PDF pages 110–120)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.8.1 Quantifying Performance Gains

## Processed artifacts

- Converted slice: `processed/code/systems-performance-quantifying-performance-gains-2-8-1.md`
- Chunks:
  - `processed/code/systems-performance-quantifying-performance-gains-2-8-1-chunk-000001.md`

## Extracted ideas (with classification)

- (method) Quantify issues and expected gains so candidate fixes can be compared and prioritized (via observation or experiments).
- (measurement) Observation-based quantification uses a reliable metric and estimates the gain from removing a component (often latency decomposition).
- (diagnosis) Ensure decomposed latency is synchronous with the request; asynchronous background work may not affect request latency directly.
- (method) Experimentation-based quantification compares before vs after using a reliable metric; may be unsuitable in production if expensive/risky.

## Concepts reused / refined / created

- Created (method): [[quantifying-performance-gains]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (technique): [[latency-analysis]]
- Reused (measurement): [[observability-vs-experimentation]]
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[quantifying-performance-gains]]
  - [[throughput-latency-metrics]]
  - [[latency-analysis]]
  - [[observability-vs-experimentation]]
  - [[model-classify-intervene]]

