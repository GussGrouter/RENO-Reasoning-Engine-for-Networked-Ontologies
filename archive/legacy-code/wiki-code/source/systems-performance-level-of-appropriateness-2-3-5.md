# Systems Performance — level of appropriateness (2.3.5) (PDF pages 66–70)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.3.5 Level of Appropriateness (depth of analysis vs ROI)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-level-of-appropriateness-2-3-5.md`
- Chunks:
  - `processed/code/systems-performance-level-of-appropriateness-2-3-5-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Depth of analysis should match environment needs and expected return on investment (ROI); “advanced” vs “basic” depends on context.
- (diagnosis) ROI can be cost-based (compute spend) or experience-based (latency/user retention), shaping prioritization.
- (measurement) Greater analysis depth often implies higher-cost measurement (more instrumentation and more detailed signals), which should be justified by ROI.

## Concepts reused / refined / created

- Reused (measurement): [[instrumentation-overhead-and-perturbation]] (more tracing/instrumentation implies additional measurement cost and potential perturbation).
- Reused (measurement): [[observability-vs-experimentation]] (depth decisions include whether to stay observational or run experiments).

## Links

- Concepts:
  - [[systems-performance]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[observability-vs-experimentation]]

