# Systems Performance — CPU hardware map: processor subsystems and dynamic headroom (6.4.1 intro) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.4.1 **Hardware** opening through optional on-chip components and **thermal-aware turbo** framing (stops before the duplicated “P-States and C-States” header in this extract)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-hardware-processor-subsystems-intro-6-4-1.md`
- Chunks:
  - `processed/code/systems-performance-cpu-hardware-processor-subsystems-intro-6-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Processor as a bundle of cooperating subsystems** (fetch/decode, shared FP, optional shared LLC, clocks, sensors)—**variance across SKUs** is a first-class performance risk: “CPU-bound” depends on **which unit is actually the limiter** ([[caching]], [[throughput-latency-metrics]]).
- (mechanism) **Dynamic frequency headroom** can be **thermally gated**—observed throughput may be **below nominal turbo** without traditional “saturation” stories, because **power/temperature envelopes** move the clock surface ([[throughput-latency-metrics]], [[cross-component-interactions]]).

## Application validation

- **Batch HPC on laptops**: sustained GFLOPS drops after minutes → suspect **thermal P-state envelope**, not algorithmic complexity alone.

## Decision clarity

- **Decision**: choose **cooling / power-cap envelope validation** over **core-count scaling** when short bursts match spec but **sustained throughput** collapses under thermal governance.

## Concepts reused / refined / created

- Reused (mechanism): [[caching]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[cross-component-interactions]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[caching]]
  - [[throughput-latency-metrics]]
  - [[cross-component-interactions]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-compiler-optimization-pointer-6-3-15]]
  - [[systems-performance-cpu-p-states-and-c-states-6-4-1]]
  - [[systems-performance-cpu-models-architecture-and-caches-6-2-1-2]]
