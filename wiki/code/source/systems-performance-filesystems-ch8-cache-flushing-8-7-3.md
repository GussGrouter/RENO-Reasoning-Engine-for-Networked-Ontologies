# Systems Performance — Linux drop_caches (§8.7.3) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.7.3 Cache Flushing** — **`/proc/sys/vm/drop_caches`**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-cache-flushing-8-7-3.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-cache-flushing-8-7-3-chunk-000001.md`

## Extracted ideas (with classification)

- **Controlled cold start:** drop pagecache and/or reclaimable slabs so successive runs share a **starting cache state**—benchmark comparability lever ([[micro-benchmarking]], [[caching]]).

## Application validation

- **Benchmark variance run-to-run:** standardize **`echo 3`** (or selective drops) **before each trial** when comparing hardware/FS knobs—not production tuning advice without ops review.

## Decision clarity

- **Decision:** choose **explicit cache drops between A/B microbench trials** over **interpretating first-run vs fifth-run throughput** as FS regressions when **warm cache dominates**.

## Concepts reused / refined / created

- Reused: [[micro-benchmarking]], [[caching]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[micro-benchmarking]], [[caching]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-experimentation-dd-8-7-1]], [[systems-performance-filesystems-ch8-cache-separation-microbench-8-5-6-8]]
