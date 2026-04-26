# Static performance tuning

- Tag: heuristic

## Definition

**Static performance tuning** checks the configured architecture and configuration of a system *at rest* (no applied load) to find obvious mismatches, degraded states, and misconfigurations that can cause performance issues.

## Relation

- Role: method (a configuration checklist distinct from load-driven diagnosis).
- Complements [[use-method]] and [[red-method]]: those screen behavior under load; static tuning screens configuration correctness and degraded states.
- Fits [[model-classify-intervene]] by supporting early classification of “misconfiguration/degraded state” vs workload-driven explanations before deeper drill-down.

## Links

- Source: [[systems-performance-static-performance-tuning-2-5-17]]
- Source: [[systems-performance-systemd-3-4-2]]
- Source: [[systems-performance-kpti-meltdown-3-4-3]]
- Source: [[systems-performance-pgo-kernels-3-5-1]]
- Source: [[systems-performance-observability-static-tools-4-1-1]]
- Source: [[systems-performance-observability-crisis-tools-4-1-2]]
- Source: [[systems-performance-chapter-4-exercises-4-7]]
- Source: [[systems-performance-application-basics-5-1]]
- Source: [[systems-performance-static-performance-tuning-application-checklist-5-4-7]]
- Source: [[systems-performance-gotchas-missing-stacks-remedies-and-unwinder-5-6-2]]
- Source: [[systems-performance-chapter-5-exercises-application-profile-role-and-metrics-5-7]]
- Source: [[systems-performance-chapter-5-exercises-under-load-lab-b-5-7]]
- Source: [[systems-performance-cpu-concepts-clock-rate-and-stalls-6-3-1]]
- Source: [[systems-performance-cpu-compiler-optimization-pointer-6-3-15]]
- Source: [[systems-performance-cpu-static-performance-tuning-checklist-6-5-7]]
- Source: [[systems-performance-cpu-micro-benchmarking-decision-rules-6-5-11]]
- Source: [[systems-performance-cpu-tuning-compiler-scheduler-sysctl-6-9-1-3]]
- Source: [[systems-performance-cpu-tuning-governors-affinity-cgroups-6-9-4-8]]
- Source: [[systems-performance-cpu-security-mitigations-boot-6-9-9]]
- Source: [[systems-performance-cpu-bios-processor-options-6-9-10]]
- Source: [[systems-performance-memory-methodology-static-resource-micro-shrinking-7-4-7-10]]
- Source: [[systems-performance-memory-observability-trace-other-7-5-11-14]]
- Source: [[systems-performance-memory-tuning-ch7-intro-7-6]]
- Source: [[systems-performance-memory-tuning-sysctl-vm-7-6-1]]
- Source: [[systems-performance-memory-tuning-huge-pages-7-6-2]]
- Source: [[systems-performance-memory-tuning-allocators-7-6-3]]
- Source: [[systems-performance-memory-tuning-numa-bind-7-6-4]]
- Source: [[systems-performance-memory-tuning-cgroup-limits-7-6-5]]
- Source: [[systems-performance-filesystems-ch8-methodology-intro-8-5]]
- Source: [[systems-performance-filesystems-ch8-static-tuning-fs-8-5-5]]
- Source: [[systems-performance-filesystems-ch8-mount-free-8-6-1-2]]
- Source: [[systems-performance-filesystems-ch8-tuning-intro-8-8]]
- Source: [[systems-performance-filesystems-ch8-application-calls-fadvise-madvise-8-8-1]]
- Source: [[systems-performance-filesystems-ch8-ext4-mount-man-atime-8-8-2a]]
- Source: [[systems-performance-filesystems-ch8-ext4-defaults-tune2fs-8-8-2b]]
- Source: [[systems-performance-filesystems-ch8-ext4-sysfs-e2fsck-8-8-2c]]
- Source: [[systems-performance-filesystems-ch8-zfs-tuning-properties-8-8-3]]
- Source: [[systems-performance-disks-ch9-architecture-raid-table-rmw-9-4-3b]]
- Source: [[systems-performance-disks-ch9-architecture-arrays-nas-9-4-3c]]
- Source: [[systems-performance-disks-ch9-architecture-os-block-stack-9-4-4]]
- Source: [[systems-performance-disks-ch9-methodology-static-tuning-9-5-6]]
- Source: [[systems-performance-disks-ch9-tuning-intro-ionice-9-9-1a]]
- Source: [[systems-performance-disks-ch9-tuning-os-cgroup-sysfs-9-9-1b]]
- Source: [[systems-performance-disks-ch9-tuning-device-hdparm-9-9-2]]
- Source: [[systems-performance-network-ch10-architecture-protocols-tcp-congestion-controls-10-4-1e]]
- Source: [[systems-performance-network-ch10-architecture-protocols-tcp-nagle-delayedacks-sack-iw-udp-quic-10-4-1f]]
- Source: [[systems-performance-network-ch10-methodology-static-performance-tuning-checklist-10-5-8]]
- Source: [[systems-performance-network-ch10-observability-ip-link-stats-routes-monitor-10-6-2]]
- Source: [[systems-performance-network-ch10-observability-ifconfig-legacy-interface-counters-10-6-3]]
- Source: [[systems-performance-network-ch10-observability-ethtool-driver-stats-offloads-10-6-8]]
- Source: [[systems-performance-network-ch10-experimentation-traceroute-ttl-path-dynamics-firewalls-10-7-2]]
- Source: [[systems-performance-network-ch10-tuning-intro-characterize-first-10-8]]
- Source: [[systems-performance-network-ch10-tuning-sysctl-system-wide-discovery-example-10-8-1a]]
- Source: [[systems-performance-network-ch10-tuning-bql-cgroups-qdisc-tuned-10-8-1d]]
- Source: [[systems-performance-disks-ch9-tuning-controller-9-9-3]]
- Source: [[systems-performance-network-ch10-tuning-socket-options-table-10-8-10-8-2a]]
- Source: [[systems-performance-network-ch10-tuning-msg-zerocopy-send-flag-10-8-2b]]
- Related concepts:
  - [[use-method]]
  - [[red-method]]
  - [[model-classify-intervene]]

