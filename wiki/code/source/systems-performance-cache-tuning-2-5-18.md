# Systems Performance — cache tuning (2.5.18) (PDF pages 98–106)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.5.18 Cache Tuning

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cache-tuning-2-5-18.md`
- Chunks:
  - `processed/code/systems-performance-cache-tuning-2-5-18-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Systems often contain multiple cache layers; tune caches per level rather than treating “the cache” as singular.
- (diagnosis) Strategy checklist: cache higher in the stack when possible; verify enabled/working; measure hit/miss + miss rate; check dynamic size; tune cache parameters for workload; tune workload to reduce unnecessary cache consumers.
- (diagnosis) Watch for double caching (duplicated memory use for the same data).
- (diagnosis) Prefer tuning cache levels with higher payoff (e.g., avoiding DRAM is larger payoff than shifting L1→L2 hits).

## Concepts reused / refined / created

- Created (method): [[cache-tuning]]
- Reused (mechanism): [[caching]]
- Reused (tradeoff): [[time-space-tradeoff]]
- Reused (heuristic): [[shift-computation-in-time]] (write-back/deferral framing)
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[cache-tuning]]
  - [[caching]]
  - [[time-space-tradeoff]]
  - [[shift-computation-in-time]]
  - [[model-classify-intervene]]

