---
id: scheduler-policy-can-move-tail-latency-without-code-change
type: insight
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Scheduler policy can move tail latency without code change"
---

# Scheduler policy can move tail latency without code change

## Claim

A change in scheduler policy — class, preemption mode, or cgroup constraint — can produce a measurable tail-latency regression or improvement on a workload whose application code has not changed. The decision rule: **when latency shifts and the diff at the application layer is empty, audit the scheduler policy stack before opening the code**. Conversely, when planning a tuning change at the policy layer, treat it as a workload-perturbing change and benchmark against the symptom interval, not against the average.

The rule cuts both ways. A "harmless" preemption-mode change pushed by a kernel upgrade can become an SLO incident. A deliberate cgroup quota intended to isolate a noisy neighbour can starve the workload it was supposed to protect, by moving wait time from "noisy neighbour" to "throttled-by-quota". Both look like application bugs through a code-only lens.

## Concepts involved

- [[scheduler-policy-shapes-latency]] — the underlying mechanism: policy decisions reshape the latency distribution.
- [[load-versus-architecture]] — a policy-induced ceiling masquerades as architecture-bound when the resource lens stays green; this insight names the rotation step.
- [[latency-as-common-currency]] — quantifying the regression in time is what makes "policy moved tail" a falsifiable claim.
- [[performance-anti-methods]] — random-change of preempt mode or cgroup quotas, without a written problem statement, is the canonical random-change anti-method.
- [[use-method]] — saturation on run-queue length and cgroup throttle counters is the USE-side projection of this policy change; absence of those signals at the symptom interval does not clear the hypothesis.

## Source basis

- [[systems-performance-ch3-operating-systems-continuation-p143-157]] — § 3.2.9 schedulers, § 3.2.15 preemption modes, and § 3.2.16 resource controls (cgroups, cgroup v2) frame these as configuration choices that trade throughput for latency predictability.
- [[systems-performance-ch3-operating-systems-p128-142]] — § 3.2 names the scheduler as a kernel mechanism whose decisions can dominate workloads that "look" compute-only.
- [[systems-performance-ch2-methodologies-continuation-p106-120]] — § 2.8 statistics: a five-minute average can hide second-level saturation that a policy change just made worse; percentile-aware reading is required.

## Decision use

- **Regression triage.** Before profiling code on a tail-latency regression, list every recent change at the scheduler-policy layer: kernel upgrade and its preemption-config defaults, cgroup quota update, scheduler-class change, CPU-set change, security-mitigation toggle. If any landed near the symptom start, that is your first hypothesis.
- **Capacity decisions.** Do not approve a "buy more nodes" request when the symptom is policy-induced wait. The new capacity will inherit the same policy and the same tail.
- **Tuning hygiene.** Treat any cgroup or preemption-mode change as a workload-shaping change. Re-run the SLO-relevant benchmark *at the symptom interval*, not at long averages — long averages will under-report exactly the bursts the policy reshaped.
- **Multi-tenant isolation.** When a quota intended to protect tenant A starves tenant B, the cure is rebalancing weights / quotas with a model of arrival shape, not raising the global cap.
- **Cross-team handoff.** When platform reports "no resource is hot" and application reports "tail got worse", suspect a policy-layer change. The platform layer often owns this knob; the application team often does not see it.
- **Architecture review.** A new service whose latency budget assumes a particular preemption mode or cgroup configuration must declare those assumptions; otherwise the service is fragile to platform-side changes its owners cannot monitor.
- **Anti-pattern check.** A "fix" that consists of toggling preemption mode or cgroup quotas without a problem statement is the random-change anti-method; reject it even if the metric line moves the right way that hour.
