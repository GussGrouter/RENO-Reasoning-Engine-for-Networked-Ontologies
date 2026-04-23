# Systems Performance — Cache tuning, spindle separation, FS micro-benchmarking (§8.5.6–§8.5.8) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.5.6 Cache Tuning** (stub) + **§8.5.7 Workload Separation** + **§8.5.8 Micro-Benchmarking** through **WSS / cold vs warm** narrative (**stops before Table 8.5**)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-cache-separation-microbench-8-5-6-8.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-cache-separation-microbench-8-5-6-8-chunk-000001.md`

## Extracted ideas (with classification)

- (composition) **Dedicated devices / FS for competing streams** (“separate spindles”) reduces **seek interleaving**—especially for rotating media; still a **placement** decision under shared pools.
- (measurement semantics) **Micro-benchmarks** must pin **working set size (WSS)** and **cache temperature**—small files can be **100% DRAM cache**; large sets may be **mostly devices**; **orders of magnitude** gap. **Cold then warm** runs expose **representation error** when a number is reported without WSS context ([[measurement-validity]], [[caching]]).
- (boundary) **Direct I/O** microbench path aims at **disk/device** characterization, not the logical FS (see Ch. 9)—do not confuse the two targets.

## Application validation

- **Marketing “GB/s” from a tiny file:** reject until **total file size vs RAM** and **cache state** are stated—otherwise the headline is **a cache benchmark**, not a disk result.

## Decision clarity

- **Decision:** choose **scaling WSS until results stop changing qualitatively** over **single-size hero numbers** when **deciding disk vs memory bottlenecks** for a planned dataset.

## Concepts reused / refined / created

- Reused: [[cache-tuning]], [[micro-benchmarking]], [[measurement-validity]], [[caching]], [[cross-component-interactions]], [[observability-vs-experimentation]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[cache-tuning]], [[micro-benchmarking]], [[measurement-validity]], [[caching]], [[cross-component-interactions]], [[observability-vs-experimentation]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-static-tuning-fs-8-5-5]], [[systems-performance-filesystems-ch8-table-8-5-expectations]], [[systems-performance-filesystems-ch8-logical-physical-io-8-3-12]]
