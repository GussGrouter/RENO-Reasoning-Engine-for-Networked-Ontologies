# Systems Performance — CPU concepts: IPC, utilization semantics, user/kernel split (6.3.7–6.3.9) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Sections 6.3.7–6.3.9 (IPC/CPI interpretation, utilization includes stall cycles, user vs kernel time ratios)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-concepts-ipc-utilization-and-user-kernel-time-6-3-7-9.md`
- Chunks:
  - `processed/code/systems-performance-cpu-concepts-ipc-utilization-and-user-kernel-time-6-3-7-9-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **IPC/CPI summarizes stall vs execute balance**—low IPC points remediation toward **memory path**; high IPC with high utilization can still mean **bad instructions** (efficiency vs effectiveness split) ([[throughput-latency-metrics]], [[measurement-validity]]).
- (measurement) **CPU utilization counts stall cycles as “busy”**—high % can misread as compute saturation when the CPU is **waiting on DRAM** ([[utilization-and-saturation]], [[measurement-validity]]).
- (diagnosis) **User/kernel time ratio** is a coarse **workload classifier** (compute vs syscall-heavy) before attaching tracers ([[kernel-user-boundary]], [[resource-analysis-vs-workload-analysis]]).

## Application validation

- **Cloud “CPU pegged”**: if IPC ~0.2 but marketing says “optimize Java,” redirect to **memory bandwidth / object churn** before JVM flag tuning.

## Decision clarity

- **Decision**: choose **memory locality / bandwidth remediation** over **higher clock or more vCPU** when IPC is low and utilization is dominated by stall-shaped cycles.

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[utilization-and-saturation]]
  - [[kernel-user-boundary]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[sampling-based-profiling]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-concepts-pipeline-width-and-smt-6-3-3-6]]
  - [[systems-performance-cpu-saturation-preemption-and-quotas-6-3-10-11]]
