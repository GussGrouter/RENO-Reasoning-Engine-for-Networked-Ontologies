# Systems Performance — Ch.10 §10.4.3 Software: pacing/TSQ/BQL/EDT (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1737–1931**; file rebuilt 2026-04-20)
- Scope: control queue growth and burstiness across layers

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-software-other-optimizations-pacing-tsq-bql-edt-10-4-3j.md`

## Extracted ideas

- Many optimizations are “queue-control” mechanisms: reduce burstiness, limit queued work, and cap driver queue depth to prevent latency inflation under load ([[queueing-theory]], [[latency-outliers]]).

## Application validation

If p99 spikes during incast-like bursts, prioritize pacing/queue-limiting strategies before increasing buffers.

## Decision clarity

**Decision:** choose **reduce burstiness / limit queue depth** over “increase buffers” when tail latency under load indicates queue growth and micro-bursts (delay propagation) ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[latency-outliers]], [[static-performance-tuning]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[latency-outliers]], [[static-performance-tuning]], [[systems-performance]]

