# Systems Performance — Ch.10 §10.4.3 Software: kernel bypass/XDP/zero-copy (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1737–1931**; file rebuilt 2026-04-20)
- Scope: performance vs observability trade when bypassing the stack

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-software-kernel-bypass-xdp-zerocopy-observability-10-4-3i.md`

## Extracted ideas

- Bypass can improve performance by removing kernel work/copies (implementation bottleneck), but it also changes what observability signals mean/contain (traditional counters/traces may go dark) ([[resource-vs-implementation-bottleneck]], [[observability-vs-experimentation]]).
- Use [[measurement-validity]] **only if evidence conflicts**: if kernel counters show “no problem” but user-space bypass path is saturated, that’s a **scope/semantics** mismatch (you’re measuring a different path).

## Decision clarity

**Decision:** choose **XDP (in-kernel fast path)** over full stack bypass when you need high packet rates but still require kernel-level observability and attribution for debugging ([[resource-vs-implementation-bottleneck]]).

## Concepts reused / refined / created

- Reused: [[resource-vs-implementation-bottleneck]], [[observability-vs-experimentation]], [[measurement-validity]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[resource-vs-implementation-bottleneck]], [[observability-vs-experimentation]], [[measurement-validity]], [[systems-performance]]

