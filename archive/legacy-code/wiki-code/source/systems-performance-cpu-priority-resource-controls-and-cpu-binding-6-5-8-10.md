# Systems Performance — Priority tuning, resource controls, CPU binding (6.5.8–6.5.10) (PDF 286–320)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.5.8** nice/RT hazards, **§6.5.9** CPU shares/limits, **§6.5.10** binding vs exclusive CPU sets (locality intent)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-priority-resource-controls-and-cpu-binding-6-5-8-10.md`
- Chunks:
  - `processed/code/systems-performance-cpu-priority-resource-controls-and-cpu-binding-6-5-8-10-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Nice is a contention play**: it reduces **scheduler interference** on high-priority work when CPUs are **actually contended**—verify with **latency of the protected class**, not only nice values ([[throughput-latency-metrics]], [[process-abstraction]]).
- (abstraction) **RT priority eliminates peers**—failure modes include **CPU starvation** for housekeeping; guardrails are part of the **operability contract**, not optional tuning ([[throughput-latency-metrics]], [[cross-component-interactions]]).
- (mechanism) **Binding trades fleet elasticity for locality**: **exclusive sets** maximize **cache warmth** but can **strand capacity**—decide based on **tail vs efficiency** goals ([[caching]], [[cross-component-interactions]]).

## Application validation

- **RT pipeline + runaway loop**: ensure **time-bounded RT budgets** and break-glass paths before granting **FIFO across all cores**.

## Decision clarity

- **Decision**: choose **exclusive cpuset** over **soft affinity** when **noisy neighbor tail risk** outweighs **bin-packing efficiency** on shared hosts.

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[process-abstraction]]
- Reused (structure): [[cross-component-interactions]]
- Reused (mechanism): [[caching]]
- Reused (structure): [[utilization-and-saturation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[process-abstraction]]
  - [[cross-component-interactions]]
  - [[caching]]
  - [[utilization-and-saturation]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-static-performance-tuning-checklist-6-5-7]]
  - [[systems-performance-cpu-micro-benchmarking-decision-rules-6-5-11]]
