# Systems Performance — factor analysis (2.7.2) (PDF pages 108–116)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.7.2 Factor Analysis

## Processed artifacts

- Converted slice: `processed/code/systems-performance-factor-analysis-2-7-2.md`
- Chunks:
  - `processed/code/systems-performance-factor-analysis-2-7-2-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Many capacity-planning factors (CPU, disks, RAM, RAID, settings, features) create a combinatorial testing problem.
- (method) Approach: test maximum configuration, vary factors one-by-one and measure drops, attribute drop and cost savings, select a cheaper config that meets required performance, then retest.
- (diagnosis) Single-factor attribution can mislead when factors interact; retest chosen combinations for confirmation.

## Concepts reused / refined / created

- Created (method): [[factor-analysis-capacity-planning]]
- Reused (diagnosis): [[cross-component-interactions]]
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[factor-analysis-capacity-planning]]
  - [[cross-component-interactions]]
  - [[model-classify-intervene]]

