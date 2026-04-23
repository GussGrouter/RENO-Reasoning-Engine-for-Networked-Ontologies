# Latency heat map

- Tag: measurement

## Definition

A **latency heat map** visualizes latency distributions over time (or another x-axis) by quantizing the x/y plane into buckets and coloring each bucket by event density, making multimodal structure and sparse outliers readable at scale.

## Relation

- Role: measurement (a visualization-backed statistic view, not a single scalar “average latency”).
- Complements scatter plots when point overlap becomes unreadable; highlights sparse high-latency regions as visually distinct blocks.
- Pairs naturally with [[metric-visualization]] for interpretation workflow, and with [[multimodal-latency-distribution]] / [[latency-outliers]] for diagnosis.

## Links

- Source: [[systems-performance-heat-maps-2-10-3]]
- Source: [[systems-performance-cpu-interrupt-gpu-tools-and-distribution-visualizations-6-6-19-6-7-4]]
- Source: [[systems-performance-filesystems-ch8-latency-presentation-drilldown-8-5-2b]]
- Source: [[systems-performance-filesystems-ch8-ext4dist-histograms-8-6-13]]
- Source: [[systems-performance-filesystems-ch8-visualizations-8-6-18]]
- Source: [[systems-performance-disks-ch9-visualizations-latency-heatmap-9-7-3]]
- Source: [[systems-performance-disks-ch9-visualizations-offset-heatmap-9-7-4]]
- Related concepts:
  - [[metric-visualization]]
  - [[multimodal-latency-distribution]]
  - [[latency-outliers]]
  - [[latency-percentiles]]
