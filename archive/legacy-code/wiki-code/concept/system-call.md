# System call

- Tag: mechanism

## Definition

A **system call** is a protected request from an unprivileged program to invoke an operating-system service, typically crossing into a more privileged execution mode.

## Scope note

System calls form a controlled boundary between application code and OS internals; they are often materially more expensive than an in-process function call.

## Relation

- One mechanism that enforces the [[kernel-user-boundary]].
- Can be an implementation bottleneck in high-rate workloads (see [[resource-vs-implementation-bottleneck]]).

## Links

- Source: [[network-algorithmics-2-4-3-system-calls-io]]
- Source: [[systems-performance-operating-systems-terminology-3-1]]
- Source: [[systems-performance-operating-systems-background-3-2]]
- Source: [[systems-performance-kernels-3-3]]
- Source: [[systems-performance-kpti-meltdown-3-4-3]]
- Source: [[systems-performance-exercises-3-7]]
- Source: [[systems-performance-proc-observability-4-3-1]]
- Source: [[systems-performance-sysfs-observability-4-3-2]]
- Source: [[systems-performance-io-size-tradeoffs-5-2-1]]
- Source: [[systems-performance-nonblocking-io-async-models-5-2-6]]
- Source: [[systems-performance-syscall-analysis-boundary-instrumentation-5-4-3]]
- Source: [[systems-performance-perf-profiling-syscall-trace-and-io-5-5-1]]
- Source: [[systems-performance-strace-ptrace-overhead-and-buffered-tracing-5-5-4]]
- Source: [[systems-performance-syscount-ranking-and-follow-on-5-5-6]]
- Related concepts:
  - [[kernel-user-boundary]]
  - [[resource-vs-implementation-bottleneck]]

