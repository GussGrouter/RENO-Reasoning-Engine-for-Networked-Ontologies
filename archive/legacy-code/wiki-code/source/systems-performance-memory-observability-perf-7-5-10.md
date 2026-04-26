# Systems Performance — perf for memory (§7.5.10) (PDF scouts 320–380 + 381–400 bridge)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.5.10** — **perf** kmem/vmscan/compaction/page-fault stacks; **page-fault flame graphs** as growth attribution

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`, `processed/code/systems-performance-ch7-scout-p381-400.txt` (opening lines complete perf narrative)
- Converted slice: `processed/code/systems-performance-memory-observability-perf-7-5-10.md`
- Chunks: `processed/code/systems-performance-memory-observability-perf-7-5-10-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Page faults track RSS growth paths**—but **system-wide `-a`** captures **short-lived noise**; scope to **PID** when attributing a service ([[sampling-based-profiling]], [[measurement-validity]]).
- (representation) **Flame graphs summarize stacks** but still encode **sampling bias**—pair counts with **rate context** ([[metric-visualization]], [[measurement-validity]]).

## Application validation

- **Heap suspected:** **page-fault profile** first localizes **which code grows RSS**; only then decide **allocator swap** vs **algorithmic leak**.

## Decision clarity

- **Decision:** choose **page-fault stack sampling for growth attribution** over **malloc tracing** when **fault rate is moderate** and **production perturbation** must stay low—escalate to uprobes/BPF **only after** hotspots are known.

## Concepts reused / refined / created

- Reused (measurement): [[sampling-based-profiling]], [[measurement-validity]]
- Reused (structure): [[metric-visualization]]
- Reused: [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[sampling-based-profiling]], [[measurement-validity]], [[metric-visualization]], [[systems-performance]]
- Related sources: [[systems-performance-memory-observability-trace-other-7-5-11-14]]
