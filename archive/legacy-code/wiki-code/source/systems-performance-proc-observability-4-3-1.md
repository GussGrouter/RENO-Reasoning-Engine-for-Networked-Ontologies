# Systems Performance — /proc observability interface (4.3.1) (PDF pages 171–220)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.3.1 /proc

## Processed artifacts

- Converted slice: `processed/code/systems-performance-proc-observability-4-3-1.md`
- Chunks:
  - `processed/code/systems-performance-proc-observability-4-3-1-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) `/proc` exposes kernel and per-process statistics through a **filesystem namespace** using familiar POSIX read patterns—convenience and permissioning are first-class design forces.
- (measurement) Most reads are cheap, but some paths can trigger expensive kernel walks (e.g., memory-map related traversals), so “/proc is free” is not universally true.
- (diagnosis) When higher-level tools are unavailable, `/proc` can still support **minimal shell-based inspection**—a fallback workflow, not a replacement for structured tooling.

## Concepts reused / refined / created

- Reused (structure): [[kernel-user-boundary]]
- Reused (mechanism): [[system-call]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[kernel-user-boundary]]
  - [[system-call]]
  - [[counters-statistics-metrics]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[systems-performance]]
