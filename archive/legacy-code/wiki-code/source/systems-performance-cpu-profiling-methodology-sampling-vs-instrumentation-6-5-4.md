# Systems Performance — CPU profiling methodology: sampling vs instrumentation (6.5.4) (PDF 286–320)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.5.4** — timer sampling vs function tracing; missed short frames; dual user/kernel stacks; sample volume vs storage perturbation; interpretation discipline

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-profiling-methodology-sampling-vs-instrumentation-6-5-4.md`
- Chunks:
  - `processed/code/systems-performance-cpu-profiling-methodology-sampling-vs-instrumentation-6-5-4-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Sampling coarseness trades fidelity for safety**—avoid **lock-step** rates with periodic workloads; production viability is an **overhead budget** problem, not only Hz ([[sampling-based-profiling]], [[instrumentation-overhead-and-perturbation]]).
- (diagnosis) **Off-CPU gaps**: on-CPU samples **miss syscall time** and can **miss short-lived frames**—profile interpretation must state **what population was eligible to be observed** ([[measurement-validity]], [[throughput-latency-metrics]]).
- (mechanism) **High-volume sample sinks** can become the bottleneck—**summarize earlier** (closer to kernel/runtime) when disk writes perturb the workload under study ([[instrumentation-overhead-and-perturbation]], [[shift-computation-in-time]]).

## Application validation

- **49 Hz × 32 CPUs × 30s**: if writing raw stacks spikes **disk IO**, switch to **in-kernel aggregation** or lower rate before changing application code.

## Decision clarity

- **Decision**: choose **lower sampling rate + longer window** over **max Hz** when overhead breaches **SLO noise budget** but you still need **coarse attribution**.

## Concepts reused / refined / created

- Reused (measurement): [[sampling-based-profiling]]
- Reused (abstraction): [[instrumentation-overhead-and-perturbation]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[shift-computation-in-time]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[sampling-based-profiling]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[measurement-validity]]
  - [[throughput-latency-metrics]]
  - [[shift-computation-in-time]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-workload-characterization-6-5-3]]
  - [[systems-performance-cpu-cycle-analysis-and-performance-monitoring-6-5-5-6]]
