# Systems Performance — Advanced workload questions, perf view, tracing cost (§8.5.3) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.5.3** — extended checklist (**omitted** as list) + **performance characterization** bullets + **event tracing** overhead note

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-workload-char-advanced-8-5-3b.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-workload-char-advanced-8-5-3b-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement pairing) Split **what you asked for** (workload characterization) from **what you got** (latency averages, outliers, distributions, throttle state)—same batch, different questions.
- (perturbation) **Full FS op tracing** is attractive as “ground truth” but often **too expensive** at production op rates → **filtered / slow-path-only** traces or **event rate control** ([[instrumentation-overhead-and-perturbation]]).
- (scope) **Resource controls:** include whether **throttles** were active when reading latency—otherwise latency is “valid” for a different policy regime.

## Application validation

- **Turn on verbose FS tracing and p99 improves:** suspect **observer effect** and **selection bias** (only slow ops logged may still perturb coherency)—validate with **before/after overhead** and **representative filters**.

## Decision clarity

- **Decision:** choose **heavyweight per-op tracing with aggressive filters** over **always-on complete logs** when **op rate is high** but **only tail events** need capture.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[event-tracing]], [[instrumentation-overhead-and-perturbation]], [[resource-analysis-vs-workload-analysis]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[event-tracing]], [[instrumentation-overhead-and-perturbation]], [[resource-analysis-vs-workload-analysis]], [[cross-component-interactions]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-workload-char-basic-8-5-3a]], [[systems-performance-filesystems-ch8-performance-monitoring-8-5-4]]
