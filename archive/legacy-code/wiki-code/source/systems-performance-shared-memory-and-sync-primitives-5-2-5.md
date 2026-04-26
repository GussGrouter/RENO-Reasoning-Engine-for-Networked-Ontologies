# Systems Performance — shared memory integrity and synchronization primitives (5.2.5 part) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.2.5 (threads + shared memory + mutex/spin/RW/semaphore roles)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-shared-memory-and-sync-primitives-5-2-5.md`
- Chunks:
  - `processed/code/systems-performance-shared-memory-and-sync-primitives-5-2-5-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) Shared-address multithreading trades **IPC cost** for **data races** unless invariants are enforced with synchronization—performance work becomes “who waits, where, and on what schedule.”
- (measurement) **Blocking locks** move contention **off-CPU** (wait time becomes scheduler/latency story); **spin locks** keep contenders **on-CPU** trading **tail latency** for **burned cycles**—the same “wait vs work” framing as busy polling elsewhere.
- (abstraction) **Reader/writer** and **counting semaphores** tune **parallelism width** vs **exclusivity**; misuse shows up as either **serialization** or **inconsistent reads**, not just “slow lock API.”

## Concepts reused / refined / created

- Reused (measurement): [[throughput-latency-metrics]]
- Reused (heuristic): [[latency-analysis]]
- Reused (mechanism): [[context-switching]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (abstraction): [[process-abstraction]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[latency-analysis]]
  - [[context-switching]]
  - [[resource-vs-implementation-bottleneck]]
  - [[process-abstraction]]
  - [[systems-performance]]
