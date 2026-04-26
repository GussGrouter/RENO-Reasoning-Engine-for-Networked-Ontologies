# Systems Performance — Read-ahead label + write-back + sync writes (§8.3.5–§8.3.7) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.3.5–§8.3.7** — **readahead syscall** naming; **write-back buffering + flush**; reliability tradeoffs; **`O_SYNC` vs `fsync` batching**, archive unpack pauses

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-writeback-sync-8-3-5-7.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-writeback-sync-8-3-5-7-chunk-000001.md`

## Extracted ideas (with classification)

- (tradeoff) **Write-back completes at RAM copy**—**throughput feels high** until **flush / power-loss / fsync** exposes **persistence latency** ([[throughput-latency-metrics]], [[measurement-validity]]).
- (structure) **`fsync` checkpoints** amortize metadata work—**latency shifts** from steady state to **commit points** ([[latency-analysis]], [[throughput-latency-metrics]]).

## Application validation

- **DB “random write” slow:** check **`fsync` frequency** vs **group commit** settings—measuring **write syscall return** alone **misstates** durability story.

## Decision clarity

- **Decision:** choose **end-to-end durability metrics (commit latency, journal flush intervals)** over **async write throughput** when **the SLO includes crash safety or cross-NFS correctness**.

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[measurement-validity]], [[latency-analysis]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[measurement-validity]], [[latency-analysis]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-direct-async-mmap-meta-8-3-8-11]]
