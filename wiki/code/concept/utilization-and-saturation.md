# Utilization and saturation

- Tag: structure

## Definition

**Utilization** measures how busy a resource is over an interval (time actively doing work, or capacity consumed for storage resources). **Saturation** measures the degree to which a resource has queued work it cannot service.

## Scope note

High utilization does not necessarily imply saturation; saturation concerns queued backlog and delayed service.

Utilization can be discussed as time-based “percent busy” (e.g., \(U = B/T\)) or as capacity-based “percent of capacity”; 100% busy does not necessarily mean 100% capacity.

## Relation

These concepts support bottleneck diagnosis by separating “busy” from “overloaded with queueing”.

For CPUs, some utilization definitions count **memory stall cycles** as busy time—high utilization can therefore coexist with low effective instruction throughput; treat that as a **semantic** issue for what “%CPU” means, not only a capacity issue ([[measurement-validity]]).

On CPUs, **saturation** can also show up as **run-queue delay**, **scheduler latency**, or **throttling** (cgroups / quotas)—even when **CPU%** is not near 100%, because those signals measure **waiting or policy-limited service**, not only “cycles executing instructions.”

## Links

- Source: [[systems-performance-terminology-2-1]]
- Source: [[systems-performance-exercises-3-7]]
- Source: [[systems-performance-delay-accounting-4-3-3]]
- Source: [[systems-performance-use-method-software-resources-5-4-4]]
- Source: [[systems-performance-cpu-models-run-queues-scheduler-latency-6-2-3]]
- Source: [[systems-performance-cpu-concepts-ipc-utilization-and-user-kernel-time-6-3-7-9]]
- Source: [[systems-performance-cpu-saturation-preemption-and-quotas-6-3-10-11]]
- Source: [[systems-performance-cpu-use-method-cpu-checklist-6-5-2]]
- Source: [[systems-performance-cpu-cycle-analysis-and-performance-monitoring-6-5-5-6]]
- Source: [[systems-performance-cpu-static-performance-tuning-checklist-6-5-7]]
- Source: [[systems-performance-cpu-priority-resource-controls-and-cpu-binding-6-5-8-10]]
- Source: [[systems-performance-cpu-observability-bpf-profile-scheduler-and-softirq-6-6-14-18]]
- Source: [[systems-performance-cpu-tuning-governors-affinity-cgroups-6-9-4-8]]
- Source: [[systems-performance-memory-chapter-intro-and-parts-7]]
- Source: [[systems-performance-memory-terminology-7-1]]
- Source: [[systems-performance-memory-concepts-paging-7-2-2]]
- Source: [[systems-performance-memory-concepts-utilization-saturation-7-2-7]]
- Source: [[systems-performance-memory-concepts-overcommit-7-2-4]]
- Source: [[systems-performance-memory-architecture-linux-freeing-ladder-7-3-2a]]
- Source: [[systems-performance-memory-architecture-swappiness-swap-cgroups-7-3-2b]]
- Source: [[systems-performance-memory-architecture-free-lists-reaping-scan-7-3-2c]]
- Source: [[systems-performance-memory-heap-growth-vs-leak-7-3-3b]]
- Source: [[systems-performance-memory-allocator-jemalloc-arenas-7-3-3h]]
- Source: [[systems-performance-memory-methodology-use-method-7-4-2]]
- Source: [[systems-performance-memory-methodology-cycle-and-monitoring-7-4-4-5]]
- Source: [[systems-performance-memory-observability-psi-swapon-7-5-2-3]]
- Source: [[systems-performance-memory-tuning-sysctl-vm-7-6-1]]
- Source: [[systems-performance-filesystems-ch8-top-vmstat-8-6-3-4]]
- Source: [[systems-performance-disks-ch9-concepts-utilization-saturation-iowait-9-3-9-11]]
- Source: [[systems-performance-disks-ch9-methodology-use-method-9-5-2]]
- Source: [[systems-performance-disks-ch9-methodology-scaling-9-5-10]]
- Source: [[systems-performance-disks-ch9-observability-iostat-9-6-1]]
- Source: [[systems-performance-disks-ch9-observability-psi-9-6-3]]
- Source: [[systems-performance-disks-ch9-visualizations-utilization-heatmap-9-7-5]]
- Source: [[systems-performance-disks-ch9-experimentation-random-read-9-8-4]]
- Source: [[systems-performance-disks-ch9-exercises-scaffold-a-9-10a]]
- Source: [[systems-performance-network-ch10-concepts-connection-backlog-10-3-7]]
- Source: [[systems-performance-network-ch10-concepts-utilization-10-3-10]]
- Source: [[systems-performance-disks-ch9-exercises-scaffold-b-9-10b]]
- Related concepts:
  - [[systems-performance]]
  - [[resource-vs-implementation-bottleneck]]
  - [[measurement-validity]]

