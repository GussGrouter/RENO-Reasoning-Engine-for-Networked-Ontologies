# Resource vs implementation bottleneck

- Tag: structure

## Definition

A performance bottleneck in a system can be:

- **Resource bottleneck**: limited by underlying hardware speed (worked around by faster hardware, at cost).
- **Implementation bottleneck**: the design/implementation makes the system slow despite adequate resources (addressed by changing the implementation).

## Relation

Distinguishing these helps target the right remedy: scale resources vs redesign the implementation. Methods like [[network-algorithmics]] primarily target implementation bottlenecks.

Metric choice (counters/metrics vs event-driven signals) affects which bottleneck class appears dominant.

Some “implementation” bottlenecks are physical-layout artifacts: independent logical locks or counters that share a cache line can serialize CPUs via coherency traffic even when algorithms look fine-grained on paper.

**Layout-induced contention** (false sharing, line ping-pong) is already an instance of this class—promoting a second “layout contention” concept would duplicate the decision rule already stated here.

## Links

- Source: [[network-algorithmics-intro-p20-24]]
- Source: [[systems-performance-kernels-3-3]]
- Source: [[systems-performance-kpti-meltdown-3-4-3]]
- Source: [[systems-performance-pgo-kernels-3-5-1]]
- Source: [[systems-performance-netlink-observability-4-3-4]]
- Source: [[systems-performance-other-observability-sources-4-3-10]]
- Source: [[systems-performance-application-objectives-5-1-1]]
- Source: [[systems-performance-algorithm-complexity-scaling-5-1-4]]
- Source: [[systems-performance-io-size-tradeoffs-5-2-1]]
- Source: [[systems-performance-buffering-polling-scalability-5-2-3-4]]
- Source: [[systems-performance-thread-pool-and-seda-patterns-5-2-5]]
- Source: [[systems-performance-shared-memory-and-sync-primitives-5-2-5]]
- Source: [[systems-performance-lock-fastpath-midpath-slowpath-rcu-5-2-5]]
- Source: [[systems-performance-hash-lock-striping-and-chains-5-2-5]]
- Source: [[systems-performance-lock-scaling-and-false-sharing-5-2-5]]
- Source: [[systems-performance-processor-affinity-locality-5-2-7]]
- Source: [[systems-performance-cpu-binding-risks-and-performance-mantras-5-2-7-8]]
- Source: [[systems-performance-lock-contention-and-hold-time-5-4-6]]
- Source: [[systems-performance-bpftrace-custom-aggregation-probe-ladder-5-5-7]]
- Source: [[systems-performance-chapter-5-exercises-conceptual-review-5-7]]
- Source: [[systems-performance-chapter-5-exercises-under-load-lab-b-5-7]]
- Source: [[systems-performance-cpu-concepts-pipeline-width-and-smt-6-3-3-6]]
- Source: [[systems-performance-cpu-multiprocess-multithreading-tradeoffs-6-3-13]]
- Source: [[systems-performance-cpu-parallelism-footprint-and-word-size-6-3-14]]
- Source: [[systems-performance-cpu-on-chip-cache-hierarchy-and-llc-6-4-1]]
- Source: [[systems-performance-cpu-cache-coherency-latency-mmu-tlb-6-4-1]]
- Source: [[systems-performance-cpu-interconnect-scalability-memory-system-6-4-1]]
- Source: [[systems-performance-memory-concepts-allocators-7-2-8]]
- Source: [[systems-performance-memory-concepts-working-set-size-7-2-10]]
- Source: [[systems-performance-memory-architecture-cpu-caches-ch7-7-3-1d]]
- Source: [[systems-performance-memory-architecture-free-lists-reaping-scan-7-3-2c]]
- Source: [[systems-performance-memory-allocator-design-tradeoffs-7-3-3c]]
- Source: [[systems-performance-memory-kernel-slab-and-magazines-7-3-3d]]
- Source: [[systems-performance-memory-slab-adoption-and-slub-7-3-3e]]
- Source: [[systems-performance-memory-allocator-glibc-dlmalloc-style-7-3-3f]]
- Source: [[systems-performance-memory-allocator-tcmalloc-thread-cache-7-3-3g]]
- Source: [[systems-performance-memory-allocator-jemalloc-arenas-7-3-3h]]
- Source: [[systems-performance-network-ch10-concepts-local-connections-loopback-uds-10-3-11]]
- Source: [[systems-performance-network-ch10-architecture-hardware-interfaces-and-controllers-10-4-2a]]
- Source: [[systems-performance-network-ch10-architecture-software-segmentation-offload-gso-gro-tso-10-4-3d]]
- Source: [[systems-performance-network-ch10-methodology-micro-benchmarking-10-5-10]]
- Source: [[systems-performance-network-ch10-observability-ethtool-driver-stats-offloads-10-6-8]]
- Source: [[systems-performance-network-ch10-tuning-bql-cgroups-qdisc-tuned-10-8-1d]]
- Source: [[systems-performance-memory-methodology-cycle-and-monitoring-7-4-4-5]]
- Source: [[systems-performance-memory-methodology-leak-detection-7-4-6]]
- Source: [[systems-performance-memory-observability-sar-7-5-4]]
- Source: [[systems-performance-memory-observability-slab-numa-7-5-5-6]]
- Source: [[systems-performance-memory-tuning-huge-pages-7-6-2]]
- Source: [[systems-performance-filesystems-ch8-intro-outline-8]]
- Source: [[systems-performance-filesystems-ch8-concept-latency-8-3-1]]
- Source: [[systems-performance-filesystems-ch8-random-prefetch-8-3-3-4]]
- Source: [[systems-performance-filesystems-ch8-direct-async-mmap-meta-8-3-8-11]]
- Source: [[systems-performance-filesystems-ch8-logical-physical-io-8-3-12]]
- Source: [[systems-performance-filesystems-ch8-fs-features-8-4-4]]
- Source: [[systems-performance-filesystems-ch8-fs-types-ffs-8-4-5a]]
- Source: [[systems-performance-filesystems-ch8-fs-types-zfs-8-4-5d]]
- Source: [[systems-performance-filesystems-ch8-volumes-pools-8-4-6]]
- Source: [[systems-performance-filesystems-ch8-disk-latency-analysis-open-8-5-1-2]]
- Source: [[systems-performance-filesystems-ch8-bonnie-8-7-2a]]
- Source: [[systems-performance-disks-ch9-architecture-storage-raid-intro-9-4-3a]]
- Source: [[systems-performance-disks-ch9-methodology-static-tuning-9-5-6]]
- Source: [[systems-performance-disks-ch9-observability-megacli-9-6-12]]
- Source: [[systems-performance-disks-ch9-tuning-controller-9-9-3]]
- Source: [[systems-performance-network-ch10-tuning-socket-options-table-10-8-10-8-2a]]
- Source: [[systems-performance-network-ch10-tuning-msg-zerocopy-send-flag-10-8-2b]]
- Related concepts:
  - [[network-algorithmics]]
  - [[throughput-latency-metrics]]
- Related insights:
  - [[model-classify-intervene]]

