# Systems Performance — write coalescing, polling, and readiness scalability (5.2.3–5.2.4) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Sections 5.2.3 Buffering + 5.2.4 Polling (incl. readiness interfaces that scale differently)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-buffering-polling-scalability-5-2-3-4.md`
- Chunks:
  - `processed/code/systems-performance-buffering-polling-scalability-5-2-3-4-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Write coalescing** trades added **write latency** (first writer waits for batchmates) for fewer, larger downstream operations—another [[throughput-latency-metrics]] coupling tied to [[shift-computation-in-time]] batching.
- (mechanism) **Ring buffers** decouple producers/consumers on a fixed footprint—classic bounded-queue backpressure pattern in streaming systems.
- (diagnosis) Naive **polling loops** burn CPU and add event-to-handler latency when work is sparse; switching to **push/event** models moves cost off the idle hot path ([[fast-path-slow-path]] framing).
- (abstraction) Readiness abstractions differ in **how work grows with monitored handles** (example narrative: scanning \(O(n)\) vs registration maps with \(O(1)\) activation)—the cross-domain lesson is “API shape determines hidden asymptotics under load,” not the syscall names.

## Concepts reused / refined / created

- Reused (measurement): [[throughput-latency-metrics]]
- Reused (heuristic): [[shift-computation-in-time]]
- Reused (structure): [[fast-path-slow-path]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused: [[systems-performance]]

## Related sections

- [[systems-performance-concurrency-parallelism-and-user-schedulers-5-2-5]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[shift-computation-in-time]]
  - [[fast-path-slow-path]]
  - [[resource-vs-implementation-bottleneck]]
  - [[systems-performance]]
