# Systems Performance — BCC `profile`: kernel-side aggregation (5.5.2) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.5.2 `profile` (timer-based sampling with stacks aggregated before user space)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-bcc-profile-kernel-side-aggregation-5-5-2.md`
- Chunks:
  - `processed/code/systems-performance-bcc-profile-kernel-side-aggregation-5-5-2-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Aggregate in kernel, emit unique stacks**: shifts work from per-sample user/kernel handoffs to bounded summaries—overhead scales more with *distinct* paths than raw event volume ([[extended-bpf]], [[instrumentation-overhead-and-perturbation]]).
- (measurement) Same **Hz-based sampling** mental model as classical profilers; what changes is *where aggregation happens*, not the statistical meaning of the picture ([[sampling-based-profiling]]).

## Application validation

- **Wide fan-out microservice**: if `perf record` files explode on disk, compare against a BPF-aggregating profiler when policy allows—judge by unique-stack cardinality, not only sample count.

## Concepts reused / refined / created

- Reused (mechanism): [[extended-bpf]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[extended-bpf]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[sampling-based-profiling]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-perf-profiling-syscall-trace-and-io-5-5-1]]
  - [[systems-performance-offcputime-aggregation-and-duration-filters-5-5-3]]
