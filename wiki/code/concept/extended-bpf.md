# Extended BPF (eBPF)

- Tag: mechanism

## Definition

**Extended BPF (eBPF)** is a kernel-managed execution environment for loading verified, sandboxed programs that run in kernel mode with restricted access mediated by a stable “helper” API.

## Relation

- Role: mechanism (a controlled way to extend kernel behavior without shipping a full custom kernel module for every change).
- Sits alongside the classical [[kernel-user-boundary]]: BPF programs run in kernel mode, but with verification and constrained interfaces rather than arbitrary kernel code paths.
- Often used to implement observability and policy hooks; performance work treats BPF as another kernel execution context that can shift work between user and kernel (see [[shift-computation-in-time]] when relevant).

## Links

- Source: [[systems-performance-operating-systems-terminology-3-1]]
- Source: [[systems-performance-operating-systems-background-3-2]]
- Source: [[systems-performance-linux-kernel-developments-3-4-1]]
- Source: [[systems-performance-kpti-meltdown-3-4-3]]
- Source: [[systems-performance-extended-bpf-3-4-4]]
- Source: [[systems-performance-chapter-3-references-3-8]]
- Source: [[systems-performance-tracepoints-4-3-5]]
- Source: [[systems-performance-kprobes-4-3-6]]
- Source: [[systems-performance-tracing-tools-survey-4-5]]
- Source: [[systems-performance-chapter-4-exercises-4-7]]
- Source: [[systems-performance-bcc-profile-kernel-side-aggregation-5-5-2]]
- Source: [[systems-performance-offcputime-aggregation-and-duration-filters-5-5-3]]
- Source: [[systems-performance-bpftrace-custom-aggregation-probe-ladder-5-5-7]]
- Source: [[systems-performance-gotchas-missing-stacks-remedies-and-unwinder-5-6-2]]
- Source: [[systems-performance-cpu-observability-bpf-profile-scheduler-and-softirq-6-6-14-18]]
- Source: [[systems-performance-cpu-interrupt-gpu-tools-and-distribution-visualizations-6-6-19-6-7-4]]
- Source: [[systems-performance-memory-observability-trace-other-7-5-11-14]]
- Source: [[systems-performance-filesystems-ch8-obs-tools-intro-8-6]]
- Source: [[systems-performance-filesystems-ch8-strace-syscall-latency-8-6-7]]
- Source: [[systems-performance-filesystems-ch8-opensnoop-8-6-10]]
- Source: [[systems-performance-filesystems-ch8-filetop-8-6-11]]
- Source: [[systems-performance-filesystems-ch8-cachestat-8-6-12]]
- Source: [[systems-performance-filesystems-ch8-ext4dist-histograms-8-6-13]]
- Source: [[systems-performance-filesystems-ch8-ext4slower-8-6-14]]
- Source: [[systems-performance-filesystems-ch8-bpftrace-oneliners-8-6-15a]]
- Source: [[systems-performance-filesystems-ch8-bpftrace-syscall-semantics-8-6-15b]]
- Source: [[systems-performance-filesystems-ch8-bpftrace-vfs-fs-internals-8-6-15c]]
- Source: [[systems-performance-filesystems-ch8-other-tools-8-6-17]]
- Source: [[systems-performance-disks-ch9-observability-intro-table-9-6]]
- Source: [[systems-performance-disks-ch9-observability-biolatency-9-6-6]]
- Source: [[systems-performance-disks-ch9-observability-biosnoop-9-6-7]]
- Source: [[systems-performance-disks-ch9-observability-biostacks-9-6-9]]
- Source: [[systems-performance-disks-ch9-observability-bpftrace-oneliners-9-6-11a]]
- Source: [[systems-performance-disks-ch9-observability-bpftrace-io-size-9-6-11b]]
- Source: [[systems-performance-disks-ch9-observability-bpftrace-issue-insert-attribution-9-6-11c]]
- Source: [[systems-performance-disks-ch9-observability-bpftrace-latency-errors-9-6-11d]]
- Source: [[systems-performance-network-ch10-architecture-software-queueing-disciplines-defaults-bpf-10-4-3e]]
- Source: [[systems-performance-network-ch10-architecture-software-kernel-bypass-xdp-zerocopy-observability-10-4-3i]]
- Source: [[systems-performance-network-ch10-observability-bpf-tracing-tools-table-10-6-b]]
- Source: [[systems-performance-network-ch10-observability-tcplife-tcp-session-lifecycle-bpf-10-6-9]]
- Source: [[systems-performance-network-ch10-observability-tcptop-process-tcp-throughput-bpf-10-6-10]]
- Source: [[systems-performance-network-ch10-observability-tcpretrans-kernel-retransmit-events-10-6-11]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-one-liners-probe-cost-10-6-12a]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-socket-layer-socketio-10-6-12b]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-tcp-tcpsynbl-backlog-10-6-12c]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-event-sources-table-10-6-12d]]
- Source: [[systems-performance-network-ch10-observability-other-tools-table-10-7-crossrefs-10-6-15a]]
- Source: [[systems-performance-network-ch10-observability-other-tools-linux-sources-monitoring-10-6-15b]]
- Source: [[systems-performance-network-ch10-tuning-bql-cgroups-qdisc-tuned-10-8-1d]]
- Related concepts:
  - [[kernel-user-boundary]]
  - [[system-call]]
  - [[resource-vs-implementation-bottleneck]]
