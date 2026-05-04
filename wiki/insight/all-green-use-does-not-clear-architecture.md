---
id: all-green-use-does-not-clear-architecture
type: insight
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "All-green USE does not clear architecture"
---

# All-green USE does not clear architecture

## Claim

A USE pass that returns "all green" — every resource at low utilisation, no saturation, no errors — does **not** prove the system has no bottleneck. When the symptom persists across an all-green USE, the working hypothesis must shift from *load-bound* to *architecture-bound*: single-threaded code, lock contention, a serial coordinator, a hard fan-out limit, or a measurement-side limit upstream of the system under test.

The rule is asymmetric. USE *failing* (red on a resource) is strong evidence of that resource as a candidate. USE *passing* is only as strong as the resource list and metric coverage you brought to it; an all-green pass with thin coverage is a known-unknown audit, not a clearance.

## Concepts involved

- [[use-method]] — supplies the resource-first triage that produced the all-green pass.
- [[load-versus-architecture]] — supplies the alternative ceiling class to rotate to.
- [[resource-analysis-vs-workload-analysis]] — names the lens you must add when the resource lens runs out of suspects.
- [[red-method-service-health]] — concrete workload-side fallback: rate / errors / duration as the next signal to read after an all-green USE pass.
- [[scheduler-policy-shapes-latency]] — a "structural" ceiling can be a scheduler / preemption / cgroup policy choice that USE will not surface, especially under voluntary or no-preempt configurations.

## Source basis

- [[systems-performance-ch2-methodologies-p60-75]] — § 2.3.8 defines load-versus-architecture; § 2.3.9 connects it to scalability-knee and contention behaviour, where the limit is structural rather than capacity.
- [[systems-performance-ch2-methodologies-continuation-p76-90]] — § 2.5.9 defines USE and explicitly treats the resource list as bounded by what you measure; missing resources surface as known-unknowns, not as silent green.
- [[systems-performance-ch2-methodologies-continuation-p91-105]] — § 2.5.10 RED gives the workload-side fallback signal (rate / errors / duration) once USE is exhausted.
- [[systems-performance-ch1-case-studies-references-p56-59]] — the Software Change case study: an all-green server with low CPU, where the structural limit is a single-threaded *client* generator.
- [[systems-performance-ch3-operating-systems-continuation-p143-157]] — § 3.2.9 / § 3.2.15 / § 3.2.16: scheduler class, preemption mode, and cgroups are policy levers under which a workload can be effectively limited while every USE-side metric still reads green.

## Decision use

- **Triage stop-rule.** Do not close an incident as "no bottleneck found" on the basis of an all-green USE pass alone. Document either an architectural hypothesis or a known-unknown gap before closing.
- **Capacity vs redesign.** An all-green USE during a capacity request is a strong signal *against* "add nodes". Switch to architecture-bound reasoning before approving the spend; otherwise more capacity will sit idle next to the same ceiling.
- **Load-test interpretation.** If a load test plateaus at a stable rate while every resource on every node sits well below saturation, suspect the load generator, the synchronous protocol, or a serial coordinator before adding hardware.
- **Architecture review.** When a proposal claims a system will scale because "no resource is hot", treat that as USE-only evidence and ask explicitly which structural limits have been ruled out.
- **Anti-pattern check.** An all-green USE that produces a recommendation to "tune until something turns red" is the streetlight anti-method in disguise; reject it. The valid next step is to switch lens, not to keep widening the same one.
- **Workload-side fallback.** When the resource lens is genuinely exhausted, move to workload-side analysis (latency, completion, errors per request) rather than declaring the system healthy.
