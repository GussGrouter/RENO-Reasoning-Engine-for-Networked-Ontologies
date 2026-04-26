# Kernel/user boundary

- Tag: structure

## Definition

The **kernel/user boundary** separates privileged operating-system code from unprivileged application code, enforcing protection and controlled access to shared resources.

## Scope note

This boundary is an implementation constraint: crossing it is deliberately restricted and typically incurs overhead.

## Relation

- Enforced via mechanisms such as [[system-call]].
- Links OS protection goals to performance tradeoffs in the fast path (see [[fast-path-slow-path]]).
- Modern kernels may also host verified kernel-mode extensions such as [[extended-bpf]], which still interact with this boundary, but through constrained APIs rather than arbitrary kernel modules.

## Links

- Source: [[network-algorithmics-2-4-3-system-calls-io]]
- Source: [[systems-performance-operating-systems-terminology-3-1]]
- Source: [[systems-performance-operating-systems-background-3-2]]
- Source: [[systems-performance-kernels-3-3]]
- Source: [[systems-performance-kpti-meltdown-3-4-3]]
- Source: [[systems-performance-exercises-3-7]]
- Source: [[systems-performance-proc-observability-4-3-1]]
- Source: [[systems-performance-sysfs-observability-4-3-2]]
- Source: [[systems-performance-netlink-observability-4-3-4]]
- Source: [[systems-performance-kprobes-4-3-6]]
- Source: [[systems-performance-uprobes-4-3-7]]
- Source: [[systems-performance-usdt-4-3-8]]
- Source: [[systems-performance-pmc-fundamentals-4-3-9]]
- Source: [[systems-performance-cpu-cache-coherency-latency-mmu-tlb-6-4-1]]
- Source: [[systems-performance-chapter-4-exercises-4-7]]
- Source: [[systems-performance-concurrency-parallelism-and-user-schedulers-5-2-5]]
- Source: [[systems-performance-nonblocking-io-async-models-5-2-6]]
- Source: [[systems-performance-cpu-profiling-kernel-vs-user-5-4-1]]
- Source: [[systems-performance-syscall-analysis-boundary-instrumentation-5-4-3]]
- Source: [[systems-performance-chapter-5-exercises-application-profile-role-and-metrics-5-7]]
- Source: [[systems-performance-cpu-concepts-instruction-lifecycle-and-stall-cycles-6-3-2]]
- Source: [[systems-performance-cpu-concepts-ipc-utilization-and-user-kernel-time-6-3-7-9]]
- Source: [[systems-performance-filesystems-ch8-bpftrace-oneliners-8-6-15a]]
- Source: [[systems-performance-filesystems-ch8-bpftrace-syscall-semantics-8-6-15b]]
- Source: [[systems-performance-disks-ch9-architecture-os-block-stack-9-4-4]]
- Related concepts:
  - [[system-call]]
  - [[fast-path-slow-path]]
  - [[extended-bpf]]
  - [[kernel-architecture-models]]

