# Systems Performance — Ch.9 §9.8.5 ioping

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p482-560.txt`
- Scope: **§9.8.5**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-experimentation-ioping-9-8-5.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Low-rate synthetic probes** keep **`%util` tiny**—useful when **full saturation benches** would be unsafe; still **active measurement** ([[micro-benchmarking]], [[instrumentation-overhead-and-perturbation]] **perturbation** as **controlled tradeoff**).

## Decision clarity

**Decision:** choose **`ioping`** over **`fio` saturation** when you need **latency proof** on **shared production disks** without **hogging the array**.

## Concepts reused / refined / created

- Reused: [[micro-benchmarking]], [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[micro-benchmarking]], [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[systems-performance]]
