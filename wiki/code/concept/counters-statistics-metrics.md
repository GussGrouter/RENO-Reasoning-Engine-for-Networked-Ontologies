# Counters, statistics, and metrics

- Tag: structure

## Definition

In performance measurement, **counters** are instrumented state variables (often cumulative) that record counts or totals; **statistics** are computed from counters (rates, averages, percentiles) by reading counters over time; **metrics** are selected statistics chosen for ongoing monitoring and evaluation.

## Scope note

Industry usage is not rigid: these terms are often used interchangeably, and alerting can be built from multiple layers.

## Relation

This terminology helps avoid category errors when discussing observability: “what is recorded” (counters) vs “what is computed” (statistics) vs “what is monitored” (metrics).

Misclassified layers produce **invalid** comparisons (e.g., comparing a raw counter to a rate); see [[measurement-validity]] for semantic-fit checks beyond naming.

## Links

- Source: [[systems-performance-observability-1-7-p46-54]]
- Source: [[systems-performance-kernels-3-3]]
- Source: [[systems-performance-observability-tool-coverage-4-1]]
- Source: [[systems-performance-observability-tool-types-4-2]]
- Source: [[systems-performance-fixed-counters-4-2-1]]
- Source: [[systems-performance-observability-monitoring-4-2-4]]
- Source: [[systems-performance-proc-observability-4-3-1]]
- Source: [[systems-performance-sysfs-observability-4-3-2]]
- Source: [[systems-performance-delay-accounting-4-3-3]]
- Source: [[systems-performance-pmc-fundamentals-4-3-9]]
- Source: [[systems-performance-cpu-pmc-hardware-counter-programming-model-6-4-1]]
- Source: [[systems-performance-cpu-pmc-register-budget-and-sku-variance-6-4-1]]
- Source: [[systems-performance-cpu-cycle-analysis-and-performance-monitoring-6-5-5-6]]
- Source: [[systems-performance-cpu-observability-load-and-system-wide-stats-6-6-1-4]]
- Source: [[systems-performance-cpu-observability-process-attribution-and-clock-tools-6-6-5-12]]
- Source: [[systems-performance-cpu-observability-perf-profiling-and-pmcs-6-6-13]]
- Source: [[systems-performance-sar-intro-and-coverage-4-4]]
- Source: [[systems-performance-sar-monitoring-collection-4-4-2]]
- Source: [[systems-performance-sar-reporting-export-formats-4-4-2]]
- Source: [[systems-performance-sar-live-4-4-3]]
- Source: [[systems-performance-sar-documentation-4-4-4]]
- Source: [[systems-performance-observing-observability-4-6]]
- Source: [[systems-performance-chapter-4-exercises-4-7]]
- Source: [[systems-performance-chapter-5-exercises-application-profile-role-and-metrics-5-7]]
- Source: [[systems-performance-chapter-5-exercises-application-profile-observability-and-community-5-7]]
- Source: [[systems-performance-chapter-5-exercises-under-load-lab-b-5-7]]
- Source: [[systems-performance-memory-observability-vmstat-7-5-1]]
- Source: [[systems-performance-memory-observability-sar-7-5-4]]
- Source: [[systems-performance-filesystems-ch8-ops-not-equal-8-3-13]]
- Source: [[systems-performance-filesystems-ch8-performance-monitoring-8-5-4]]
- Source: [[systems-performance-filesystems-ch8-mount-free-8-6-1-2]]
- Source: [[systems-performance-filesystems-ch8-sar-cache-dentry-8-6-5]]
- Source: [[systems-performance-filesystems-ch8-slabtop-fs-caches-8-6-6]]
- Source: [[systems-performance-filesystems-ch8-zfs-arc-iostat-8-6-zfs]]
- Source: [[systems-performance-disks-ch9-concepts-measuring-time-9-3-1]]
- Source: [[systems-performance-disks-ch9-concepts-io-size-iops-commands-9-3-6-8]]
- Source: [[systems-performance-disks-ch9-methodology-use-method-9-5-2]]
- Source: [[systems-performance-disks-ch9-methodology-workload-characterization-9-5-4]]
- Source: [[systems-performance-disks-ch9-observability-iostat-9-6-1]]
- Source: [[systems-performance-disks-ch9-observability-sar-9-6-2]]
- Source: [[systems-performance-network-ch10-terminology-10-1]]
- Source: [[systems-performance-network-ch10-observability-traditional-stats-tools-table-10-6-a]]
- Source: [[systems-performance-network-ch10-observability-ss-socket-stats-tcp-internal-info-10-6-1]]
- Source: [[systems-performance-network-ch10-observability-ip-link-stats-routes-monitor-10-6-2]]
- Source: [[systems-performance-network-ch10-observability-ifconfig-legacy-interface-counters-10-6-3]]
- Source: [[systems-performance-network-ch10-observability-nstat-snmp-kernel-metrics-interval-reset-10-6-4]]
- Source: [[systems-performance-network-ch10-observability-netstat-multi-socket-interface-stack-stats-10-6-5]]
- Source: [[systems-performance-network-ch10-observability-sar-network-stats-options-table-10-5-part-a-10-6-6a]]
- Source: [[systems-performance-network-ch10-observability-sar-examples-interval-filtering-part-b-10-6-6b]]
- Source: [[systems-performance-network-ch10-observability-nicstat-throughput-utilization-saturation-10-6-7]]
- Source: [[systems-performance-network-ch10-observability-tcptop-process-tcp-throughput-bpf-10-6-10]]
- Source: [[systems-performance-network-ch10-observability-other-tools-linux-sources-monitoring-10-6-15b]]
- Related concepts:
  - [[measurement-validity]]
  - [[systems-performance]]
