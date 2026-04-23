# Systems Performance — Bonnie family + “what are you testing?” (§8.7.2 open) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.7.2** opening + **Bonnie** — **fio** recommended; Bonnie output trimmed

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-bonnie-8-7-2a.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-bonnie-8-7-2a-chunk-000001.md`

## Extracted ideas (with classification)

- **Wrong target:** **`putc` path** can benchmark **libc**, not the file system—scope slip between layers ([[resource-vs-implementation-bottleneck]]).
- **Cache saturation:** **100% CPU** during tests often means **never blocked on disk**—classic sign the default file size is **RAM-resident** ([[micro-benchmarking]]).

## Application validation

- Bonnie shows **CPU-bound** micro-ops at default size: grow **`-s`** until you see **wait** / device signals if the goal is **backing-store** behavior.

## Decision clarity

- **Decision:** choose **explicit file size + Active Benchmarking discipline** over **tool defaults** when **the decision depends on disk**, not libc micro-performance.

## Concepts reused / refined / created

- Reused: [[micro-benchmarking]], [[resource-vs-implementation-bottleneck]], [[scientific-method]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[micro-benchmarking]], [[resource-vs-implementation-bottleneck]], [[scientific-method]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-fio-8-7-2b]], [[systems-performance-filesystems-ch8-experimentation-dd-8-7-1]]
