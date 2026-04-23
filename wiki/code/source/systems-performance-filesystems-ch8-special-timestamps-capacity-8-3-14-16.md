# Systems Performance — Special FS, timestamps, capacity (§8.3.14–§8.3.16) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.3.14–§8.3.16** — **pseudo file systems**, **atime metadata write tax**, **full-pool / fragmentation** slowdowns

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-special-timestamps-capacity-8-3-14-16.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-special-timestamps-capacity-8-3-14-16-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **atime turns reads into metadata write load**—workload shape changes **layer of bottleneck** ([[throughput-latency-metrics]], [[measurement-validity]], [[caching]]).
- (resource) **High utilization / fragmentation** shifts cost to **allocation path**—different from bandwidth ceilings ([[resource-vs-implementation-bottleneck]], [[throughput-latency-metrics]]).

## Application validation

- **Web server stat storm + disk write load:** test **relatime/noatime** before buying SSDs—**representation** of “read-only” workload may be wrong.

## Decision clarity

- **Decision:** choose **mount/atime policy + inode write batching review** over **horizontal storage scale-out** when **metrics show metadata write amplification** dominating **data throughput**.

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[measurement-validity]], [[caching]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[measurement-validity]], [[caching]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-architecture-intro-stack-8-4-1]]
