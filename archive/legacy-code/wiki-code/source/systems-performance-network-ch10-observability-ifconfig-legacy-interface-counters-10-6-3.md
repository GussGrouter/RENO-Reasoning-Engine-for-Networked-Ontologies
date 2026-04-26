# Systems Performance — Ch.10 §10.6.3 ifconfig (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2660–2693**; file rebuilt 2026-04-20)
- Scope: legacy interface counters + “obsolete but everywhere” operational tradeoff

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-ifconfig-legacy-interface-counters-10-6-3.md`

## Extracted ideas

- The decision is not “which CLI is morally best,” but **whether your stats path is stale/mismatched** for the kernel you run—when in doubt, prefer **iproute2**-family tools for feature parity ([[streetlight-anti-method]] as a coverage risk, not a vendor choice).
- **`txqueuelen` semantics are not portable truths**: drivers may ignore; byte queue limits change queue dynamics—avoid turning a printed field into a tuning religion ([[measurement-validity]] **scope/semantics**: field meaning vs actual device queue behavior).

## Decision clarity

**Decision:** choose **`ip`** over **`ifconfig`** on Linux when you need **consistent modern behavior** and fewer footguns correlating counters across kernel versions ([[static-performance-tuning]]).

## Concepts reused / refined / created

- Reused: [[streetlight-anti-method]], [[static-performance-tuning]], [[measurement-validity]], [[counters-statistics-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[streetlight-anti-method]], [[static-performance-tuning]], [[measurement-validity]], [[counters-statistics-metrics]], [[systems-performance]]
