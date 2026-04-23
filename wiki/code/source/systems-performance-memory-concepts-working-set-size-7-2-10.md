# Systems Performance — Working set size (WSS) concept vs measurable RSS (7.2.10) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.2.10** — **WSS** as **frequently touched** footprint; **cache fit vs DRAM** vs **swap** regimes; **RSS proxy gap** and **experimental** estimation (forward refs)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-concepts-working-set-size-7-2-10.md`
- Chunks:
  - `processed/code/systems-performance-memory-concepts-working-set-size-7-2-10-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **WSS vs RSS**: RSS answers **resident pages**, not **temporal locality**—capacity plans for **cache sensitivity** need **experiments**, not one dashboard field ([[measurement-validity]], [[scientific-method]]).
- (structure) **Tiered performance**: WSS **below cache** vs **above DRAM** are different **latency regimes**—same as CPU chapter’s **locality vs pressure** story ([[resource-vs-implementation-bottleneck]], [[caching]], [[time-space-tradeoff]]).

## Application validation

- **“128G RAM but slow”** with **RSS ≪ DRAM**: suspect **working set >> cache** or **remote NUMA** before declaring **CPU bound**—validate with **miss/fault experiments**, not RSS alone.

## Decision clarity

- **Decision**: choose **WSS-style experiments (slowdown vs induced pressure)** over **RSS-only sizing** when **p99** depends on **whether hot data fits cache/DRAM** more than on **peak allocated bytes**.

## Concepts reused / refined / created

- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[scientific-method]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (mechanism): [[caching]]
- Reused (abstraction): [[time-space-tradeoff]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[measurement-validity]]
  - [[scientific-method]]
  - [[resource-vs-implementation-bottleneck]]
  - [[caching]]
  - [[time-space-tradeoff]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-concepts-demand-paging-7-2-3]]
  - [[systems-performance-cpu-on-chip-cache-hierarchy-and-llc-6-4-1]]
