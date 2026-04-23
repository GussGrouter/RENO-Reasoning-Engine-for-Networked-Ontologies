# Systems Performance — non-blocking / asynchronous I/O rationales (5.2.6) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.2.6 Non-Blocking I/O

## Processed artifacts

- Converted slice: `processed/code/systems-performance-nonblocking-io-async-models-5-2-6.md`
- Chunks:
  - `processed/code/systems-performance-nonblocking-io-async-models-5-2-6-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Blocking thread-per-work-unit** couples **concurrency width** to **thread/memory footprint** and amplifies [[context-switching]] under bursty short I/O—classic production tail-latency and CPU “mystery idle” source.
- (abstraction) **Async submission** moves “wait for device” off the request thread’s critical path; ring-buffered submission interfaces are another instance of **batching + shared queue** between protection domains ([[kernel-user-boundary]], [[shift-computation-in-time]]).
- (measurement) Kernel-deferred paths (example narrative: zero-copy style handoffs) reduce **user/kernel boundary crossings** for bulk transfer—same category decision as pushing work to the cheaper side of a boundary in distributed RPC stacks.

## Concepts reused / refined / created

- Reused (mechanism): [[context-switching]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (heuristic): [[shift-computation-in-time]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (mechanism): [[system-call]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[context-switching]]
  - [[throughput-latency-metrics]]
  - [[shift-computation-in-time]]
  - [[kernel-user-boundary]]
  - [[system-call]]
  - [[systems-performance]]
