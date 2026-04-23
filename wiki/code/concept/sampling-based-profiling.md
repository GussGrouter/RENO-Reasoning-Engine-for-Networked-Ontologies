# Sampling-based profiling

- Tag: measurement

## Definition

**Sampling-based profiling** measures a system by periodically sampling its state (e.g., instruction pointer or stack trace) and analyzing the set of samples to build a coarse picture of where time is spent.

## Scope note

The coarseness depends on the sampling rate: higher rates capture more detail but can increase overhead.

Hardware performance counters sampled in overflow mode inherit an extra attribution caveat: interrupts (and CPU reordering) may “skid” so the recorded instruction pointer is only approximately where the triggering condition occurred—vendor “precise event” mechanisms exist to tighten that mapping when the diagnosis depends on pinpoint accuracy.

The same **head vs tail** sampling tension appears when retaining **end-to-end request traces**: sampling at entry preserves cheap bulk coverage, while deferring the keep/drop decision until outcomes (latency/errors) are known trades storage for rare-tail fidelity.

Interpreting stacks also depends on **symbolization and unwind metadata** matching how artifacts were built and shipped (stripped binaries, separate debuginfo/BTF, JIT supplemental maps, frame-pointer conventions). “`[unknown]`” or mis-resolved frames are usually a **data-quality / build pipeline** issue before they are evidence of a novel runtime bug.

**Unwind strategy** matters independently: frame-pointer walks fail on `-fomit-frame-pointer` style builds and many libc paths, while DWARF/LBR-style walkers can recover depth in some tools but are not universally available from every BPF stack capture path—compare like-for-like before declaring “no user stack.”

## Relation

Profiling complements counters/metrics when you need attribution (which code paths consume resources) rather than just rates and totals.

For whether a profile or sample set **supports a specific conclusion** (not just how it was collected), use [[measurement-validity]] as the cross-cutting checklist—this page focuses on sampling mechanics, coarseness, and stack representation limits.

## Links

- Source: [[systems-performance-profiling-2-3-13]]
- Source: [[systems-performance-pgo-kernels-3-5-1]]
- Source: [[systems-performance-chapter-4-intro-4]]
- Source: [[systems-performance-observability-tool-types-4-2]]
- Source: [[systems-performance-profiling-4-2-2]]
- Source: [[systems-performance-pmc-challenges-and-docs-4-3-9]]
- Source: [[systems-performance-pmc-fundamentals-4-3-9]]
- Source: [[systems-performance-tracing-tools-survey-4-5]]
- Source: [[systems-performance-chapter-4-exercises-4-7]]
- Source: [[systems-performance-optimize-common-case-5-1-2]]
- Source: [[systems-performance-compiled-languages-performance-5-3-1]]
- Source: [[systems-performance-application-methodology-overview-5-4]]
- Source: [[systems-performance-cpu-profiling-kernel-vs-user-5-4-1]]
- Source: [[systems-performance-lock-contention-and-hold-time-5-4-6]]
- Source: [[systems-performance-distributed-request-trace-sampling-5-4-8]]
- Source: [[systems-performance-perf-profiling-syscall-trace-and-io-5-5-1]]
- Source: [[systems-performance-application-gotchas-missing-symbols-5-6-1]]
- Source: [[systems-performance-gotchas-missing-stacks-causes-5-6-2]]
- Source: [[systems-performance-gotchas-missing-stacks-remedies-and-unwinder-5-6-2]]
- Source: [[systems-performance-chapter-5-exercises-under-load-lab-a-5-7]]
- Source: [[systems-performance-cpu-concepts-ipc-utilization-and-user-kernel-time-6-3-7-9]]
- Source: [[systems-performance-cpu-profiling-methodology-sampling-vs-instrumentation-6-5-4]]
- Source: [[systems-performance-cpu-cycle-analysis-and-performance-monitoring-6-5-5-6]]
- Source: [[systems-performance-cpu-observability-perf-profiling-and-pmcs-6-6-13]]
- Source: [[systems-performance-cpu-observability-bpf-profile-scheduler-and-softirq-6-6-14-18]]
- Source: [[systems-performance-cpu-interrupt-gpu-tools-and-distribution-visualizations-6-6-19-6-7-4]]
- Source: [[systems-performance-cpu-chapter-6-exercises-scaffold-6-10]]
- Source: [[systems-performance-memory-concepts-demand-paging-7-2-3]]
- Source: [[systems-performance-memory-observability-perf-7-5-10]]
- Related concepts:
  - [[counters-statistics-metrics]]
  - [[instrumentation-overhead-and-perturbation]]

