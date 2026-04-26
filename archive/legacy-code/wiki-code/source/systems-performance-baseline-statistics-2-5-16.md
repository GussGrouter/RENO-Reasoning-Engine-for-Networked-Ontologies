# Systems Performance — baseline statistics (2.5.16) (PDF pages 96–104)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.5.16 Baseline Statistics

## Processed artifacts

- Converted slice: `processed/code/systems-performance-baseline-statistics-2-5-16.md`
- Chunks:
  - `processed/code/systems-performance-baseline-statistics-2-5-16-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Dashboards and trended metrics help spot changes, but many statistics aren’t already monitored; unfamiliar values are hard to interpret without reference.
- (measurement) Collect baseline statistics under “normal” load and record them for later comparison; include deeper tools (profilers/tracing) when safe.
- (diagnosis) Baselines can be captured periodically and before/after changes to support differential analysis; be mindful of measurement overhead/perturbation.
- (measurement) When no baselines exist, summary-since-boot averages can provide a coarse reference.

## Concepts reused / refined / created

- Created (method): [[baseline-statistics]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[baseline-statistics]]
  - [[counters-statistics-metrics]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[model-classify-intervene]]

