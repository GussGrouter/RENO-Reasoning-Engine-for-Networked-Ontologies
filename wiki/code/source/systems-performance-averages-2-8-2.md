# Systems Performance — averages (2.8.2) (PDF pages 110–120)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.8.2 Averages

## Processed artifacts

- Converted slice: `processed/code/systems-performance-averages-2-8-2.md`
- Chunks:
  - `processed/code/systems-performance-averages-2-8-2-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) “Average” summarizes a dataset; different means apply in different contexts (arithmetic, geometric, harmonic).
- (measurement) Geometric mean is useful when effects are multiplicative (layered improvements compound).
- (measurement) Harmonic mean is appropriate for averaging rates over a fixed total quantity.
- (measurement) Many performance metrics are averages over time; the interval matters (long averages can hide short saturation bursts).
- (measurement) Decayed averages weight recent time more heavily to damp fluctuations.
- (diagnosis) Averages can hide tails/outliers; use distribution-aware statistics when needed.

## Concepts reused / refined / created

- Created (technique): [[geometric-mean]]
- Created (technique): [[harmonic-mean]]
- Reused (diagnosis): [[utilization-and-saturation]] (bursts hidden by long-window utilization averages).
- Reused (measurement): [[latency-percentiles]] (distribution-aware alternative to means).

## Links

- Concepts:
  - [[geometric-mean]]
  - [[harmonic-mean]]
  - [[utilization-and-saturation]]
  - [[latency-percentiles]]

