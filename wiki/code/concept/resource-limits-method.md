# Resource limits method

- Tag: heuristic

## Definition

The **resource limits method** estimates system capacity by expressing request rate in terms of resource consumption and extrapolating to per-resource limits to predict which resource will bottleneck first.

## Relation

- Role: method (capacity planning checklist for “what hits 100% first?”).
- Builds on [[resource-analysis-vs-workload-analysis]] (translate workload rate into resource usage) and relates to [[resource-vs-implementation-bottleneck]] (capacity vs implementation changes).
- Fits [[model-classify-intervene]] by classifying the expected limiter before choosing interventions (scale up/out, reduce load, change design).

## Links

- Source: [[systems-performance-resource-limits-2-7-1]]
- Source: [[systems-performance-network-ch10-methodology-tcp-analysis-ephemeral-ports-timewait-10-5-7]]
- Source: [[systems-performance-network-ch10-methodology-resource-controls-10-5-9]]
- Source: [[systems-performance-network-ch10-tuning-bql-cgroups-qdisc-tuned-10-8-1d]]
- Source: [[systems-performance-network-ch10-observability-sar-network-stats-options-table-10-5-part-a-10-6-6a]]
- Source: [[systems-performance-network-ch10-tuning-configuration-jumbo-lacp-firewall-dscp-10-8-3]]
- Related concepts:
  - [[resource-analysis-vs-workload-analysis]]
  - [[resource-vs-implementation-bottleneck]]
  - [[model-classify-intervene]]

