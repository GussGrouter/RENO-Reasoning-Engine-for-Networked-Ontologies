# Systems Performance — Table 8.5 benchmark expectations — honesty about logical vs physical I/O (§8.5.8 tail) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.5.8** conclusion — **Table 8.5** (**grid summarized** in processed extract) + misleading-benchmark warning + **direct I/O still touches FS**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-table-8-5-expectations.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-table-8-5-expectations-chunk-000001.md`

## Extracted ideas (with classification)

- (representation / scope) **Same benchmark name, different dominant layer:** tiny **WSS** vs RAM yields cache-shaped numbers; **direct I/O** shifts claims toward disks; large random reads split cache vs disk—each row answers a **different experimental question** ([[measurement-validity]], [[micro-benchmarking]]).
- (semantics) **“Disk benchmark” using tiny files** often measures **cache / logical path**, not platters or NAND ([[systems-performance-filesystems-ch8-logical-physical-io-8-3-12]]).
- (boundary) Even **O_DIRECT** benchmarks still pay **FS mapping/code-path** costs—the measured object is “device via FS,” not raw elevator curves.

## Application validation

- Before trusting vendor GB/s: classify whether the published recipe fixes **WSS**, **cache state**, **write sync semantics**, and **read pattern**—otherwise you may compare **DRAM curves** to someone else’s **disk curves**.

## Decision clarity

- **Decision:** choose **explicit WSS + cold/warm disclosure + logical-vs-physical labeling** over **headline throughput numbers** when **deciding hardware sizing from microbench scripts**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[micro-benchmarking]], [[observability-vs-experimentation]], [[throughput-latency-metrics]], [[caching]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[micro-benchmarking]], [[observability-vs-experimentation]], [[streetlight-anti-method]], [[throughput-latency-metrics]], [[caching]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-cache-separation-microbench-8-5-6-8]], [[systems-performance-filesystems-ch8-obs-tools-intro-8-6]]
