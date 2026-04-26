# Systems Performance — Page cache + flush threads (§8.4.3 opening) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.4.3** (part A) — **unified buffer cache**, **page cache**, **dirty flush reasons**, **kswapd** interaction with FS dirty data

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-caches-page-flush-8-4-3a.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-caches-page-flush-8-4-3a-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Double caching problems** historically motivated **unified page cache** with buffer cache folded in ([[caching]], [[resource-vs-implementation-bottleneck]]).
- (cross-layer) **Memory pressure ↔ dirty writeback**: **kswapd** and **flush** threads show why **RAM and disk charts couple** ([[cross-component-interactions]], [[measurement-validity]]).

## Application validation

- **Flush threads hot during memory squeeze:** treat as **memory + FS joint incident**—raising **disk QoS alone** misses **reclaim forcing writeback**.

## Decision clarity

- **Decision:** choose **joint memory-pressure + dirty-page telemetry** over **disk-only scaling** when **stalls correlate with kswapd/flush activity**, not sustained **random read bandwidth limits**.

## Concepts reused / refined / created

- Reused: [[caching]], [[cross-component-interactions]], [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[caching]], [[cross-component-interactions]], [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-caches-dentry-inode-8-4-3b]]
