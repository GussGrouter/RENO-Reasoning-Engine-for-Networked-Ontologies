# Systems Performance — Random vs sequential + prefetch (§8.3.3–§8.3.4) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.3.3–§8.3.4** — access pattern semantics, **fragmentation**, **prefetch / read-ahead** benefits and **cache pollution** when detection misfires

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-random-prefetch-8-3-3-4.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-random-prefetch-8-3-3-4-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Logical sequential stream can become physical random** under fragmentation—**pattern labels must match the plane** measured ([[measurement-validity]], [[resource-vs-implementation-bottleneck]]).
- (tradeoff) **Prefetch reduces latency when prediction matches**; **mis-prefetch wastes bandwidth + cache**, hurting unrelated workloads ([[caching]], [[throughput-latency-metrics]]).

## Application validation

- **Flash vs HDD tuning:** aggressive prefetch helps **rotational latency amortization** more than **random-read NVMe**—don’t cargo-cult prefetch depth.

## Decision clarity

- **Decision:** choose **prefetch/read-ahead tuning experiments** over **block-size changes** when **workload is provably sequential** but **physical layout is already contiguous** and **misses dominate**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[caching]], [[throughput-latency-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[caching]], [[throughput-latency-metrics]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-writeback-sync-8-3-5-7]]
