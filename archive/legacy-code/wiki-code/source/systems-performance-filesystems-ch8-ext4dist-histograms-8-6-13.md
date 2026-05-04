# Systems Performance — ext4dist / *dist histograms (§8.6.13) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.13** — FS-internal latency **histograms** (`ext4dist`, xfs/zfs/btrfs/nfs variants); ASCII output trimmed

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-ext4dist-histograms-8-6-13.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-ext4dist-histograms-8-6-13-chunk-000001.md`

## Extracted ideas (with classification)

- **Bi-modal reads:** sub-20 µs cluster vs hundreds of µs—**two populations** on one op name ([[multimodal-latency-distribution]], [[latency-heatmap]] as visualization path).
- **Prefer FS layer before disk tools:** applications may not block on raw device latency; **logical** traces align with user stalls per [[systems-performance-filesystems-ch8-logical-physical-io-8-3-12]].

## Application validation

- **Disk `iostat` ugly but app fine:** confirm with `*dist` whether work is **cache-fast** vs **backing-store slow** before array changes.

## Decision clarity

- **Decision:** choose **`*dist` at the FS type** over **Chapter 9 disk latency first** when **isolating user-visible FS operations** vs **storage fabric** matters for the investigation.

## Concepts reused / refined / created

- Reused: [[latency-analysis]], [[multimodal-latency-distribution]], [[latency-heatmap]], [[extended-bpf]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[latency-analysis]], [[multimodal-latency-distribution]], [[latency-heatmap]], [[extended-bpf]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-logical-physical-io-8-3-12]], [[systems-performance-filesystems-ch8-ext4slower-8-6-14]]
