# Systems Performance — Ch.10 §10.8.2 MSG_ZEROCOPY — performance hint with correctness constraints (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **4476–4487**; file rebuilt 2026-04-20)
- Scope: syscall-flag tuning that changes lifecycle semantics

## Processed artifacts

- `processed/code/systems-performance-network-ch10-tuning-msg-zerocopy-send-flag-10-8-2b.md`

## Extracted ideas

- Some “performance flags” are really **semantic shifts**: `MSG_ZEROCOPY` trades CPU/memory-copy cost for a **buffer-lifetime protocol** between app and kernel. This is not a knob you can safely toggle without reasoning about concurrency and ownership ([[measurement-validity]] **scope/semantics**; [[cross-component-interactions]]).

## Decision clarity

**Decision:** choose **`MSG_ZEROCOPY`** over **regular `send(2)`** when copy CPU is a measured bottleneck *and* you can implement the required **completion notification** to preserve buffer correctness; otherwise treat it as too risky for production changes ([[resource-vs-implementation-bottleneck]]).

## Application validation

- If you see throughput limited by CPU in memcpy paths under high outbound bandwidth, prototype `MSG_ZEROCOPY` behind a feature flag and validate correctness by asserting buffers aren’t reused before completion events fire ([[static-performance-tuning]]).

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[cross-component-interactions]], [[resource-vs-implementation-bottleneck]], [[static-performance-tuning]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[cross-component-interactions]], [[resource-vs-implementation-bottleneck]], [[static-performance-tuning]], [[systems-performance]]
