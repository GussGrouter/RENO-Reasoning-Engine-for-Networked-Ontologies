# Systems Performance — Ch.10 §10.4.3 Software: TCP connection queues (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1737–1931**; file rebuilt 2026-04-20)
- Scope: backlog staging as overload and attack-surface behavior

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-software-tcp-connection-queues-syn-vs-listen-10-4-3b.md`

## Extracted ideas

- Connection queues are explicit queueing points; backlog saturation produces connect latency and drop/retransmit amplification ([[queueing-theory]], [[utilization-and-saturation]]).

## Decision clarity

**Decision:** choose **backlog sizing/accept-rate fixes** over “increase client retries” when SYN/listen backlogs saturate and connect latency is dominated by retransmit waits ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[utilization-and-saturation]], [[throughput-latency-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[utilization-and-saturation]], [[throughput-latency-metrics]], [[systems-performance]]

