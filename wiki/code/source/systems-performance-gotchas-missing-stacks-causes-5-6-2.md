# Systems Performance — gotchas: missing stacks (causes) (5.6.2 partial) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.6.2 Missing Stacks (symptom, “grass,” dual-factor root cause through libc paths)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-gotchas-missing-stacks-causes-5-6-2.md`
- Chunks:
  - `processed/code/systems-performance-gotchas-missing-stacks-causes-5-6-2-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Truncated stacks hide application context** just above libc/pthread boundaries—the failure mode looks like “kernel wait” when the missing frames are the product logic ([[drill-down-analysis]], [[sampling-based-profiling]]).
- (measurement) **Frame-pointer walking** plus **`-fomit-frame-pointer` style builds** yields `[unknown]` or, worse, **accidental resolvability** to unrelated symbols—treat bogus names as falsified evidence, not nuance ([[instrumentation-overhead-and-perturbation]], [[known-unknowns-framework]]).
- (diagnosis) **Many single-frame bottoms** (“grass”) are a **signature** of systematic unwind breakage through common runtime paths, not independent micro-optimizations ([[sampling-based-profiling]]).

## Application validation

- **MySQL off-CPU**: if every deep stack stops at `pthread_cond_timedwait` with one junk frame below, fix unwind/Fp policy before blaming InnoDB condition timing.

## Decision clarity

- **Decision**: choose **validating stack unwind prerequisites (frame pointers / libc build)** over **micro-optimizing the leaf syscall or mutex** when stacks are systematically shallow or contradictory.

## Concepts reused / refined / created

- Reused (heuristic): [[drill-down-analysis]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[drill-down-analysis]]
  - [[sampling-based-profiling]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[known-unknowns-framework]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-application-gotchas-missing-symbols-5-6-1]]
  - [[systems-performance-gotchas-missing-stacks-remedies-and-unwinder-5-6-2]]
