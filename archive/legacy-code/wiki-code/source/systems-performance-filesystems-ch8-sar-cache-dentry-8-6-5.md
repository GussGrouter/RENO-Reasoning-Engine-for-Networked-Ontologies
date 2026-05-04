# Systems Performance — sar -v directory cache + file handle pressure (§8.6.5) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.5 sar** — `sar -v` **dentry / file / inode** pressure + **-r** buffer/page cache sizes (sample **omitted**)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-sar-cache-dentry-8-6-5.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-sar-cache-dentry-8-6-5-chunk-000001.md`

## Extracted ideas (with classification)

- (semantics) **dentunusd** reports directory-entry cache **unused** entries; **file-nr** / **inode-nr** track **open handles / inodes**—together they expose **namespace pressure** in the same long-horizon tool as other `sar` series without enabling a syscall trace.
- (cross-link) **-r** path recapitulates **kbbuffers / kbcached** for people who already run `sar` for storage work.

## Application validation

- **Spikes in file handle or inode columns** while CPU is “idle” in the app: check for **runaway open files** or **metadata storms** before buying more CPU.

## Decision clarity

- **Decision:** choose **historical `sar` file / dentry / inode series** over **one-off strace** when **the question is week-scale growth of metadata cache objects** and you need **low-perturbation** baselines.

## Concepts reused / refined / created

- Reused: [[counters-statistics-metrics]], [[time-series-monitoring]], [[cross-component-interactions]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[counters-statistics-metrics]], [[time-series-monitoring]], [[cross-component-interactions]], [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-top-vmstat-8-6-3-4]], [[systems-performance-filesystems-ch8-slabtop-fs-caches-8-6-6]]
