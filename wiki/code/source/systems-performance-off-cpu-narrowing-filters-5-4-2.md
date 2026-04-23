# Systems Performance — off-CPU narrowing and filters (5.4.2 tail) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.4.2 Off-CPU Analysis (techniques to focus meaningful off-CPU time; excludes tool-specific cookbook forward references)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-off-cpu-narrowing-filters-5-4-2.md`
- Chunks:
  - `processed/code/systems-performance-off-cpu-narrowing-filters-5-4-2-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Request-path scoping**: zoom off-CPU stacks to the application’s request-handling entry so idle housekeeping and unrelated blocking do not dominate the narrative ([[drill-down-analysis]], [[throughput-latency-metrics]]).
- (measurement) **State filters at collection** shrink noise but **drop legitimate states**—treat filter choice as part of the measurement hypothesis, not a neutral default ([[observability-vs-experimentation]], [[instrumentation-overhead-and-perturbation]]).
- (diagnosis) **Lock-related off-CPU** often needs **holder-side latency** (why the release was slow), not only waiter stacks—same causal direction pattern as cross-layer investigations ([[drill-down-analysis]], [[cross-component-interactions]]).

## Application validation

- **Path-specific SLO miss**: before declaring “the runtime blocks,” filter or symbol-search to the HTTP/gRPC handler frame so queue-depth waits on unrelated background threads do not masquerade as user-visible stalls.

## Concepts reused / refined / created

- Reused (heuristic): [[drill-down-analysis]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (abstraction): [[cross-component-interactions]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[drill-down-analysis]]
  - [[observability-vs-experimentation]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[throughput-latency-metrics]]
  - [[cross-component-interactions]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-profiling-kernel-vs-user-5-4-1]]
  - [[systems-performance-syscall-analysis-boundary-instrumentation-5-4-3]]
