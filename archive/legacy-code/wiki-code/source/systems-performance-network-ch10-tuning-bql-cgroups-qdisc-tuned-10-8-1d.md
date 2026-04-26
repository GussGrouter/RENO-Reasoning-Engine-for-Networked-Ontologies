# Systems Performance — Ch.10 §10.8.1 system-wide tuning — BQL, cgroup/qdisc policy, tuned profiles (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **4661–4751**; file rebuilt 2026-04-20)
- Scope: **queue-depth governance**, **policy bundles**, and **where classification work runs**

## Processed artifacts

- `processed/code/systems-performance-network-ch10-tuning-bql-cgroups-qdisc-tuned-10-8-1d.md`

## Extracted ideas

- **BQL** is a **driver-queue sizing feedback loop** in bytes: clamping min/max is a deliberate trade between **standing queue delay** (tails) and **TX starvation** risk when the NIC cannot accept work ([[queueing-theory]]).
- **Cgroup tagging + qdisc/BPF hooks** is fundamentally about **moving contention**: if the root qdisc lock is hot, shifting classification/remarking to **egress hooks** can change *who waits on which mutex*—still a **queueing + implementation bottleneck** story, not “BPF magic” ([[resource-vs-implementation-bottleneck]]).
- **Default qdisc** is fleet-level **AQM/scheduling policy** (`pfifo_fast` vs `fq_codel`, etc.): it changes how **backpressure** manifests (drops/marks/coalescing behavior), so validate with workload-shaped traffic, not microbench-only ([[throughput-latency-metrics]]).
- **`tuned` profiles** are **bundled hypotheses** (sysctl + bootloader + VM behavior): treat as **static-performance-tuning** templates with explicit **power/latency** tradeoffs; verify on your kernel line because names drift faster than semantics ([[static-performance-tuning]]; [[measurement-validity]] **scope/semantics**).

## Decision clarity

**Decision:** choose **`tuned` profile + canary diff review** over **copy/pasting sysctl fragments** when you need **repeatable fleet policy** and an auditable bundle—still re-validate because profile meaning shifts across distro/kernel generations ([[measurement-validity]] **scope/semantics**).

## Application validation

- **Standing latency on idle-ish links:** if tails correlate with large TX queues, inspect BQL sysfs limits before raising buffer sysctl maxima—bigger buffers can **increase delay** under lossy paths ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[throughput-latency-metrics]], [[resource-vs-implementation-bottleneck]], [[static-performance-tuning]], [[measurement-validity]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[throughput-latency-metrics]], [[resource-vs-implementation-bottleneck]], [[static-performance-tuning]], [[measurement-validity]], [[systems-performance]]
