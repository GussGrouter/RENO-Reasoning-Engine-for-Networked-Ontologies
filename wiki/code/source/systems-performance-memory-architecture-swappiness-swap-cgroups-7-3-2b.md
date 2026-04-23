# Systems Performance — swappiness, swap vs no-swap, cgroup memory limits (7.3.2) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.2** — **swappiness** trade (cache warmth vs paging apps), **no swap** behavior (faster fail / OOM), **Netflix-style** ops pattern, **cgroup limit** vs **host abundance**

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-architecture-swappiness-swap-cgroups-7-3-2b.md`
- Chunks:
  - `processed/code/systems-performance-memory-architecture-swappiness-swap-cgroups-7-3-2b-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Swap is a grace-period vs determinism knob**: with swap, **leaks become latency**; without swap, **leaks become hard failures**—pick based on **debuggability vs blast radius** ([[throughput-latency-metrics]], [[utilization-and-saturation]]).
- (structure) **Cgroup caps** decouple **“plenty of host RAM”** from **process survival**—classic **platform coupling** for containers ([[cross-component-interactions]], [[measurement-validity]] for **scope**).

## Application validation

- **Pods OOM while node shows free**: treat as **limit semantics**, not **kernel bug**—raise **cgroup high watermark** or **fix RSS**, not **node purchase**.

## Decision clarity

- **Decision**: choose **no swap + fast fail + traffic shift** over **swap-enabled grace** when **SLO favors shedding load** over **keeping one bad instance limping**.

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (structure): [[cross-component-interactions]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[utilization-and-saturation]]
  - [[cross-component-interactions]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-architecture-linux-freeing-ladder-7-3-2a]]
  - [[systems-performance-memory-architecture-free-lists-reaping-scan-7-3-2c]]
