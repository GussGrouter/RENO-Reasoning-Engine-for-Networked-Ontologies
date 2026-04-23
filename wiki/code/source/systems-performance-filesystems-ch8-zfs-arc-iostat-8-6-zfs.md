# Systems Performance — ZFS pool I/O + ARC statistics (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **ZFS** subsection after **§8.6.17** — **`zpool iostat`** + **`arcstat.pl` / kstat**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-zfs-arc-iostat-8-6-zfs.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-zfs-arc-iostat-8-6-zfs-chunk-000001.md`

## Extracted ideas (with classification)

- **Layered cache observability:** pool throughput vs **ARC/L2ARC** hit accounting—ties cache sizing decisions to named counters ([[caching]], [[counters-statistics-metrics]]).

## Application validation

- **ARC hits fine but pool latency noisy:** split “**disk vs ARC miss path**” using **miss-class columns**, not only aggregate IOPS.

## Decision clarity

- **Decision:** choose **ARC + pool stats together** over **pool IOPS alone** when **read working set hovers near DRAM+L2ARC boundaries**.

## Concepts reused / refined / created

- Reused: [[caching]], [[counters-statistics-metrics]], [[time-series-monitoring]], [[systems-performance]]
- **Created:** none (pool product surface absorbed as **example channel** for cache concepts)

## Links

- Concepts: [[caching]], [[counters-statistics-metrics]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-visualizations-8-6-18]], [[systems-performance-filesystems-ch8-concept-caching-8-3-2]]
