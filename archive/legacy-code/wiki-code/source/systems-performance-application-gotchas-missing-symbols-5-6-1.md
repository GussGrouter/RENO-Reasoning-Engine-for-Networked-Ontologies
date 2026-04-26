# Systems Performance — gotchas: missing symbols (5.6 intro + 5.6.1) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.6 Gotchas (framing) and 5.6.1 Missing Symbols (ELF strip vs debuginfo; JIT supplemental maps; symbol churn vs timestamped maps)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-application-gotchas-missing-symbols-5-6-1.md`
- Chunks:
  - `processed/code/systems-performance-application-gotchas-missing-symbols-5-6-1-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **`[unknown]` is a validity defect, not a cosmetic UI issue**: without symbols, stacks mis-rank work and mis-route fixes—resolve build/packaging and supplemental maps before debating algorithms ([[measurement-validity]], [[sampling-based-profiling]], [[known-unknowns-framework]]).
- (measurement) **JIT symbol tables move independently of on-disk ELF**; snapshot maps close to capture windows, or use timestamped symbol logging when churn would otherwise lie about hot frames ([[instrumentation-overhead-and-perturbation]]).
- (abstraction) **Multiple symbol sources** (ELF, debuginfo/BTF, `/tmp/perf-*.map`, runtime helpers) are an explicit **precondition checklist** for interpretable profiles ([[observability-vs-experimentation]]).

## Application validation

- **Java CPU mystery**: if stacks show only `[unknown]` above libc, ship `PreserveFramePointer` or a perf-map workflow *before* rewriting GC tuning—otherwise you optimize ghosts.

## Decision clarity

- **Decision**: choose **JIT supplemental map capture immediately adjacent to profiling** over **reusing stale map files** when symbol churn could mislabel hot frames.

## Concepts reused / refined / created

- Reused (abstraction): [[measurement-validity]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[measurement-validity]]
  - [[sampling-based-profiling]]
  - [[known-unknowns-framework]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[observability-vs-experimentation]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-bpftrace-custom-aggregation-probe-ladder-5-5-7]]
  - [[systems-performance-gotchas-missing-stacks-causes-5-6-2]]
  - [[systems-performance-compiled-languages-performance-5-3-1]]
