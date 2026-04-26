# Systems Performance — FS latency visualization (bimodal + heat map) (§8.6.18) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.18 Visualizations** — **bimodal latency** + **Figure 8.13** NFS/L2ARC story

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-visualizations-8-6-18.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-visualizations-8-6-18-chunk-000001.md`

## Extracted ideas (with classification)

- **Representation risk (measurement-validity):** collapsing a **bimodal** FS latency distribution to one number (mean/median/mode) misstates user experience; use **distribution or heat-map** views ([[latency-heatmap]], [[multimodal-latency-distribution]]).
- **Tier fills the gap:** secondary cache (**L2ARC**) can occupy latencies **between** DRAM-fast and rotational-cloud—a compositional story, not “faster disk” only ([[caching]]).

## Application validation

- **Dashboard median flat, users feel spikes:** switch to **heat map / percentiles**—median can sit in the **void between modes** on rotational backing stores.

## Decision clarity

- **Decision:** choose **latency heat maps or histograms** over **single-number FS latency KPIs** when **workloads are clearly cache-hit vs storage-miss split**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[latency-heatmap]], [[multimodal-latency-distribution]], [[metric-visualization]], [[caching]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[latency-heatmap]], [[multimodal-latency-distribution]], [[metric-visualization]], [[caching]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-ext4dist-histograms-8-6-13]], [[systems-performance-filesystems-ch8-zfs-arc-iostat-8-6-zfs]]
