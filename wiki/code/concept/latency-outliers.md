# Latency outliers

- Tag: diagnosis

## Definition

**Latency outliers** are rare extreme latency values that do not match the bulk of a distribution (unimodal or multimodal). They can dominate user-visible performance even when averages look healthy.

## Relation

- Role: diagnosis (a distribution pathology signal, not a single “number goes up” metric).
- Often requires distribution inspection (histograms, scatter plots) rather than relying on means alone (see [[multimodal-latency-distribution]] and [[latency-percentiles]]).
- Fits [[model-classify-intervene]] when deciding whether the dominant problem is tail latency vs typical-case latency.

## Links

- Source: [[systems-performance-outliers-2-8-6]]
- Source: [[systems-performance-filesystems-ch8-latency-presentation-drilldown-8-5-2b]]
- Source: [[systems-performance-filesystems-ch8-ext4slower-8-6-14]]
- Source: [[systems-performance-disks-ch9-intro-parts-terminology-9-1]]
- Source: [[systems-performance-disks-ch9-architecture-hdd-advanced-smr-ddc-9-4-1b]]
- Source: [[systems-performance-disks-ch9-visualizations-scatter-9-7-2]]
- Source: [[systems-performance-disks-ch9-exercises-scaffold-a-9-10a]]
- Source: [[systems-performance-network-ch10-architecture-protocols-tcp-dupacks-retransmits-tlp-10-4-1d]]
- Related concepts:
  - [[latency-percentiles]]
  - [[multimodal-latency-distribution]]
  - [[metric-visualization]]
  - [[model-classify-intervene]]
