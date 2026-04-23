# Systems Performance — RED method (2.5.10) (PDF pages 86–96)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.5.10 The RED Method

## Processed artifacts

- Converted slice: `processed/code/systems-performance-red-method-2-5-10.md`
- Chunks:
  - `processed/code/systems-performance-red-method-2-5-10-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) The RED method monitors user-perspective service health: for every service, check request rate, errors, and duration.
- (measurement) Duration should consider distributions (e.g., percentiles), not just the average.
- (diagnosis) Request rate can distinguish load vs architecture explanations: steady rate + rising duration suggests service/architecture issues; rising rate + rising duration suggests load-driven issues.
- (abstraction) The method encourages drawing the service graph and ensuring the three metrics exist per service (coverage).

## Concepts reused / refined / created

- Created (heuristic): [[red-method]]
- Reused (heuristic): [[use-method]] (complement: machine vs user health).
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (diagnosis): [[resource-vs-implementation-bottleneck]] (architecture vs load clueing).
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[red-method]]
  - [[use-method]]
  - [[throughput-latency-metrics]]
  - [[resource-vs-implementation-bottleneck]]
  - [[model-classify-intervene]]

