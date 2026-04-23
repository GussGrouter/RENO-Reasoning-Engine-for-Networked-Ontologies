# Systems Performance — Disk-only analysis trap + latency op definition (§8.5.1–§8.5.2 open) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.5.1 Disk Analysis** + **§8.5.2 Latency Analysis** through the **definition of operation latency**, **stopping before Table 8.4** (**table omitted** here)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-disk-latency-analysis-open-8-5-1-2.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-disk-latency-analysis-open-8-5-1-2-chunk-000001.md`

## Extracted ideas (with classification)

- (scope / validity) **Disk-only troubleshooting** misses **logical vs physical I/O** divergence—valid for a historical “disk is always the slow path” world, misleading under large caches and rich FS semantics ([[systems-performance-filesystems-ch8-logical-physical-io-8-3-12]]).
- (representation) **Latency of “file system operations”** includes **non-read/write paths** (example: `sync(2)`); defining “I/O latency” as disk latency is often the wrong object.

## Application validation

- **Measurement-validity triage:** classify whether the probe observes **syscall-to-completion** time, **block-layer time**, or **device busy**—same English word “latency,” different populations (**representation + scope**).

## Decision clarity

- **Decision:** choose **end-to-end operation latency at the syscall/VFS boundary** over **disk adapter utilization** when **diagnosing intermittent stalls whose reproduction involves metadata or cache-heavy paths**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[latency-analysis]], [[resource-vs-implementation-bottleneck]], [[streetlight-anti-method]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[latency-analysis]], [[resource-vs-implementation-bottleneck]], [[streetlight-anti-method]], [[throughput-latency-metrics]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-logical-physical-io-8-3-12]], [[systems-performance-filesystems-ch8-methodology-intro-8-5]], [[systems-performance-filesystems-ch8-latency-layers-table-8-5-2a]]
