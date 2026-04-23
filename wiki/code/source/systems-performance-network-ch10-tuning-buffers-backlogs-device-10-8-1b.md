# Systems Performance — Ch.10 §10.8.1 system-wide tuning — buffers/backlogs (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **4579–4613**; file rebuilt 2026-04-20)
- Scope: **queue depths vs memory trade-offs** for common `sysctl` knobs

## Processed artifacts

- `processed/code/systems-performance-network-ch10-tuning-buffers-backlogs-device-10-8-1b.md`

## Extracted ideas

- **Listen backlog** (`somaxconn`) caps how many completed handshakes can wait before accept; raising it shifts **queueing** from “dropped at kernel” toward “accepted but still delayed in app” ([[queueing-theory]]).
- **Device input backlog** (`netdev_max_backlog`) is a **kernel-side queue** before user delivery; saturation shows up as drops/retransmits downstream when the consumer can’t keep up ([[queueing-theory]]).
- **SYN backlog** is a **half-open queue**; too-small values under SYN floods or bursty connects amplify **tail latency** and failures ([[queueing-theory]]).
- **Socket memory caps** (`rmem_max`/`wmem_max` + `tcp_rmem`/`tcp_wmem`) trade **BDP/latency** vs RAM pressure; oversized buffers can **inflate latency** under loss ([[throughput-latency-metrics]]).

## Decision clarity

**Decision:** choose **raise listen/device backlogs** over **only raising app thread pools** when SYN/accept queues or NIC→socket delivery queues are the measured saturation points ([[queueing-theory]]).

## Application validation

- **SYN flood symptoms:** if `tcp_max_syn_backlog`/`somaxconn` are tiny but CPU is fine, you may be shedding work at the wrong queue—validate with accept-queue metrics and drops before scaling out ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[throughput-latency-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[throughput-latency-metrics]], [[systems-performance]]
