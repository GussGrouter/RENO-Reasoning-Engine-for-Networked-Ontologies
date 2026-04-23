# Systems Performance — CPU BIOS / processor options for benchmark validity (6.9.10) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.9.10** — **BIOS-level processor features** (example: **Turbo**) mainly for **repeatable benchmark conditions** vs **production defaults**

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-bios-processor-options-6-9-10.md`
- Chunks:
  - `processed/code/systems-performance-cpu-bios-processor-options-6-9-10-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Disabling Turbo** to stabilize clocks is a **representation choice** for experiments: it narrows variance so differences reflect **software**, not opportunistic frequency—mis-apply it to prod capacity planning and you mis-estimate **burst throughput** ([[micro-benchmarking]], [[measurement-validity]]).
- (abstraction) **Static configuration** (BIOS/firmware) belongs in the **pre-flight checklist** alongside kernel flags: it defines what “100% CPU” even means across runs ([[static-performance-tuning]], [[throughput-latency-metrics]]).

## Application validation

- **Regression suite comparing two compiler flags**: lock **Turbo policy + governor + thermal headroom** first; otherwise you may be measuring **thermal opportunism**, not codegen.

## Decision clarity

- **Decision**: choose **fixed-frequency / fixed-boost policy** over **default Turbo-on** when the goal is **isolate software deltas**; choose **production-like power behavior** when the goal is **capacity or tail latency under real bursts**.

## Concepts reused / refined / created

- Reused (heuristic): [[micro-benchmarking]]
- Reused (abstraction): [[measurement-validity]]
- Reused (heuristic): [[static-performance-tuning]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[micro-benchmarking]]
  - [[measurement-validity]]
  - [[static-performance-tuning]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-micro-benchmarking-decision-rules-6-5-11]]
  - [[systems-performance-cpu-security-mitigations-boot-6-9-9]]
