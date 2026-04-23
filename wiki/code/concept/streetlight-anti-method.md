# Streetlight anti-method

- Tag: heuristic

## Definition

The **streetlight anti-method** is diagnosing performance by only using familiar or convenient tools (or random tools) and then reasoning from whatever they show, even if those tools are not appropriate for the suspected problem.

## Failure mode

It can overlook many issue types, waste time on unrelated signals, and produce **false positives** (finding “an issue” that isn’t the root cause).

## Relation

- This is an *observability coverage* failure: it tends to leave important parts of the system as [[known-unknowns-framework]].
- It often leads to mistaking symptoms for causes, increasing the risk of misclassifying bottlenecks (see [[resource-vs-implementation-bottleneck]]).

## Links

- Source: [[systems-performance-streetlight-anti-method-2-5-1]]
- Source: [[systems-performance-cpu-methodology-cookbook-and-tools-method-6-5-intro-6-5-1]]
- Source: [[systems-performance-memory-methodology-tools-method-7-4-1]]
- Source: [[systems-performance-filesystems-ch8-disk-latency-analysis-open-8-5-1-2]]
- Source: [[systems-performance-filesystems-ch8-table-8-5-expectations]]
- Source: [[systems-performance-disks-ch9-methodology-intro-tools-9-5-1]]
- Source: [[systems-performance-disks-ch9-observability-intro-table-9-6]]
- Source: [[systems-performance-disks-ch9-observability-other-tools-table-9-6-15]]
- Source: [[systems-performance-network-ch10-observability-tools-intro-table-10-6]]
- Source: [[systems-performance-network-ch10-observability-traditional-stats-tools-table-10-6-a]]
- Source: [[systems-performance-network-ch10-observability-sar-examples-interval-filtering-part-b-10-6-6b]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-event-sources-table-10-6-12d]]
- Source: [[systems-performance-network-ch10-observability-other-tools-table-10-7-crossrefs-10-6-15a]]
- Related concepts:
  - [[known-unknowns-framework]]
  - [[counters-statistics-metrics]]
  - [[resource-vs-implementation-bottleneck]]

