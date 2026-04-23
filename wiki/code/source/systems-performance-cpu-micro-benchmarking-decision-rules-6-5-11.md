# Systems Performance — CPU micro-benchmarking: what is actually being measured (6.5.11) (PDF 286–320)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.5.11** — micro-benchmark targets (instructions, memory hierarchy, language/runtime, OS primitives) and **cross-system comparability** pitfalls (stops before **§6.6** tool survey)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-micro-benchmarking-decision-rules-6-5-11.md`
- Chunks:
  - `processed/code/systems-performance-cpu-micro-benchmarking-decision-rules-6-5-11-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Micro-benchmarks answer narrow questions**—they are strongest for **hierarchy latency / instruction costs**, weakest when passed off as **whole-application truth** ([[micro-benchmarking]], [[measurement-validity]]).
- (diagnosis) **Cross-machine scoreboards often test the compiler/toolchain**, not the benchmark’s nominal story—publish **build flags + threading model + compiler** with any number ([[scientific-method]], [[static-performance-tuning]]).
- (abstraction) **Single-thread scores mis-scale** on multi-CPU systems—throughput under **parallel runnable work** is the relevant translation for capacity decisions ([[universal-scalability-law]], [[throughput-latency-metrics]]).

## Application validation

- **“Dhrystone says we’re faster”** but prod throughput flat → rerun with **pinned threads + representative heap + same compiler** or discard the comparison.

## Decision clarity

- **Decision**: choose **fixed-build micro-benchmarks for regression gates on one SKU class** over **vendor leaderboard chasing** when the decision is **capacity planning for parallel workloads**.

## Concepts reused / refined / created

- Reused (heuristic): [[micro-benchmarking]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[scientific-method]]
- Reused (heuristic): [[static-performance-tuning]]
- Reused (abstraction): [[universal-scalability-law]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[micro-benchmarking]]
  - [[measurement-validity]]
  - [[scientific-method]]
  - [[static-performance-tuning]]
  - [[universal-scalability-law]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-priority-resource-controls-and-cpu-binding-6-5-8-10]]
  - [[systems-performance-cpu-observability-load-and-system-wide-stats-6-6-1-4]]
