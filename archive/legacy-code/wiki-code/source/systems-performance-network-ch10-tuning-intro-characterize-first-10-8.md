# Systems Performance — Ch.10 §10.8 Tuning intro (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **4496–4508**; file rebuilt 2026-04-20)
- Scope: **tuning as last-mile**, after evidence

## Processed artifacts

- `processed/code/systems-performance-network-ch10-tuning-intro-characterize-first-10-8.md`

## Extracted ideas

- **Tuning without a model** is low leverage: first remove **wrong work / misconfig / wrong path** via [[static-performance-tuning]] + [[resource-analysis-vs-workload-analysis]].
- “Adaptive stack” implies many symptoms are **queueing/resource** stories; sysctl changes alter **queue capacities and scheduling**—still [[queueing-theory]] reasoning, not magic numbers.
- Version drift makes **copy/paste sysctl recipes** a [[measurement-validity]] **scope/semantics** hazard (same name, different behavior across kernels).

## Decision clarity

**Decision:** choose **work elimination + capacity evidence** over **sysctl shopping** when wins are still available from architecture and workload fixes ([[static-performance-tuning]]).

## Application validation

- **Regressions after image upgrade:** re-baseline with characterization before re-applying old tunables—defaults may have changed purposefully ([[measurement-validity]]).

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[resource-analysis-vs-workload-analysis]], [[queueing-theory]], [[measurement-validity]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[resource-analysis-vs-workload-analysis]], [[queueing-theory]], [[measurement-validity]], [[systems-performance]]
