# Systems Performance — CPU tuning: compiler, priorities, scheduler knobs (6.9.1–6.9.3) (PDF 321–360)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.9** introduction + **§6.9.1–6.9.3** (compiler flags, `nice`/`chrt` class selection, scheduler **CONFIG/sysctl** examples—tables treated as evidence artifacts, not concepts)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-tuning-compiler-scheduler-sysctl-6-9-1-3.md`
- Chunks:
  - `processed/code/systems-performance-cpu-tuning-compiler-scheduler-sysctl-6-9-1-3-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Compiler/ABI choices remain the cheapest “hardware upgrade”** when the bottleneck is instruction throughput under a fixed topology ([[static-performance-tuning]], [[throughput-latency-metrics]]).
- (diagnosis) **Scheduling class selection** is a **risk management** decision (RT can remove peers)—pair policy changes with **starvation guardrails** and measurement windows ([[throughput-latency-metrics]], [[process-abstraction]]).
- (measurement) **Sysctl migration cost knobs** encode **cache warmth economics**—raising/lowering them changes **load spread vs locality** without touching application code ([[cross-component-interactions]], [[measurement-validity]]).

## Application validation

- **Build farm latency**: before kernel sysctl tuning, confirm whether stragglers are **cache-cold migrations** vs **true CPU shortage** using **per-rung queue + IPC** panels.

## Decision clarity

- **Decision**: choose **CFS sysctl migration-cost tuning** over **more cores** when profiles show **thrashing migrations** with **low effective IPC** on otherwise idle neighbors.

## Concepts reused / refined / created

- Reused (heuristic): [[static-performance-tuning]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[process-abstraction]]
- Reused (structure): [[cross-component-interactions]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[static-performance-tuning]]
  - [[throughput-latency-metrics]]
  - [[process-abstraction]]
  - [[cross-component-interactions]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-experimentation-adhoc-and-sysbench-6-8]]
  - [[systems-performance-cpu-tuning-governors-affinity-cgroups-6-9-4-8]]
