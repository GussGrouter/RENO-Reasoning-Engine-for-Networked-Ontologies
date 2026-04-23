# Micro-benchmarking

- Tag: heuristic

## Definition

**Micro-benchmarking** measures performance using small, artificial workloads that target a specific operation or subsystem, to reduce confounding factors and isolate bottlenecks.

## Relation

- Role: method (an experimental measurement approach for isolating a component).
- Complements [[observability-vs-experimentation]]: micro-benchmarks are typically experimentation; production observability can cross-check and catch mismatches.
- Supports [[model-classify-intervene]] by providing targeted evidence to classify bottlenecks before choosing interventions.

## Links

- Source: [[systems-performance-micro-benchmarking-2-5-19]]
- Source: [[systems-performance-kernel-comparisons-3-6]]
- Source: [[systems-performance-observing-observability-4-6]]
- Source: [[systems-performance-cpu-cache-coherency-latency-mmu-tlb-6-4-1]]
- Source: [[systems-performance-cpu-micro-benchmarking-decision-rules-6-5-11]]
- Source: [[systems-performance-cpu-experimentation-adhoc-and-sysbench-6-8]]
- Source: [[systems-performance-cpu-bios-processor-options-6-9-10]]
- Source: [[systems-performance-memory-methodology-usage-checklist-7-4-3b]]
- Source: [[systems-performance-memory-methodology-static-resource-micro-shrinking-7-4-7-10]]
- Source: [[systems-performance-memory-tuning-allocators-7-6-3]]
- Source: [[systems-performance-filesystems-ch8-ops-not-equal-8-3-13]]
- Source: [[systems-performance-filesystems-ch8-methodology-intro-8-5]]
- Source: [[systems-performance-filesystems-ch8-cache-separation-microbench-8-5-6-8]]
- Source: [[systems-performance-filesystems-ch8-performance-monitoring-8-5-4]]
- Source: [[systems-performance-filesystems-ch8-table-8-5-expectations]]
- Source: [[systems-performance-filesystems-ch8-experimentation-dd-8-7-1]]
- Source: [[systems-performance-filesystems-ch8-bonnie-8-7-2a]]
- Source: [[systems-performance-filesystems-ch8-fio-8-7-2b]]
- Source: [[systems-performance-filesystems-ch8-filebench-8-7-2c]]
- Source: [[systems-performance-filesystems-ch8-cache-flushing-8-7-3]]
- Source: [[systems-performance-filesystems-ch8-exercises-8-9]]
- Source: [[systems-performance-disks-ch9-concepts-time-scales-9-3-2]]
- Source: [[systems-performance-disks-ch9-concepts-io-size-iops-commands-9-3-6-8]]
- Source: [[systems-performance-disks-ch9-architecture-ssd-flash-9-4-1c]]
- Source: [[systems-performance-disks-ch9-methodology-performance-monitoring-9-5-3]]
- Source: [[systems-performance-disks-ch9-methodology-cache-resource-microbench-9-5-7-9]]
- Source: [[systems-performance-disks-ch9-methodology-scaling-9-5-10]]
- Source: [[systems-performance-disks-ch9-experimentation-intro-dd-9-8-1]]
- Source: [[systems-performance-disks-ch9-experimentation-custom-load-9-8-2]]
- Source: [[systems-performance-disks-ch9-experimentation-microbench-hdparm-9-8-3]]
- Source: [[systems-performance-disks-ch9-experimentation-random-read-9-8-4]]
- Source: [[systems-performance-disks-ch9-experimentation-ioping-9-8-5]]
- Source: [[systems-performance-network-ch10-methodology-micro-benchmarking-10-5-10]]
- Source: [[systems-performance-network-ch10-experimentation-intro-probes-vs-observability-10-7]]
- Source: [[systems-performance-network-ch10-experimentation-pathchar-pchar-bandwidth-probing-10-7-3]]
- Source: [[systems-performance-network-ch10-experimentation-iperf-throughput-parallel-intervals-10-7-4]]
- Source: [[systems-performance-network-ch10-experimentation-netperf-tcp-rr-latency-10-7-5]]
- Source: [[systems-performance-network-ch10-experimentation-tc-netem-loss-lab-10-7-6]]
- Source: [[systems-performance-network-ch10-experimentation-other-tools-pktgen-flent-mtr-tcpreplay-10-7-7]]
- Source: [[systems-performance-disks-ch9-experimentation-fio-blkreplay-9-8-6-7]]
- Related concepts:
  - [[observability-vs-experimentation]]
  - [[counters-statistics-metrics]]
  - [[throughput-latency-metrics]]
  - [[model-classify-intervene]]

