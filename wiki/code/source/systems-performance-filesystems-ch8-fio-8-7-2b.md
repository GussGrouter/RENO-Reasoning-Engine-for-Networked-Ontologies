# Systems Performance — fio: distributions + percentile tails (§8.7.2) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.7.2** — **fio** features + worked random-read example (full output trimmed)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-fio-8-7-2b.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-fio-8-7-2b-chunk-000001.md`

## Extracted ideas (with classification)

- **Workload realism:** non-uniform random distributions approximate **skewed production access** better than uniform draws ([[micro-benchmarking]]).
- **Representation note (measurement-validity):** printed **percentiles** highlight the **slow-mode tail** but still **collapse** multimodal structure—pair with histograms/heat maps when stakes are high ([[latency-percentiles]], [[multimodal-latency-distribution]]).

## Application validation

- **p50 µs vs p99.99 ms:** treat as evidence of **two populations** (cache vs disk path), not “one noisy FS.”

## Decision clarity

- **Decision:** choose **fio + percentile tail targets** over **Bonnie headline MB/s** when **SLO language is tail latency under skewed IO**.

## Concepts reused / refined / created

- Reused: [[micro-benchmarking]], [[latency-percentiles]], [[multimodal-latency-distribution]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[micro-benchmarking]], [[latency-percentiles]], [[multimodal-latency-distribution]], [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-visualizations-8-6-18]], [[systems-performance-filesystems-ch8-filebench-8-7-2c]]
