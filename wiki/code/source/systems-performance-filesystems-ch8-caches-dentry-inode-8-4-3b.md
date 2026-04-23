# Systems Performance — Dentry + inode caches (§8.4.3 continued) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.4.3** (part B) — **Dcache** path walks (RCU-walk vs ref-walk), **negative caching**, **inode cache** scaling

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-caches-dentry-inode-8-4-3b.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-caches-dentry-inode-8-4-3b-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Path resolution is its own hot path**—metadata-light workloads can still spend CPU on **dcache/inode** structures ([[caching]], [[resource-vs-implementation-bottleneck]]).
- (measurement) **High path lookup rates** trigger **different scalability modes** (RCU-walk vs fallback)—**throughput cliffs** may be **implementation sensitivity**, not disk ([[measurement-validity]], [[throughput-latency-metrics]]).

## Application validation

- **Millions of `open`/`stat` on cold cache:** profile **dcache hit ratio** before blaming **disk latency**—**fix may be fewer path probes**, not faster arrays.

## Decision clarity

- **Decision:** choose **reducing path churn / caching negative lookups at app layer** over **NVMe upgrades** when **CPU + Dcache contention** dominate and **read bytes are tiny**.

## Concepts reused / refined / created

- Reused: [[caching]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[throughput-latency-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[caching]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[throughput-latency-metrics]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-fs-features-8-4-4]]
