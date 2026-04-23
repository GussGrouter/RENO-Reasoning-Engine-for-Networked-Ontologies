# Systems Performance — Ch.10 §10.4.3 Software: qdisc defaults + bufferbloat trade (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1737–1931**; file rebuilt 2026-04-20)
- Scope: queue management defaults as a latency/complexity trade

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-software-queueing-disciplines-defaults-bpf-10-4-3e.md`

## Extracted ideas

- Default queue management can trade **tail latency** against complexity; fq_codel is chosen to reduce bufferbloat-like queue growth ([[queueing-theory]], [[latency-outliers]]).

## Decision clarity

**Decision:** choose **aqm/fair-queue defaults** over FIFO when tail latency under load indicates queue growth and you control host queueing policy ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[latency-outliers]], [[static-performance-tuning]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[latency-outliers]], [[static-performance-tuning]], [[systems-performance]]

