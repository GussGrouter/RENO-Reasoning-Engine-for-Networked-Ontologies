---
id: queueing-latency-rises-before-100-percent-utilization
type: insight
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Queueing latency rises long before 100% utilization"
---

# Queueing latency rises long before 100% utilization

## Claim

For non-preemptible queueing systems — canonically disks, but also network buffers, lock-protected paths, and any serial coordinator — **mean response time rises non-linearly with utilization, well before saturation**, and tail percentiles degrade faster still. Treating "utilization < 100%" as "no problem" is a category error: the resource is a queue, and queue latency is a non-linear function of utilization.

The canonical demonstration is the **M/D/1 disk model**, where mean response time roughly **doubles by ~60% utilization** and **triples by ~80%**. Those exact numbers are *example-specific* — they come from M/D/1 service-time assumptions on a disk — but the *shape* of the curve (non-linear rise long before 100%) is the reusable property. Other queue disciplines move the knee; they do not flatten the curve.

The decision rule: **when latency rises and a non-preemptible resource sits at moderate utilization, trust the queueing math, not the headroom number.** Plan capacity, alert thresholds, and SLO budgets accordingly. The same resource at 70% has very different semantics depending on whether it is preemptible (CPU) or non-preemptible (disk, lock, NIC buffer); when in doubt, derive the actual knee for the service distribution at hand rather than reusing the M/D/1 disk numbers as a constant.

## Concepts involved

- [[use-method]] — USE's *saturation* axis is precisely the queue length / wait time this insight names.
- [[load-versus-architecture]] — a queue saturating at 60% can look architecture-bound through a utilization lens; it is actually a load problem with a non-linear cost curve.
- [[latency-as-common-currency]] — converting "70% busy" into "request will wait Xms longer" is what makes the M/D/1 curve actionable.

## Source basis

- [[systems-performance-ch2-methodologies-continuation-p106-120]] — § 2.6.5 derives the M/D/1 disk curve, shows the doubling at ~60% and tripling at ~80% behaviour, and notes that p90 / p99 degrade faster than the mean.
- [[systems-performance-ch2-methodologies-p60-75]] — § 2.3.11 – § 2.3.12 set up the time-busy vs capacity-delivered distinction that makes "<100% utilization" misleading for queueing resources.

## Decision use

- **Capacity headroom.** Set non-preemptible-resource alerts well below 100% (commonly around 60–70%); document the queueing-cost rationale in the runbook so the next responder does not "fix" the alert by raising the threshold.
- **Disk utilization debate.** When platform reports "disk is at 70%, it's fine" and the application team sees rising tail latency, this rule is the resolution: 70% is *expected* to be slow on a deterministic-service queue.
- **Capacity buys.** Refuse "wait for >90%" capacity-trigger policies on disks, NICs, lock-bound paths; user-visible damage is already done by then.
- **SLO design.** When tail-latency SLOs sit on top of queueing resources, budget against the M/D/1 (or appropriate model) curve, not against utilization.
- **Migration planning.** When a workload is moving onto vs off non-preemptible resources (CPU vs disk, async vs sync, batched vs serial), explicitly note that the headroom semantics are not portable.
- **Architecture review.** A new design that depends on running a serial queue past ~70% is a red flag; ask for the queueing analysis or evidence that the workload is bursty / preemptible enough to absorb the curve.
