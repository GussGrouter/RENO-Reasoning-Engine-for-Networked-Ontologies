# Systems Performance — Ch.10 §10.8.2 socket options — per-socket tuning surface (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **4440–4474**; file rebuilt 2026-04-20)
- Scope: tuning choices that require **application control**

## Processed artifacts

- `processed/code/systems-performance-network-ch10-tuning-socket-options-table-10-8-10-8-2a.md`

## Extracted ideas

- Per-socket tuning is a **scope constraint**: it’s only available when you can change the application, so it’s an intervention with higher organizational cost than sysctl flips ([[static-performance-tuning]]).
- Many options are **throughput↔latency tradeoffs** (Nagle/ACK timing/corking/pacing). Treat them as **queueing/scheduling policy** changes at the endpoint, not generic “speedups” ([[throughput-latency-metrics]], [[queueing-theory]]).
- `SO_REUSEPORT` is a scalability tactic: it changes how **accept load is distributed** across workers; if your bottleneck is serialization in a single acceptor, this can move you toward parallel service ([[resource-vs-implementation-bottleneck]]).

## Decision clarity

**Decision:** choose **per-socket options** over **system-wide sysctl** when the behavior you need is **workload-specific (only some sockets/flows)** and you can safely change the application without affecting unrelated traffic ([[static-performance-tuning]]).

## Application validation

- If p99 latency worsens after disabling Nagle globally, revert and instead set `TCP_NODELAY` only on the latency-critical RPC sockets; keep bulk sockets corked/paced ([[throughput-latency-metrics]]).

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[throughput-latency-metrics]], [[queueing-theory]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[throughput-latency-metrics]], [[queueing-theory]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
