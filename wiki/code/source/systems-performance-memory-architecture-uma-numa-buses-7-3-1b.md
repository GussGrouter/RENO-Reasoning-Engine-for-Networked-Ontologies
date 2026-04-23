# Systems Performance — UMA vs NUMA memory topology and buses (7.3.1) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.1** — **UMA vs NUMA** diagrams (narrative), **local vs remote** latency, **memory nodes**, **bus / interconnect** access patterns

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-architecture-uma-numa-buses-7-3-1b.md`
- Chunks:
  - `processed/code/systems-performance-memory-architecture-uma-numa-buses-7-3-1b-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Remote DRAM is extra hops**—the same instruction stream can satisfy **locality SLOs** or miss them depending on **placement policy**, not only GHz ([[cross-component-interactions]], [[throughput-latency-metrics]]).
- (measurement) **“Memory bandwidth test”** on the wrong socket/node answers a **different question** than production **thread+memory binding** ([[measurement-validity]]).
- (abstraction) **Functional diagram discipline** (“trace CPUs→memory”) is a **validity prerequisite** before trusting **A/B numbers** across machines ([[scientific-method]]-compatible triangulation).

## Application validation

- **Benchmark moved from dev laptop to NUMA server**: if p99 jumps, first check **node-local allocation** vs **accidental cross-node** before rewriting algorithms.

## Decision clarity

- **Decision**: choose **explicit first-touch / bind policies + node-local witnesses** over **socket-agnostic tuning** when **RSS fits in DRAM** but **tail latency** still scales with **socket count**.

## Concepts reused / refined / created

- Reused (structure): [[cross-component-interactions]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[scientific-method]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[cross-component-interactions]]
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[scientific-method]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-architecture-intro-dram-latency-7-3-1a]]
  - [[systems-performance-memory-architecture-ddr-multichannel-7-3-1c]]
