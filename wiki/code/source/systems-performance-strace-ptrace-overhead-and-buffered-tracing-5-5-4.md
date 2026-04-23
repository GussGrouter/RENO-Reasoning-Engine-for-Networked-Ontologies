# Systems Performance — `strace`: ptrace overhead vs buffered tracing (5.5.4) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.5.4 `strace` (human-readable syscall summaries; ptrace overhead; contrast with buffered kernel tracing)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-strace-ptrace-overhead-and-buffered-tracing-5-5-4.md`
- Chunks:
  - `processed/code/systems-performance-strace-ptrace-overhead-and-buffered-tracing-5-5-4-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **ptrace-style syscall traps** can dominate end-to-end time for syscall-heavy programs—the observer effect is sometimes order-of-magnitude, not a few percent ([[instrumentation-overhead-and-perturbation]]).
- (abstraction) **Buffered kernel ring buffers + periodic drain** reduce user/kernel ping-pong; choose this class when you need sustained syscall visibility under load ([[event-tracing]], [[observability-vs-experimentation]]).
- (measurement) **Summaries (`-c`)** remain the low-risk first step even when attach-tracing is acceptable only briefly ([[drill-down-analysis]]).

## Application validation

- **Storage microbenchmark regression**: comparing `dd` throughput with and without attach-tracing exposes whether a “tracing-first” habit is falsifying the baseline entirely.

## Decision clarity

- **Decision**: choose **buffered kernel tracers** over **ptrace syscall attach** for sustained or production-adjacent captures when syscall rate is high enough that stop/contend semantics dominate.

## Concepts reused / refined / created

- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (measurement): [[event-tracing]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (heuristic): [[drill-down-analysis]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[instrumentation-overhead-and-perturbation]]
  - [[event-tracing]]
  - [[observability-vs-experimentation]]
  - [[drill-down-analysis]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-offcputime-aggregation-and-duration-filters-5-5-3]]
  - [[systems-performance-execsnoop-execve-lineage-discovery-5-5-5]]
