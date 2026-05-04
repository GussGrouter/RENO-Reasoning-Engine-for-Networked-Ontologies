---
id: drill-down-is-only-as-good-as-stage-one-telemetry
type: insight
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Drill-down is only as good as stage-one telemetry"
---

# Drill-down is only as good as stage-one telemetry

## Claim

Drill-down methodology — the **monitor → identify → analyze** progression behind tools like USE checklists, perf flame graphs, `strace`, BCC, and `bpftrace` — is a *refinement* loop. It cannot reveal a problem that the first stage (monitoring, dashboards, exporters, default agents) failed to expose. **Stage-1 telemetry sets a hard upper bound on what any later stage can find:** if a service has no dashboard, if a metric is averaged over the wrong interval, or if the first-stage tool only watches the resources it already knows how to ask about, the deeper stages are silently bounded by that gap.

The decision rule: **before promising what a deeper investigation will deliver, audit the stage-1 layer it depends on.** If stage 1 is blind, low-resolution, or filtered, fix stage 1 first; do not buy more depth on top of a shallow base. Coverage and resolution at stage 1 dominate the value of stage 2 and stage 3 tooling.

The corollary: many streetlight, blame-someone-else, and tools-method failures are stage-1 telemetry problems wearing stage-3 clothing — a missing first-stage signal is read as a missing answer in the deeper tool.

## Concepts involved

- [[use-method]] — USE's resource-first checklist *is* stage 1 for machine-side investigations; its known-unknown audit is a stage-1 hygiene check.
- [[red-method-service-health]] — RED's three signals per service are the canonical stage-1 layer for request-side investigations.
- [[performance-anti-methods]] — streetlight is the dominant stage-1 failure mode; tools-method is the subtler stage-1 failure mode (your stage-1 surface is the union of your tools, not the union of your resources).
- [[problem-statement-first-response]] — the problem statement is built from stage-1 evidence; if stage 1 is incomplete the statement is incomplete by construction.
- [[workload-characterization-input-model]] — workload characterization is the input-side stage 1; drill-down without it can refine the wrong load with great precision.
- [[stack-trace-as-execution-cause]] — stage-3 evidence primitive; a stack captured outside the symptom window is just any-stack, not symptom-stack.

## Source basis

- [[systems-performance-ch2-methodologies-continuation-p91-105]] — § 2.5.12 defines drill-down as monitor → identify → analyze, naming dashboards / exporters at stage 1, intermediate diagnostic tools at stage 2, and deep tracing (`strace`, `perf`, BCC, `bpftrace`, Ftrace) at stage 3; the worked example explicitly threads from a stage-1 dashboard down to a stage-3 trace.
- [[systems-performance-ch2-methodologies-continuation-p76-90]] — § 2.5 frames the streetlight, random-change, blame-someone-else, and tools-method anti-methods, all of which manifest first as stage-1 failures.
- [[systems-performance-ch1-case-studies-references-p56-59]] — the Slow Disks case study: minute-resolution stage-1 monitoring (AcmeMon) misframes the diagnosis until stage-1 resolution is increased; deeper tools were never the missing piece.
- [[systems-performance-ch3-operating-systems-p128-142]] — § 3.2.7 introduces stacks (user + kernel) as the stage-3 evidence primitive; without a stage-1 trigger, that primitive fires blind.

## Decision use

- **Telemetry investment.** When choosing between deeper tracing and broader / faster stage-1 monitoring, default to stage 1 unless stage 1 is already proven adequate for the symptom. Depth is wasted on a base it cannot reach into.
- **Incident triage.** When drill-down dead-ends, do not escalate to deeper tools first; back up and check whether stage 1 was complete, at the right resolution, and aimed at the right service / resource.
- **Architecture review.** Before approving a "we'll trace it in production" plan, demand that stage 1 already detects the symptom. Otherwise the trace will not know when to start.
- **Onboarding.** New responders should learn the stage-1 layer first — it is the bottleneck of every later move they will make. Stage-3 tooling is glamorous; stage-1 hygiene is decisive.
- **Anti-method check.** When a fix is justified by a deep trace alone, ask which stage-1 signal the trace was triggered by. Absence of that signal is the streetlight pattern in disguise: depth without a hypothesis stage 1 produced.
- **Capacity / SLO design.** SLO budgets sit on stage-1 metrics. A stage-1 layer that cannot resolve burst saturation or tail latency cannot defend a tail-aware SLO regardless of what stage-3 tools exist below it.
- **Cross-team handoff.** When platform owns stage-1 (USE, host metrics) and application owns RED (per-service stage 1), drill-down disagreements between teams are usually stage-1 coverage disagreements; resolve at stage 1, not by escalating to deeper tools on either side.
