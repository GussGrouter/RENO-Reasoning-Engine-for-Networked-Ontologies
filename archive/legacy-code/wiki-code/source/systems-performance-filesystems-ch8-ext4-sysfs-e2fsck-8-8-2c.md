# Systems Performance — Ch.8 §8.8.2 ext4 (`/sys/fs/ext4`, docs, e2fsck) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.8.2** — **`/sys/fs/ext4/<dev>`**, kernel **ext4** docs, **`e2fsck -D`**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-ext4-sysfs-e2fsck-8-8-2c.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-ext4-sysfs-e2fsck-8-8-2c-chunk-000001.md`

## Extracted ideas (with classification)

- **Live introspection:** sysfs exposes **per-filesystem** tunables and counters—**discoverability** beats memorizing names; **documentation** defines which knobs are safe to move in production ([[static-performance-tuning]]).
- **Maintenance vs tuning:** **`e2fsck -D`** is a **heavyweight** directory reindex pass—not a substitute for fixing **application access patterns**.

## Application validation

- **`inode_readahead_blks`:** interpret through **kernel docs**—changing read-ahead affects **metadata-heavy** workloads (lots of **`readdir`/inode scans**), not streaming throughput alone.

## Decision clarity

- **Decision:** choose **kernel ext4.rst + sysfs discovery** over **guesswork** when **changing a sysfs knob** whose default came from **mount-time geometry and workload archetype** you did not measure.

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[scientific-method]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[scientific-method]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-ext4-defaults-tune2fs-8-8-2b]]
