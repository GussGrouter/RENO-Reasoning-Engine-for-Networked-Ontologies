# Systems Performance — chapter 5 exercises: under-load lab (hypothesis → attribution) (5.7 partial) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.7 Exercises, item 4 (through I/O size characterization; book mentions stack-based CPU/off-CPU views—ingestion omits visualization command detail)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-chapter-5-exercises-under-load-lab-a-5-7.md`
- Chunks:
  - `processed/code/systems-performance-chapter-5-exercises-under-load-lab-a-5-7-chunk-000001.md`

## Extracted ideas (with classification)

- (heuristic) **Hypothesize CPU vs I/O bound before measuring**—forces explicit model of dominant resources and falsifiable checks ([[scientific-method]], [[resource-analysis-vs-workload-analysis]]).
- (diagnosis) **Cross-check hypothesis with observability** instead of trusting intuition when mixed workloads exist ([[observability-vs-experimentation]], [[drill-down-analysis]]).
- (measurement) **Hottest on-CPU stacks vs longest off-CPU waits** (with idle excluded) split “compute vs waiting” without collapsing them into a single CPU% ([[sampling-based-profiling]], [[latency-analysis]]).
- (measurement) **I/O size characterization** bridges syscall-level evidence to workload design choices ([[throughput-latency-metrics]], [[event-tracing]]).

## Application validation

- **Latency regression**: write CPU-vs-I/O hypothesis in the ticket, then attach the two stack-attribution captures that would falsify it—mirrors exercise ordering.

## Decision clarity

- **Decision**: choose **off-CPU wait analysis (non-idle)** over **CPU profiling alone** when the hypothesis is “blocked on external dependencies” but CPU utilization looks healthy.

## Concepts reused / refined / created

- Reused (heuristic): [[scientific-method]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (heuristic): [[drill-down-analysis]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused (measurement): [[latency-analysis]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (measurement): [[event-tracing]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[scientific-method]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[observability-vs-experimentation]]
  - [[drill-down-analysis]]
  - [[sampling-based-profiling]]
  - [[latency-analysis]]
  - [[throughput-latency-metrics]]
  - [[event-tracing]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-chapter-5-exercises-application-profile-observability-and-community-5-7]]
  - [[systems-performance-chapter-5-exercises-under-load-lab-b-5-7]]
