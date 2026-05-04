# Systems Performance — sar data collection / scheduling (4.4.2 part) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.4.2 — enabling periodic collection, cron scheduling, completeness flags (`-S ALL` / `XALL`)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-sar-monitoring-collection-4-4-2.md`
- Chunks:
  - `processed/code/systems-performance-sar-monitoring-collection-4-4-2-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Absent archives are often configuration**, not evidence of idle systems—checking whether collection is enabled precedes interpreting missing history files.
- (measurement) **Resolution vs retention**: tighter sampling intervals increase archive growth and I/O; choosing cadence is a fleet-scale storage/bandwidth tradeoff, not only an analyst preference.
- (measurement) **Completeness flags**: default recording may omit statistic groups; forcing full groups trades richer longitudinal evidence against larger archives—decision belongs next to [[baseline-statistics]] planning.

## Concepts reused / refined / created

- Reused (measurement): [[time-series-monitoring]]
- Reused (abstraction): [[centralized-monitoring-architecture]]
- Reused (measurement): [[baseline-statistics]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[time-series-monitoring]]
  - [[centralized-monitoring-architecture]]
  - [[baseline-statistics]]
  - [[counters-statistics-metrics]]
  - [[systems-performance]]
