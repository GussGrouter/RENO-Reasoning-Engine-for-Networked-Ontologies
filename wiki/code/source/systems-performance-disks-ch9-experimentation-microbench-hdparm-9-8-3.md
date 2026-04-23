# Systems Performance — Ch.9 §9.8.3 Micro-benchmark tools (hdparm example)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p482-560.txt`
- Scope: **§9.8.3**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-experimentation-microbench-hdparm-9-8-3.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **`hdparm -T` vs `-t`** is a built-in **A/B** between **memory/cache path** and **on-media reads**—misreading the labels optimizes the wrong layer ([[measurement-validity]] **representation**, [[micro-benchmarking]]).

## Application hook

When marketing claims **“GB/s”** from **`hdparm -T`**: **demote** that number in architecture decisions—it is often **not device-limited**.

## Concepts reused / refined / created

- Reused: [[micro-benchmarking]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[micro-benchmarking]], [[measurement-validity]], [[systems-performance]]
