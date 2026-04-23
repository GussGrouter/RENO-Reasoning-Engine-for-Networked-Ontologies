# Systems Performance — thread state investigation and measurement (5.4.5 continued) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.4.5 Thread State Analysis (per-state follow-ups, OS mapping, Linux measurement strategies; tool names as operational pointers)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-thread-state-investigation-and-measurement-5-4-5.md`
- Chunks:
  - `processed/code/systems-performance-thread-state-investigation-and-measurement-5-4-5-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Each state suggests a **different next measurement**: CPU scheduler vs swap vs block I/O vs syscall-shaped network vs voluntary sleep reasons vs lock graphs ([[drill-down-analysis]], [[resource-analysis-vs-workload-analysis]]).
- (abstraction) **OS thread letters are incomplete** relative to the nine-state ideal—recover finer splits with **multiple counters** (user/system split, schedstats run delay, paging indicators) ([[observability-vs-experimentation]]).
- (measurement) On Linux, combine **cheap clues**, targeted **off-CPU analysis**, and **direct timers** when the question justifies the cost and risk ([[instrumentation-overhead-and-perturbation]], [[latency-analysis]]).
- (diagnosis) **Network and lock waits** often represent **waiting for work** (keep-alive, condition variables)—mislabeling them as “hot I/O” misroutes fixes ([[resource-analysis-vs-workload-analysis]]).

## Application validation

- **Many threads in uninterruptible sleep**: correlate process `iodelay` with **system-wide swap** counters—if swap is zero, attribute delay to real block I/O paths; if swap is active, treat as memory pressure first.

## Decision clarity

- **Decision**: choose **correlating coarse scheduler/paging signals** over **single-metric CPU%** when threads spend time in run-queue or anonymous paging–shaped states.

## Concepts reused / refined / created

- Reused (heuristic): [[drill-down-analysis]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (measurement): [[latency-analysis]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[drill-down-analysis]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[observability-vs-experimentation]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[latency-analysis]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-thread-state-nine-state-model-5-4-5]]
  - [[systems-performance-delay-accounting-4-3-3]]
  - [[systems-performance-lock-contention-and-hold-time-5-4-6]]
