# Centralized monitoring architecture

- Tag: abstraction

## Definition

A **centralized monitoring architecture** collects metrics from many systems via agents/exporters, stores time series centrally, and provides interactive visualization and alerting across an entire environment.

## Relation

- Role: abstraction (a common system shape for fleet-scale observability, independent of any single vendor).
- Agents may gather metrics by reading kernel interfaces directly (preferred) vs parsing tool output (often less efficient).
- Supports [[time-series-monitoring]] at scale and complements [[counters-statistics-metrics]] as the operational layer that persists and surfaces those signals.

## Links

- Source: [[systems-performance-monitoring-products-2-9-2]]
- Source: [[systems-performance-observability-monitoring-4-2-4]]
- Source: [[systems-performance-sar-intro-and-coverage-4-4]]
- Source: [[systems-performance-sar-monitoring-collection-4-4-2]]
- Source: [[systems-performance-sar-reporting-export-formats-4-4-2]]
- Related concepts:
  - [[time-series-monitoring]]
  - [[counters-statistics-metrics]]
  - [[model-classify-intervene]]
