# Systems Performance — latency + time scales (2.3.1–2.3.2) (PDF pages 62–66)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Sections 2.3.1–2.3.2 (latency definition/qualification + time scales)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-latency-and-time-scales-2-3-1-2-3-2.md`
- Chunks:
  - `processed/code/systems-performance-latency-and-time-scales-2-3-1-2-3-2-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Latency is time spent waiting before an operation is performed; response time includes latency plus operation/service time.
- (measurement) “Latency” is best treated as a qualified measurement target (request latency, connection latency, etc.) to avoid ambiguity.
- (diagnosis) Latency enables comparisons and ranking because it shares a single unit (time); other rate metrics (e.g., IOPS) are less directly comparable across contexts.
- (diagnosis) Estimating potential speedup is possible when latency can be decomposed into contributing waits and reduced/removed.
- (measurement) Time scales across system components span orders of magnitude; building intuition for time units and typical latencies helps set expectations during diagnosis.

## Concepts reused / refined / created

- Reused (measurement): [[throughput-latency-metrics]]
- Refined (measurement): [[throughput-latency-metrics]] (added explicit “qualified latency target” framing).

## Links

- Concepts:
  - [[systems-performance]]
  - [[throughput-latency-metrics]]

