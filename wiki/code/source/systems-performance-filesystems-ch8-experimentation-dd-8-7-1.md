# Systems Performance — Experimentation intro + dd ad hoc (§8.7–§8.7.1) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.7 Experimentation** + **§8.7.1 Ad Hoc** (`dd`)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-experimentation-dd-8-7-1.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-experimentation-dd-8-7-1-chunk-000001.md`

## Extracted ideas (with classification)

- **Cross-check:** keep **`iostat` (Ch.9) running** to verify whether the supposed disk workload is **actually hitting disks**—cache-heavy WSS can show **hero GB/s** with **no device traffic** ([[micro-benchmarking]], [[observability-vs-experimentation]]).
- **`dd` writes:** printed throughput may reflect **dirty page cache + vm.dirty_** policy, not sustained device completion in the same second.

## Application validation

- **“1.4 GB/s write” from `dd`:** confirm with **disk metrics** whether you measured **RAM fill rate** or **stable write-to-platter** behavior.

## Decision clarity

- **Decision:** choose **paired `dd` + block-device observability** over **`dd` numbers alone** when **policy must be about durable write rate**, not dirty cache acceptance.

## Concepts reused / refined / created

- Reused: [[micro-benchmarking]], [[observability-vs-experimentation]], [[throughput-latency-metrics]], [[caching]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[micro-benchmarking]], [[observability-vs-experimentation]], [[throughput-latency-metrics]], [[caching]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-table-8-5-expectations]], [[systems-performance-filesystems-ch8-cache-flushing-8-7-3]]
