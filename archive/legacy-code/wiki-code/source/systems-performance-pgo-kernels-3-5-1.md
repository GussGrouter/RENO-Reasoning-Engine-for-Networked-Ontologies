# Systems Performance — PGO kernels (3.5.1) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.5.1 PGO Kernels

## Processed artifacts

- Converted slice: `processed/code/systems-performance-pgo-kernels-3-5-1.md`
- Chunks:
  - `processed/code/systems-performance-pgo-kernels-3-5-1-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Profile-guided kernel builds close the loop “observe hot behavior → recompile → redeploy,” trading engineering effort and specialization for throughput on a representative workload.
- (diagnosis) AutoFDO-style flows reduce the need for a special instrumented kernel by converting perf-style profiles into compiler inputs—still the same decision pattern: evidence must match production reality.

## Concepts reused / refined / created

- Reused (measurement): [[sampling-based-profiling]]
- Reused (heuristic): [[static-performance-tuning]]
- Reused (heuristic): [[optimize-expected-case]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]

## Links

- Concepts:
  - [[sampling-based-profiling]]
  - [[static-performance-tuning]]
  - [[optimize-expected-case]]
  - [[resource-vs-implementation-bottleneck]]
