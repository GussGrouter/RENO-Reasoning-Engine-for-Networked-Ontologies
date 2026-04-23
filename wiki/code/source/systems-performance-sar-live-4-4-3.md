# Systems Performance — sar live mode (4.4.3) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.4.3 (interval/count live reporting)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-sar-live-4-4-3.md`
- Chunks:
  - `processed/code/systems-performance-sar-live-4-4-3-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Live mode does not require historical collection**—it answers “what is happening *right now*” with per-second (or finer) structure, while archived `sad` data is built for long windows and coarser intervals.
- (diagnosis) Choosing live vs archive parallels choosing **latency-sensitive diagnostics** vs **baseline drift detection**: same statistic families, different control loops ([[time-series-monitoring]] posture vs incident microscope).

## Concepts reused / refined / created

- Reused (measurement): [[time-series-monitoring]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused (measurement): [[baseline-statistics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[time-series-monitoring]]
  - [[counters-statistics-metrics]]
  - [[baseline-statistics]]
  - [[systems-performance]]
