# Kernel architecture models

- Tag: abstraction

## Definition

**Kernel architecture models** classify how operating system responsibilities are partitioned across kernel mode vs user mode, notably monolithic kernels, microkernels, unikernels, and hybrid designs.

## Relation

- Role: abstraction (a vocabulary for comparing where privileged code lives and what crosses the [[kernel-user-boundary]]).
- Monolithic kernels concentrate subsystems in one privileged codebase; microkernels push much functionality to user-mode servers; unikernels fuse application and kernel into one deployable image; hybrids mix strategies.
- Implementation choices change which costs dominate (syscalls, IPC, verification, maintenance), connecting to [[resource-vs-implementation-bottleneck]].

## Links

- Source: [[systems-performance-operating-systems-background-3-2]]
- Source: [[systems-performance-kernels-3-3]]
- Source: [[systems-performance-linux-intro-3-4]]
- Source: [[systems-performance-other-topics-intro-3-5]]
- Source: [[systems-performance-unikernels-3-5-2]]
- Source: [[systems-performance-microkernels-and-hybrid-kernels-3-5-3]]
- Source: [[systems-performance-distributed-operating-systems-3-5-4]]
- Source: [[systems-performance-chapter-3-references-3-8]]
- Source: [[systems-performance-chapter-3-additional-reading-3-8-1]]
- Source: [[systems-performance-filesystems-ch8-architecture-intro-stack-8-4-1]]
- Source: [[systems-performance-filesystems-ch8-bpftrace-vfs-fs-internals-8-6-15c]]
- Related concepts:
  - [[kernel-user-boundary]]
  - [[system-call]]
  - [[extended-bpf]]
  - [[resource-vs-implementation-bottleneck]]
