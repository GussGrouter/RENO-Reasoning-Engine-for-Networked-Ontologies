# Systems Performance — Latency summaries, outliers, drill-down (§8.5.2) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.5.2** — layer tooling ladder + **averages vs distributions** + drill-down pointer

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-latency-presentation-drilldown-8-5-2b.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-latency-presentation-drilldown-8-5-2b-chunk-000001.md`

## Extracted ideas (with classification)

- (representation) **Interval averages vs full distributions:** with **>99% cache hits**, means can track **hit latency** and **hide rare slow misses**—outline investigation needs **histograms / heat maps / per-op lists** ([[latency-heatmap]] practice in §8.6 cross-ref).
- (method) Once a slow region is visible, **drill-down** inside the FS stack follows—same loop as generic [[drill-down-analysis]], different probes.

## Application validation

- **Dashboard mean flat, users angry:** verify you are not **over-aggregating** cache hits with long misses; promote to **distribution or high-percentile views** before resizing disks.

## Decision clarity

- **Decision:** choose **histogram/percentile or per-operation traces** over **per-interval means** when **hit rate is extremely high** but **tail episodes still matter**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[latency-outliers]], [[latency-percentiles]], [[drill-down-analysis]], [[latency-analysis]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[latency-outliers]], [[latency-percentiles]], [[drill-down-analysis]], [[latency-analysis]], [[metric-visualization]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-latency-layers-table-8-5-2a]], [[systems-performance-filesystems-ch8-transaction-cost-fs-8-5-2c]]
