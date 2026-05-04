---
id: instrumentation-reach-stability-overhead-tradeoff
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Instrumentation reach / stability / overhead tradeoff"
---

# Instrumentation reach / stability / overhead tradeoff

## Definition

Any choice of instrumentation trades along three axes that move together:

- **Reach** — what the instrumentation can observe. Static probes are limited to what was placed in advance; dynamic probes can attach to almost anything; sampling can only observe what happens to be running at sample time.
- **Stability** — how robust the contract is across kernel/runtime upgrades. Tracepoints and USDT are stable APIs with documented arguments; kprobes and uprobes expose raw functions and argument layouts that can change across versions; MSRs and PMCs are processor-specific.
- **Overhead and skew** — CPU per event, storage per event, and *measurement skew* introduced by the probe path itself (return-probe trampolines, `ptrace(2)` stop-and-copy, `/proc` text parsing). Disabled instrumentation is rarely free either: NOPs, function-profiling hooks, and tracepoint metadata cost a small amount even when off.

These axes are not independent. Adding reach typically reduces stability, increases overhead, or both; reducing overhead typically reduces reach (sampling) or stability (raw probes). The reusable move is to **state the three for any candidate instrumentation choice and reject the ones whose tradeoff curve does not match the question**.

## Use when

- Choosing an event source for production tracing — pick the most stable, lowest-overhead interface that still has the reach to answer the question.
- Reviewing a proposed observability addition — compute the per-event cost against expected event rate; reject if the curve crosses the production-safety budget.
- Diagnosing a measurement-induced regression — measurement that moves the symptom is on the wrong point of the curve.
- Comparing two tools that "do the same thing" — they often sit at different points (e.g. tracepoint-based `biosnoop` vs uprobe-based variant).
- Setting per-tool overhead budgets in shared production hosts — explicit tradeoff curve makes the budget defensible.

## Do not use when

- Off-production debugging where overhead is irrelevant; high-cost interfaces are fine in that mode.
- Trivial point reads (one-shot `/proc` lookup, single counter); the curve adds no decision.
- Correctness or safety-bound choices, where the right primitive is dictated by semantics, not by overhead.

## Related concepts

- [[observability-source-interface]] — the underlying primitive: each source interface sits at a particular point on this curve.
- [[mode-switch-vs-context-switch]] — uprobes and ptrace pay extra mode/context-switch cost; tracepoints/USDT amortize it; the cost shows up here as overhead.
- [[stack-trace-as-execution-cause]] — stack walking adds reach (cause chain) at extra unwinder/storage cost; same curve, different axis.
- [[scheduler-policy-shapes-latency]] — observation cost can interact with policy (probes can perturb cgroup-throttled or preempt-disabled paths); the curve is workload-dependent.
- [[performance-anti-methods]] — random-change of probe types without overhead reasoning is the random-change pattern; "we'll just bpftrace it in prod" without naming the curve is a streetlight move on instrumentation.

## Source support

- [[systems-performance-ch4-observability-tools-p168-182]] — § 4.2 distinguishes counters (cheap, always-on), profiling (sampled, bounded overhead), tracing (per-event, higher overhead and possible skew), and monitoring (continuous archival); explicitly notes tracing/profiling "are not free" and that stack-walking reliability is a prerequisite.
- [[systems-performance-ch4-observability-tools-continuation-p183-197]] — tracepoints (stable API, small enabled+disabled overhead), kprobes/uprobes (unstable, higher cost; uretprobe overhead called out), USDT (stable, requires rebuild flags), PMCs (overflow "skid", precise events), with example overhead numbers and event-rate guidance.
- [[systems-performance-ch4-observability-tools-tail-p198-209]] — § 4.3.10 ptrace 100×+ slowdown, libpcap CPU+storage overhead, function-profiling NOP-until-enabled hooks; § 4.6 "observing observability" reinforces that the act of measuring can be wrong or harmful and motivates the curve as part of correct interpretation.
