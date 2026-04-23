# Systems Performance — Idle thread, NUMA topology, resource-aware scheduling (6.4.2) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.4.2 — **Idle thread** (halt/power vs wakeup), **NUMA grouping / scheduling domains**, **processor resource-aware** scheduling (stops before §6.5 Methodology)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-idle-numa-topology-scheduler-awareness-6-4-2.md`
- Chunks:
  - `processed/code/systems-performance-cpu-idle-numa-topology-scheduler-awareness-6-4-2-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) **Idle thread is not “free zero work”**: it negotiates **halt / throttle** with hardware—ties scheduler policy to **C-state behavior** and **interrupt wake latency** ([[throughput-latency-metrics]], [[cross-component-interactions]]).
- (abstraction) **NUMA-aware kernels estimate access cost from topology**—**scheduling domains** are the portable idea: locality is a **graph**, not a CPU list ([[cross-component-interactions]], [[caching]]).
- (diagnosis) **Manual binding vs automatic domains** is a governance tradeoff: exclusivity can win determinism but **hides** fleet-level imbalance—choose based on **SLO class** ([[measurement-validity]], [[resource-analysis-vs-workload-analysis]]).

## Application validation

- **Low utilization + bad tail on NUMA**: enable/compare **autosplit by domain** vs **cpuset isolation** using **remote DRAM counters**, not socket maps alone.

## Decision clarity

- **Decision**: choose **cpuset / explicit NUMA partition** over **kernel auto balance** when **noisy neighbor + tail SLO** requires **hard locality contracts** on shared hosts.

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[cross-component-interactions]]
- Reused (mechanism): [[caching]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (abstraction): [[process-abstraction]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[cross-component-interactions]]
  - [[caching]]
  - [[measurement-validity]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[process-abstraction]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-scheduling-classes-policies-workload-shape-6-4-2]]
  - [[systems-performance-cpu-kernel-scheduler-functions-and-locality-6-4-2]]
  - [[systems-performance-cpu-methodology-cookbook-and-tools-method-6-5-intro-6-5-1]]
