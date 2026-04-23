# Systems Performance — chapter 5 exercises: application profile (role, mode, config, metrics) (5.7 partial) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.7 Exercises, item 3 (opening prompts through built-in performance metrics)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-chapter-5-exercises-application-profile-role-and-metrics-5-7.md`
- Chunks:
  - `processed/code/systems-performance-chapter-5-exercises-application-profile-role-and-metrics-5-7-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Define the unit of work** (role + discrete operation) before choosing metrics—otherwise dashboards track activity that does not align with customer-visible latency ([[resource-analysis-vs-workload-analysis]], [[throughput-latency-metrics]]).
- (heuristic) **User vs kernel mode** classification steers whether the first deep dive is syscall/I/O vs on-CPU profiling ([[kernel-user-boundary]], [[drill-down-analysis]]).
- (heuristic) **First-party metrics and config knobs** are part of the **static + runtime contract** of the service—treat “what the app can report” as a discovery step, not an afterthought ([[static-performance-tuning]], [[counters-statistics-metrics]]).

## Application validation

- **On-call handover**: require “one sentence role + one sentence unit of work + three native metrics” before approving a production change window—mirrors this exercise block.

## Concepts reused / refined / created

- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (heuristic): [[drill-down-analysis]]
- Reused (heuristic): [[static-performance-tuning]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-analysis-vs-workload-analysis]]
  - [[throughput-latency-metrics]]
  - [[kernel-user-boundary]]
  - [[drill-down-analysis]]
  - [[static-performance-tuning]]
  - [[counters-statistics-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-chapter-5-exercises-conceptual-review-5-7]]
  - [[systems-performance-chapter-5-exercises-application-profile-observability-and-community-5-7]]
