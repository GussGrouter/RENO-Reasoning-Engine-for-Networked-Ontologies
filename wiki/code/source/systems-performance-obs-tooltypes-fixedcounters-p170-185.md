# Systems Performance — observability tool types & fixed counters (PDF pages 170–185)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: PDF pages 170–185 (Chapter 4, sections 4.2 Tool Types and 4.2.1 Fixed Counters)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-obs-tooltypes-fixedcounters-p170-185.md`
- Chunks:
  - `processed/code/systems-performance-obs-tooltypes-fixedcounters-chunk-000001.md` (PDF 172–173)

## Refined concepts (from this batch)

- [[protocol-state-machine-model]]
  - Evidence: fixed counters provide count and total time, enabling average latency inference via deltas; tool types (counters vs events) shape what observables you can map to state/work.
- [[resource-vs-implementation-bottleneck]]
  - Evidence: classification depends on the metrics you read (counts/time vs events) and what they imply about resource vs implementation constraints.
- [[network-algorithmics]]
  - Evidence: identifying implementation bottlenecks depends on observability choices that expose the relevant work signals.

## Links

- Concepts:
  - [[protocol-state-machine-model]]
  - [[resource-vs-implementation-bottleneck]]
  - [[network-algorithmics]]
- Related insights:
  - [[model-classify-intervene]]

