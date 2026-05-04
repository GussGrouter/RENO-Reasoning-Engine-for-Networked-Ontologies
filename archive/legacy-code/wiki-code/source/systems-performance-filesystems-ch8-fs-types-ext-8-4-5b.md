# Systems Performance — ext2/3/4 lineage (§8.4.5) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.4.5** — **ext** family overview (**per-feature bullet grids + sysfs examples omitted** in processed extract)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-fs-types-ext-8-4-5b.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-fs-types-ext-8-4-5b-chunk-000001.md`

## Extracted ideas (with classification)

- (history / scope) **ext** evolves by stacking generic FS mechanisms already discussed abstractly (**journaling**, **growth**, **extent-like placement**)—the Linux-specific bullets are largely an implementation index, not new decision primitives.

## Application validation

- Before tuning **ext*-specific knobs**, reconcile claims with **§8.4.4 features** (journal semantics, extents, allocator behavior)—avoid treating sysfs flags as goals without an end-to-end latency/throughput hypothesis.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[systems-performance]]
- **Created:** none (catalog absorbed by [[systems-performance-filesystems-ch8-fs-features-8-4-4]] abstractions)

## Links

- Concepts: [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-fs-features-8-4-4]], [[systems-performance-filesystems-ch8-fs-types-xfs-8-4-5c]]
