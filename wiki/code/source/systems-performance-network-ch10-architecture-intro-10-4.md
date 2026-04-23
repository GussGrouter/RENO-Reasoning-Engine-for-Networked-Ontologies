# Systems Performance — Ch.10 §10.4 Architecture (intro) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1932–2056**; file rebuilt 2026-04-20)
- Scope: architecture as a scoping map for debugging

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-intro-10-4.md`

## Extracted ideas

- Use architecture summaries to pick the next layer to measure (protocol vs device vs kernel stack) instead of defaulting to one tool or one metric [[drill-down-analysis]].

## Decision clarity

**Decision:** choose **layer scoping** over immediate tuning when you can’t yet localize the performance limit to protocol, hardware, or kernel stack ([[drill-down-analysis]]).

## Concepts reused / refined / created

- Reused: [[drill-down-analysis]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[drill-down-analysis]], [[systems-performance]]

