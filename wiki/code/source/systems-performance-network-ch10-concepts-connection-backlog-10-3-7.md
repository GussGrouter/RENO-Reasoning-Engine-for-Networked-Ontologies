# Systems Performance — Ch.10 §10.3.7 Connection backlog (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1229–1241**; file rebuilt 2026-04-20)
- Scope: backlog as a queueing signal of endpoint overload

## Processed artifacts

- `processed/code/systems-performance-network-ch10-concepts-connection-backlog-10-3-7.md`

## Extracted ideas

- Backlog is a **queue**; SYN drops + retransmits create **latency via queue overflow**, and they implicate endpoint overload rather than path RTT changes ([[queueing-theory]], [[utilization-and-saturation]]).

## Application validation

If connect time jumps by seconds under bursty traffic, check for **SYN retransmits/backlog drops** before blaming DNS or WAN RTT.

## Decision clarity

**Decision:** choose **endpoint overload investigation** over “network RTT investigation” when connect latency increases and SYN retransmits/backlog drops are present ([[utilization-and-saturation]], [[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[utilization-and-saturation]], [[queueing-theory]], [[throughput-latency-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[utilization-and-saturation]], [[queueing-theory]], [[throughput-latency-metrics]], [[systems-performance]]

