# Systems Performance — point-in-time recommendations (2.3.7) (PDF pages 68–72)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.3.7 Point-in-Time Recommendations (validity over time)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-point-in-time-recommendations-2-3-7.md`
- Chunks:
  - `processed/code/systems-performance-point-in-time-recommendations-2-3-7-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Performance recommendations and tuning values are valid only at a point in time; upgrades and workload shifts can move the bottleneck and invalidate prior advice.
- (diagnosis) “Internet tunables” can mislead: values can be workload-specific, time-specific, or temporary workarounds; treat them as hypotheses to validate.
- (measurement) Capturing configuration/tunable changes with history (e.g., versioned records) preserves context needed to interpret later performance changes.

## Concepts reused / refined / created

- Reused (diagnosis): [[cross-component-interactions]] (changes can shift which component dominates and how effects compose).

## Links

- Concepts:
  - [[systems-performance]]
  - [[cross-component-interactions]]

