# Systems Performance — Ch.10 §10.4.1 Protocols: TCP dupACKs/retransmits/TLP (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2149–2186**; file rebuilt 2026-04-20)
- Scope: loss detection mechanisms as latency drivers

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-protocols-tcp-dupacks-retransmits-tlp-10-4-1d.md`

## Extracted ideas

- Loss recovery is a major latency amplifier; prefer mechanisms that avoid long timer waits when diagnosing tail spikes under loss ([[queueing-theory]], [[latency-outliers]]).

## Application validation

If tail latency clusters at ~RTO multiples, treat it as retransmit/timer behavior before chasing CPU micro-optimizations.

## Decision clarity

**Decision:** choose **retransmit/loss recovery investigation** over “optimize handler time” when tail latency aligns with retransmit timeouts or exponential backoff patterns ([[latency-outliers]], [[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[latency-outliers]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[latency-outliers]], [[systems-performance]]

