# Systems Performance — Cycle analysis + performance monitoring (7.4.4–7.4.5) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.4.4–7.4.5** — memory stalls (IPC, **MEM_LOAD_RETIRED**, **LAST_LEVEL_CACHE**), sampling + PMC tradeoffs; **monitoring**: **pressure + top + OOM logs** (+ **perf** hooks as pattern)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-methodology-cycle-and-monitoring-7-4-4-5.md`
- Chunks:
  - `processed/code/systems-performance-memory-methodology-cycle-and-monitoring-7-4-4-5-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **PMC memory-stall stories** tie **slow execution** to **DRAM vs LLC**, but **scope + aggregation** dominate validity—per-thread vs system-wide counters answer different questions ([[measurement-validity]], [[throughput-latency-metrics]], [[resource-vs-implementation-bottleneck]]).

## Application validation

- **Low IPC + rising LLC misses**: validate **parallelism contention** vs **NUMA locality** before blaming **DRAM bandwidth**—PMC labels mislead without **topology context**.

## Decision clarity

- **Decision**: choose **pressure + reclaim/OOM telemetry for saturation triage** over **PMC stall stacks** when **customers feel latency**, but **swap/scan/OOM already explain** delay.

## Concepts reused / refined / created

- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[resource-vs-implementation-bottleneck]]
- Reused (structure): [[utilization-and-saturation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[measurement-validity]]
  - [[throughput-latency-metrics]]
  - [[resource-vs-implementation-bottleneck]]
  - [[utilization-and-saturation]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-methodology-leak-detection-7-4-6]]
