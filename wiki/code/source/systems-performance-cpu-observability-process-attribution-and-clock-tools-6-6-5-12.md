# Systems Performance — Process/thread attribution and clock/PMC surface tools (6.6.5–6.6.12) (PDF 286–320)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.6.5–6.6.12** — who is on-CPU (`ps`/`top`/`pidstat`/`time`) vs **what frequency/PMC/TLB story** the hardware is presenting (`turbostat`/`showboost`/`pmcarch`/`tlbstat`)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-observability-process-attribution-and-clock-tools-6-6-5-12.md`
- Chunks:
  - `processed/code/systems-performance-cpu-observability-process-attribution-and-clock-tools-6-6-5-12-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Top consumers are necessary but not sufficient**—they answer **who**, while stalls/frequency answer **why cycles aren’t productive** ([[resource-analysis-vs-workload-analysis]], [[throughput-latency-metrics]]).
- (measurement) **User vs system split at process granularity** is a **workload classifier** before expensive tracing ([[resource-analysis-vs-workload-analysis]], [[measurement-validity]]).
- (measurement) **Clock/PMC “surface reads”** validate whether **performance state matches the mental model** of the investigation (thermal caps, governor, turbo) ([[measurement-validity]], [[counters-statistics-metrics]]).

## Application validation

- **“Java is slow”** but `pidstat` shows **sys ≫ user** → pivot to **syscall / lock / IO** evidence paths, not bytecode micro-opts first.

## Decision clarity

- **Decision**: choose **clock-state + IPC/PMC sanity panel** over **more heap profiling** when CPU time is high but **effective throughput per GHz** is suspicious.

## Concepts reused / refined / created

- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-analysis-vs-workload-analysis]]
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[counters-statistics-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-observability-load-and-system-wide-stats-6-6-1-4]]
  - [[systems-performance-cpu-observability-perf-profiling-and-pmcs-6-6-13]]
