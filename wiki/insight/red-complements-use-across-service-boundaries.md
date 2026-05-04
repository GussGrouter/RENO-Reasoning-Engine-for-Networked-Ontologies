---
id: red-complements-use-across-service-boundaries
type: insight
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "RED complements USE across service boundaries"
---

# RED complements USE across service boundaries

## Claim

USE and RED are not alternatives — they are the **machine-side** and **service-side** halves of the same triage discipline. USE alone misses user-visible duration shifts that hit before any resource looks hot; RED alone misses resource exhaustion that has not yet propagated into duration or errors. The decision rule: **for every service, run both — USE on the resources hosting it, RED on the requests crossing it — and treat green-on-one with red-on-the-other as a signal, not a contradiction.**

The asymmetry doubles as a load-vs-architecture cue: RED's *rate steady + duration rising* is the canonical architecture-bound signature, available before USE has a chance to argue.

## Concepts involved

- [[use-method]] — resource-side, machine-health triage.
- [[red-method-service-health]] — request-side, service-health triage.
- [[resource-analysis-vs-workload-analysis]] — names the two lenses that USE and RED operationalize.
- [[load-versus-architecture]] — RED's rate-vs-duration cue is the cheapest way to pick the right ceiling class.

## Source basis

- [[systems-performance-ch2-methodologies-continuation-p91-105]] — § 2.5.9 (USE recap) and § 2.5.10 (RED) are presented explicitly as complementary, with the rate-vs-duration heuristic for load vs architecture.
- [[systems-performance-ch2-methodologies-continuation-p76-90]] — § 2.5.9 defines USE and frames it as resource-first, motivating a paired service-side method to cover request-shaped questions.

## Decision use

- **Telemetry coverage.** A service is not "covered" by USE alone or RED alone. Every service needs both sets of signals, even if the underlying data overlaps; the disagreement between the two is what makes them useful.
- **Microservice mesh.** Where per-service USE causes cardinality explosion, RED becomes the minimum-viable health view; USE remains for the underlying nodes / clusters.
- **Incident framing.** When USE is green but users are unhappy, immediately ask for RED. When RED is green but the cluster is on fire, immediately ask for USE. The first lens that turns red owns the next move.
- **Architecture review.** New services should declare their RED and USE points before launch. Reject "we'll add metrics later" — it leaves both lenses blind in production.
- **Alerting hygiene.** Alerts on USE only (e.g. CPU%) miss user-visible regressions that arrive first via duration. Alerts on RED only miss saturation building up before errors appear. Pair them.
- **Cross-team handoff.** When platform owns USE and application owns RED, the handoff conversation reduces to "which lens disagreed first?" — a much cheaper question than "whose fault is it?".
- **Capacity vs reliability.** RED rate trends drive capacity conversations; RED error / duration trends and USE saturation drive reliability conversations. Mixing them up turns one budget into the other.
