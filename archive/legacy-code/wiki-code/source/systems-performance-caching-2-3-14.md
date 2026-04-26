# Systems Performance — caching (2.3.14) (PDF pages 72–75)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.3.14 Caching (tiers; hit ratio and miss rate; policies; cache warmth)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-caching-2-3-14.md`
- Chunks:
  - `processed/code/systems-performance-caching-2-3-14-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) Caching stores results from a slower tier in a faster tier; systems often use multiple cache tiers (hardware and software).
- (measurement) Hit ratio is a common cache metric: hits / (hits + misses).
- (diagnosis) Hit ratio can be misleading across workloads because performance impact is nonlinear; miss rate (misses/sec) can be more interpretable for penalty estimation.
- (diagnosis) A simple serialized runtime model can decompose time into hit and miss components using rates and average latencies.
- (mechanism) Cache management policies (LRU/MRU/LFU/MFU variants) and cache warmth (cold/warm/hot) affect observed hit ratios over time (warm-up).

## Concepts reused / refined / created

- Created (mechanism): [[caching]]
- Reused (tradeoff): [[time-space-tradeoff]] (tiering and space↔latency trade).
- Reused (measurement): [[throughput-latency-metrics]] (latency penalty framing for misses).

## Links

- Concepts:
  - [[caching]]
  - [[time-space-tradeoff]]
  - [[throughput-latency-metrics]]

