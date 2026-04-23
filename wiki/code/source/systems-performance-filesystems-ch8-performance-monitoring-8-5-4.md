# Systems Performance — File system performance monitoring (§8.5.4) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.5.4 Performance Monitoring** — rate + latency as core pair; Linux gap noted

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-performance-monitoring-8-5-4.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-performance-monitoring-8-5-4-chunk-000001.md`

## Extracted ideas (with classification)

- (representation) Pair **operation rate** (load) with **latency** (outcome); when “good/bad” is unclear, **calibrate** with **known cache-hit vs cache-miss** micro-workloads ([[micro-benchmarking]]) as probes—not as production truth.
- (distribution) Prefer **histogram/heat-map** views when hunting **outliers**, not only per-second averages and stddev.
- (scope gap) **Linux often lacks ready per-FS-op stats** locally—**nfsstat**-class paths are exceptions; dashboard green may mean **missing telemetry**, not health ([[measurement-validity]]).

## Application validation

- **No FS op counters in `/proc`:** avoid declaring “FS is fine” from disk charts alone—use **syscall/VFS tracing** or **app-level metrics** deliberately.

## Decision clarity

- **Decision:** choose **syscall-level or NFS-specific counters** over **assuming generic OS “file system dashboards” exist** when **you are on Linux** and **need FS op breakdowns**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[counters-statistics-metrics]], [[micro-benchmarking]], [[latency-outliers]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[counters-statistics-metrics]], [[micro-benchmarking]], [[latency-outliers]], [[time-series-monitoring]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-workload-char-advanced-8-5-3b]], [[systems-performance-filesystems-ch8-static-tuning-fs-8-5-5]]
