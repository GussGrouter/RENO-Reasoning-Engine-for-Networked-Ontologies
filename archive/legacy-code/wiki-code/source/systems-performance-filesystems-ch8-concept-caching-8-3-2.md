# Systems Performance — FS caching & free memory (§8.3.2) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.3.2** — cache grows / “free” shrinks; **Table 8.1 omitted**; references Ch.3 **full cache list**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-concept-caching-8-3-2.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-concept-caching-8-3-2-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Page cache reclaim is normal**—“low free RAM” often means **useful cache**, not leak ([[caching]], [[measurement-validity]]).
- (structure) **Read cache vs write buffer**—different invalidation and risk profiles ([[caching]], [[throughput-latency-metrics]]).

## Application validation

- **Paging alarms while FS throughput high:** distinguish **reclaimable cache pressure** from **anonymous memory pressure** before calling it an OOM scenario.

## Decision clarity

- **Decision:** choose **cache hit ratio / logical latency evidence** over **free-memory headline metrics** when **deciding if FS caching is helping or masking disk limits**.

## Concepts reused / refined / created

- Reused: [[caching]], [[measurement-validity]], [[throughput-latency-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[caching]], [[measurement-validity]], [[throughput-latency-metrics]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-random-prefetch-8-3-3-4]]
