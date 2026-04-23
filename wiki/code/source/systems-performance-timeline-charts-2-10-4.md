# Systems Performance — timeline charts (2.10.4) (PDF pages 118–140)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.10.4 Timeline Charts

## Processed artifacts

- Converted slice: `processed/code/systems-performance-timeline-charts-2-10-4.md`
- Chunks:
  - `processed/code/systems-performance-timeline-charts-2-10-4-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Timeline charts show activities as bars on a timeline; common for front-end “waterfall” views of network request timing.
- (measurement) Bars can decompose duration into components (DNS, connect, wait/TTFB, receive), highlighting dominant waiting phases.
- (abstraction) With explicit dependency arrows, timelines resemble Gantt charts; similar timelines are used for threads/CPUs in kernel tracing tools.

## Concepts reused / refined / created

- Created (measurement): [[timeline-waterfall-chart]]
- Reused (method): [[metric-visualization]]
- Reused (technique): [[latency-analysis]]
- Reused (measurement): [[throughput-latency-metrics]]

## Links

- Concepts:
  - [[timeline-waterfall-chart]]
  - [[metric-visualization]]
  - [[latency-analysis]]
  - [[throughput-latency-metrics]]
