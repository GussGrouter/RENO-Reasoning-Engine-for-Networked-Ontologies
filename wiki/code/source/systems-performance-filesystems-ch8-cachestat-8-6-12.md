# Systems Performance — cachestat (§8.6.12) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.12** — page-cache **hits/misses/dirties** via **experimental kprobe** script

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-cachestat-8-6-12.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-cachestat-8-6-12-chunk-000001.md`

## Extracted ideas (with classification)

- **Feedback loop:** hit ratio while tuning **app footprint vs cache** / **swappiness** ([[caching]], [[throughput-latency-metrics]]).
- **Brittleness:** implementation ties to **specific kernel internals**—may need rework across versions; stable counters/tracepoints would be preferable ([[measurement-validity]] applies as **representation risk**: same script name may not mean the same measured kernel functions after an upgrade).

## Application validation

- After **kernel bump**, if `cachestat` prints nothing or nonsense, treat as **instrumentation mismatch**, not “cache infinite.”

## Decision clarity

- **Decision:** choose **upstream `/proc` / tracepoint-backed stats** over **shipping Gregg’s kprobe script verbatim** when **you require multi-year reproducible dashboards**.

## Concepts reused / refined / created

- Reused: [[caching]], [[measurement-validity]], [[instrumentation-overhead-and-perturbation]], [[extended-bpf]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[caching]], [[measurement-validity]], [[instrumentation-overhead-and-perturbation]], [[extended-bpf]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-table-8-5-expectations]], [[systems-performance-filesystems-ch8-mount-free-8-6-1-2]]
