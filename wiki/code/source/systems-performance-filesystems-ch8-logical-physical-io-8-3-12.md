# Systems Performance — Logical vs. physical I/O (§8.3.12) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.3.12** — mismatch families + **1-byte write** amplification example (classification bullets **omitted** in processed extract)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-logical-physical-io-8-3-12.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-logical-physical-io-8-3-12-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Logical syscall/stream ≠ disk footprint**—same app event can shrink, enlarge, defer, or redirect device work ([[measurement-validity]], [[resource-vs-implementation-bottleneck]]).
- (scope) **Multi-tenant / admin / scrub** traffic can dominate **disks** while **your** `read(2)` latency stays cache-bound ([[cross-component-interactions]], [[measurement-validity]]).

## Application validation

- **Disk queue deep but app p99 flat:** classify whether bytes are **unrelated/indirect flush** before resizing arrays—use **per-process/block-layer attribution**, not aggregate IOPS alone.

## Decision clarity

- **Decision:** choose **logical-operation latency + workload attribution tracing** over **disk-device saturation charts** when **deciding if storage scaling fixes user-visible stalls**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[cross-component-interactions]], [[throughput-latency-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[cross-component-interactions]], [[throughput-latency-metrics]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-ops-not-equal-8-3-13]]
