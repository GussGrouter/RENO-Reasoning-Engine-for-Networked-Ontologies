# Systems Performance — Ch.10 §10.7.5 netperf (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt`
- Scope: **RR latency** as an experimental complement to bulk `iperf`

## Processed artifacts

- `processed/code/systems-performance-network-ch10-experimentation-netperf-tcp-rr-latency-10-7-5.md`

## Extracted ideas

- **RR micro-benchmarks** stress **synchronous queueing** (small messages, frequent turns)—often inflates sensitivity to **RTT tails** vs bulk flows ([[throughput-latency-metrics]], [[queueing-theory]]).
- Results are **workload-shaped**: a ping-like RR path is not equivalent to large streaming TCP—apply [[measurement-validity]] **representation** when extrapolating to app SLOs.
- Still fits [[micro-benchmarking]]: isolate “**baseline interactive network RTT**” between two hosts when counters are ambiguous ([[observability-vs-experimentation]]).

## Decision clarity

**Decision:** choose **`netperf TCP_RR`** over **`iperf`** when the production symptom is **small-message latency / transaction stalls**, not bulk Gbps ceilings ([[micro-benchmarking]]).

## Application validation

- **DB-ish chatter:** if RR latency is bad but `iperf` is fine, suspect **queueing + scheduling + syscall overhead** on small transactions—not “bandwidth purchase” ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[micro-benchmarking]], [[throughput-latency-metrics]], [[queueing-theory]], [[measurement-validity]], [[observability-vs-experimentation]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[micro-benchmarking]], [[throughput-latency-metrics]], [[queueing-theory]], [[measurement-validity]], [[observability-vs-experimentation]], [[systems-performance]]
