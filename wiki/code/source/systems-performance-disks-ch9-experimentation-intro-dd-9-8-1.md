# Systems Performance — Ch.9 §9.8 Experimentation (intro + §9.8.1 Ad hoc `dd`)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p482-560.txt`
- Scope: **§9.8** opening + **§9.8.1**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-experimentation-intro-dd-9-8-1.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Active tests** sit under **§9.5.9** methodology—pair **`iostat`** with **`dd`** so numbers map to **real device behavior**, not **page cache fiction** ([[observability-vs-experimentation]], [[micro-benchmarking]], [[measurement-validity]]).

## Decision clarity

**Decision:** choose **`oflag=direct` file targets** over **raw `dd` to partitions** when you need **disk-ish signal** without **wiping volume metadata**.

## Concepts reused / refined / created

- Reused: [[observability-vs-experimentation]], [[micro-benchmarking]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[observability-vs-experimentation]], [[micro-benchmarking]], [[measurement-validity]], [[systems-performance]]
