# Systems Performance — Ch.8 §8.9 Exercises (scaffold) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.9** — numbered exercises (**answers not transcribed**)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-exercises-8-9.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-exercises-8-9-chunk-000001.md`

## Extracted ideas (with classification)

- **Skill checklist:** exercises reinforce **distribution-level latency**, **thread time-in-FS**, **WSS vs cache**, and **logical↔physical I/O** reasoning—same primitives as earlier chapters ([[latency-analysis]], [[micro-benchmarking]], [[event-tracing]]).

## Application validation

- **Exercise 5 (micro-benchmark cache size):** force explicit **warmup**, **cache drop policy**, and **observability** (`iostat`, FS stats) so the inferred “cache size” is not **`dd` hero bandwidth** fiction.

## Decision clarity

- **Decision:** choose **distribution + per-thread FS time** over **single mean latency** when **staging an FS regression budget** tied to **tail SLOs**.

## Concepts reused / refined / created

- Reused: [[micro-benchmarking]], [[latency-analysis]], [[scientific-method]], [[drill-down-analysis]], [[model-classify-intervene]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[micro-benchmarking]], [[latency-analysis]], [[scientific-method]], [[drill-down-analysis]], [[model-classify-intervene]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-cache-flushing-8-7-3]], [[systems-performance-filesystems-ch8-fio-8-7-2b]]
