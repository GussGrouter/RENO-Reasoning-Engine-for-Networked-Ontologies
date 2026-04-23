# Systems Performance — application caching (5.2.2) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.2.2 Caching

## Processed artifacts

- Converted slice: `processed/code/systems-performance-application-caching-5-2-2.md`
- Chunks:
  - `processed/code/systems-performance-application-caching-5-2-2-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) Application caches repeat the general pattern: **reuse expensive read results** from a faster tier; deployment work is discovering which caches exist, enabling them, and **sizing** against memory pressure.
- (abstraction) Caches often **double as write buffers**—read and write paths are coupled in configuration, so cache sizing decisions are simultaneously **latency, throughput, and durability** decisions.

## Concepts reused / refined / created

- Reused (mechanism): [[caching]]
- Reused (abstraction): [[time-space-tradeoff]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[caching]]
  - [[time-space-tradeoff]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
