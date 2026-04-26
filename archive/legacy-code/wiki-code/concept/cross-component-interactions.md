# Cross-component interactions

- Tag: structure

## Definition

**Cross-component interactions** are cases where the behavior or cost of a change in one component is dominated by how it composes with other components (protocols, caches, schedulers, layers), so the local optimization does not yield the expected end-to-end improvement.

## Scope note

This is about *composition effects* (second-order effects) rather than a single component’s internal efficiency.

**Platform coupling** (for this wiki’s CPU chapter) includes **NUMA**, **IRQ handling**, **cgroups / quotas**, and **governors / power states**—cases where scheduling, topology, firmware, and policy change the cost or visibility of the same logical work. That is distinct from **microarchitectural** effects inside a core’s pipeline and memory hierarchy (see [[resource-vs-implementation-bottleneck]] and [[caching]]), where the issue is often locality, contention, or false sharing at a finer grain without changing the platform policy story.

## Relation

- Motivates measuring and profiling whole-system behavior in [[network-algorithmics]] rather than assuming local improvements compose.
- A common failure mode for performance work, linking to [[model-classify-intervene]].

## Links

- Source: [[network-algorithmics-3-5-caveats]]
- Source: [[systems-performance-off-cpu-narrowing-filters-5-4-2]]
- Source: [[systems-performance-cpu-models-run-queues-scheduler-latency-6-2-3]]
- Source: [[systems-performance-cpu-saturation-preemption-and-quotas-6-3-10-11]]
- Source: [[systems-performance-cpu-priority-inversion-and-inheritance-6-3-12]]
- Source: [[systems-performance-cpu-multiprocess-multithreading-tradeoffs-6-3-13]]
- Source: [[systems-performance-cpu-p-states-and-c-states-6-4-1]]
- Source: [[systems-performance-cpu-interconnect-scalability-memory-system-6-4-1]]
- Source: [[systems-performance-cpu-heterogeneous-accelerators-observability-6-4-1]]
- Source: [[systems-performance-cpu-kernel-scheduler-functions-and-locality-6-4-2]]
- Source: [[systems-performance-cpu-scheduling-classes-policies-workload-shape-6-4-2]]
- Source: [[systems-performance-cpu-idle-numa-topology-scheduler-awareness-6-4-2]]
- Source: [[systems-performance-cpu-interrupt-gpu-tools-and-distribution-visualizations-6-6-19-6-7-4]]
- Source: [[systems-performance-cpu-tuning-governors-affinity-cgroups-6-9-4-8]]
- Source: [[systems-performance-cpu-priority-resource-controls-and-cpu-binding-6-5-8-10]]
- Source: [[systems-performance-memory-chapter-intro-and-parts-7]]
- Source: [[systems-performance-memory-architecture-intro-dram-latency-7-3-1a]]
- Source: [[systems-performance-memory-architecture-uma-numa-buses-7-3-1b]]
- Source: [[systems-performance-memory-architecture-ddr-multichannel-7-3-1c]]
- Source: [[systems-performance-memory-architecture-swappiness-swap-cgroups-7-3-2b]]
- Source: [[systems-performance-memory-architecture-free-lists-reaping-scan-7-3-2c]]
- Source: [[systems-performance-memory-kernel-slab-and-magazines-7-3-3d]]
- Source: [[systems-performance-memory-slab-adoption-and-slub-7-3-3e]]
- Source: [[systems-performance-memory-allocator-jemalloc-arenas-7-3-3h]]
- Source: [[systems-performance-memory-methodology-use-method-7-4-2]]
- Source: [[systems-performance-memory-methodology-static-resource-micro-shrinking-7-4-7-10]]
- Source: [[systems-performance-memory-observability-psi-swapon-7-5-2-3]]
- Source: [[systems-performance-memory-observability-slab-numa-7-5-5-6]]
- Source: [[systems-performance-memory-tuning-numa-bind-7-6-4]]
- Source: [[systems-performance-memory-tuning-cgroup-limits-7-6-5]]
- Source: [[systems-performance-memory-tuning-allocators-7-6-3]]
- Source: [[systems-performance-filesystems-ch8-direct-async-mmap-meta-8-3-8-11]]
- Source: [[systems-performance-filesystems-ch8-logical-physical-io-8-3-12]]
- Source: [[systems-performance-filesystems-ch8-caches-page-flush-8-4-3a]]
- Source: [[systems-performance-filesystems-ch8-fs-types-btrfs-8-4-5e]]
- Source: [[systems-performance-filesystems-ch8-volumes-pools-8-4-6]]
- Source: [[systems-performance-filesystems-ch8-fs-types-zfs-8-4-5d]]
- Source: [[systems-performance-filesystems-ch8-cache-separation-microbench-8-5-6-8]]
- Source: [[systems-performance-filesystems-ch8-sar-cache-dentry-8-6-5]]
- Source: [[systems-performance-disks-ch9-models-9-2]]
- Source: [[systems-performance-disks-ch9-concepts-caching-patterns-9-3-3-5]]
- Source: [[systems-performance-disks-ch9-concepts-utilization-saturation-iowait-9-3-9-11]]
- Source: [[systems-performance-disks-ch9-concepts-async-mismatch-9-3-12-13]]
- Source: [[systems-performance-disks-ch9-architecture-hdd-advanced-smr-ddc-9-4-1b]]
- Source: [[systems-performance-disks-ch9-architecture-interfaces-pmem-9-4-2]]
- Source: [[systems-performance-disks-ch9-architecture-storage-raid-intro-9-4-3a]]
- Source: [[systems-performance-disks-ch9-architecture-raid-table-rmw-9-4-3b]]
- Source: [[systems-performance-disks-ch9-architecture-arrays-nas-9-4-3c]]
- Source: [[systems-performance-disks-ch9-methodology-use-method-9-5-2]]
- Source: [[systems-performance-disks-ch9-visualizations-scatter-9-7-2]]
- Source: [[systems-performance-disks-ch9-tuning-intro-ionice-9-9-1a]]
- Source: [[systems-performance-network-ch10-models-protocol-stack-10-2-3]]
- Source: [[systems-performance-network-ch10-concepts-networks-and-routing-10-3-1]]
- Source: [[systems-performance-network-ch10-methodology-resource-controls-10-5-9]]
- Source: [[systems-performance-network-ch10-experimentation-intro-probes-vs-observability-10-7]]
- Source: [[systems-performance-network-ch10-experimentation-traceroute-ttl-path-dynamics-firewalls-10-7-2]]
- Related concepts/insights:
  - [[network-algorithmics]]
  - [[model-classify-intervene]]
- Source: [[systems-performance-network-ch10-tuning-msg-zerocopy-send-flag-10-8-2b]]
