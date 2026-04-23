# Systems Performance — `syscount`: ranking syscalls before deep tracing (5.5.6) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.5.6 `syscount` (system-wide syscall ranking; per-process mode as follow-on)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-syscount-ranking-and-follow-on-5-5-6.md`
- Chunks:
  - `processed/code/systems-performance-syscount-ranking-and-follow-on-5-5-6-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Rank syscalls first** to choose which event types deserve argument-level or stack-bearing tracers—cheap ordering before expensive attachment ([[drill-down-analysis]], [[system-call]]).
- (diagnosis) **Per-process ranking** (`-P`) reframes “what is the system doing?” into “which actor is driving the syscall mix?” for multi-tenant hosts ([[resource-analysis-vs-workload-analysis]]).

## Application validation

- **Spiky kernel CPU**: if `recvfrom`/`sendto` dominate counts, follow with filtered syscall trace or stack-bearing tools on those entry points instead of tracing every `futex`.

## Decision clarity

- **Decision**: choose **system-wide syscall ranking** over **full syscall tracing** when you still need to pick *which* syscall family explains most kernel time.

## Concepts reused / refined / created

- Reused (heuristic): [[drill-down-analysis]]
- Reused (mechanism): [[system-call]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[drill-down-analysis]]
  - [[system-call]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-execsnoop-execve-lineage-discovery-5-5-5]]
  - [[systems-performance-bpftrace-custom-aggregation-probe-ladder-5-5-7]]
