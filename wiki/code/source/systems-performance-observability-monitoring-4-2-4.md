# Systems Performance — monitoring (4.2.4) (PDF pages 171–220)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.2.4 Monitoring

## Processed artifacts

- Converted slice: `processed/code/systems-performance-observability-monitoring-4-2-4.md`
- Chunks:
  - `processed/code/systems-performance-observability-monitoring-4-2-4-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Monitoring emphasizes **continuous collection** so statistics exist when an incident starts—different default posture than “enable tracing only when investigating.”
- (abstraction) Fleet monitoring architectures repeat a common shape: agents/exporters → time-series store → UI/alerting (vendor-specific details map to the same decision: where truth is archived and who can query it).
- (diagnosis) Parsing human-oriented tool output is a recurring **integration tax**; better designs read stable programmatic interfaces when available.

## Concepts reused / refined / created

- Reused (measurement): [[time-series-monitoring]]
- Reused (abstraction): [[centralized-monitoring-architecture]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[time-series-monitoring]]
  - [[centralized-monitoring-architecture]]
  - [[counters-statistics-metrics]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[systems-performance]]
