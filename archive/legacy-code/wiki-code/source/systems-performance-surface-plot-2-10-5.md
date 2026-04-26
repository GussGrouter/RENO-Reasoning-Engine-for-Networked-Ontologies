# Systems Performance — surface plot (2.10.5) (PDF pages 118–140)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.10.5 Surface Plot

## Processed artifacts

- Converted slice: `processed/code/systems-performance-surface-plot-2-10-5.md`
- Chunks:
  - `processed/code/systems-performance-surface-plot-2-10-5-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Surface plots encode three+ dimensions (often x, y, height; color can add another channel) when values change smoothly enough to read as terrain.
- (diagnosis) Useful for spotting sustained plateaus (e.g., CPUs pegged near 100%) and subtle low-level utilization ridges across many entities/time slices.

## Concepts reused / refined / created

- Created (measurement): [[multivariate-metric-surface-plot]]
- Reused (method): [[metric-visualization]]
- Reused (diagnosis): [[utilization-and-saturation]]
- Reused (measurement): [[time-series-monitoring]]

## Links

- Concepts:
  - [[multivariate-metric-surface-plot]]
  - [[metric-visualization]]
  - [[utilization-and-saturation]]
  - [[time-series-monitoring]]
