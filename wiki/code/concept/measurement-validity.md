# Measurement validity

- Tag: abstraction

## Definition

**Measurement validity** is whether an observed signal can support the specific claim you want to make: same name of metric, same population and time window, same causal scope, and a representation faithful enough (units, aggregation, symbols/stacks where relevant) that acting on the number is not a category error.

Validity is separate from **whether measurement perturbed the system** (cost/observer effect) and from **which instrument produced the trace** (tool choice).

## Decision rule

Before a costly intervention, classify doubt about evidence into:

1. **Perturbation class** — the act of measuring may have changed outcomes → revisit [[instrumentation-overhead-and-perturbation]] and measurement mode (rate, duration, production safety).
2. **Representation class** — the pipeline from raw events to displayed stacks or rates loses or distorts attribution → pair with [[sampling-based-profiling]] (sample bias, unwind/symbol limits) and trace/log shaping practices.
3. **Scope/semantics class** — the metric is “true” but answers a different question than the SLO (wrong endpoint, wrong window, mixed tenants, cold vs warm traffic) → tighten the model of *what work exists* ([[scientific-method]], [[resource-analysis-vs-workload-analysis]]) and what [[counters-statistics-metrics]] actually count.

If two independent instruments disagree, treat that as a **validity triangulation** problem before choosing which one to trust.

## When to use

- Production and lab disagree on “the same” latency or CPU story.
- Dashboards look green while users report pain (or the reverse).
- You are about to change architecture based on a profile or trace whose definitions you have not spelled out.

## Relation

- Role: abstraction (a **truth-condition checklist** for performance evidence).
- Complements [[instrumentation-overhead-and-perturbation]]: that concept stresses *cost and observer effect*; validity stresses *semantic fit and representation limits even at zero overhead*.
- Complements [[sampling-based-profiling]]: that concept stresses *how sampling and stacks behave*; validity stresses *whether the resulting picture answers your claim*.
- Touches [[throughput-latency-metrics]] when the claim is about user-visible latency but the metric is component-local or throughput-shaped.
- Feeds [[known-unknowns-framework]] by turning “unknown-unknowns” into checkable validity gaps.
- Supports [[scientific-method]] by clarifying what would falsify a hypothesis under your actual definitions.

### CPU metrics (quick mapping)

Short map from Chapter 6 practice to the **doubt classes** above:

- **CPU%** → semantics (what “busy” counts, e.g., stalls) + representation (aggregation, per-CPU vs global).
- **Load average** → semantics (OS definition, non-CPU contributors on some systems) + scope (which population / subsystem demand).
- **IPC / PMCs** → semantics (SKU-relative IPC, event ↔ claim fit) + representation (multiplexing, width, skid / attribution when tied to code).
- **Profiling** → perturbation (overhead, storage side effects) + representation (sampling gaps, stacks, symbolization).

## Links

