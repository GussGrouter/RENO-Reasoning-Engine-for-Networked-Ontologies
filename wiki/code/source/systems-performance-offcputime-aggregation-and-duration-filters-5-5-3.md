# Systems Performance — `offcputime`: aggregation and duration gates (5.5.3) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.5.3 `offcputime` (off-CPU stacks, kernel aggregation, min/max duration filtering; excludes flame-graph recipe text)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-offcputime-aggregation-and-duration-filters-5-5-3.md`
- Chunks:
  - `processed/code/systems-performance-offcputime-aggregation-and-duration-filters-5-5-3-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Minimum duration thresholds** drop micro-scheduler noise; **maximum caps** strip multi-second “waiting for work” stacks so off-CPU views focus on request-relevant blocking ([[drill-down-analysis]], [[instrumentation-overhead-and-perturbation]]).
- (measurement) Kernel-side uniqueness aggregation mirrors the “bounded export” pattern for high-volume scheduler events ([[extended-bpf]], [[event-tracing]]).

## Application validation

- **Batch worker idle loops**: if off-CPU stacks are 90% seconds-long parking threads, tighten `-M` (max duration) before stakeholders misread “disk” from idle blocking.

## Decision clarity

- **Decision**: choose **max-duration filters on off-CPU captures** over **raw unlimited off-CPU dumps** when the dominant stacks are long-lived idle parking rather than request-path waits.

## Concepts reused / refined / created

- Reused (heuristic): [[drill-down-analysis]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (mechanism): [[extended-bpf]]
- Reused (measurement): [[event-tracing]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[drill-down-analysis]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[extended-bpf]]
  - [[event-tracing]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-bcc-profile-kernel-side-aggregation-5-5-2]]
  - [[systems-performance-strace-ptrace-overhead-and-buffered-tracing-5-5-4]]
