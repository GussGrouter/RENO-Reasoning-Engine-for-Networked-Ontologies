# Systems Performance — Ch.8 §8.8.3 ZFS tuning (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.8.3** — **`zfs get`/`set`**, Table 8.10 (paraphrased), **recordsize**, **ARC/L2ARC**, **logbias**, **sync**, **TXG** tunables

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-zfs-tuning-properties-8-8-3.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-zfs-tuning-properties-8-8-3-chunk-000001.md`

## Extracted ideas (with classification)

- **Shape vs policy:** **`recordsize`** aligns **zfs block granularity** with **application I/O**; **`primarycache`/`secondarycache`** steer **tier pollution** ([[caching]], [[cache-tuning]], [[time-space-tradeoff]]).
- **Durability vs placement:** **`logbias`** and **`sync`** sit on the **latency–throughput–correctness** frontier for sync writes—not interchangeable “performance boosts” ([[throughput-latency-metrics]], [[queueing-theory]] for TXG contention).
- **Measurement-validity (scope/semantics):** interpreting **`recordsize`** without **object size distribution** mistakes **allocation behavior** for “slow disks.”

## Application validation

- **Small random writes on default 128 KiB:** expect **amplification**; validate with **dataset** + **pool** latency and **write** histograms—not aggregate IOPS alone.

## Decision clarity

- **Decision:** choose **`primarycache=metadata`** (or **`none`**) over **`all`** on **archive/backfill datasets** when **ARC pollution** steals RAM from **latency-sensitive** tenants sharing the pool.

## Concepts reused / refined / created

- Reused: [[caching]], [[cache-tuning]], [[static-performance-tuning]], [[throughput-latency-metrics]], [[time-space-tradeoff]], [[queueing-theory]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[caching]], [[cache-tuning]], [[static-performance-tuning]], [[throughput-latency-metrics]], [[time-space-tradeoff]], [[queueing-theory]], [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-zfs-arc-iostat-8-6-zfs]], [[systems-performance-filesystems-ch8-fs-types-zfs-8-4-5d]]
