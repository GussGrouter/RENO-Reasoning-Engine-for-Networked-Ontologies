# Systems Performance — File system features overview (§8.4.4) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.4.4** — block vs extent, journaling tradeoffs, **COW**, scrubbing cost (**stops before §8.4.5 FS-type catalog**)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-fs-features-8-4-4.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-fs-features-8-4-4-chunk-000001.md`

## Extracted ideas (with classification)

- (tradeoff) **Journaling** buys fast recovery / write coalescing but can **multiply physical writes** ([[throughput-latency-metrics]], [[resource-vs-implementation-bottleneck]]).
- (tradeoff) **COW** improves safety + can sequentialize writes; **near-full pools** fragment and hurt HDD-style latency ([[throughput-latency-metrics]], [[measurement-validity]]).
- (perturbation) **Scrubbing** is **validity-friendly** health checking but competes for **bandwidth**—schedule as capacity decision ([[measurement-validity]], [[throughput-latency-metrics]]).

## Application validation

- **Write amplification after enabling journal-data mode:** measure **physical bytes per logical write** before declaring **application bug**—may be **expected FS tax**.

## Decision clarity

- **Decision:** choose **FS feature flags that match durability math (journal metadata-only vs data)** over **application-level double-writes** when **the bottleneck is redundant persistence layers** you can **turn down safely**.

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[systems-performance]]
