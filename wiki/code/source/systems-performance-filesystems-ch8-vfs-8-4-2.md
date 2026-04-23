# Systems Performance — VFS (§8.4.2) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.4.2** — **VFS** as common measurement/observability **locus**; on-disk vs in-memory object name collision **semantics**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-vfs-8-4-2.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-vfs-8-4-2-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **`inode`/`superblock` wording can mean VFS objects or on-disk structs**—**representation** drift breaks cross-team RCA ([[measurement-validity]]).
- (structure) **VFS as choke point** for comparing FS implementations under similar workloads ([[kernel-architecture-models]], [[resource-vs-implementation-bottleneck]]).

## Application validation

- **Docs say “inode storm”:** confirm whether speakers mean **`struct inode` churn**, **ext4 on-disk inode writes**, or **POSIX stat traffic**—align words before tuning.

## Decision clarity

- **Decision:** choose **explicit VFS vs FS-specific counter names** over **hand-wavy “metadata”** when **two teams disagree on bottleneck layer**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[kernel-architecture-models]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[kernel-architecture-models]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-caches-page-flush-8-4-3a]]
