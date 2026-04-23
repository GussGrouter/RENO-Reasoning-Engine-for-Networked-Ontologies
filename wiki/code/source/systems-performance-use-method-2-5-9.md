# Systems Performance — USE method (2.5.9) (PDF pages 86–96)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.5.9 The USE Method

## Processed artifacts

- Converted slice: `processed/code/systems-performance-use-method-2-5-9.md`
- Chunks:
  - `processed/code/systems-performance-use-method-2-5-9-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) The USE method should be used early to identify systemic bottlenecks: for every resource, check utilization, saturation, and errors.
- (measurement) Utilization and saturation require careful interpretation: short bursts can create saturation even if long-window utilization averages look low.
- (diagnosis) Iterating resources (not tools) promotes coverage; missing metrics become explicit [[known-unknowns-framework]].
- (abstraction) A resource list or functional block diagram can structure the iteration and surface overlooked components (e.g., interconnects).
- (mechanism) Some resources (e.g., caches) behave differently under utilization; they may not fit the same “degrades under high utilization” model and can be addressed with other methodologies.

## Concepts reused / refined / created

- Created (heuristic): [[use-method]]
- Reused (diagnosis): [[utilization-and-saturation]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (abstraction): [[known-unknowns-framework]]
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[use-method]]
  - [[utilization-and-saturation]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[known-unknowns-framework]]
  - [[model-classify-intervene]]

