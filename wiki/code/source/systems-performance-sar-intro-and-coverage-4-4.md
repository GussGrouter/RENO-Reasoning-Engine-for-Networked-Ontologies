# Systems Performance — sar introduction and coverage map (4.4 / 4.4.1) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Sections 4.4 (sar framing) + 4.4.1 coverage overview (Figure 4.6 narrative)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-sar-intro-and-coverage-4-4.md`
- Chunks:
  - `processed/code/systems-performance-sar-intro-and-coverage-4-4-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Breadth-first monitoring discipline**: sar remains a practical default for kernel/device-wide counters even when newer tracing stacks exist—story arc cautions against replacing foundational multi-domain rollups with niche deep traces alone.
- (measurement) Good monitoring UX (self-describing columns, grouped network/power metrics, documentation) raises **signal usability**—the same counters are easier to apply under incident pressure, which affects real decisions more than raw data availability alone.
- (measurement) Coverage narrative highlights that a single long-lived statistics tool can span CPU, memory, disk, net, power, thermal, and peripheral sensors—useful when triage must stay **cross-resource** before zooming.

## Concepts reused / refined / created

- Reused (measurement): [[time-series-monitoring]]
- Reused (abstraction): [[centralized-monitoring-architecture]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused (measurement): [[baseline-statistics]]
- Reused: [[systems-performance]]

## Related sections

- [[systems-performance-sar-monitoring-collection-4-4-2]]
- [[systems-performance-sar-reporting-export-formats-4-4-2]]
- [[systems-performance-sar-live-4-4-3]]
- [[systems-performance-sar-documentation-4-4-4]]
- [[systems-performance-tracing-tools-survey-4-5]]
- [[systems-performance-observing-observability-4-6]]
- [[systems-performance-chapter-4-exercises-4-7]]
- [[systems-performance-chapter-4-references-4-8]]

## Links

- Concepts:
  - [[time-series-monitoring]]
  - [[centralized-monitoring-architecture]]
  - [[counters-statistics-metrics]]
  - [[baseline-statistics]]
  - [[systems-performance]]
