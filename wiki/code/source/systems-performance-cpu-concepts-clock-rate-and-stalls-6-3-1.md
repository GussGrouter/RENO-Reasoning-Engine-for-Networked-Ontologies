# Systems Performance — CPU concepts: clock rate vs useful work (6.3.1) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.3.1 Clock Rate (DVFS; marketing GHz vs cycles spent stalling on memory)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-concepts-clock-rate-and-stalls-6-3-1.md`
- Chunks:
  - `processed/code/systems-performance-cpu-concepts-clock-rate-and-stalls-6-3-1-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Clock rate scales how fast cycles tick**, not automatically **how many useful instructions retire**—stall-heavy intervals can absorb higher GHz with little throughput gain ([[throughput-latency-metrics]], [[caching]]).
- (abstraction) **Dynamic frequency scaling** ties CPU performance to **power/thermal policy** and idle behavior—interpreting “CPU slow” requires checking **governor intent**, not only code ([[observability-vs-experimentation]], [[static-performance-tuning]]).

## Application validation

- **“Buy faster SKUs” proposal**: if profiles show memory-bound stalls, model uplift from DRAM/cache work first—GHz alone may only move the stall counter faster.

## Decision clarity

- **Decision**: choose **memory subsystem / locality work** over **CPU frequency upgrades** when cycles are mostly waiting on memory, not executing.

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (mechanism): [[caching]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (heuristic): [[static-performance-tuning]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[caching]]
  - [[observability-vs-experimentation]]
  - [[static-performance-tuning]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-models-run-queues-scheduler-latency-6-2-3]]
  - [[systems-performance-cpu-concepts-instruction-lifecycle-and-stall-cycles-6-3-2]]
