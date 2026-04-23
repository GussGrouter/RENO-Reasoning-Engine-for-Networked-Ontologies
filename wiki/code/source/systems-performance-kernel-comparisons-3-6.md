# Systems Performance — kernel comparisons (3.6) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.6 Kernel Comparisons

## Processed artifacts

- Converted slice: `processed/code/systems-performance-kernel-comparisons-3-6.md`
- Chunks:
  - `processed/code/systems-performance-kernel-comparisons-3-6-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) “Which kernel is fastest?” is workload- and configuration-dependent; community scale and driver maturity can dominate micro-optimizations in practice.
- (diagnosis) Isolated syscall microbenchmarks are a common trap: a fast syscall path may be irrelevant if production rarely uses that syscall—or uses different flags/paths than the benchmark.
- (measurement) Fair comparisons require comparable tuning maturity; otherwise you may be measuring “default config drift” rather than intrinsic kernel limits.

## Concepts reused / refined / created

- Reused (heuristic): [[micro-benchmarking]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (heuristic): [[static-performance-tuning]]
- Reused (mechanism): [[extended-bpf]]

## Links

- Concepts:
  - [[micro-benchmarking]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[observability-vs-experimentation]]
  - [[static-performance-tuning]]
  - [[extended-bpf]]
