# Systems Performance — Leak detection methodology (7.4.6) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.4.6** — establish **growth vs variance**, isolate **allocation sites**, distinguish **true leaks vs caches**, track **allocator slowdown vs footprint**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-methodology-leak-detection-7-4-6.md`
- Chunks:
  - `processed/code/systems-performance-memory-methodology-leak-detection-7-4-6-chunk-000001.md`

## Extracted ideas (with classification)

- (method) **Leak workflow = controlled experiment**: **baseline → change one variable → diff** beats ad-hoc heap snapshots ([[scientific-method]], [[measurement-validity]], [[resource-vs-implementation-bottleneck]]).
- (heuristic) **Unbounded caches** mimic leaks—requires **intent + bounds** audit, not only **allocation stack proof** ([[caching]]).

## Application validation

- **Suspected leak**: capture **growth slope under identical traffic**, then **toggle single cache/feature flag**—if slope unchanged, revisit **representation** (RSS vs cgroup accounting).

## Decision clarity

- **Decision**: choose **growth slope + single-variable toggles** over **heap dumps alone** when **RSS rises slowly** but **GC/allocator CPU stays flat** (hinting **reference retention/caching**, not allocator pathology).

## Concepts reused / refined / created

- Reused (method): [[scientific-method]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[resource-vs-implementation-bottleneck]]
- Reused (mechanism): [[caching]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[scientific-method]]
  - [[measurement-validity]]
  - [[resource-vs-implementation-bottleneck]]
  - [[caching]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-methodology-cycle-and-monitoring-7-4-4-5]]
