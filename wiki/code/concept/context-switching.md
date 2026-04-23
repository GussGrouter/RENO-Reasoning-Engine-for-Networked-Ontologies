# Context switching

- Tag: mechanism

## Definition

**Context switching** saves the execution state of one activity and restores the saved state of another, allowing a processor to alternate among tasks over time.

## Scope note

This is a general mechanism: “switch active state” appears in OS schedulers, runtimes, and event-driven systems.

Designs that map each concurrent unit of work to a dedicated blocking OS thread can inflate switch volume and scheduler load even when CPUs are not “doing useful work,” because blocking and wakeups are still state transitions.

## Relation

- A core mechanism that realizes [[process-abstraction]].
- Its overhead can turn scheduling and interrupts into an implementation bottleneck, linking to [[resource-vs-implementation-bottleneck]].

## Links

- Source: [[network-algorithmics-2-4-1-processes]]
- Source: [[systems-performance-operating-systems-terminology-3-1]]
- Source: [[systems-performance-operating-systems-background-3-2]]
- Source: [[systems-performance-kpti-meltdown-3-4-3]]
- Source: [[systems-performance-microkernels-and-hybrid-kernels-3-5-3]]
- Source: [[systems-performance-exercises-3-7]]
- Source: [[systems-performance-concurrency-parallelism-and-user-schedulers-5-2-5]]
- Source: [[systems-performance-shared-memory-and-sync-primitives-5-2-5]]
- Source: [[systems-performance-nonblocking-io-async-models-5-2-6]]
- Source: [[systems-performance-processor-affinity-locality-5-2-7]]
- Source: [[systems-performance-cpu-binding-risks-and-performance-mantras-5-2-7-8]]
- Source: [[systems-performance-thread-state-nine-state-model-5-4-5]]
- Source: [[systems-performance-cpu-models-run-queues-scheduler-latency-6-2-3]]
- Source: [[systems-performance-chapter-5-exercises-under-load-lab-b-5-7]]
- Source: [[systems-performance-cpu-multiprocess-multithreading-tradeoffs-6-3-13]]
- Source: [[systems-performance-cpu-kernel-scheduler-functions-and-locality-6-4-2]]
- Related concepts:
  - [[process-abstraction]]
  - [[resource-vs-implementation-bottleneck]]

