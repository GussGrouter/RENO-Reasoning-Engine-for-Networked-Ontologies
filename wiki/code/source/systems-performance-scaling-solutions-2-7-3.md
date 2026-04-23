# Systems Performance — scaling solutions (2.7.3) (PDF pages 108–116)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.7.3 Scaling Solutions

## Processed artifacts

- Converted slice: `processed/code/systems-performance-scaling-solutions-2-7-3.md`
- Chunks:
  - `processed/code/systems-performance-scaling-solutions-2-7-3-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) Vertical scaling increases capacity by making a system bigger; horizontal scaling spreads load across many systems behind a load balancer.
- (diagnosis) Cloud enables finer-grained horizontal scaling with smaller increments, reducing early need for large up-front capacity planning.
- (method) Automated scaling can adjust instance/pod count based on a metric target (e.g., CPU utilization thresholds).
- (mechanism) Sharding scales databases by partitioning data; the sharding key is crucial to distribute load evenly.

## Concepts reused / refined / created

- Reused (diagnosis): [[scalability-knee-point]] (scaling often encounters knees/limits).
- Reused (diagnosis): [[utilization-and-saturation]] (metric targets like CPU utilization are about proximity to saturation).
- Reused (insight): [[model-classify-intervene]] (choose scaling intervention based on classified limiter).

## Links

- Concepts:
  - [[scalability-knee-point]]
  - [[utilization-and-saturation]]
  - [[model-classify-intervene]]

