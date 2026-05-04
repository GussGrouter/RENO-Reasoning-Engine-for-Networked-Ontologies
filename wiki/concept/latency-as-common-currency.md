---
id: latency-as-common-currency
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Latency as common currency"
---

# Latency as common currency

## Definition

A reasoning move that converts heterogeneous units of work into *time* so they can be compared, ranked, and combined.

- Counts (IOPS, requests/s, bytes/s) tell you *rate* but not *cost*. Latency tells you *cost per unit of work*, in seconds or fractions thereof.
- Once everything is in time, you can **add** it (serial paths sum), **compare** it (a 2 ms function and a 200 µs syscall are commensurable), and **compress** it across orders of magnitude (CPU cycle → DRAM access → disk seek → network round trip → wall clock).
- The conversion forces you to *qualify* the word "latency" — wait time vs service time, end-to-end vs hop, p50 vs tail, client-observed vs server-observed — because the unit alone does not.

The currency metaphor is deliberate: time is a common denominator for budgeting, not a substitute for the underlying mechanics. Like any currency, it lets you trade across categories at the cost of hiding what is being traded.

## Use when

- Comparing two paths or implementations whose work counts differ in shape (e.g. one batch of 10 k IOPS vs one synchronous request that touches DRAM only).
- Setting or reviewing SLOs; latency budgets compose and decompose, raw counts do not.
- Building intuition about a stack you do not own — the scaled-time analogy (CPU cycle as 1 s, disk seek as months) is for memory, not arithmetic, but it speeds up rough order-of-magnitude calls.
- Deciding whether a 10× count improvement actually moves user-visible time.
- Benchmarking heterogeneous work where commensurate units are the only honest summary.
- Architecture review: making the cost of a serial hop visible against an end-to-end budget.

## Do not use when

- Throughput *is* the deliverable (e.g. batch ETL with no user waiting); converting to per-record latency hides aggregate cost.
- The latency you have is unqualified — averaged across mixed work, lacking a tail, measured only from inside one hop. Convert with caution and label the assumption rather than averaging blindly.
- Capacity decisions where the question is "how much more load can the system absorb"; [[load-versus-architecture]] frames that better than time alone.
- For systems where the dominant cost is energy, money, or carbon rather than wall-clock time; pick the currency that matches the decision.

## Related concepts

- [[resource-analysis-vs-workload-analysis]] — workload-side analysis runs on latency; this concept is its unit of account.
- [[load-versus-architecture]] — architecture-bound limits often show up as serial latency that no extra capacity can shrink.
- [[use-method]] — saturation in USE is read in time; latency-as-currency makes that reading legible.
- [[mode-switch-vs-context-switch]] — both kinds of CPU transition are paid in time; the time-currency frame keeps them comparable to other latency sources.
- [[stack-trace-as-execution-cause]] — flame-graph height aggregates stack samples in time, which is the bridge from code paths to time budgets.
- *cache-hit-ratio-and-miss-rate* (deferred) — formalises how miss-rate changes shift effective latency by orders of magnitude.

## Source support

- [[systems-performance-ch2-methodologies-p60-75]] — § 2.3.1 and § 2.3.2 define latency, contrast it with raw counts, and use Tables 2.1 and 2.2 to scale time across many orders of magnitude.
- [[systems-performance-ch2-methodologies-continuation-p76-90]] — § 2.4 frames latency as the headline workload-side metric.
- [[systems-performance-ch2-methodologies-continuation-p106-120]] — § 2.8 statistics: composing latency for what-if estimates, percentile / SLA framing, and the multimodal-latency warning that requires distributions instead of means.
