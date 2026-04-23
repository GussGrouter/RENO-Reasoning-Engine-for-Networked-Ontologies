# Systems Performance — Ch.8 §8.8.2 ext4 (kernel defaults, tune2fs) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.8.2** — **2.6.30+** atime defaults, **ext4(5)**, **tune2fs**, **noatime** as I/O saver

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-ext4-defaults-tune2fs-8-8-2b.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-ext4-defaults-tune2fs-8-8-2b-chunk-000001.md`

## Extracted ideas (with classification)

- **Defaults move under you:** “**We need noatime**” may be **legacy** if **relatime** already matches needs—re-validate on **target kernel** ([[static-performance-tuning]]).
- **Measurement-validity (scope/semantics):** the **cost and correctness** of atime depend on **mount flag semantics** and **app expectations**, not the string “atime” in isolation.

## Application validation

- **Regression after mount change:** check **MAILDIR/mutt-class** workloads if moving between **strictatime**, **relatime**, and **noatime**.

## Decision clarity

- **Decision:** choose **measurement + app compatibility audit** over **cargo-cult noatime** when **baseline latency** is already dominated by something other than metadata writes.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[static-performance-tuning]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[static-performance-tuning]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-ext4-mount-man-atime-8-8-2a]], [[systems-performance-filesystems-ch8-ext4-sysfs-e2fsck-8-8-2c]]
