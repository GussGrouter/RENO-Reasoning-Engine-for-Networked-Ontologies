# Systems Performance — experimentation (1.8) (PDF pages 52–54)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 1, Section 1.8 Experimentation (benchmarking as synthetic workload; macro vs micro)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-experimentation-1-8.md`
- Chunks:
  - `processed/code/systems-performance-experimentation-1-8-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Experimentation tools apply a synthetic workload to measure performance; they can perturb the system under test and must be used carefully.
- (measurement) Macro-benchmarks (workload-like) vs micro-benchmarks (component-focused) differ in stability/debuggability; micro-benchmarks are typically easier to repeat and understand.
- (diagnosis) Fixed-workload experiments can remove client variance, revealing other sources of variance; observability-first in production is prudent, but experimentation can reach answers faster in some cases.

## Concepts reused / refined / created

- Created (measurement): [[observability-vs-experimentation]]

## Links

- Concepts:
  - [[observability-vs-experimentation]]
  - [[throughput-latency-metrics]]

