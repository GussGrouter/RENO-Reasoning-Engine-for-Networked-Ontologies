---
id: resource-analysis-vs-workload-analysis
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Resource analysis vs workload analysis"
---

# Resource analysis vs workload analysis

## Definition

Two complementary lenses on the same system:

- **Resource analysis** examines hardware and OS resources bottom-up — CPUs, memory, network interfaces, storage devices, controllers, interconnects, and any accelerators in use. Its native metrics are IOPS, throughput, utilisation, and saturation.
- **Workload analysis** examines the application top-down — what requests come in, how they complete, and the latency they experience. Its native metrics are request rate, latency, and completion or error status.

Choosing a lens is a decision about *where to start an investigation*, not a claim about which layer is at fault. A competent investigation usually switches between lenses rather than picking one for the whole incident.

## Use when

- Incident ownership is split between platform/SRE and application teams, and matching the lens to *who can act* compresses time to fix.
- A latency SLO is failing and the workload lens is the cheapest path to a quantified problem statement.
- Capacity planning or shared-tenant noise hunting pushes toward the resource lens because workload-side metrics are not under your control.
- A previous round of analysis fixated on one lens and stalled — switching deliberately reframes the problem instead of repeating it harder.

## Do not use when

- As a binary truth claim about the system. Both lenses can be wrong simultaneously, and either can mislead without the other.
- To assign blame across teams. A picked lens is a starting place, not a verdict.
- When the actual limit is structural — single-threaded code, lock contention, or an architectural ceiling — the resource lens may show low utilisation across many resources and look healthy. Pair with structural reasoning before reading green metrics as health.
- For a black-box endpoint with no measurable internals, where workload-only is your only option; calling that a deliberate choice is fine, but "picking a lens" is misleading there.

## Related concepts

- [[use-method]] — the canonical resource-side methodology that operationalises the resource lens.
- [[red-method-service-health]] — the canonical workload-side / service-health methodology that operationalises the workload lens.
- [[workload-characterization-input-model]] — input modeling on the workload-analysis side; pairs naturally with RED.
- [[load-versus-architecture]] — sharpens when low resource utilisation should not be read as health.
- [[latency-as-common-currency]] — supports the workload lens when comparing heterogeneous work in commensurate units.

## Source support

- [[systems-performance-ch2-methodologies-continuation-p76-90]] — defines the two perspectives in §2.4 and pairs them with USE/RED in §2.5.
- [[systems-performance-ch2-methodologies-continuation-p91-105]] — § 2.5.10 makes RED explicit as the workload-side counterpart to USE, sharpening the lens contrast.
- [[systems-performance-ch1-case-studies-references-p56-59]] — illustrates the lenses through the Slow Disks (resource lens) and Software Change (workload lens) case studies.
