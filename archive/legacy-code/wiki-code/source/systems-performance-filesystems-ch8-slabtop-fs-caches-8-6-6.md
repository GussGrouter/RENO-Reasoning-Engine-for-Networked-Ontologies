# Systems Performance — slabtop: seeing FS-related kernel caches (§8.6.6) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.6 slabtop** (full table **omitted**; per-FS name list **shortened** in processed extract)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-slabtop-fs-caches-8-6-6.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-slabtop-fs-caches-8-6-6-chunk-000001.md`

## Extracted ideas (with classification)

- (representation) **Slab view** is a **different projection** of kernel memory than `free`: it exposes **named caches** (`dentry`, inode caches)—fit for “which metadata structures are swollen?” questions ([[measurement-validity]]).
- (scope note) **`/proc/slabinfo`** availability ties to kernel build options—missing file is itself a validity signal.

## Application validation

- **`dentry`/`inode` slabs huge** while app RSS looks fine: investigate **path churn / millions of tiny files** before resizing DRAM for the workload dataset.

## Decision clarity

- **Decision:** choose **slabtop classification** over **heap profiling in userspace** when **symptoms align with metadata cache pressure** (many paths, millions of inodes).

## Concepts reused / refined / created

- Reused: [[caching]], [[counters-statistics-metrics]], [[measurement-validity]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[caching]], [[counters-statistics-metrics]], [[measurement-validity]], [[cross-component-interactions]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-sar-cache-dentry-8-6-5]], [[systems-performance-filesystems-ch8-strace-syscall-latency-8-6-7]]
