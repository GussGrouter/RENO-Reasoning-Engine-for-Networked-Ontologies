# Systems Performance — GPUs/accelerators as coupled capacity (6.4.1) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.4.1 — **GPUs** (parallel kernel offload pattern) + **Other accelerators** (FPGA/TPU offload); Table 6.6 retained in extract as comparison scaffold, not as concepts to memorize

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-heterogeneous-accelerators-observability-6-4-1.md`
- Chunks:
  - `processed/code/systems-performance-cpu-heterogeneous-accelerators-observability-6-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Heterogeneous execution splits a workload** into **host orchestration + device kernels**—end-to-end performance is bounded by **PCIe/bus**, **serialization**, and **device-local memory hierarchy**, not CPU cores alone ([[cross-component-interactions]], [[throughput-latency-metrics]]).
- (measurement) **Device observability is rarely the same toolchain as host PMCs**—SLO work must explicitly budget **second instrumentation plane** or accept **blind tail risk** ([[measurement-validity]], [[observability-vs-experimentation]]).
- (structure) **Throughput vs latency shape differs**: many **narrow SIMD lanes** at **lower clocks** favor **batchable parallel kernels**; CPU favors **branchy control**—this is a **placement** decision, not “GPU always faster” ([[throughput-latency-metrics]], [[resource-analysis-vs-workload-analysis]]).

## Application validation

- **Inference service**: GPU queue depth grows while CPU looks idle → optimize **H2D batching + stream sync**, not Python GIL first.

## Decision clarity

- **Decision**: choose **device-resident batching + fused kernels** over **more vCPU** when **Amdahl-serial segments and PCIe** dominate wall time.

## Concepts reused / refined / created

- Reused (structure): [[cross-component-interactions]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[cross-component-interactions]]
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[observability-vs-experimentation]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-pmc-register-budget-and-sku-variance-6-4-1]]
  - [[systems-performance-cpu-kernel-scheduler-functions-and-locality-6-4-2]]
