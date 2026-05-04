# Systems Performance — perf: sampling, syscall summaries, and I/O filters (5.5.1) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.5.1 `perf` (CPU sampling, `perf trace` patterns, filtered I/O syscall study; excludes flame-graph command recipes per ingestion filter)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-perf-profiling-syscall-trace-and-io-5-5-1.md`
- Chunks:
  - `processed/code/systems-performance-perf-profiling-syscall-trace-and-io-5-5-1-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Kernel-buffered collection** changes the cost model versus stop-the-world style tracing interfaces for syscall-heavy workloads—treat “safe by default” as an engineering constraint, not a slogan ([[instrumentation-overhead-and-perturbation]]).
- (diagnosis) **`perf trace -s` before line-by-line**: rank syscall time and counts, then attach narrow `-e` filters for I/O shape questions (sizes, flags) ([[drill-down-analysis]], [[event-tracing]]).
- (abstraction) One toolchain spans **timer sampling** and **syscall events**—pick the mode that matches the hypothesis phase instead of running both at full blast ([[observability-vs-experimentation]], [[sampling-based-profiling]]).

## Application validation

- **Noisy broker**: run syscall totals, discover `sendto`/`recvfrom` dominate, then filter only those syscalls before asking the team to read megabytes of per-event text.

## Decision clarity

- **Decision**: choose **syscall summaries plus targeted filters** over **raw per-syscall streams** when syscall rate would flood operators and hide the few types that matter.

## Concepts reused / refined / created

- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (heuristic): [[drill-down-analysis]]
- Reused (measurement): [[event-tracing]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[instrumentation-overhead-and-perturbation]]
  - [[drill-down-analysis]]
  - [[event-tracing]]
  - [[observability-vs-experimentation]]
  - [[sampling-based-profiling]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-observability-tools-chapter-framing-5-5]]
  - [[systems-performance-bcc-profile-kernel-side-aggregation-5-5-2]]
