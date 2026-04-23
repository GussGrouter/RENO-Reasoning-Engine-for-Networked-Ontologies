# Systems Performance — crisis tools (4.1.2) (PDF pages 118–220)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.1.2 Crisis Tools (slice spans end of `…ch3-background…` extract plus start of `…ch4-scout…` extract due to PDF page boundary)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-observability-crisis-tools-4-1-2.md`
- Chunks:
  - `processed/code/systems-performance-observability-crisis-tools-4-1-2-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) In a production crisis, “missing packages” and slow installs can dominate wall-clock more than analysis time—preparedness is part of performance readiness, not only skill.
- (mechanism) Many tools require *advance* kernel/user-space configuration (CONFIG options, frame pointers vs DWARF, BPF enablement) or they silently degrade—this is a pre-incident validation problem, not a last-minute discovery problem.

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]]
- Reused: [[known-unknowns-framework]]
- Reused: [[observability-vs-experimentation]]
- Reused: [[instrumentation-overhead-and-perturbation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[static-performance-tuning]]
  - [[known-unknowns-framework]]
  - [[observability-vs-experimentation]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[systems-performance]]
