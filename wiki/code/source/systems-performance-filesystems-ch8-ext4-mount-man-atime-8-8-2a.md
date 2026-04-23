# Systems Performance — Ch.8 §8.8.2 ext4 (four levers, mount excerpt) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.8.2** open — **mount / tune2fs / sysfs / e2fsck**; **man mount** atime family (transcript omitted)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-ext4-mount-man-atime-8-8-2a.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-ext4-mount-man-atime-8-8-2a-chunk-000001.md`

## Extracted ideas (with classification)

- **Configuration surface area:** ext4 tuning is **not** one switch—**mount**, **tune2fs**, **sysfs**, and **maintenance tools** each change different **persistence and risk** profiles ([[static-performance-tuning]]).
- **atime family:** **atime / noatime / relatime** connect **read** paths to **metadata write** volume; always read **current** `mount(8)` for your kernel.

## Application validation

- **“News spool” noatime lore:** verify **app** still compatible with **relatime** defaults on modern kernels before hard-tuning.

## Decision clarity

- **Decision:** choose **noatime/relatime** over **strict atime** when **read-heavy** and **no correct app** depends on **precise per-read atime** on that mount.

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[throughput-latency-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[throughput-latency-metrics]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-ext4-defaults-tune2fs-8-8-2b]], [[systems-performance-filesystems-ch8-mount-free-8-6-1-2]]
