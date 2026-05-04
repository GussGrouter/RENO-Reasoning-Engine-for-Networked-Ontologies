---
id: load-versus-architecture
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Load versus architecture"
---

# Load versus architecture

## Definition

A diagnostic distinction between two unrelated kinds of performance ceiling:

- **Load-bound** systems are limited by how much work is offered relative to capacity. Resource utilisation rises with offered load; queues form; metrics like CPU%, run-queue length, and saturation react to demand. Adding capacity helps.
- **Architecture-bound** systems are limited by *structure*: single-threaded code, lock contention, a serial choke point, an algorithmic class, a synchronous protocol, or a hard fan-out limit. Resource utilisation may stay low even at saturation; adding capacity does not help, or helps only sideways.

The point of the distinction is not to label a system once and for all. The same system can be load-bound at one workload and architecture-bound at another. The decision is which model to apply to the *current* symptom and which class of fix is plausible.

## Use when

- A performance investigation has plateaued: resource metrics look healthy but throughput will not climb or latency will not fall.
- You are choosing between *scaling* (more capacity) and *redesigning* (changing structure) and need a defensible answer rather than reflex.
- A load test hits a ceiling at a specific request rate while resource utilisation stays well below 100% on every node.
- Reviewing an architecture proposal: spot the future structural ceiling before it is built.
- Reading a post-mortem that blames load when the underlying limit is single-threading, lock contention, or a serial coordinator.
- A USE pass comes back all-green and the symptom persists.

## Do not use when

- You have not yet ruled out *measurement-side* limits (saturated load generators, throttled clients, network bottlenecks between client and server). The dichotomy assumes the load you measure is the load you sent.
- The system is genuinely over-capacity and the obvious answer is "add nodes"; do not over-frame a plain load problem as architectural.
- For a single-shot latency budget question; latency dominated by serial work is better expressed via [[latency-as-common-currency]] than via this binary frame.
- As a verdict on a whole platform; apply per workload and per symptom.

## Related concepts

- [[resource-analysis-vs-workload-analysis]] — green resource metrics under saturation are the canonical case where the load-versus-architecture frame is required.
- [[use-method]] — when a USE pass returns all-green and the symptom persists, suspect architecture-bound, not no-bottleneck.
- [[latency-as-common-currency]] — useful when the structural limit shows up as latency rather than throughput.
- [[scheduler-policy-shapes-latency]] — scheduler class, preemption mode, and cgroup constraints can shift the architecture-bound knee without changing application code.
- *scalability-knee-and-contention* (deferred) — formalises how load-bound systems transition into contention-bound regions and look architecture-bound at scale.

## Source support

- [[systems-performance-ch2-methodologies-p60-75]] — § 2.3.8 defines the load-versus-architecture distinction; § 2.3.9 connects it to scalability-knee and contention behaviour.
- [[systems-performance-ch2-methodologies-continuation-p91-105]] — § 2.5.10 RED supplies the rate-vs-duration shortcut: rate steady + duration rising is the architecture-bound signature.
- [[systems-performance-ch1-case-studies-references-p56-59]] — the Software Change case study illustrates an architecture-bound *test rig* (single-threaded client) masquerading as a server-side regression.
