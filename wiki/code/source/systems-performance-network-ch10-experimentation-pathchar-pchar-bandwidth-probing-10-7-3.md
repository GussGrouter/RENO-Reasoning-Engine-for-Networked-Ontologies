# Systems Performance — Ch.10 §10.7.3 pathchar / pchar (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt`
- Scope: **heavy experimental probing** for link capacity estimates (use sparingly)

## Processed artifacts

- `processed/code/systems-performance-network-ch10-experimentation-pathchar-pchar-bandwidth-probing-10-7-3.md`

## Extracted ideas

- This class of tool answers **“which hop is the narrow pipe?”** with more ambition than traceroute RTTs—but outputs are still **model estimates**, not billing truth ([[measurement-validity]] **representation**).
- Long runtimes imply **shared-queue interference** risk: probes can perturb production latency while you measure—treat observed app delays during runs as potentially **measurement-coupled queueing** ([[instrumentation-overhead-and-perturbation]], **perturbation** when correlated).
- Prefer **modern maintained substitutes** and **controlled windows** over vintage binaries—availability is part of measurement validity ([[measurement-validity]] **scope/semantics**: what you can actually run).

## Decision clarity

**Decision:** choose **short controlled iperf/microbench between known endpoints** over **multi-hop pathchar campaigns** when you only need **end-to-end capacity** for a fixed dependency pair ([[micro-benchmarking]]).

## Application validation

- **Capacity disputes between teams:** if hop estimates disagree with **interface counters + sar**, trust the **counter-backed path** first—multi-hop inference is fragile ([[counters-statistics-metrics]]).

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[instrumentation-overhead-and-perturbation]], [[micro-benchmarking]], [[counters-statistics-metrics]], [[observability-vs-experimentation]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[instrumentation-overhead-and-perturbation]], [[micro-benchmarking]], [[counters-statistics-metrics]], [[observability-vs-experimentation]], [[systems-performance]]
