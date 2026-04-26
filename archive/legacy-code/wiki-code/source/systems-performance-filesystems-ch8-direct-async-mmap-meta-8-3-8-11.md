# Systems Performance — Direct/raw, async I/O, mmap, metadata layers (§8.3.8–§8.3.11) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.3.8–§8.3.11** — **raw vs direct I/O**, **non-blocking / aio / io_uring**, **mmap** tradeoffs & TLB shootdowns, **logical vs physical metadata** workload mix

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-direct-async-mmap-meta-8-3-8-11.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-direct-async-mmap-meta-8-3-8-11-chunk-000001.md`

## Extracted ideas (with classification)

- (decision) **Bypassing FS cache** trades **double management** in the app vs **kernel cache policy**—**representation of “fast” changes** ([[resource-vs-implementation-bottleneck]], [[measurement-validity]]).
- (perturbation) **mmap** can be dominated by **disk latency**, not syscall cost—**micro-optimizing mapping** without I/O diagnosis is mis-layered ([[resource-vs-implementation-bottleneck]]).
- (scope) **Metadata-heavy workloads** (`stat`-bound) differ from **data throughput** stories—different **bottleneck class** ([[throughput-latency-metrics]], [[cross-component-interactions]]).

## Application validation

- **Riak mmap mode:** if p99 latency is disk-bound, **syscall removal** alone won’t move **SLO**—validate **device queue + cache** first.

## Decision clarity

- **Decision:** choose **proving disk/FS path dominance with latency stacks** over **switching to mmap/direct I/O by default** when **measured syscall overhead is negligible** vs **device service time**.

## Concepts reused / refined / created

- Reused: [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]
