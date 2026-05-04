---
id: use-method
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "USE method"
---

# USE method

## Definition

A triage methodology for resource-bound systems: **for every resource, check utilisation, saturation, and errors**. Iteration is *resource-first*, never tool-first; the tool list is a consequence of the resource list, not the other way around. Within each resource the procedure is **errors → saturation → utilisation**, because errors are the cheapest to interpret and saturation reads more directly than time-based utilisation does.

A USE pass yields:

- a checklist that names every resource in scope (CPU sockets/cores, memory, NIC, storage, accelerators, controllers, interconnects), and
- for each resource, either a metric you can fetch today or an explicit *known-unknown* you cannot fetch yet.

The known-unknown audit is part of the value: USE converts silent blind spots into named gaps you can prioritise.

## Use when

- Triaging a complex stack where the bottleneck location is unknown and the time budget is small.
- You suspect the problem is missing instrumentation more than missing analysis; USE is designed to make blind spots visible rather than hide them.
- You are about to reach for "whatever tool is familiar" and want to discipline the search before guessing.
- You need a defensible inventory to hand off — the same checklist works as a runbook for the next responder.
- Burst utilisation is suspected and long-window averages might hide it; USE forces you to ask whether the metric interval matches the symptom interval.

## Do not use when

- The resource list is the wrong shape. USE is weakest for caches, which improve performance under high utilisation; for cache investigations use cache-specific metrics (hit ratio, miss rate, warm-up).
- The bottleneck lives in application logic, single-threading, or lock contention. USE may show every resource as idle while the architecture is the limit; pair with workload-side analysis.
- You have no measurement coverage at all for several resources and no realistic way to add it; in that case treat USE's output as a known-unknown audit, not a finished investigation.
- For latency budgeting and SLO design, where workload analysis is the primary lens.
- When the symptom is clearly a regression tied to a recent change; start with version control and change history before iterating across every resource.

## Related concepts

- [[resource-analysis-vs-workload-analysis]] — USE is the resource-side method; pair with workload-side analysis for end-to-end coverage.
- [[red-method-service-health]] — the service-side counterpart; pair USE and RED so machine and service health stay jointly bounded.
- [[problem-statement-first-response]] — usually runs before USE, to bound the question.
- [[load-versus-architecture]] — explains why an all-green USE pass can still be hiding the limit.
- [[workload-characterization-input-model]] — characterizing input often selects which resources USE should walk first.
- [[performance-anti-methods]] — USE is structurally resistant to the streetlight pattern (resource-first, not tool-first).
- [[scheduler-policy-shapes-latency]] — CPU-side USE readings (utilisation, run-queue saturation) are read against the active scheduler / preemption / cgroup policy.
- [[mode-switch-vs-context-switch]] — context-switch saturation and mode-switch rate are first-class USE signals on CPU resources.

## Source support

- [[systems-performance-ch2-methodologies-continuation-p76-90]] — defines USE in §2.5.9, the errors → saturation → utilisation order, the resource list, and the known-unknowns view of the metric checklist.
- [[systems-performance-ch2-methodologies-continuation-p91-105]] — § 2.5.9 extends USE to *software resources* (mutex, thread pool, FD limits) and to tenant caps, and contrasts USE with RED.
- [[systems-performance-ch1-introduction-p40-55]] — forward-pointer framing in §1.5 and §1.10 that motivates a methodology over ad-hoc fishing.
