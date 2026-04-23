# Systems Performance — visual identification (2.6.2) (PDF pages 98–114)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.6.2 Visual Identification

## Processed artifacts

- Converted slice: `processed/code/systems-performance-visual-identification-2-6-2.md`
- Chunks:
  - `processed/code/systems-performance-visual-identification-2-6-2-chunk-000001.md`

## Extracted ideas (with classification)

- (technique) Plot delivered performance vs a scaling parameter; patterns can reveal knee points and scalability regimes.
- (diagnosis) A visually identified knee point can be investigated by checking configuration thresholds or architectural limits near that scale point.
- (framework) Common scalability profiles to recognize: linear scalability, contention, coherence, knee point, scalability ceiling.
- (diagnosis) Model-vs-data deviations can indicate model misunderstanding or real system behavior worth investigating.

## Concepts reused / refined / created

- Reused (diagnosis): [[scalability-knee-point]]
- Reused (diagnosis): [[cross-component-interactions]] (shared resource contention/coherence patterns).
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[scalability-knee-point]]
  - [[cross-component-interactions]]
  - [[model-classify-intervene]]

