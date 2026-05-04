# Systems Performance — Ch.10 §10.4.3 Software: TCP buffering (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1737–1931**; file rebuilt 2026-04-20)
- Scope: buffer sizing as a throughput/memory trade

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-software-tcp-buffering-10-4-3c.md`

## Extracted ideas

- Socket buffer sizes are a knob trading throughput against memory footprint per connection; apply as tuning after characterizing RTT/throughput regime ([[static-performance-tuning]], [[time-space-tradeoff]]).

## Decision clarity

**Decision:** choose **increase socket buffers** over “optimize application CPU” when throughput is limited by windowing/RTT effects and the system is not saturated elsewhere ([[static-performance-tuning]]).

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[time-space-tradeoff]], [[throughput-latency-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[time-space-tradeoff]], [[throughput-latency-metrics]], [[systems-performance]]

