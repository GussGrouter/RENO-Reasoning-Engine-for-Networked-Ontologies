# Event tracing

- Tag: measurement

## Definition

**Event tracing** records and inspects individual events (requests and completions) with their attributes and timestamps, instead of only studying summarized statistics, to preserve detail needed for diagnosing behavior and latency.

## Operational role

- Category: measurement
- Use when summary metrics hide important structure (e.g., outliers, queue effects, request/result attributes).

## Relation

- Complements [[counters-statistics-metrics]]: counters summarize; tracing preserves per-event detail.
- Supports [[latency-analysis]] by providing start/end times and per-event latency, and can reveal queue-driven latency outliers (caused by prior events).
- Useful during [[drill-down-analysis]] when you need deeper inspection of a suspect layer.
- Fits [[model-classify-intervene]] by providing evidence to validate a model of where time goes before interventions.

## Links

- Source: [[systems-performance-event-tracing-2-5-15]]
- Source: [[systems-performance-kernels-solaris-3-3-3]]
- Source: [[systems-performance-linux-kernel-developments-3-4-1]]
- Source: [[systems-performance-extended-bpf-3-4-4]]
- Source: [[systems-performance-chapter-4-intro-4]]
- Source: [[systems-performance-observability-tool-types-4-2]]
- Source: [[systems-performance-fixed-counters-4-2-1]]
- Source: [[systems-performance-tracing-4-2-3]]
- Source: [[systems-performance-tracepoints-4-3-5]]
- Source: [[systems-performance-kprobes-4-3-6]]
- Source: [[systems-performance-uprobes-4-3-7]]
- Source: [[systems-performance-usdt-4-3-8]]
- Source: [[systems-performance-other-observability-sources-4-3-10]]
- Source: [[systems-performance-tracing-tools-survey-4-5]]
- Source: [[systems-performance-chapter-4-exercises-4-7]]
- Source: [[systems-performance-interpreted-languages-performance-5-3-2]]
- Source: [[systems-performance-language-virtual-machines-5-3-3]]
- Source: [[systems-performance-syscall-analysis-boundary-instrumentation-5-4-3]]
- Source: [[systems-performance-distributed-request-trace-sampling-5-4-8]]
- Source: [[systems-performance-perf-profiling-syscall-trace-and-io-5-5-1]]
- Source: [[systems-performance-strace-ptrace-overhead-and-buffered-tracing-5-5-4]]
- Source: [[systems-performance-execsnoop-execve-lineage-discovery-5-5-5]]
- Source: [[systems-performance-bpftrace-custom-aggregation-probe-ladder-5-5-7]]
- Source: [[systems-performance-chapter-5-exercises-application-profile-observability-and-community-5-7]]
- Source: [[systems-performance-filesystems-ch8-workload-char-advanced-8-5-3b]]
- Source: [[systems-performance-filesystems-ch8-fatrace-latencytop-8-6-8-9]]
- Source: [[systems-performance-filesystems-ch8-opensnoop-8-6-10]]
- Source: [[systems-performance-filesystems-ch8-filetop-8-6-11]]
- Source: [[systems-performance-filesystems-ch8-ext4slower-8-6-14]]
- Source: [[systems-performance-disks-ch9-concepts-measuring-time-9-3-1]]
- Source: [[systems-performance-disks-ch9-methodology-workload-characterization-9-5-4]]
- Source: [[systems-performance-disks-ch9-observability-perf-9-6-5]]
- Source: [[systems-performance-disks-ch9-observability-biostacks-9-6-9]]
- Source: [[systems-performance-disks-ch9-observability-blktrace-intro-default-9-6-10a]]
- Source: [[systems-performance-disks-ch9-observability-blktrace-actions-filter-9-6-10b]]
- Source: [[systems-performance-disks-ch9-observability-bpftrace-oneliners-9-6-11a]]
- Source: [[systems-performance-disks-ch9-observability-bpftrace-latency-errors-9-6-11d]]
- Source: [[systems-performance-disks-ch9-observability-scsi-logging-9-6-14]]
- Source: [[systems-performance-network-ch10-observability-bpf-tracing-tools-table-10-6-b]]
- Source: [[systems-performance-network-ch10-observability-tcplife-tcp-session-lifecycle-bpf-10-6-9]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-socket-layer-socketio-10-6-12b]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-tcp-tcpsynbl-backlog-10-6-12c]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-event-sources-table-10-6-12d]]
- Related concepts:
  - [[counters-statistics-metrics]]
  - [[latency-analysis]]
  - [[drill-down-analysis]]
  - [[model-classify-intervene]]

