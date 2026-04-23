# Systems Performance — micro-benchmarking (2.5.19) (PDF pages 98–106)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.5.19 Micro-Benchmarking

## Processed artifacts

- Converted slice: `processed/code/systems-performance-micro-benchmarking-2-5-19.md`
- Chunks:
  - `processed/code/systems-performance-micro-benchmarking-2-5-19-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Micro-benchmarks use simple/artificial workloads to test a narrow target; macro-benchmarks aim for realistic workload simulation and can be harder to reason about.
- (diagnosis) Micro-benchmarks can isolate external bottlenecks that are hard to spot in production workloads.
- (measurement) Micro-benchmarking may be done with a tool that both generates load and measures, or with a load generator + independent observability (cross-check).
- (measurement) Typical approach: run many operations and compute average time as runtime/operation count; test multiple dimensions (e.g., varying sizes/buffers).

## Concepts reused / refined / created

- Created (method): [[micro-benchmarking]]
- Reused (measurement): [[observability-vs-experimentation]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[micro-benchmarking]]
  - [[observability-vs-experimentation]]
  - [[counters-statistics-metrics]]
  - [[throughput-latency-metrics]]
  - [[model-classify-intervene]]

