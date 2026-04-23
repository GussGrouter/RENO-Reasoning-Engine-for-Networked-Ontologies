# Systems Performance — application basics (5.1) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.1 Application Basics (context questionnaire before objectives)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-application-basics-5-1.md`
- Chunks:
  - `processed/code/systems-performance-application-basics-5-1-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Context before tuning**: role of the service, request shape, SLO posture, configuration knobs, host limits, metrics/logs, version/release notes, bug trackers, source/community/books/experts—mirrors a domain-expanded [[problem-statement-method]] for packaged software.
- (abstraction) **Workload expression**: operational rate of meaningful operations is the bridge from business load to capacity work—aligns with [[resource-analysis-vs-workload-analysis]] (requests vs resources).
- (diagnosis) A **functional diagram** (when available) collapses unknown-unknown risk by making dominant paths and dependencies explicit.

## Concepts reused / refined / created

- Reused (heuristic): [[problem-statement-method]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (heuristic): [[static-performance-tuning]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[problem-statement-method]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[static-performance-tuning]]
  - [[known-unknowns-framework]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
