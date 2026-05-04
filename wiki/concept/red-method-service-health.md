---
id: red-method-service-health
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "RED method"
---

# RED method

## Definition

A workload-side methodology for any request-response service. For every service, monitor:

- **Rate** — request rate (requests per second).
- **Errors** — failed requests (rate or count).
- **Duration** — request latency, expressed as a *distribution* (median, p95, p99, p99.9), not a single mean.

RED is the canonical workload-side / user-facing complement to USE. USE asks *"is the machine OK?"*; RED asks *"is the service OK?"*. The active practice is to draw the service architecture and ensure all three signals exist *per service* — distributed-tracing tools may produce both the diagram and the metrics.

The shape of the three signals also gives a cheap **load-versus-architecture** cue: rate steady + duration rising → architecture; rate rising + duration rising → load.

## Use when

- Designing dashboards or SLOs for any request-response service.
- A microservice mesh where per-service USE cardinality is unmanageable — RED's three-per-service is the minimum viable health view.
- Distinguishing whether degradation is load-bound or architecture-bound from telemetry alone, before profiling.
- Auditing incident telemetry coverage: every service must expose at least these three.
- Comparing user-visible health between services with very different internal mechanics.

## Do not use when

- Background or batch jobs without a clear request boundary — queue length and progress are more meaningful than rate / duration.
- Stream / event systems where "request rate" is meaningless or replaced by throughput and lag.
- The system is single-tenant and resource-bound — USE on the host may already explain the symptom; do not invent a per-request frame just to fit the method.
- Deeply asynchronous pipelines where "duration" does not map to a user-visible event.

## Related concepts

- [[use-method]] — machine-side counterpart; pair USE and RED for full coverage.
- [[resource-analysis-vs-workload-analysis]] — RED is the canonical workload-side telemetry triad.
- [[load-versus-architecture]] — RED's rate-vs-duration shape is the cheapest load-vs-architecture cue.
- [[latency-as-common-currency]] — RED's *duration* must be a latency distribution, not a single mean.

## Source support

- [[systems-performance-ch2-methodologies-continuation-p91-105]] — § 2.5.10 defines RED, contrasts it with USE as machine vs user health, and gives the rate-vs-duration shortcut for load vs architecture.
