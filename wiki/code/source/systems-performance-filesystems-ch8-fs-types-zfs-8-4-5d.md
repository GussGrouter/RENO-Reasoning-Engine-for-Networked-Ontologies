# Systems Performance — ZFS framing + integrity vs latency (§8.4.5) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.4.5** — **ZFS** (**large feature bullet catalog omitted**); retains **license/integration context** + **two decision hazards**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-fs-types-zfs-8-4-5d.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-fs-types-zfs-8-4-5d-chunk-000001.md`

## Extracted ideas (with classification)

- (integration / scope) **License + packaging** constrains where ZFS ships and how aggressively the kernel integrates it—an environment constraint on *using* the stack, separate from micro-benchmark winners.
- (semantics vs measurement) **Default cache flushes** buy **power-loss integrity** at the cost of **operation latency**—the number is “valid” but the *meaning* shifts with your failure model.
- (representation hazard) **Deduplication** can invert performance when the **hash table footprint** escapes RAM—throughput/latency change is not a smooth function of “dedup on.”

## Application validation

- **P99 FS stalls after enabling dedup:** validate **RAM headroom for dedup metadata** and device amplification before blaming disks—same symptom as “slow disks,” different intervention.

## Decision clarity

- **Decision:** choose **relaxed flush / alternative sync paths** (where integrity policy allows) over **disk upgrades** when **ZFS-side latency tracks flush epochs** and power-loss guarantees are over-provisioned for the actual deployment class.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none (integrity/latency coupling absorbed by existing measurement + resource-framing concepts)

## Links

- Concepts: [[measurement-validity]], [[throughput-latency-metrics]], [[instrumentation-overhead-and-perturbation]], [[cross-component-interactions]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-fs-types-btrfs-8-4-5e]], [[systems-performance-filesystems-ch8-caches-page-flush-8-4-3a]]
