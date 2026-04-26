# Systems Performance — CPU profiling: kernel-first evidence (5.4.1 partial) (PDF ~182–230)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.4.1 CPU Profiling (opening through kernel vs user-mode profiler bias; excludes flame-graph visualization detail per ingestion filter)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-profiling-kernel-vs-user-5-4-1.md`
- Chunks:
  - `processed/code/systems-performance-cpu-profiling-kernel-vs-user-5-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Kernel-attached profilers** see both user and kernel stacks (“mixed mode”), reducing blind spots when time disappears into syscalls or drivers ([[kernel-user-boundary]]).
- (diagnosis) **User-only profilers** can **skew CPU time** because descheduling is invisible—treat as a last resort when kernel capture is blocked by policy, not as the default truth source ([[observability-vs-experimentation]]).
- (measurement) **Sampling rate × CPUs × duration** explodes sample volume—aggregation strategy is part of the measurement design, not an afterthought ([[sampling-based-profiling]], [[instrumentation-overhead-and-perturbation]]).

## Application validation

- **Managed runtime in containers**: if `perf` is blocked but the JVM’s user profiler shows “100% Java,” escalate policy for **kernel stacks** before accepting that kernel time is negligible—otherwise you optimize the wrong half of the story.

## Concepts reused / refined / created

- Reused (measurement): [[sampling-based-profiling]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[sampling-based-profiling]]
  - [[kernel-user-boundary]]
  - [[observability-vs-experimentation]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-off-cpu-narrowing-filters-5-4-2]]
