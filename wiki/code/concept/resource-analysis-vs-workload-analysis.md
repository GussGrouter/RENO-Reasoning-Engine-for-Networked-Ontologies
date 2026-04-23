# Resource analysis vs workload analysis

- Tag: abstraction

## Definition

**Resource analysis** and **workload analysis** are complementary perspectives for performance analysis:

- **resource analysis**: start from system resources (CPU, memory, disks, network, interconnects); focus on utilization/saturation and capacity limits
- **workload analysis**: start from application requests and responses; focus on latency, throughput, and completion (errors/retries)

## Relation

Resource analysis can quickly identify likely bottleneck resource types; workload analysis localizes which requests and code paths are responsible and validates improvement by checking latency.

## Links

- Source: [[systems-performance-perspectives-2-4]]
- Source: [[systems-performance-kernel-comparisons-3-6]]
- Source: [[systems-performance-distributed-operating-systems-3-5-4]]
- Source: [[systems-performance-observability-tool-coverage-4-1]]
- Source: [[systems-performance-observability-sources-intro-4-3]]
- Source: [[systems-performance-application-basics-5-1]]
- Source: [[systems-performance-syscall-analysis-boundary-instrumentation-5-4-3]]
- Source: [[systems-performance-use-method-software-resources-5-4-4]]
- Source: [[systems-performance-thread-state-investigation-and-measurement-5-4-5]]
- Source: [[systems-performance-syscount-ranking-and-follow-on-5-5-6]]
- Source: [[systems-performance-chapter-5-exercises-terminology-scaffold-5-7]]
- Source: [[systems-performance-chapter-5-exercises-application-profile-role-and-metrics-5-7]]
- Source: [[systems-performance-chapter-5-exercises-under-load-lab-a-5-7]]
- Source: [[systems-performance-cpu-terminology-6-1]]
- Source: [[systems-performance-cpu-concepts-ipc-utilization-and-user-kernel-time-6-3-7-9]]
- Source: [[systems-performance-cpu-workload-characterization-6-5-3]]
- Source: [[systems-performance-cpu-observability-process-attribution-and-clock-tools-6-6-5-12]]
- Source: [[systems-performance-cpu-heterogeneous-accelerators-observability-6-4-1]]
- Source: [[systems-performance-cpu-idle-numa-topology-scheduler-awareness-6-4-2]]
- Source: [[systems-performance-cpu-chapter-6-exercises-scaffold-6-10]]
- Source: [[systems-performance-memory-methodology-ch7-intro-and-order-7-4]]
- Source: [[systems-performance-memory-methodology-characterizing-usage-7-4-3a]]
- Source: [[systems-performance-memory-methodology-usage-checklist-7-4-3b]]
- Source: [[systems-performance-memory-observability-ps-top-pmap-7-5-7-9]]
- Source: [[systems-performance-memory-ch7-exercises-scaffold-7-7]]
- Source: [[systems-performance-filesystems-ch8-fs-types-xfs-8-4-5c]]
- Source: [[systems-performance-filesystems-ch8-volumes-pools-8-4-6]]
- Source: [[systems-performance-filesystems-ch8-transaction-cost-fs-8-5-2c]]
- Source: [[systems-performance-filesystems-ch8-workload-char-basic-8-5-3a]]
- Source: [[systems-performance-filesystems-ch8-fatrace-latencytop-8-6-8-9]]
- Source: [[systems-performance-filesystems-ch8-filetop-8-6-11]]
- Source: [[systems-performance-disks-ch9-intro-parts-terminology-9-1]]
- Source: [[systems-performance-disks-ch9-concepts-caching-patterns-9-3-3-5]]
- Source: [[systems-performance-disks-ch9-methodology-workload-characterization-9-5-4]]
- Source: [[systems-performance-disks-ch9-observability-pidstat-9-6-4]]
- Source: [[systems-performance-disks-ch9-observability-iotop-biotop-9-6-8]]
- Source: [[systems-performance-disks-ch9-exercises-scaffold-c-9-10c]]
- Source: [[systems-performance-network-ch10-observability-ss-socket-stats-tcp-internal-info-10-6-1]]
- Source: [[systems-performance-network-ch10-observability-sar-examples-interval-filtering-part-b-10-6-6b]]
- Source: [[systems-performance-network-ch10-observability-tcplife-tcp-session-lifecycle-bpf-10-6-9]]
- Source: [[systems-performance-network-ch10-tuning-sysctl-system-wide-discovery-example-10-8-1a]]
- Related concepts:
  - [[throughput-latency-metrics]]
  - [[utilization-and-saturation]]
  - [[counters-statistics-metrics]]
  - [[sampling-based-profiling]]

