# Systems Performance — trade-offs (2.3.3) (PDF pages 64–71)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.3.3 Trade-Offs (project and tuning trade-offs)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-trade-offs-2-3-3.md`
- Chunks:
  - `processed/code/systems-performance-trade-offs-2-3-3-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Project trade-offs can defer performance work; early architectural choices can inhibit later performance improvement.
- (mechanism) CPU–memory trade-offs can be implemented via caching or compression depending on which resource is abundant.
- (mechanism) Tunables often encode trade-offs (e.g., buffer sizes, record sizes) that shift costs between memory, throughput, latency, and scalability.
- (diagnosis) Performance changes should be evaluated with explicit trade-offs in mind (what got better, what got worse, and under which workload).

## Concepts reused / refined / created

- Reused (mechanism/tradeoff): [[time-space-tradeoff]]

## Links

- Concepts:
  - [[systems-performance]]
  - [[time-space-tradeoff]]

