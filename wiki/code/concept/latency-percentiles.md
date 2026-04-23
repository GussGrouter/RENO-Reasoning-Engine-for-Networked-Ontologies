# Latency percentiles

- Tag: measurement

## Definition

**Latency percentiles** (e.g., p50/median, p90, p95, p99, p99.9) summarize where observed latencies fall in a distribution, allowing performance to be expressed for the “typical” case and the slow tail.

## Relation

- Role: measurement (distribution-aware latency reporting, often used for SLOs/SLAs).
- Addresses a limitation of averages by exposing tail behavior and outliers (often critical for user experience).
- Commonly interpreted alongside [[throughput-latency-metrics]] and methods like [[latency-analysis]] for attribution.

Choosing **which tail** (p95 vs p99.9) and **which window** to measure is a [[measurement-validity]] decision when percentiles gate releases or SLOs—“tail-focused measurement” is not a separate idea from picking the percentile level that matches the risk you manage.

## Links

- Source: [[systems-performance-standard-deviation-percentiles-median-2-8-3]]
- Source: [[systems-performance-application-objectives-5-1-1]]
- Source: [[systems-performance-garbage-collection-performance-5-3-4]]
- Source: [[systems-performance-chapter-5-exercises-under-load-lab-b-5-7]]
- Source: [[systems-performance-filesystems-ch8-fio-8-7-2b]]
- Related concepts:
  - [[throughput-latency-metrics]]
  - [[latency-analysis]]
  - [[counters-statistics-metrics]]
  - [[measurement-validity]]

