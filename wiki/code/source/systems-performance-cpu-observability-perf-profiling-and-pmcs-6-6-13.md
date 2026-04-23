# Systems Performance — perf as the combined profiling + PMC workbench (6.6.13) (PDF 286–320)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.6.13** — `perf` for **stack sampling**, **PMC events**, and **experiment design** tradeoffs (tool specifics stay in the extract; concepts are portable)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-observability-perf-profiling-and-pmcs-6-6-13.md`
- Chunks:
  - `processed/code/systems-performance-cpu-observability-perf-profiling-and-pmcs-6-6-13-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **One workbench can span attribution + microarchitecture**, but each mode has different **validity and overhead envelopes**—treat mode switches as **new experiments** ([[sampling-based-profiling]], [[measurement-validity]]).
- (diagnosis) **PMC-backed evidence** is strongest when tied to **ratios and hypotheses** (IPC, stall classes), not raw event vanity metrics ([[counters-statistics-metrics]], [[scientific-method]]).
- (abstraction) **Preserving raw samples vs kernel summaries** is the recurring **storage/perturbation vs reprocessability** tradeoff ([[instrumentation-overhead-and-perturbation]], [[shift-computation-in-time]]).

## Application validation

- **Production incident**: prefer **short perf sample + saved perf.data** when you may need **two different aggregations** from the same capture window.

## Decision clarity

- **Decision**: choose **perf archive + post-process** over **live-only BPF summaries** when legal/compliance requires **reproducible evidence** of the same run.

## Concepts reused / refined / created

- Reused (measurement): [[sampling-based-profiling]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused (abstraction): [[scientific-method]]
- Reused (abstraction): [[instrumentation-overhead-and-perturbation]]
- Reused (abstraction): [[shift-computation-in-time]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[sampling-based-profiling]]
  - [[measurement-validity]]
  - [[counters-statistics-metrics]]
  - [[scientific-method]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[shift-computation-in-time]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-observability-process-attribution-and-clock-tools-6-6-5-12]]
  - [[systems-performance-cpu-observability-bpf-profile-scheduler-and-softirq-6-6-14-18]]
