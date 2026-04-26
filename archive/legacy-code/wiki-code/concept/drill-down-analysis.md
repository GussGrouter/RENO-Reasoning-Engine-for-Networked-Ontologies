# Drill-down analysis

- Tag: heuristic

## Definition

**Drill-down analysis** is a structured approach that starts with a high-level view of a suspected issue and repeatedly narrows focus based on findings, discarding uninteresting areas and digging deeper (down the software stack, to hardware if needed) to identify and quantify root cause.

## Operational role

- Category: method
- Use when you need a repeatable way to go from “something is slow” to a specific bottleneck and its cause.

## Relation

- Role: method (general narrowing strategy; uses techniques like profiling/tracing during deeper stages).
- Often staged as monitoring → identification → analysis; the “analysis” stage may use profiling/tracing.
- Works as the “model + evidence” loop inside [[model-classify-intervene]] (narrow the candidate causes, then intervene).
- Can be paired with [[diagnosis-cycle]] to iterate quickly as hypotheses change.

## Links

- Source: [[systems-performance-drill-down-analysis-2-5-12]]
- Source: [[systems-performance-optimize-common-case-5-1-2]]
- Source: [[systems-performance-lock-fastpath-midpath-slowpath-rcu-5-2-5]]
- Source: [[systems-performance-application-methodology-overview-5-4]]
- Source: [[systems-performance-off-cpu-narrowing-filters-5-4-2]]
- Source: [[systems-performance-syscall-analysis-boundary-instrumentation-5-4-3]]
- Source: [[systems-performance-thread-state-investigation-and-measurement-5-4-5]]
- Source: [[systems-performance-lock-contention-and-hold-time-5-4-6]]
- Source: [[systems-performance-perf-profiling-syscall-trace-and-io-5-5-1]]
- Source: [[systems-performance-execsnoop-execve-lineage-discovery-5-5-5]]
- Source: [[systems-performance-syscount-ranking-and-follow-on-5-5-6]]
- Source: [[systems-performance-bpftrace-custom-aggregation-probe-ladder-5-5-7]]
- Source: [[systems-performance-gotchas-missing-stacks-causes-5-6-2]]
- Source: [[systems-performance-chapter-5-exercises-application-profile-role-and-metrics-5-7]]
- Source: [[systems-performance-chapter-5-exercises-under-load-lab-a-5-7]]
- Source: [[systems-performance-chapter-5-exercises-under-load-lab-b-5-7]]
- Source: [[systems-performance-cpu-concepts-instruction-lifecycle-and-stall-cycles-6-3-2]]
- Source: [[systems-performance-cpu-methodology-cookbook-and-tools-method-6-5-intro-6-5-1]]
- Source: [[systems-performance-memory-observability-tools-ch7-intro-table-7-5]]
- Source: [[systems-performance-memory-observability-vmstat-7-5-1]]
- Source: [[systems-performance-memory-observability-sar-7-5-4]]
- Source: [[systems-performance-filesystems-ch8-intro-outline-8]]
- Source: [[systems-performance-filesystems-ch8-latency-presentation-drilldown-8-5-2b]]
- Source: [[systems-performance-filesystems-ch8-obs-tools-intro-8-6]]
- Source: [[systems-performance-filesystems-ch8-opensnoop-8-6-10]]
- Source: [[systems-performance-filesystems-ch8-other-tools-8-6-17]]
- Source: [[systems-performance-filesystems-ch8-exercises-8-9]]
- Source: [[systems-performance-disks-ch9-methodology-intro-tools-9-5-1]]
- Source: [[systems-performance-disks-ch9-methodology-latency-analysis-9-5-5]]
- Source: [[systems-performance-disks-ch9-observability-intro-table-9-6]]
- Source: [[systems-performance-disks-ch9-observability-perf-9-6-5]]
- Source: [[systems-performance-disks-ch9-observability-biosnoop-9-6-7]]
- Source: [[systems-performance-disks-ch9-observability-bpftrace-oneliners-9-6-11a]]
- Source: [[systems-performance-disks-ch9-observability-biostacks-9-6-9]]
- Source: [[systems-performance-disks-ch9-observability-other-tools-table-9-6-15]]
- Source: [[systems-performance-disks-ch9-exercises-scaffold-c-9-10c]]
- Source: [[systems-performance-network-ch10-observability-tools-intro-table-10-6]]
- Source: [[systems-performance-network-ch10-observability-ss-socket-stats-tcp-internal-info-10-6-1]]
- Source: [[systems-performance-network-ch10-observability-sar-examples-interval-filtering-part-b-10-6-6b]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-event-sources-table-10-6-12d]]
- Related concepts:
  - [[diagnosis-cycle]]
  - [[sampling-based-profiling]]
  - [[counters-statistics-metrics]]
  - [[measurement-validity]]
  - [[model-classify-intervene]]

