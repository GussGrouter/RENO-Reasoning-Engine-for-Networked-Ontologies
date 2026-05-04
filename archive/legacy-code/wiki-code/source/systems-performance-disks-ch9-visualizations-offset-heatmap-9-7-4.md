# Systems Performance — Ch.9 §9.7.4 Offset heat maps

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p482-560.txt`
- Scope: **§9.7.4**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-visualizations-offset-heatmap-9-7-4.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Offset vs latency views:** **where** on disk you hit often drives **scheduler/array** tuning; **latency heat maps** alone do not show **spatial creep** vs **random spray** ([[metric-visualization]], [[latency-heatmap]], [[multivariate-metric-surface-plot]] as **multi-axis** presentation).

## Application hook

If **`biolatency` shows pain** but **workload “should be sequential”**: an **offset heat map** quickly falsifies **misaligned files**, **fragmentation**, or **multi-tenant interleaving**.

## Decision clarity

**Decision:** choose **offset heat maps** over **latency-only heat maps** when the hypothesis is **access pattern geometry** (sequential vs random), not **queue depth alone**.

## Concepts reused / refined / created

- Reused: [[metric-visualization]], [[latency-heatmap]], [[multivariate-metric-surface-plot]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[metric-visualization]], [[latency-heatmap]], [[multivariate-metric-surface-plot]], [[measurement-validity]], [[systems-performance]]
