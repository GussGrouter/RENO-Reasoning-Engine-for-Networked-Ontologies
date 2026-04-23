# Systems Performance — CPU tuning: governors, idle depth, affinity, cpusets, cgroups (6.9.4–6.9.8) (PDF 321–360)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.9.4–6.9.8** — frequency governors vs **power/environment cost**, **C-state exit latency tuning**, **taskset/numactl**, **exclusive cpusets**, **cgroups CPU shares/limits** (stops before **§6.9.9** security/mitigation catalog)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-tuning-governors-affinity-cgroups-6-9-4-8.md`
- Chunks:
  - `processed/code/systems-performance-cpu-tuning-governors-affinity-cgroups-6-9-4-8-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **“Performance governor” is a sustainability trade**, not a free win—validate **latency/throughput delta** against **power/thermal reality** ([[throughput-latency-metrics]], [[cross-component-interactions]]).
- (mechanism) **Disabling deep C-states** is a **tail-latency vs energy** knob—exit latency can dominate **short RPC** budgets ([[throughput-latency-metrics]], [[measurement-validity]]).
- (mechanism) **Exclusive cpusets** buy **deterministic locality** by **stranding capacity**—decide explicitly on **fleet efficiency vs tenant isolation** ([[caching]], [[cross-component-interactions]]).
- (structure) **cgroups shares vs limits** mirror **multi-tenant product semantics**—the engineering move is aligning **scheduler policy** with **billing/SLO units** ([[utilization-and-saturation]], [[cross-component-interactions]]).

## Application validation

- **Latency-sensitive shard on shared host**: test **shallower idle floor + exclusive cpuset** against **performance governor** using the same **p99 + power** yardstick.

## Decision clarity

- **Decision**: choose **exclusive cpuset + irq awareness** over **global performance governor** when **noisy neighbor + tail SLO** dominates **average throughput per host**.

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[cross-component-interactions]]
- Reused (abstraction): [[measurement-validity]]
- Reused (mechanism): [[caching]]
- Reused (structure): [[utilization-and-saturation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[cross-component-interactions]]
  - [[measurement-validity]]
  - [[caching]]
  - [[utilization-and-saturation]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-tuning-compiler-scheduler-sysctl-6-9-1-3]]