- Source: [[systems-performance-application-gotchas-missing-symbols-5-6-1]]
- Source: [[systems-performance-gotchas-missing-stacks-causes-5-6-2]]
- Source: [[systems-performance-gotchas-missing-stacks-remedies-and-unwinder-5-6-2]]
- Source: [[systems-performance-distributed-request-trace-sampling-5-4-8]]
- Source: [[systems-performance-cpu-concepts-ipc-utilization-and-user-kernel-time-6-3-7-9]]
- Source: [[systems-performance-cpu-p-states-and-c-states-6-4-1]]
- Source: [[systems-performance-cpu-pmc-hardware-counter-programming-model-6-4-1]]
- Source: [[systems-performance-cpu-pmc-register-budget-and-sku-variance-6-4-1]]
- Source: [[systems-performance-cpu-heterogeneous-accelerators-observability-6-4-1]]
- Source: [[systems-performance-cpu-profiling-methodology-sampling-vs-instrumentation-6-5-4]]
- Source: [[systems-performance-cpu-cycle-analysis-and-performance-monitoring-6-5-5-6]]
- Source: [[systems-performance-cpu-micro-benchmarking-decision-rules-6-5-11]]
- Source: [[systems-performance-cpu-observability-load-and-system-wide-stats-6-6-1-4]]
- Source: [[systems-performance-cpu-observability-process-attribution-and-clock-tools-6-6-5-12]]
- Source: [[systems-performance-cpu-observability-perf-profiling-and-pmcs-6-6-13]]
- Source: [[systems-performance-cpu-observability-bpf-profile-scheduler-and-softirq-6-6-14-18]]
- Source: [[systems-performance-cpu-interrupt-gpu-tools-and-distribution-visualizations-6-6-19-6-7-4]]
- Source: [[systems-performance-cpu-experimentation-adhoc-and-sysbench-6-8]]
- Source: [[systems-performance-cpu-security-mitigations-boot-6-9-9]]
- Source: [[systems-performance-cpu-bios-processor-options-6-9-10]]
- Source: [[systems-performance-memory-terminology-7-1]]
- Source: [[systems-performance-memory-concepts-virtual-memory-7-2-1]]
- Source: [[systems-performance-memory-concepts-paging-7-2-2]]
- Source: [[systems-performance-memory-concepts-demand-paging-7-2-3]]
- Source: [[systems-performance-memory-concepts-overcommit-7-2-4]]
- Source: [[systems-performance-memory-concepts-process-swapping-7-2-5]]
- Source: [[systems-performance-memory-concepts-filesystem-cache-usage-7-2-6]]
- Source: [[systems-performance-memory-concepts-utilization-saturation-7-2-7]]
- Source: [[systems-performance-memory-concepts-shared-memory-pss-7-2-9]]
- Source: [[systems-performance-memory-concepts-working-set-size-7-2-10]]
- Source: [[systems-performance-memory-concepts-word-size-7-2-11]]
- Source: [[systems-performance-memory-architecture-intro-dram-latency-7-3-1a]]
- Source: [[systems-performance-memory-architecture-uma-numa-buses-7-3-1b]]
- Source: [[systems-performance-memory-architecture-ddr-multichannel-7-3-1c]]
- Source: [[systems-performance-memory-architecture-mmu-tlb-7-3-1e]]
- Source: [[systems-performance-memory-architecture-linux-freeing-ladder-7-3-2a]]
- Source: [[systems-performance-memory-architecture-swappiness-swap-cgroups-7-3-2b]]
- Source: [[systems-performance-memory-architecture-free-lists-reaping-scan-7-3-2c]]
- Source: [[systems-performance-memory-process-address-space-segments-7-3-3a]]
- Source: [[systems-performance-memory-heap-growth-vs-leak-7-3-3b]]
- Source: [[systems-performance-memory-allocator-design-tradeoffs-7-3-3c]]
- Source: [[systems-performance-memory-slab-adoption-and-slub-7-3-3e]]
- Source: [[systems-performance-memory-allocator-glibc-dlmalloc-style-7-3-3f]]
- Source: [[systems-performance-memory-allocator-tcmalloc-thread-cache-7-3-3g]]
- Source: [[systems-performance-memory-allocator-jemalloc-arenas-7-3-3h]]
- Source: [[systems-performance-memory-methodology-tools-method-7-4-1]]
- Source: [[systems-performance-memory-methodology-use-method-7-4-2]]
- Source: [[systems-performance-memory-methodology-usage-checklist-7-4-3b]]
- Source: [[systems-performance-memory-methodology-cycle-and-monitoring-7-4-4-5]]
- Source: [[systems-performance-memory-methodology-leak-detection-7-4-6]]
- Source: [[systems-performance-memory-methodology-static-resource-micro-shrinking-7-4-7-10]]
- Source: [[systems-performance-memory-observability-tools-ch7-intro-table-7-5]]
- Source: [[systems-performance-memory-observability-vmstat-7-5-1]]
- Source: [[systems-performance-memory-observability-psi-swapon-7-5-2-3]]
- Source: [[systems-performance-memory-observability-sar-7-5-4]]
- Source: [[systems-performance-memory-observability-ps-top-pmap-7-5-7-9]]
- Source: [[systems-performance-memory-observability-perf-7-5-10]]
- Source: [[systems-performance-memory-observability-trace-other-7-5-11-14]]
- Source: [[systems-performance-memory-tuning-ch7-intro-7-6]]
- Source: [[systems-performance-memory-tuning-sysctl-vm-7-6-1]]
- Source: [[systems-performance-memory-tuning-huge-pages-7-6-2]]
- Source: [[systems-performance-memory-tuning-allocators-7-6-3]]
- Source: [[systems-performance-memory-tuning-numa-bind-7-6-4]]
- Source: [[systems-performance-memory-tuning-cgroup-limits-7-6-5]]
- Source: [[systems-performance-filesystems-ch8-intro-outline-8]]
- Source: [[systems-performance-filesystems-ch8-terminology-8-1]]
- Source: [[systems-performance-filesystems-ch8-concept-latency-8-3-1]]
- Source: [[systems-performance-filesystems-ch8-concept-caching-8-3-2]]
- Source: [[systems-performance-filesystems-ch8-random-prefetch-8-3-3-4]]
- Source: [[systems-performance-filesystems-ch8-writeback-sync-8-3-5-7]]
- Source: [[systems-performance-filesystems-ch8-direct-async-mmap-meta-8-3-8-11]]
- Source: [[systems-performance-filesystems-ch8-logical-physical-io-8-3-12]]
- Source: [[systems-performance-filesystems-ch8-ops-not-equal-8-3-13]]
- Source: [[systems-performance-filesystems-ch8-special-timestamps-capacity-8-3-14-16]]
- Source: [[systems-performance-filesystems-ch8-architecture-intro-stack-8-4-1]]
- Source: [[systems-performance-filesystems-ch8-vfs-8-4-2]]
- Source: [[systems-performance-filesystems-ch8-caches-page-flush-8-4-3a]]
- Source: [[systems-performance-filesystems-ch8-caches-dentry-inode-8-4-3b]]
- Source: [[systems-performance-filesystems-ch8-fs-features-8-4-4]]
- Source: [[systems-performance-filesystems-ch8-fs-types-ffs-8-4-5a]]
- Source: [[systems-performance-filesystems-ch8-fs-types-ext-8-4-5b]]
- Source: [[systems-performance-filesystems-ch8-fs-types-xfs-8-4-5c]]
- Source: [[systems-performance-filesystems-ch8-fs-types-zfs-8-4-5d]]
- Source: [[systems-performance-filesystems-ch8-fs-types-btrfs-8-4-5e]]
- Source: [[systems-performance-filesystems-ch8-volumes-pools-8-4-6]]
- Source: [[systems-performance-filesystems-ch8-methodology-intro-8-5]]
- Source: [[systems-performance-filesystems-ch8-disk-latency-analysis-open-8-5-1-2]]
- Source: [[systems-performance-filesystems-ch8-latency-layers-table-8-5-2a]]
- Source: [[systems-performance-filesystems-ch8-latency-presentation-drilldown-8-5-2b]]
- Source: [[systems-performance-filesystems-ch8-transaction-cost-fs-8-5-2c]]
- Source: [[systems-performance-filesystems-ch8-workload-char-basic-8-5-3a]]
- Source: [[systems-performance-filesystems-ch8-workload-char-advanced-8-5-3b]]
- Source: [[systems-performance-filesystems-ch8-performance-monitoring-8-5-4]]
- Source: [[systems-performance-filesystems-ch8-static-tuning-fs-8-5-5]]
- Source: [[systems-performance-filesystems-ch8-cache-separation-microbench-8-5-6-8]]
- Source: [[systems-performance-filesystems-ch8-table-8-5-expectations]]
- Source: [[systems-performance-filesystems-ch8-obs-tools-intro-8-6]]
- Source: [[systems-performance-filesystems-ch8-mount-free-8-6-1-2]]
- Source: [[systems-performance-filesystems-ch8-top-vmstat-8-6-3-4]]
- Source: [[systems-performance-filesystems-ch8-sar-cache-dentry-8-6-5]]
- Source: [[systems-performance-filesystems-ch8-slabtop-fs-caches-8-6-6]]
- Source: [[systems-performance-filesystems-ch8-strace-syscall-latency-8-6-7]]
- Source: [[systems-performance-filesystems-ch8-fatrace-latencytop-8-6-8-9]]
- Source: [[systems-performance-filesystems-ch8-cachestat-8-6-12]]
- Source: [[systems-performance-filesystems-ch8-bpftrace-syscall-semantics-8-6-15b]]
- Source: [[systems-performance-filesystems-ch8-visualizations-8-6-18]]
- Source: [[systems-performance-filesystems-ch8-fio-8-7-2b]]
- Source: [[systems-performance-filesystems-ch8-ext4-defaults-tune2fs-8-8-2b]]
- Source: [[systems-performance-filesystems-ch8-zfs-tuning-properties-8-8-3]]
- Source: [[systems-performance-disks-ch9-concepts-measuring-time-9-3-1]]
- Source: [[systems-performance-disks-ch9-concepts-time-scales-9-3-2]]
- Source: [[systems-performance-disks-ch9-concepts-io-size-iops-commands-9-3-6-8]]
- Source: [[systems-performance-disks-ch9-concepts-utilization-saturation-iowait-9-3-9-11]]
- Source: [[systems-performance-disks-ch9-concepts-async-mismatch-9-3-12-13]]
- Source: [[systems-performance-disks-ch9-architecture-hdd-throughput-9-4-1a]]
- Source: [[systems-performance-disks-ch9-architecture-hdd-advanced-smr-ddc-9-4-1b]]
- Source: [[systems-performance-disks-ch9-architecture-interfaces-pmem-9-4-2]]
- Source: [[systems-performance-disks-ch9-architecture-raid-table-rmw-9-4-3b]]
- Source: [[systems-performance-disks-ch9-architecture-arrays-nas-9-4-3c]]
- Source: [[systems-performance-disks-ch9-architecture-os-block-stack-9-4-4]]
- Source: [[systems-performance-disks-ch9-methodology-intro-tools-9-5-1]]
- Source: [[systems-performance-disks-ch9-methodology-use-method-9-5-2]]
- Source: [[systems-performance-disks-ch9-methodology-performance-monitoring-9-5-3]]
- Source: [[systems-performance-disks-ch9-methodology-workload-characterization-9-5-4]]
- Source: [[systems-performance-disks-ch9-methodology-latency-analysis-9-5-5]]
- Source: [[systems-performance-disks-ch9-methodology-cache-resource-microbench-9-5-7-9]]
- Source: [[systems-performance-disks-ch9-observability-iostat-9-6-1]]
- Source: [[systems-performance-disks-ch9-observability-sar-9-6-2]]
- Source: [[systems-performance-disks-ch9-observability-psi-9-6-3]]
- Source: [[systems-performance-disks-ch9-observability-pidstat-9-6-4]]
- Source: [[systems-performance-disks-ch9-observability-perf-9-6-5]]
- Source: [[systems-performance-disks-ch9-observability-biolatency-9-6-6]]
- Source: [[systems-performance-disks-ch9-observability-biosnoop-9-6-7]]
- Source: [[systems-performance-disks-ch9-observability-iotop-biotop-9-6-8]]
- Source: [[systems-performance-disks-ch9-observability-blktrace-intro-default-9-6-10a]]
- Source: [[systems-performance-disks-ch9-observability-blktrace-btt-viz-9-6-10c]]
- Source: [[systems-performance-disks-ch9-observability-bpftrace-io-size-9-6-11b]]
- Source: [[systems-performance-disks-ch9-observability-bpftrace-issue-insert-attribution-9-6-11c]]
- Source: [[systems-performance-disks-ch9-observability-bpftrace-latency-errors-9-6-11d]]
- Source: [[systems-performance-disks-ch9-observability-megacli-9-6-12]]
- Source: [[systems-performance-disks-ch9-observability-smartctl-9-6-13]]
- Source: [[systems-performance-disks-ch9-observability-scsi-logging-9-6-14]]
- Source: [[systems-performance-disks-ch9-visualizations-intro-line-9-7-1]]
- Source: [[systems-performance-disks-ch9-visualizations-scatter-9-7-2]]
- Source: [[systems-performance-disks-ch9-visualizations-offset-heatmap-9-7-4]]
- Source: [[systems-performance-disks-ch9-experimentation-intro-dd-9-8-1]]
- Source: [[systems-performance-disks-ch9-experimentation-custom-load-9-8-2]]
- Source: [[systems-performance-disks-ch9-experimentation-microbench-hdparm-9-8-3]]
- Source: [[systems-performance-disks-ch9-experimentation-ioping-9-8-5]]
- Source: [[systems-performance-disks-ch9-experimentation-fio-blkreplay-9-8-6-7]]
- Source: [[systems-performance-disks-ch9-tuning-os-cgroup-sysfs-9-9-1b]]
- Source: [[systems-performance-disks-ch9-tuning-device-hdparm-9-9-2]]
- Source: [[systems-performance-disks-ch9-tuning-controller-9-9-3]]
- Source: [[systems-performance-network-ch10-architecture-software-kernel-bypass-xdp-zerocopy-observability-10-4-3i]]
- Source: [[systems-performance-network-ch10-observability-ss-socket-stats-tcp-internal-info-10-6-1]]
- Source: [[systems-performance-network-ch10-observability-nstat-snmp-kernel-metrics-interval-reset-10-6-4]]
- Source: [[systems-performance-network-ch10-observability-netstat-multi-socket-interface-stack-stats-10-6-5]]
- Source: [[systems-performance-network-ch10-observability-sar-network-stats-options-table-10-5-part-a-10-6-6a]]
- Source: [[systems-performance-network-ch10-observability-nicstat-throughput-utilization-saturation-10-6-7]]
- Source: [[systems-performance-network-ch10-observability-ethtool-driver-stats-offloads-10-6-8]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-one-liners-probe-cost-10-6-12a]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-socket-layer-socketio-10-6-12b]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-tcp-tcpsynbl-backlog-10-6-12c]]
- Source: [[systems-performance-network-ch10-observability-bpftrace-event-sources-table-10-6-12d]]
- Source: [[systems-performance-network-ch10-observability-tcpdump-capture-filters-overhead-10-6-13]]
- Source: [[systems-performance-network-ch10-observability-other-tools-linux-sources-monitoring-10-6-15b]]
- Source: [[systems-performance-network-ch10-experimentation-ping-icmp-rtt-accuracy-10-7-1]]
- Source: [[systems-performance-network-ch10-experimentation-traceroute-ttl-path-dynamics-firewalls-10-7-2]]
- Source: [[systems-performance-network-ch10-experimentation-pathchar-pchar-bandwidth-probing-10-7-3]]
- Source: [[systems-performance-network-ch10-tuning-intro-characterize-first-10-8]]
- Source: [[systems-performance-network-ch10-tuning-sysctl-system-wide-discovery-example-10-8-1a]]
- Source: [[systems-performance-network-ch10-tuning-congestion-tcp-options-ecn-10-8-1c]]
- Source: [[systems-performance-network-ch10-tuning-bql-cgroups-qdisc-tuned-10-8-1d]]
- Source: [[systems-performance-network-ch10-tuning-msg-zerocopy-send-flag-10-8-2b]]
- Source: [[systems-performance-network-ch10-tuning-configuration-jumbo-lacp-firewall-dscp-10-8-3]]
- Related concepts:
  - [[instrumentation-overhead-and-perturbation]]
  - [[sampling-based-profiling]]
  - [[throughput-latency-metrics]]
  - [[known-unknowns-framework]]
  - [[scientific-method]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[counters-statistics-metrics]]
  - [[systems-performance]]
