# Scalability knee point

- Tag: heuristic

## Definition

A **scalability knee point** is the load level where throughput stops scaling linearly and begins to degrade due to contention and queueing overheads.

## Scope note

The knee point often appears near saturation behavior (queueing becomes frequent/significant), and it is a practical boundary for “safe operating range” under load.

## Relation

Identifying a knee point helps separate pre-saturation linear scaling from regimes dominated by contention and increasing latency.

## Links

- Source: [[systems-performance-scalability-2-3-9]]
- Related concepts:
  - [[throughput-latency-metrics]]
  - [[utilization-and-saturation]]

