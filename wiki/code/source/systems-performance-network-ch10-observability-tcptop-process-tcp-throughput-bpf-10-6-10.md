# Systems Performance — Ch.10 §10.6.10 tcptop (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3240–3274**; file rebuilt 2026-04-20)
- Scope: attribution of **bytes moved** (rates over the sampling interval)

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-tcptop-process-tcp-throughput-bpf-10-6-10.md`

## Extracted ideas

- Output is inherently **interval rates** (KB per refresh), not lifetime totals—good for “who is flooding NIC queues **right now**” ([[counters-statistics-metrics]] discipline).
- **Probe cost scales with traffic**, not just “BPF is cheap”: when send/recv fires constantly, **CPU overhead + observer skew** become real risks ([[instrumentation-overhead-and-perturbation]] **perturbation** class when correlation suggests it).
- Attribution answers **which tenant/workload** deserves deeper drill-down vs global TCP tuning ([[resource-analysis-vs-workload-analysis]]).

## Decision clarity

**Decision:** choose **`tcptop`** over **`tcplife`** when you need **live bulk attribution per second**, not finished-flow summaries ([[drill-down-analysis]]).

## Application validation

- **Noisy neighbor on host:** one Java PID dominates RX—next step is NIC/interface saturation + queue drops, not “kernel TCP is broken” ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[counters-statistics-metrics]], [[instrumentation-overhead-and-perturbation]], [[resource-analysis-vs-workload-analysis]], [[drill-down-analysis]], [[queueing-theory]], [[extended-bpf]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[counters-statistics-metrics]], [[instrumentation-overhead-and-perturbation]], [[resource-analysis-vs-workload-analysis]], [[drill-down-analysis]], [[queueing-theory]], [[extended-bpf]], [[systems-performance]]
