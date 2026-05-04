---
id: choose-observability-source-by-question-risk
type: insight
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Choose observability source by question and risk"
---

# Choose observability source by question and risk

## Claim

Pick observability **source first, tool second**, governed by the question being asked and the production risk you can afford. The decision rule: **start from the symptom-shaped question, choose the cheapest source interface with sufficient coverage at acceptable stability and overhead, then pick a tool over that interface.** Reaching for the most powerful tool by default is the streetlight pattern dressed up as competence; reusing a familiar tool whose interface cannot see the question is the same pattern dressed differently.

The rule is asymmetric. **Insufficient coverage** is a hard veto — no overhead budget makes a blind interface see. **Insufficient stability or excess overhead** is a budget question — sometimes you accept a kprobe in production with a strict event-rate ceiling; sometimes you do not. Either way, the question and the curve must be named *before* the tool, not derived after it.

The corollary is for cross-checking. When two metrics agree because they read the same source interface, you have one signal twice; when they agree across *different* interfaces, you have a real cross-check. Pick disagreement candidates by interface, not by tool.

## Concepts involved

- [[observability-source-interface]] — names the unit of choice (interface, not tool) and its properties (coverage, stability, overhead, permissions, data model).
- [[instrumentation-reach-stability-overhead-tradeoff]] — names the curve every interface sits on; the rule walks that curve to the cheapest sufficient point.
- [[problem-statement-first-response]] — supplies the question that bounds "sufficient coverage"; without it, "sufficient" is undefined.
- [[performance-anti-methods]] — streetlight (familiar tool) and tools-method (familiar tool list) are the dominant failure modes this rule guards against.

## Source basis

- [[systems-performance-ch4-observability-tools-p168-182]] — § 4.2 distinguishes counters / profiling / tracing / monitoring as different source families with different cost and coverage; § 4.3 (Table 4.2) enumerates source interfaces explicitly so the choice is interface-first.
- [[systems-performance-ch4-observability-tools-continuation-p183-197]] — tracepoints vs kprobes/uprobes/USDT placed on a stability/overhead curve, with event-rate guidance and explicit per-probe overheads; PMCs constrained by register count, sampling skid, and cloud availability — concrete instances of "right interface at acceptable risk".
- [[systems-performance-ch4-observability-tools-tail-p198-209]] — § 4.3.10 contrasts cheap and expensive sources (`getrusage(2)` vs `ptrace(2)`'s 100× slowdown, libpcap CPU/storage overhead, MSR availability constraints); § 4.6 "observing observability" prescribes cross-checking with overlapping tools backed by *different* instrumentation frameworks.

## Decision use

- **Triage.** Name the question, then walk down the source list from cheapest/most-stable to most-expensive/least-stable, stopping at the first interface that has enough coverage. Do not open a deep tracer when `sar(1)` or a counter answers the question.
- **Production safety.** Bound per-tool event rates against the expected probe overhead before enabling kprobes, uprobes, packet capture, or `ptrace`-based tracing in production; budget against the symptom interval, not the daily average.
- **Telemetry investment.** Prefer stable interfaces (tracepoints, USDT, perf_events, `/sys`, netlink, sar archives) for long-lived dashboards and SLOs; reserve unstable interfaces (kprobes, uprobes, raw MSRs) for ad-hoc investigations with named scope and end conditions.
- **Cross-checking.** When a metric is suspect, validate against a *different* interface (e.g. cross-check disk activity from `/proc/diskstats` against block tracepoints) — not against another tool reading the same `/proc` file.
- **Architecture review.** New services should declare which source interfaces their observability depends on, and which interfaces become unreachable after deployment (containers without privileged probes, kernel-bypass paths that hide a hop, hypervisors that disable PMCs).
- **Anti-pattern check.** "We need bpftrace for this" without naming what tracepoint or counter cannot answer is the streetlight-by-tool pattern; require an interface-level reason. "It's slow because the disk is at 70%" backed only by the same `iostat` interface that produced the symptom is one signal twice, not a cross-check.
- **Cross-team handoff.** When platform reports "the host is fine" and application reports "the call is slow", the disagreement is usually that the two teams read different source interfaces; agree on which interface owns the next claim before escalating.
- **Stage-1 vs stage-3 hygiene.** Same logic applies across investigation stages — see [[drill-down-is-only-as-good-as-stage-one-telemetry]] — prefer cheap stage-1 sources where they suffice and do not buy stage-3 reach on a stage-1 base that cannot trigger it.
