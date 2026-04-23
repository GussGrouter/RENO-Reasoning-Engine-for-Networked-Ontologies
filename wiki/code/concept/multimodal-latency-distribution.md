# Multimodal latency distribution

- Tag: diagnosis

## Definition

A **multimodal latency distribution** has multiple “modes” (peaks), commonly because different execution paths or tiers produce distinct latency populations (e.g., cache hits vs cache misses, fast path vs slow path).

## Relation

- Role: diagnosis (a warning sign that averages and single summaries can mislead).
- Often indicates a structural split such as [[fast-path-slow-path]] or tiering via [[caching]], and motivates using [[latency-percentiles]] and visualization rather than only means.
- Rare extreme points may still exist within a mode; see [[latency-outliers]] when tail events matter.
- Can guide intervention selection in [[model-classify-intervene]] by focusing fixes on the slow mode’s causes.

## Links

- Source: [[systems-performance-multimodal-distributions-2-8-5]]
- Source: [[systems-performance-filesystems-ch8-ext4dist-histograms-8-6-13]]
- Source: [[systems-performance-filesystems-ch8-visualizations-8-6-18]]
- Source: [[systems-performance-filesystems-ch8-fio-8-7-2b]]
- Source: [[systems-performance-disks-ch9-concepts-time-scales-9-3-2]]
- Source: [[systems-performance-disks-ch9-methodology-performance-monitoring-9-5-3]]
- Source: [[systems-performance-disks-ch9-observability-biolatency-9-6-6]]
- Source: [[systems-performance-disks-ch9-visualizations-intro-line-9-7-1]]
- Source: [[systems-performance-disks-ch9-visualizations-latency-heatmap-9-7-3]]
- Related concepts:
  - [[caching]]
  - [[fast-path-slow-path]]
  - [[latency-percentiles]]
  - [[model-classify-intervene]]

