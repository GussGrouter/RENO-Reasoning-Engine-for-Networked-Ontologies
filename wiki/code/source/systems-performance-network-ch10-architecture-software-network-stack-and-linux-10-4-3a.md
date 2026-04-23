# Systems Performance — Ch.10 §10.4.3 Software: network stack + Linux model (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1737–1931**; file rebuilt 2026-04-20)
- Scope: locate likely queueing/cost points in the stack

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-software-network-stack-and-linux-10-4-3a.md`

## Extracted ideas

- The stack is a queueing system with multiple layers; use it as a map for drill-down and for attributing where time/queueing could exist ([[drill-down-analysis]], [[queueing-theory]]).

## Decision clarity

**Decision:** choose **stack-layer drill-down** over “blame the network” when you need to localize whether delay is in driver queues, socket buffers, protocol processing, or reassembly queues ([[drill-down-analysis]]).

## Concepts reused / refined / created

- Reused: [[drill-down-analysis]], [[queueing-theory]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[drill-down-analysis]], [[queueing-theory]], [[systems-performance]]

