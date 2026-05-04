# Systems Performance — event tracing (2.5.15) (PDF pages 96–104)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.5.15 Event Tracing

## Processed artifacts

- Converted slice: `processed/code/systems-performance-event-tracing-2-5-15.md`
- Chunks:
  - `processed/code/systems-performance-event-tracing-2-5-15-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) Systems process discrete events (I/O, packets, syscalls, transactions, queries, etc.). Summary metrics can lose critical detail.
- (measurement) Tracing inspects events individually and records request attributes, timestamps (start/end/latency), and results (including errors).
- (diagnosis) Event history helps explain latency outliers: high-latency events may be slow because of prior queued events, not their own properties.

## Concepts reused / refined / created

- Created (measurement): [[event-tracing]]
- Reused (method): [[latency-analysis]]
- Reused (method): [[drill-down-analysis]]
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[event-tracing]]
  - [[latency-analysis]]
  - [[drill-down-analysis]]
  - [[model-classify-intervene]]

