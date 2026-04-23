# Latency analysis

- Tag: heuristic

## Definition

**Latency analysis** decomposes the time to complete an operation into components, then repeatedly subdivides the highest-latency component to identify and quantify the origin of latency (potentially across layers of the software stack).

## Operational role

- Category: method
- Use when you need to localize *where time goes* for an operation, and to prioritize the component with the largest latency contribution.

## Relation

- Role: technique (a decomposition strategy for “where time goes” that can be embedded within [[drill-down-analysis]]).
- Can be performed as a “binary split” of latency contributions (a decision-tree style narrowing), which fits the iterative evidence loop in [[diagnosis-cycle]].
- Anchors to common performance framing in [[throughput-latency-metrics]] and complements [[sampling-based-profiling]] (profiling attributes resource use; latency analysis attributes time-in-operation).
- Supports [[model-classify-intervene]] by producing a concrete latency breakdown before selecting an intervention.

## Links

- Source: [[systems-performance-latency-analysis-2-5-13]]
- Source: [[systems-performance-systemd-3-4-2]]
- Source: [[systems-performance-delay-accounting-4-3-3]]
- Source: [[systems-performance-shared-memory-and-sync-primitives-5-2-5]]
- Source: [[systems-performance-garbage-collection-performance-5-3-4]]
- Source: [[systems-performance-thread-state-investigation-and-measurement-5-4-5]]
- Source: [[systems-performance-distributed-request-trace-sampling-5-4-8]]
- Source: [[systems-performance-bpftrace-custom-aggregation-probe-ladder-5-5-7]]
- Source: [[systems-performance-chapter-5-exercises-under-load-lab-a-5-7]]
- Source: [[systems-performance-chapter-5-exercises-under-load-lab-b-5-7]]
- Source: [[systems-performance-filesystems-ch8-models-8-2]]
- Source: [[systems-performance-filesystems-ch8-concept-latency-8-3-1]]
- Source: [[systems-performance-filesystems-ch8-writeback-sync-8-3-5-7]]
- Source: [[systems-performance-filesystems-ch8-methodology-intro-8-5]]
- Source: [[systems-performance-filesystems-ch8-disk-latency-analysis-open-8-5-1-2]]
- Source: [[systems-performance-filesystems-ch8-latency-layers-table-8-5-2a]]
- Source: [[systems-performance-filesystems-ch8-latency-presentation-drilldown-8-5-2b]]
- Source: [[systems-performance-filesystems-ch8-transaction-cost-fs-8-5-2c]]
- Source: [[systems-performance-filesystems-ch8-workload-char-basic-8-5-3a]]
- Source: [[systems-performance-filesystems-ch8-workload-char-advanced-8-5-3b]]
- Source: [[systems-performance-filesystems-ch8-performance-monitoring-8-5-4]]
- Source: [[systems-performance-filesystems-ch8-static-tuning-fs-8-5-5]]
- Source: [[systems-performance-filesystems-ch8-cache-separation-microbench-8-5-6-8]]
- Source: [[systems-performance-filesystems-ch8-table-8-5-expectations]]
- Source: [[systems-performance-filesystems-ch8-strace-syscall-latency-8-6-7]]
- Source: [[systems-performance-filesystems-ch8-ext4dist-histograms-8-6-13]]
- Source: [[systems-performance-filesystems-ch8-ext4slower-8-6-14]]
- Source: [[systems-performance-filesystems-ch8-bpftrace-syscall-semantics-8-6-15b]]
- Source: [[systems-performance-filesystems-ch8-bpftrace-vfs-fs-internals-8-6-15c]]
- Source: [[systems-performance-filesystems-ch8-exercises-8-9]]
- Source: [[systems-performance-disks-ch9-concepts-measuring-time-9-3-1]]
- Source: [[systems-performance-disks-ch9-concepts-utilization-saturation-iowait-9-3-9-11]]
- Source: [[systems-performance-disks-ch9-concepts-async-mismatch-9-3-12-13]]
- Source: [[systems-performance-disks-ch9-methodology-latency-analysis-9-5-5]]
- Source: [[systems-performance-disks-ch9-observability-biosnoop-9-6-7]]
- Source: [[systems-performance-disks-ch9-observability-biostacks-9-6-9]]
- Source: [[systems-performance-disks-ch9-observability-blktrace-btt-viz-9-6-10c]]
- Source: [[systems-performance-disks-ch9-observability-bpftrace-latency-errors-9-6-11d]]
- Source: [[systems-performance-network-ch10-concepts-latency-measurement-types-10-3-5]]
- Source: [[systems-performance-disks-ch9-observability-smartctl-9-6-13]]
- Related concepts:
  - [[throughput-latency-metrics]]
  - [[sampling-based-profiling]]
  - [[diagnosis-cycle]]
  - [[model-classify-intervene]]

