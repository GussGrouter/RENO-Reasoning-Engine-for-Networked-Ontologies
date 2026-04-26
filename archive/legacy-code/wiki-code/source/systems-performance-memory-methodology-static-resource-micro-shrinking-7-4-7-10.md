# Systems Performance — Static tuning, resource controls, micro-benchmarking, shrinking (7.4.7–7.4.10) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.4.7–7.4.10** — **static tuning knobs**, **cgroups/memory QoS**, **allocator micro-benchmark caveats**, **shrinking footprint** tactics

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-methodology-static-resource-micro-shrinking-7-4-7-10.md`
- Chunks:
  - `processed/code/systems-performance-memory-methodology-static-resource-micro-shrinking-7-4-7-10-chunk-000001.md`

## Extracted ideas (with classification)

- (decision) **Static tuning without workload proof** risks tuning **symptoms on the wrong plane**—pair each knob with **who pays** under **quota/limit semantics** ([[static-performance-tuning]], [[measurement-validity]], [[cross-component-interactions]]).
- (measurement) **Allocator micro-benchmarks invert under fragmentation + concurrency**—keep claims scoped to **representation tested** ([[micro-benchmarking]], [[measurement-validity]], [[throughput-latency-metrics]]).

## Application validation

- **Raise vm.swappiness** after seeing swap thrash: confirm **whether caps/cgroups already enforce eviction**—otherwise you tune **kernel reclaim policy on the wrong isolation layer**.

## Decision clarity

- **Decision**: choose **limit/quota observability first** over **kernel VM sysctl sweeps** when **saturation correlates with cgroup pressure**, not global free memory.

## Concepts reused / refined / created

- Reused (decision): [[static-performance-tuning]]
- Reused (structure): [[cross-component-interactions]]
- Reused (measurement): [[micro-benchmarking]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[observability-vs-experimentation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[static-performance-tuning]]
  - [[cross-component-interactions]]
  - [[micro-benchmarking]]
  - [[measurement-validity]]
  - [[throughput-latency-metrics]]
  - [[observability-vs-experimentation]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-methodology-use-method-7-4-2]]
