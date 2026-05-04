---
id: scheduler-policy-shapes-latency
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Scheduler policy shapes latency"
---

# Scheduler policy shapes latency

## Definition

The OS scheduler is not neutral. The choice of scheduling **class** (timesharing, real-time, deadline), **preemption mode** (full / voluntary / none), and **resource control** (cgroup quotas, weights, CPU sets) directly reshapes the latency distribution of every workload running on the host — without changing one line of application code. The same machine, same binary, same workload can show a different tail under different policy combinations.

Three policy levers matter most for performance reasoning:

- **Scheduling class / policy** — CPU-bound and I/O-bound work compete differently under classic timesharing (which de-prioritises long compute to give I/O-bound and interactive work lower latency) than under real-time or deadline classes (which reserve CPU at fixed priorities).
- **Preemption mode** — a fully preemptible kernel offers lower scheduling latency at the cost of throughput; voluntary preemption trades latency for throughput; no-preempt favours throughput and is suitable for batch.
- **Resource controls (cgroups)** — quotas, weights, and CPU sets bound the share each tenant can consume. They make multi-tenant latency predictable but introduce throttling delays whose cost must be reasoned about as a first-class latency source.

The point of the concept is that "the scheduler" is a configurable policy stack, and policy is itself a performance variable.

## Use when

- A latency regression appears with no application change — check whether scheduler class, preemption mode, kernel build configuration, or cgroup limits changed first, before reading the code.
- Designing for predictable tail latency (real-time control loops, low-latency trading, request-response services with tight SLOs) — the policy choice is part of the design, not an afterthought.
- Multi-tenant capacity planning — quotas and weights determine how a noisy neighbour propagates; reasoning about them is more useful than averaging CPU%.
- Migrating workloads between hosts or kernels with different default policies — what looked tuned on host A may be a different shape on host B.
- Auditing a USE pass that returns "low CPU utilisation, high tail latency" — the gap is often scheduler-induced wait, not idle hardware.

## Do not use when

- The application is single-threaded and the symptom is structural — no scheduling policy will make a serial path parallel; switch to [[load-versus-architecture]] reasoning instead.
- The platform forbids scheduler tuning (managed PaaS, sandboxed runtimes); use the concept to *frame* what the platform is hiding from you, not to chase knobs you cannot turn.
- For correctness or fairness questions (real-time guarantees, mandatory access controls); the concept is about latency shape, not about safety properties.
- Stand-alone CPU-bound benchmarks where the scheduler is essentially out of the loop; tuning policy here only adds noise.

## Related concepts

- [[use-method]] — saturation on CPU run-queues and cgroup-throttle counters is the USE-side projection of this policy choice.
- [[load-versus-architecture]] — scheduler policy can shift the apparent architecture-bound knee; the same workload is "architecture-bound" under one policy and "load-bound" under another.
- [[latency-as-common-currency]] — policy-induced wait must be expressed in time alongside service time to be comparable to other latency sources.
- [[performance-anti-methods]] — random-change of preemption modes or cgroup quotas, without a problem statement, is a textbook random-change pattern.
- [[mode-switch-vs-context-switch]] — context-switch cadence is a scheduler-policy outcome and is the cost the policy stack is trading.
- [[red-method-service-health]] — RED's *duration* is what changes when policy shifts, often before any USE metric reacts.

## Source support

- [[systems-performance-ch3-operating-systems-continuation-p143-157]] — § 3.2.9 schedulers (CPU-bound vs I/O-bound priority shaping), § 3.2.15 preemption modes (full / voluntary / none), § 3.2.16 resource controls (cgroups, cgroup v2).
- [[systems-performance-ch3-operating-systems-p128-142]] — § 3.2 frames the scheduler as a kernel mechanism whose decisions can dominate workloads that "look" compute-only.
- [[systems-performance-ch2-methodologies-continuation-p106-120]] — § 2.8 statistics reinforces that long averages hide policy-induced burst latency, requiring percentile-aware reading of any policy change.
