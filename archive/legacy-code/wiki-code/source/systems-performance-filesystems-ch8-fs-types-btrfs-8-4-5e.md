# Systems Performance — btrfs COW + pooled FS/VM combined architecture (§8.4.5) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.4.5** — **btrfs** (**feature bullet list omitted** in processed extract)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-fs-types-btrfs-8-4-5e.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-fs-types-btrfs-8-4-5e-chunk-000001.md`

## Extracted ideas (with classification)

- (architecture pattern) **COW B-tree FS + volume manager**: same *class* of compositional tradeoffs as ZFS-style stacks (pooling, snapshots, growth), not a fresh decision frame.

## Application validation

- When planning **snapshots/clones-heavy** services on btrfs, reason about **COW write amplification under your object churn** using workload shapes, not just “same as ext4 tuning.”

## Concepts reused / refined / created

- Reused: [[cross-component-interactions]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[cross-component-interactions]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-fs-types-zfs-8-4-5d]], [[systems-performance-filesystems-ch8-volumes-pools-8-4-6]]
