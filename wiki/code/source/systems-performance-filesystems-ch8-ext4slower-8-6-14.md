# Systems Performance — ext4slower / *slower tail capture (§8.6.14) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.14** — thresholded **slow op** lines + optional **full firehose** (`0 ms`)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-ext4slower-8-6-14.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-ext4slower-8-6-14-chunk-000001.md`

## Extracted ideas (with classification)

- **Tail hunting:** complements histograms—prints **which files/syncs** breached **SLO-scale** latency.
- **Writes vs sync separation:** bursts of fast writes followed by slower **sync** ops mirror **buffered vs durability** behavior ([[latency-analysis]]).
- **Cost discipline:** threshold `0` explodes volume—short windows only ([[instrumentation-overhead-and-perturbation]]).

## Application validation

- **Redo log stalls:** scan **sync rows** over **write rows** first—the sync path often binds durability stories.

## Decision clarity

- **Decision:** choose **threshold > 0 for steady capture** over **`ext4slower 0` indefinitely** when **you need survivable overhead** on busy databases.

## Concepts reused / refined / created

- Reused: [[latency-analysis]], [[instrumentation-overhead-and-perturbation]], [[latency-outliers]], [[extended-bpf]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[latency-analysis]], [[instrumentation-overhead-and-perturbation]], [[latency-outliers]], [[extended-bpf]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-ext4dist-histograms-8-6-13]], [[systems-performance-filesystems-ch8-bpftrace-oneliners-8-6-15a]]
