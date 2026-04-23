# Observability vs experimentation

- Tag: tradeoff

## Definition

**Observability** tools measure a system by observing its existing behavior and workload (counters, metrics, profiling, tracing). **Experimentation** tools measure a system by applying a workload experiment (often a synthetic benchmark) and observing the result.

## Scope note

Experimentation can perturb the system under test (and may be unsuitable for production workloads), while observability is often safer to try first in production environments.

## Relation

This distinction guides measurement choice and helps interpret results: fixed-workload experiments can reduce input variance, while observability can reveal behavior under real production conditions.

## Links

- Source: [[systems-performance-experimentation-1-8]]
- Source: [[systems-performance-kernel-comparisons-3-6]]
- Source: [[systems-performance-chapter-4-intro-4]]
- Source: [[systems-performance-observability-crisis-tools-4-1-2]]
- Source: [[systems-performance-observability-tool-types-4-2]]
- Source: [[systems-performance-profiling-4-2-2]]
- Source: [[systems-performance-tracing-4-2-3]]
- Source: [[systems-performance-observability-monitoring-4-2-4]]
- Source: [[systems-performance-pmc-challenges-and-docs-4-3-9]]
- Source: [[systems-performance-observing-observability-4-6]]
- Source: [[systems-performance-application-observability-selection-5-1-3]]
- Source: [[systems-performance-programming-languages-intro-5-3]]
- Source: [[systems-performance-compiled-languages-performance-5-3-1]]
- Source: [[systems-performance-language-virtual-machines-5-3-3]]
- Source: [[systems-performance-cpu-profiling-kernel-vs-user-5-4-1]]
- Source: [[systems-performance-off-cpu-narrowing-filters-5-4-2]]
- Source: [[systems-performance-thread-state-investigation-and-measurement-5-4-5]]
- Source: [[systems-performance-perf-profiling-syscall-trace-and-io-5-5-1]]
- Source: [[systems-performance-strace-ptrace-overhead-and-buffered-tracing-5-5-4]]
- Source: [[systems-performance-application-gotchas-missing-symbols-5-6-1]]
- Source: [[systems-performance-gotchas-missing-stacks-remedies-and-unwinder-5-6-2]]
- Source: [[systems-performance-chapter-5-exercises-application-profile-observability-and-community-5-7]]
- Source: [[systems-performance-cpu-concepts-clock-rate-and-stalls-6-3-1]]
- Source: [[systems-performance-cpu-heterogeneous-accelerators-observability-6-4-1]]
- Source: [[systems-performance-cpu-interrupt-gpu-tools-and-distribution-visualizations-6-6-19-6-7-4]]
- Source: [[systems-performance-cpu-experimentation-adhoc-and-sysbench-6-8]]
- Source: [[systems-performance-memory-methodology-static-resource-micro-shrinking-7-4-7-10]]
- Source: [[systems-performance-memory-observability-trace-other-7-5-11-14]]
- Source: [[systems-performance-filesystems-ch8-cache-separation-microbench-8-5-6-8]]
- Source: [[systems-performance-filesystems-ch8-table-8-5-expectations]]
- Source: [[systems-performance-filesystems-ch8-experimentation-dd-8-7-1]]
- Source: [[systems-performance-disks-ch9-experimentation-intro-dd-9-8-1]]
- Source: [[systems-performance-disks-ch9-experimentation-fio-blkreplay-9-8-6-7]]
- Source: [[systems-performance-network-ch10-architecture-software-kernel-bypass-xdp-zerocopy-observability-10-4-3i]]
- Source: [[systems-performance-network-ch10-methodology-micro-benchmarking-10-5-10]]
- Source: [[systems-performance-network-ch10-observability-tools-intro-table-10-6]]
- Source: [[systems-performance-network-ch10-observability-packet-capture-tools-table-10-6-c]]
- Source: [[systems-performance-network-ch10-observability-tcpretrans-kernel-retransmit-events-10-6-11]]
- Source: [[systems-performance-network-ch10-observability-tcpdump-capture-filters-overhead-10-6-13]]
- Source: [[systems-performance-network-ch10-experimentation-intro-probes-vs-observability-10-7]]
- Source: [[systems-performance-network-ch10-experimentation-pathchar-pchar-bandwidth-probing-10-7-3]]
- Source: [[systems-performance-network-ch10-experimentation-iperf-throughput-parallel-intervals-10-7-4]]
- Source: [[systems-performance-network-ch10-experimentation-netperf-tcp-rr-latency-10-7-5]]
- Source: [[systems-performance-network-ch10-experimentation-tc-netem-loss-lab-10-7-6]]
- Source: [[systems-performance-network-ch10-experimentation-other-tools-pktgen-flent-mtr-tcpreplay-10-7-7]]
- Related concepts:
  - [[counters-statistics-metrics]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[measurement-validity]]
  - [[systems-performance]]

