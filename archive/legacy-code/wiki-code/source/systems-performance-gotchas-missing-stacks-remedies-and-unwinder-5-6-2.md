# Systems Performance — gotchas: missing stacks (remedies and unwinder gap) (5.6.2 partial) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.6.2 Missing Stacks (frame-pointer build/runtime remedies; alternative unwinders; BPF capability caveat)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-gotchas-missing-stacks-remedies-and-unwinder-5-6-2.md`
- Chunks:
  - `processed/code/systems-performance-gotchas-missing-stacks-remedies-and-unwinder-5-6-2-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Re-enabling frame pointers** (C/C++ `-fno-omit-frame-pointer`, JVM `PreserveFramePointer`) is usually a **small steady-state cost** traded for trustworthy stacks—defaults should be decided like any other observability tax ([[static-performance-tuning]], [[instrumentation-overhead-and-perturbation]]).
- (abstraction) **`perf`-class tools can use non-FP unwind** (DWARF/ORC/LBR) but **BPF stack capture historically lagged** those modes—capability mismatch drives “why perf looks fine but BPF tools don’t” disputes ([[observability-vs-experimentation]], [[extended-bpf]], [[sampling-based-profiling]]).

## Application validation

- **BPF-only fleet policy**: if on-host triage relies on BPF stack maps but profiles look empty while `perf` DWARF stacks look rich, the decision is often “change capture agent,” not “the service has no user stack.”

## Concepts reused / refined / created

- Reused (heuristic): [[static-performance-tuning]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (mechanism): [[extended-bpf]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[static-performance-tuning]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[observability-vs-experimentation]]
  - [[extended-bpf]]
  - [[sampling-based-profiling]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-gotchas-missing-stacks-causes-5-6-2]]
  - [[systems-performance-chapter-5-exercises-terminology-scaffold-5-7]]
