# Timeline waterfall chart

- Tag: measurement

## Definition

A **timeline waterfall chart** (often called a waterfall chart in browser tooling) shows activities as horizontal bars on a timeline, decomposing a duration into subcomponents (e.g., DNS, connect, wait/TTFB, receive) and revealing dependencies between sequential work.

## Relation

- Role: measurement (a structured visualization of where time goes within an interval).
- Analogous in spirit to [[latency-analysis]] for end-to-end request timing, but expressed as a timeline decomposition rather than a numeric split tree.
- Fits [[model-classify-intervene]] by making dominant waiting phases obvious before intervention.

## Links

- Source: [[systems-performance-timeline-charts-2-10-4]]
- Related concepts:
  - [[throughput-latency-metrics]]
  - [[latency-analysis]]
  - [[metric-visualization]]
  - [[model-classify-intervene]]
