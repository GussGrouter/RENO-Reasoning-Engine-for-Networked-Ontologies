# Instrumentation overhead and perturbation

- Tag: tradeoff

## Definition

**Instrumentation overhead and perturbation** is the measurement constraint that observing events (especially at high rates) consumes resources and can measurably change the system being observed.

## Scope note

Overhead can come from:

- per-event work when instrumentation is enabled (e.g., tracepoint execution)
- tool-side processing and recording costs (CPU and I/O)
- baseline (“disabled”) costs of having instrumentation sites present (usually small but non-zero)

Whether perturbation matters depends on event rate, CPU count, and workload sensitivity.

## Relation

This constrains what measurements are safe to run in production and how to interpret observed latencies and rates.

**Validity vs perturbation**: overhead tells you whether the *act of observing* distorted the system; [[measurement-validity]] asks whether the *resulting signal still answers your question* once perturbation is controlled (definitions, window, cohort, semantic match to the SLO).

Perturbation can also come from other concurrent system activity (scheduled tasks, other users/workloads, or other tenants), not just the measurement tool itself.

This is often referred to as the observer effect: measurement overhead can change the measured system.

## Links

- Source: [[systems-performance-tracepoints-overhead-kprobes-p186-194]]
- Source: [[systems-performance-linux-kernel-developments-3-4-1]]
- Source: [[systems-performance-unikernels-3-5-2]]
- Source: [[systems-performance-chapter-4-intro-4]]
- Source: [[systems-performance-observability-crisis-tools-4-1-2]]
- Source: [[systems-performance-fixed-counters-4-2-1]]
- Source: [[systems-performance-profiling-4-2-2]]
- Source: [[systems-performance-tracing-4-2-3]]
- Source: [[systems-performance-observability-monitoring-4-2-4]]
- Source: [[systems-performance-proc-observability-4-3-1]]
- Source: [[systems-performance-netlink-observability-4-3-4]]
- Source: [[systems-performance-tracepoints-4-3-5]]
- Source: [[systems-performance-kprobes-4-3-6]]
- Source: [[systems-performance-uprobes-4-3-7]]
- Source: [[systems-performance-usdt-4-3-8]]
- Source: [[systems-performance-pmc-fundamentals-4-3-9]]
- Source: [[systems-performance-other-observability-sources-4-3-10]]
- Source: [[systems-performance-tracing-tools-survey-4-5]]
- Source: [[systems-performance-observing-observability-4-6]]
- Source: [[systems-performance-chapter-4-exercises-4-7]]
- Source: [[systems-performance-application-observability-selection-5-1-3]]
- Source: [[systems-performance-interpreted-languages-performance-5-3-2]]
- Source: [[systems-performance-language-virtual-machines-5-3-3]]
- Source: [[systems-performance-garbage-collection-performance-5-3-4]]
- Source: [[systems-performance-cpu-profiling-kernel-vs-user-5-4-1]]
- Source: [[systems-performance-off-cpu-narrowing-filters-5-4-2]]
- Source: [[systems-performance-thread-state-investigation-and-measurement-5-4-5]]
- Source: [[systems-performance-distributed-request-trace-sampling-5-4-8]]
- Source: [[systems-performance-perf-profiling-syscall-trace-and-io-5-5-1]]
- Source: [[systems-performance-offcputime-aggregation-and-duration-filters-5-5-3]]
- Source: [[systems-performance-strace-ptrace-overhead-and-buffered-tracing-5-5-4]]
- Source: [[systems-performance-bpftrace-custom-aggregation-probe-ladder-5-5-7]]
- Source: [[systems-performance-application-gotchas-missing-symbols-5-6-1]]
- Source: [[systems-performance-gotchas-missing-stacks-causes-5-6-2]]
- Source: [[systems-performance-cpu-pmc-register-budget-and-sku-variance-6-4-1]]
- Source: [[systems-performance-cpu-profiling-methodology-sampling-vs-instrumentation-6-5-4]]
- Source: [[systems-performance-cpu-observability-perf-profiling-and-pmcs-6-6-13]]
- Source: [[systems-performance-memory-methodology-tools-method-7-4-1]]
- Source: [[systems-performance-memory-observability-trace-other-7-5-11-14]]
- Source: [[systems-performance-filesystems-ch8-workload-char-advanced-8-5-3b]]
- Source: [[systems-performance-filesystems-ch8-strace-syscall-latency-8-6-7]]
- Source: [[systems-performance-filesystems-ch8-fatrace-latencytop-8-6-8-9]]
- Source: [[systems-performance-filesystems-ch8-cachestat-8-6-12]]
- Source: [[systems-performance-filesystems-ch8-ext4slower-8-6-14]]
- Source: [[systems-performance-disks-ch9-methodology-workload-characterization-9-5-4]]
- Source: [[systems-performance-disks-ch9-observability-perf-9-6-5]]
- Source: [[systems-performance-disks-ch9-observability-blktrace-intro-default-9-6-10a]]
- Source: [[systems-performance-disks-ch9-observability-scsi-logging-9-6-14]]
- Source: [[systems-performance-disks-ch9-experimentation-ioping-9-8-5]]
- Source: [[systems-performance-network-ch10-observability-tools-intro-table-10-6]]
- Source: [[systems-performance-network-ch10-observability-packet-capture-tools-table-10-6-c]]
- Source: [[systems-performance-network-ch10-observability-ss-socket-stats-tcp-internal-info-10-6-1]]
- Source: [[systems-performance-network-ch10-observability-tcptop-process-tcp-throughput-bpf-10-6-10]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-one-liners-probe-cost-10-6-12a]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-tcp-tcpsynbl-backlog-10-6-12c]]
- Source: [[systems-performance-network-ch10-observability-tcpdump-capture-filters-overhead-10-6-13]]
- Source: [[systems-performance-network-ch10-observability-wireshark-gui-packet-inspection-10-6-14]]
- Source: [[systems-performance-network-ch10-experimentation-pathchar-pchar-bandwidth-probing-10-7-3]]
- Related concepts:
  - [[throughput-latency-metrics]]
  - [[resource-vs-implementation-bottleneck]]
  - [[systems-performance]]

