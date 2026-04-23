# Systems Performance — perspectives (2.4) (PDF pages 75–82)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.4 Perspectives (resource vs workload analysis)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-perspectives-2-4.md`
- Chunks:
  - `processed/code/systems-performance-perspectives-2-4-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) There are two common analysis perspectives: resource analysis (bottom-up) and workload analysis (top-down); each has different audiences and typical metrics.
- (diagnosis) Resource analysis starts with system resources and often focuses on utilization/saturation to identify approach-to-limit behavior; it supports issue triage and capacity planning.
- (measurement) Resource analysis uses metrics like IOPS, throughput, utilization, saturation (plus latency to evaluate response).
- (diagnosis) Workload analysis starts with application requests and response time (latency), and considers completion/errors (including retries that accumulate latency).
- (measurement) Workload analysis commonly uses throughput and latency to express request rate and response performance; workload characterization summarizes request attributes to identify unnecessary or unbalanced work.

## Concepts reused / refined / created

- Created (diagnosis): [[resource-analysis-vs-workload-analysis]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (diagnosis): [[utilization-and-saturation]]

## Links

- Concepts:
  - [[resource-analysis-vs-workload-analysis]]
  - [[throughput-latency-metrics]]
  - [[utilization-and-saturation]]

