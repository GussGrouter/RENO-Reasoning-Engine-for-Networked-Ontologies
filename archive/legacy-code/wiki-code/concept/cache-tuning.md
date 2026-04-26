# Cache tuning

- Tag: heuristic

## Definition

**Cache tuning** is a method for improving system performance by selecting and configuring cache levels, policies, and sizes to match the workload and maximize the value of cache hits.

## Relation

- Role: method (a practical checklist for making caching effective for a workload).
- Instantiates [[caching]] and often expresses a [[time-space-tradeoff]] (space and management overhead vs reduced latency).
- “Do it later” and write-back caching are instances of [[shift-computation-in-time]] (moving work off the critical path).
- Fits [[model-classify-intervene]] by choosing interventions (cache placement/policy/workload adjustments) based on observed hit/miss behavior.

## Links

- Source: [[systems-performance-cache-tuning-2-5-18]]
- Source: [[systems-performance-filesystems-ch8-cache-separation-microbench-8-5-6-8]]
- Source: [[systems-performance-filesystems-ch8-tuning-intro-8-8]]
- Source: [[systems-performance-filesystems-ch8-application-calls-fadvise-madvise-8-8-1]]
- Source: [[systems-performance-filesystems-ch8-zfs-tuning-properties-8-8-3]]
- Source: [[systems-performance-disks-ch9-concepts-caching-patterns-9-3-3-5]]
- Source: [[systems-performance-disks-ch9-methodology-cache-resource-microbench-9-5-7-9]]
- Related concepts:
  - [[caching]]
  - [[time-space-tradeoff]]
  - [[shift-computation-in-time]]
  - [[model-classify-intervene]]

