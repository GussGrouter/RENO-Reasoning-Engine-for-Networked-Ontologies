# Systems Performance — heat maps (2.10.3) (PDF pages 118–140)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.10.3 Heat Maps

## Processed artifacts

- Converted slice: `processed/code/systems-performance-heat-maps-2-10-3.md`
- Chunks:
  - `processed/code/systems-performance-heat-maps-2-10-3-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Heat maps quantize x/y into buckets and color by density, addressing scatter-plot overlap and “wall of paint” scalability limits.
- (diagnosis) High-latency outliers can appear as sparse high buckets; bulk multimodal structure can become visible across long time ranges.
- (diagnosis) Heat maps can reveal bimodal latency populations (e.g., near-zero vs ~1 ms) that are hard to read from means alone.

## Concepts reused / refined / created

- Created (measurement): [[latency-heatmap]]
- Reused (method): [[metric-visualization]]
- Reused (diagnosis): [[latency-outliers]]
- Reused (diagnosis): [[multimodal-latency-distribution]]

## Links

- Concepts:
  - [[latency-heatmap]]
  - [[metric-visualization]]
  - [[latency-outliers]]
  - [[multimodal-latency-distribution]]
