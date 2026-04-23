# Systems Performance — CPU saturation, scheduler queues, preemption cushion (6.3.10–6.3.11) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Sections 6.3.10–6.3.11 (CPU saturation forms, scheduler latency vs preemption)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-saturation-preemption-and-quotas-6-3-10-11.md`
- Chunks:
  - `processed/code/systems-performance-cpu-saturation-preemption-and-quotas-6-3-10-11-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Two saturation shapes**: **100% utilization** (runnable threads queue for CPU time) vs **quota/cgroup ceilings** where the CPU is not fully busy but runnable work still waits—visibility depends on how virtualization maps limits ([[utilization-and-saturation]], [[cross-component-interactions]]).
- (mechanism) **Scheduler latency** here is time **waiting in run-queue structures**, not just “off-CPU” in a generic sense—still a capacity signal once runnable backlog appears ([[utilization-and-saturation]]).
- (abstraction) **Preemption as cushion**: compared with disks, CPU saturation is often **less catastrophic for mixed priorities** because higher-priority runnable work can **preempt** lower-priority on-CPU threads—this changes what “bad saturation” looks like in product SLO terms ([[throughput-latency-metrics]], [[cross-component-interactions]]).

## Application validation

- **Kubernetes throttling**: p95 latency rises while node CPU charts look “fine” → treat **throttling / cfs_quota** as **saturation** evidence, not disproof of CPU bottlenecks.

## Decision clarity

- **Decision**: choose **quota / limiter remediation** over **blind horizontal scale-out** when runnable delay tracks **policy ceilings** more than **aggregate utilization**.

## Concepts reused / refined / created

- Reused (structure): [[utilization-and-saturation]]
- Reused (structure): [[cross-component-interactions]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[utilization-and-saturation]]
  - [[cross-component-interactions]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-concepts-ipc-utilization-and-user-kernel-time-6-3-7-9]]
  - [[systems-performance-cpu-priority-inversion-and-inheritance-6-3-12]]
