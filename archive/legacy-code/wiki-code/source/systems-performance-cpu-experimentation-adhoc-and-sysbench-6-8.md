# Systems Performance — CPU experimentation: known workloads vs benchmarks (6.8) (PDF 321–360)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.8** — ad hoc **calibration loops** and **SysBench**-style comparative runs (ties back to §6.5.11)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-experimentation-adhoc-and-sysbench-6-8.md`
- Chunks:
  - `processed/code/systems-performance-cpu-experimentation-adhoc-and-sysbench-6-8-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Ad hoc burn loops** are **instrumentation calibration**, not benchmarks—their value is proving **observability claims** under a known shape ([[observability-vs-experimentation]], [[measurement-validity]]).
- (measurement) **Controlled benchmarks** still require **parallelism confirmation** (`mpstat` class signals)—otherwise “CPU benchmark” measures **scheduler + thread count**, not silicon ([[micro-benchmarking]], [[scientific-method]]).
- (abstraction) **Cross-system numbers** assume hidden variables (compiler, flags, power state)—publish **environment contract** alongside results ([[measurement-validity]], [[static-performance-tuning]]).

## Application validation

- **New tracing agent**: validate with **single-thread hot loop + mpstat** before trusting **first production incident** captures.

## Decision clarity

- **Decision**: choose **instrument calibration workloads + parallel witness metrics** over **benchmark leaderboard deltas** when the decision is **whether observability is lying**.

## Concepts reused / refined / created

- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (abstraction): [[measurement-validity]]
- Reused (heuristic): [[micro-benchmarking]]
- Reused (abstraction): [[scientific-method]]
- Reused (heuristic): [[static-performance-tuning]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[observability-vs-experimentation]]
  - [[measurement-validity]]
  - [[micro-benchmarking]]
  - [[scientific-method]]
  - [[static-performance-tuning]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-interrupt-gpu-tools-and-distribution-visualizations-6-6-19-6-7-4]]
  - [[systems-performance-cpu-tuning-compiler-scheduler-sysctl-6-9-1-3]]
  - [[systems-performance-cpu-micro-benchmarking-decision-rules-6-5-11]]
