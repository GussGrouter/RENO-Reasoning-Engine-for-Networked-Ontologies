# Systems Performance — Cache coherency costs, latency ladder, MMU/TLB (6.4.1 tail) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.4.1 — post–Table 6.3 commentary through **MMU** (shared caches, coherency penalties, experimental latency steps, address translation)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-cache-coherency-latency-mmu-tlb-6-4-1.md`
- Chunks:
  - `processed/code/systems-performance-cpu-cache-coherency-latency-mmu-tlb-6-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) **Coherency is a multi-socket design constraint**: modifying memory forces **invalidation / ownership traffic** on shared lines—LLC access cost depends on **sharing state**, not only hit/miss ([[caching]], [[resource-vs-implementation-bottleneck]]).
- (measurement) **Latency “steps”** in controlled scans reveal **which hierarchy level** you exceeded—use as an **experimental complement** to counter-based attribution ([[micro-benchmarking]], [[measurement-validity]]).
- (mechanism) **MMU + TLB** sit on the hot path for every translated access; **hardware vs software table walk** changes the cost model for “pointer chasing” workloads ([[kernel-user-boundary]], [[throughput-latency-metrics]]).

## Application validation

- **Multi-writer hot struct**: rising LLC cycles without rising DRAM bandwidth → suspect **line bouncing / false sharing** before blaming “slow RAM.”

## Decision clarity

- **Decision**: choose **layout / partition-by-socket** remediation over **more DRAM channels** when profiles show **coherency-shaped LLC penalties** on shared lines.

## Concepts reused / refined / created

- Reused (mechanism): [[caching]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (heuristic): [[micro-benchmarking]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[universal-scalability-law]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[caching]]
  - [[resource-vs-implementation-bottleneck]]
  - [[micro-benchmarking]]
  - [[measurement-validity]]
  - [[kernel-user-boundary]]
  - [[throughput-latency-metrics]]
  - [[universal-scalability-law]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-on-chip-cache-hierarchy-and-llc-6-4-1]]
  - [[systems-performance-cpu-interconnect-scalability-memory-system-6-4-1]]
