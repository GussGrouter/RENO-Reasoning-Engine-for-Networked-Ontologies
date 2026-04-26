# Systems Performance — hardware counters / PMC fundamentals (4.3.9) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.3.9 opening (PMC roles, architectural sets, interfaces, counting vs sampling)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-pmc-fundamentals-4-3-9.md`
- Chunks:
  - `processed/code/systems-performance-pmc-fundamentals-4-3-9-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Hardware performance counters expose **cycle- and microarchitecture-level** facts (IPC/CPI proxies, cache interaction, stalls) that pure software counters cannot substitute—deciding CPU efficiency vs memory vs branch behavior leans on PMC-class signals.
- (abstraction) **Multiplexing constraint**: only a handful of counters can be armed simultaneously; broad studies require either prioritizing a small simultaneous set or **rotating** measurements across windows (a planning tradeoff in any constrained sensor budget, not only CPUs).
- (measurement) Modes split into **counting** (aggregate with very low perturbation) versus **overflow sampling** (interrupt-driven attribution to instruction context). The choice mirrors “how much vs where” priorities from [[counters-statistics-metrics]] and [[sampling-based-profiling]].

## Concepts reused / refined / created

- Reused (measurement): [[counters-statistics-metrics]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (structure): [[kernel-user-boundary]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[counters-statistics-metrics]]
  - [[sampling-based-profiling]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[kernel-user-boundary]]
  - [[systems-performance]]
