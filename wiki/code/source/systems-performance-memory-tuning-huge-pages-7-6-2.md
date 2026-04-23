# Systems Performance — Huge / transparent huge pages (§7.6.2) (PDF scout 381–400)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.6.2** — **multiple page sizes**, hugetlbfs / mmap flags, **THP** automatic promotion

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p381-400.txt`
- Converted slice: `processed/code/systems-performance-memory-tuning-huge-pages-7-6-2.md`
- Chunks: `processed/code/systems-performance-memory-tuning-huge-pages-7-6-2-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Larger pages extend TLB reach**—benefit ties to **working set shape** and **fault behavior**, not “always on” ([[measurement-validity]], [[resource-vs-implementation-bottleneck]]).
- (risk) **THP carried historical latency caveats**—decisions must reference **kernel generation + workload**, not folklore ([[measurement-validity]], [[static-performance-tuning]]).

## Application validation

- **Database micro-benchmark improves with huge pages:** confirm production **fragmentation + NUMA placement** matches the lab—otherwise **representation** of the gain collapses.

## Decision clarity

- **Decision:** choose **explicit huge-page allocation paths (hugetlbfs / mapped pools)** over **relying on THP defaults** when **tail latency regressions** were previously traced to **THP/compaction interactions** on your **kernel vintage**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[static-performance-tuning]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[static-performance-tuning]], [[systems-performance]]
- Related sources: [[systems-performance-memory-tuning-allocators-7-6-3]]
