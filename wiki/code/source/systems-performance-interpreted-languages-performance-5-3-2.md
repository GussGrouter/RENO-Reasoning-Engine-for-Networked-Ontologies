# Systems Performance — interpreted languages: observability gaps (5.3.2) (PDF ~182–230)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.3.2 Interpreted Languages

## Processed artifacts

- Converted slice: `processed/code/systems-performance-interpreted-languages-performance-5-3-2.md`
- Chunks:
  - `processed/code/systems-performance-interpreted-languages-performance-5-3-2-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Profiles often collapse to **interpreter internals**—user semantics disappear from stacks unless tooling projects them back—same class of **representation loss** as metrics that only expose proxy-level signals.
- (diagnosis) **Dynamic instrumentation** or controlled memory inspection can recover context when static maps are absent—cost/risk tradeoff vs printf timing ([[instrumentation-overhead-and-perturbation]]).

## Application validation

- **Shell-heavy automation**: before blaming “slow bash,” confirm whether spend is in fork/exec, builtin parsing, or external tools—CPU profiles of the interpreter frame often redirect the fix away from “rewrite in Go.”

## Concepts reused / refined / created

- Reused (measurement): [[sampling-based-profiling]]
- Reused (measurement): [[event-tracing]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[sampling-based-profiling]]
  - [[event-tracing]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[known-unknowns-framework]]
  - [[systems-performance]]
