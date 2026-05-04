# Systems Performance — FFS and the original Unix layout (§8.4.5) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.4.5** opening — **FFS** narrative (figures referenced only in PDF)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-fs-types-ffs-8-4-5a.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-fs-types-ffs-8-4-5a-chunk-000001.md`

## Extracted ideas (with classification)

- (behavior over lifetime) **Randomizing free-block allocation** turns sequential layouts into seek-heavy placement—the historical Unix excerpt quantifies throughput collapse over weeks (same nominal disk bandwidth).
- (design axis) **FFS locality**: cylinder groups + larger minimum blocks + fragments trade metadata vs throughput and reduce seeks versus the inode/table split layout.
- (hardware-era tactic) **Rotational interleaving** inserts spacing so the CPU/kernel can issue the next sequential read before the sector passes the head—latency coupling across layers, not just “faster disk.”

## Application validation

- **“It was fast at format time, now it’s slow”:** consider **allocation structure aging** and **metadata free-list state**, not only device error rates or fill factor in the capacity sense.

## Decision clarity

- **Decision:** choose **file-system–level layout/fragmentation analysis (or informed reformat/migration strategies)** over **raw device benchmark reruns** when **workload is seek-dominated and the system has a long service history** (the signal is *where* blocks ended up, not whether the disk’s spec changed).

## Concepts reused / refined / created

- Reused: [[resource-vs-implementation-bottleneck]], [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none (mechanism history; catalog of other FS types continues in following sources)

## Links

- Concepts: [[resource-vs-implementation-bottleneck]], [[throughput-latency-metrics]], [[cross-component-interactions]], [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-fs-features-8-4-4]], [[systems-performance-filesystems-ch8-fs-types-ext-8-4-5b]]
