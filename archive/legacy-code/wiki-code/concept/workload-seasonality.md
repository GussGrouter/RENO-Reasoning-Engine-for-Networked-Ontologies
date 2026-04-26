# Workload seasonality

- Tag: diagnosis

## Definition

**Workload seasonality** refers to recurring time-based patterns in load (hourly, daily, weekly, quarterly, yearly) plus irregular spikes/drops driven by releases, promotions, outages, or external events.

## Relation

- Role: diagnosis (a pattern class used to interpret monitoring time series and avoid misreading transient noise as structural regressions).
- Best observed via [[time-series-monitoring]] and contrasted with baselines ([[baseline-statistics]]).
- Fits [[model-classify-intervene]] by separating “expected cyclical load” from “new architectural bottleneck” explanations.

## Links

- Source: [[systems-performance-time-based-patterns-2-9-1]]
- Related concepts:
  - [[time-series-monitoring]]
  - [[baseline-statistics]]
  - [[model-classify-intervene]]
