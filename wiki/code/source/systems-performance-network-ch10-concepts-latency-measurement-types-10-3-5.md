# Systems Performance — Ch.10 §10.3.5 Latency (definitions/measurements) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1109–1183**; file rebuilt 2026-04-20)
- Scope: choose the right latency definition for the claim

## Processed artifacts

- `processed/code/systems-performance-network-ch10-concepts-latency-measurement-types-10-3-5.md`

## Extracted ideas

- Latency terms are **layered**: some isolate network path, others include endpoint scheduling/overload; select the measure that matches the hypothesis ([[throughput-latency-metrics]], [[latency-analysis]]).

## Application validation

If ping is flat but TTFB spikes, investigate **server-side scheduling/overload** rather than the network path.

## Decision clarity

**Decision:** choose **TTFB** over **ping RTT** when the user symptom is “slow first response” and you need to include server think time in the measurement ([[throughput-latency-metrics]]).

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[latency-analysis]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[latency-analysis]], [[systems-performance]]

