# Process abstraction

- Tag: abstraction

## Definition

The **process abstraction** is an operating-system environment for executing a program: isolation (e.g., address space, descriptors) plus one or more schedulable threads of execution.

## Scope note

This is an operating-system abstraction for managing interruptions and sharing a CPU among multiple activities safely.
Each thread still executes a mostly sequential instruction stream, while the OS multiplexes CPUs and enforces isolation at the process boundary.

Runtimes may add another scheduling layer above OS threads (e.g., lightweight tasks scheduled onto a thread pool) to reduce kernel involvement for common interleavings—without removing the need for OS threads when true parallelism or blocking kernel work is involved.

## Relation

- Implemented via mechanisms such as [[context-switching]] and scheduling.
- Related to [[abstraction-design-principles]] as an example where the abstraction’s mechanism cost and hidden constraints can matter for performance.
- Threads are the schedulable CPU contexts grouped under one process environment.

## Links

- Source: [[network-algorithmics-2-4-1-processes]]
- Source: [[systems-performance-operating-systems-terminology-3-1]]
- Source: [[systems-performance-linux-intro-3-4]]
- Source: [[systems-performance-exercises-3-7]]
- Source: [[systems-performance-concurrency-parallelism-and-user-schedulers-5-2-5]]
- Source: [[systems-performance-thread-pool-and-seda-patterns-5-2-5]]
- Source: [[systems-performance-shared-memory-and-sync-primitives-5-2-5]]
- Source: [[systems-performance-cpu-binding-risks-and-performance-mantras-5-2-7-8]]
- Source: [[systems-performance-thread-state-nine-state-model-5-4-5]]
- Source: [[systems-performance-cpu-terminology-6-1]]
- Source: [[systems-performance-cpu-priority-inversion-and-inheritance-6-3-12]]
- Source: [[systems-performance-cpu-multiprocess-multithreading-tradeoffs-6-3-13]]
- Source: [[systems-performance-cpu-kernel-scheduler-functions-and-locality-6-4-2]]
- Source: [[systems-performance-cpu-scheduling-classes-policies-workload-shape-6-4-2]]
- Source: [[systems-performance-cpu-idle-numa-topology-scheduler-awareness-6-4-2]]
- Source: [[systems-performance-cpu-priority-resource-controls-and-cpu-binding-6-5-8-10]]
- Source: [[systems-performance-cpu-tuning-compiler-scheduler-sysctl-6-9-1-3]]
- Source: [[systems-performance-memory-terminology-7-1]]
- Source: [[systems-performance-memory-concepts-allocators-7-2-8]]
- Source: [[systems-performance-memory-concepts-shared-memory-pss-7-2-9]]
- Source: [[systems-performance-memory-concepts-word-size-7-2-11]]
- Source: [[systems-performance-memory-process-address-space-segments-7-3-3a]]
- Source: [[systems-performance-memory-heap-growth-vs-leak-7-3-3b]]
- Related concepts:
  - [[context-switching]]
  - [[abstraction-design-principles]]

