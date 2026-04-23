# Systems Performance — Memory architecture intro, DRAM, CAS latency (7.3 + 7.3.1 open) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3** framing + **§7.3.1** — **DRAM role**, **scale**, **CAS-style latency** vs **cache hits**, **UMA** preview (through SMP)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-architecture-intro-dram-latency-7-3-1a.md`
- Chunks:
  - `processed/code/systems-performance-memory-architecture-intro-dram-latency-7-3-1a-chunk-000001.md`

## Extracted ideas (with classification)

- (tradeoff) **DRAM vs SRAM-class latency** is the recurring **fast small vs slow large** axis for where hot state should live ([[memory-technology-tradeoff]], [[throughput-latency-metrics]]).
- (structure) **Pooled instances** change **coherency / traffic** economics even when **per-VM DRAM** looks small—**composition** dominates at fleet scale ([[cross-component-interactions]]).
- (measurement) **Quoting “~10–20ns DRAM”** without **cache hierarchy + NUMA hop** context is a **scope error** for end-to-end latency claims ([[measurement-validity]]).

## Application validation

- **Edge inference “memory bound”** from a microbench **DRAM latency figure**: first state whether **L3 hit vs local DRAM vs remote NUMA** is the population your SLO actually exercises.

## Decision clarity

- **Decision**: choose **topology-aware memory benchmarks + fleet coherency cost** over **single-stick CAS marketing numbers** when sizing **distributed in-memory** capacity.

## Concepts reused / refined / created

- Reused (tradeoff): [[memory-technology-tradeoff]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[cross-component-interactions]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[memory-technology-tradeoff]]
  - [[throughput-latency-metrics]]
  - [[cross-component-interactions]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-architecture-uma-numa-buses-7-3-1b]]
