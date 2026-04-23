# Systems Performance — profiling (2.3.13) (PDF pages 72–75)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.3.13 Profiling (sampling-based measurement)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-profiling-2-3-13.md`
- Chunks:
  - `processed/code/systems-performance-profiling-2-3-13-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Profiling builds a picture of a target by sampling system state at timed intervals and analyzing the resulting samples.
- (measurement) Sampling yields a coarse view; how coarse depends on sampling rate.
- (diagnosis) Profiling can attribute resource consumption to code paths (e.g., which paths consume CPU), supporting root-cause localization beyond aggregate metrics.

## Concepts reused / refined / created

- Created (measurement): [[sampling-based-profiling]]
- Reused (measurement): [[counters-statistics-metrics]] (profiling is positioned as deeper than metrics when metrics lack causal detail).
- Reused (measurement): [[instrumentation-overhead-and-perturbation]] (sampling rate affects overhead/coarseness trade-off).

## Links

- Concepts:
  - [[sampling-based-profiling]]
  - [[counters-statistics-metrics]]
  - [[instrumentation-overhead-and-perturbation]]

