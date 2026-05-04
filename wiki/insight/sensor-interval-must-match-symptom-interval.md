---
id: sensor-interval-must-match-symptom-interval
type: insight
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Sensor interval must match symptom interval"
---

# Sensor interval must match symptom interval

## Claim

A metric is only useful if its averaging window is shorter than the phenomenon you care about. When the symptom is *bursty* — saturation, latency tail, error rate — a long-window average will dilute it into invisibility. The decision rule is: **sample at or below the symptom's interval, and treat any longer-window dashboard as a summary, not as evidence of absence.**

The rule applies in both directions. A sensor that samples much *faster* than the symptom only buys noise and observer-effect overhead, so the goal is *match*, not *minimise*.

## Concepts involved

- [[use-method]] — saturation in USE is the canonical metric category that long averages can hide.
- [[latency-as-common-currency]] — once time is the unit of account, the question of *which interval* becomes explicit instead of implicit.
- [[resource-analysis-vs-workload-analysis]] — both lenses break when the chosen sensor interval mismatches the symptom; this rule binds them.

## Source basis

- [[systems-performance-ch2-methodologies-continuation-p76-90]] — § 2.5.9 USE explicitly notes that short 100 % bursts can hide inside five-minute averages (the tollbooth analogy), and that the resource checklist must be read at an interval that matches the symptom.
- [[systems-performance-ch2-methodologies-continuation-p106-120]] — § 2.8 statistics: a five-minute CPU average hides second-level 100% saturation; decayed averages damp short noise; percentiles tie to SLAs only at the right interval.
- [[systems-performance-ch1-case-studies-references-p56-59]] — the Slow Disks case study: minute-granular AcmeMon misframes the diagnosis until refined with one-second `iostat`, which exposes saturation and latency that the longer window had averaged away.
- [[systems-performance-ch2-methodologies-p60-75]] — § 2.3 frames latency, utilisation, and saturation in time; § 2.3.10 warns that metric overhead and observer effect rise with sampling rate, so over-sampling is also a real cost.

## Decision use

- **Dashboard design.** Before trusting a green dashboard, check the panel's averaging window against the symptom interval. A one-minute panel hides ten-second saturation by construction; do not read its green as health.
- **SLO and alerting.** Match alert windows to the user-perceptible burst length. A p99 latency alert on a five-minute window is a coarse summary, not a tail-aware signal; it will under-report exactly the events the SLO exists to catch.
- **Incident triage.** When a USE pass comes back green at coarse intervals and the symptom is intermittent, drop to second-resolution sampling on the suspected resources before rotating hypotheses or escalating.
- **Benchmarking.** Publish the sampling interval next to every aggregate metric. A throughput or latency number without its averaging window is uninterpretable and should not be compared across runs.
- **Capacity sizing.** Size from peak-interval data, not from monthly averages, when arrivals are bursty; capacity sized to the average will absorb the average and saturate at the burst.
- **Cost trade-off.** Do not buy higher sampling than the symptom requires. Observer effect and storage cost both rise with rate. Pick the coarsest interval that still resolves the burst, then stop.
- **Cross-team handoff.** When a platform team reports "no saturation" and an app team reports "intermittent stalls", suspect an interval mismatch before suspecting either team is wrong.
