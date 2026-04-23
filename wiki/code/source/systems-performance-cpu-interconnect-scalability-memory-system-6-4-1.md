# Systems Performance — CPU interconnect vs shared bus (6.4.1) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.4.1 — **Interconnects** (topology vs memory system; bus contention; private links; bandwidth math; coherency mode as a latency/bandwidth trade surface)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-interconnect-scalability-memory-system-6-4-1.md`
- Chunks:
  - `processed/code/systems-performance-cpu-interconnect-scalability-memory-system-6-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Interconnect topology couples to memory model (UMA vs NUMA)**—remote access and **coherency traffic** ride the same fabric story as “CPU interconnect” ([[cross-component-interactions]], [[throughput-latency-metrics]]).
- (diagnosis) **Shared bus contention** is a classic **scaling cliff**: adding sockets increases **serialization on a shared resource**—symptoms resemble **coherency + bandwidth** ceilings ([[universal-scalability-law]], [[resource-vs-implementation-bottleneck]]).
- (measurement) **Interconnect pressure** often shows up indirectly as **IPC collapse** on memory-related ops; treat vendor bandwidth tables as **capacity hints**, not root-cause labels ([[measurement-validity]], [[counters-statistics-metrics]]).

## Application validation

- **4-socket legacy vs mesh modern**: same “low CPU%” but higher **remote DRAM fraction** → validate **topology / hop count** before tuning app threads only.

## Decision clarity

- **Decision**: choose **fabric-aware placement (NUMA pinning)** over **socket count scale-out** when **remote memory + snoop** traffic tracks latency more than **core utilization**.

## Concepts reused / refined / created

- Reused (structure): [[cross-component-interactions]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[universal-scalability-law]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[cross-component-interactions]]
  - [[throughput-latency-metrics]]
  - [[universal-scalability-law]]
  - [[resource-vs-implementation-bottleneck]]
  - [[measurement-validity]]
  - [[counters-statistics-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-cache-coherency-latency-mmu-tlb-6-4-1]]
  - [[systems-performance-cpu-pmc-hardware-counter-programming-model-6-4-1]]
