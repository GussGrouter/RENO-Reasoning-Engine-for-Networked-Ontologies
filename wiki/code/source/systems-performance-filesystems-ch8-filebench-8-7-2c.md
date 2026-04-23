# Systems Performance — FileBench programmable workloads (§8.7.2) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.7.2** — **FileBench** capsule (Oracle personality mentioned)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-filebench-8-7-2c.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-filebench-8-7-2c-chunk-000001.md`

## Extracted ideas (with classification)

- **Complexity trade:** WML-defined multi-thread workloads enable **database-shaped** experiments at cost of **tooling tax**—reserve for **deep FS engineering**, not routine checks ([[micro-benchmarking]]).

## Application validation

- Team lacks WML expertise: default to **fio** recipes first; escalate to FileBench only when **thread/sync semantics** must match a packaged personality.

## Decision clarity

- **Decision:** choose **FileBench** over **fio one-liners** when **you must simulate multi-role concurrent FS semantics** (personalities), not just IOPS shapes.

## Concepts reused / refined / created

- Reused: [[micro-benchmarking]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[micro-benchmarking]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-fio-8-7-2b]], [[systems-performance-filesystems-ch8-cache-flushing-8-7-3]]
