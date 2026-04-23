# Systems Performance — Ch.8 §8.8 Tuning (intro) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.8** intro — tunables vs **§8.5** methodology; ext4/ZFS examples; page cache in Ch.7

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-tuning-intro-8-8.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-tuning-intro-8-8-chunk-000001.md`

## Extracted ideas (with classification)

- **Method vs knob:** highest wins still come from **workload characterization** and **removing unnecessary work**; this section is **concrete parameters** on top of that story ([[static-performance-tuning]], [[cache-tuning]]).
- **Context dependency:** valid options and values depend on **OS, fs type, workload**—treat the book as **examples**, not a single global map.

## Application validation

- Before changing ZFS `recordsize` or ext4 mount flags, confirm you have a **workload model** (I/O size, sync pattern, cache tier) from §8.5-style analysis so the knob matches the actual hot path.

## Decision clarity

- **Decision:** choose **methodology-first (§8.5) evidence** over **tuning shopping** when **the bulk of time is still unaccounted work** or **wrong software I/O pattern**, not a mis-set `recordsize` or `noatime`.

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[cache-tuning]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[cache-tuning]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-methodology-intro-8-5]], [[systems-performance-filesystems-ch8-static-tuning-fs-8-5-5]], [[systems-performance-filesystems-ch8-zfs-tuning-properties-8-8-3]]
