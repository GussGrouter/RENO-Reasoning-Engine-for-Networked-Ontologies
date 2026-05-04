---
id: workload-characterization-input-model
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Workload characterization (input model)"
---

# Workload characterization (input model)

## Definition

A method that frames performance work around the **input** to the system rather than the system's output. It builds a model of the load by answering four questions:

- **Who** is causing the load — process / user / source IP / tenant?
- **Why** is the load being called — code path, stack trace, business reason?
- **What** are the load characteristics — IOPS, throughput, direction (read / write), type, distribution and variance?
- **How** is the load changing over time — daily / weekly / seasonal cycles, growth, sudden ramps?

The output is a model of *incoming work* you can reason about *before* asking whether the system is fast enough. Common surprises this surfaces include unnecessary work, hostile load (DoS / runaway clients / retry storms), mis-scheduled batch jobs, and workloads that have outgrown their original sizing assumptions.

## Use when

- Performance is bad and the system itself "looks fine" — characterizing the input often reveals the load is the bug.
- Designing simulation benchmarks or load tests — distribution and variance feed realistic generators; an averaged-only model produces unreliable test rigs.
- Capacity planning — projecting hardware needs requires knowing what hardware will actually absorb.
- Pre-redesign sanity check — before scaling or rearchitecting, confirm that the load you have is the load you should have.
- Cross-team incident reviews where a downstream service is overwhelmed — naming the upstream load makes ownership concrete and answers "who do we ask to back off?".

## Do not use when

- The input is well known and stable, and the symptom is clearly an internal regression — start with version control, profiling, or USE first.
- Black-box services with no input visibility — fall back to RED or workload-output proxies first, then revisit characterization once data is in reach.
- For purely structural (architecture-bound) limits — input characterization is a red herring; switch lens.
- During an active incident where rolling back the most recent change is the cheaper move.

## Related concepts

- [[use-method]] — characterizing input often reveals which resources to USE-check first.
- [[red-method-service-health]] — RED measures the *response*; workload characterization studies the *input*.
- [[resource-analysis-vs-workload-analysis]] — workload characterization sits firmly on the workload-analysis side of the lens choice.
- [[load-versus-architecture]] — confirming that the load is what you think it is is a precondition for the load-vs-architecture decision.
- [[problem-statement-first-response]] — workload characterization is often the data behind questions 3 and 4 of the problem statement.

## Source support

- [[systems-performance-ch2-methodologies-continuation-p91-105]] — § 2.5.11 defines workload characterization, gives the four discovery questions, and the DoS surprise example where "obvious" client identity was wrong.
