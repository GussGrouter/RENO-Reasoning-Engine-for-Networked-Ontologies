# Systems Performance — Ch.10 §10.6.5 netstat (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2751–2910**; file rebuilt 2026-04-20)
- Scope: “multi-tool” stats surfaces + interpreting drops/retransmits as saturation/queue stories

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-netstat-multi-socket-interface-stack-stats-10-6-5.md`

## Extracted ideas

- **Drops/overruns** on interfaces imply **queues filled faster than drained**—expect **tail latency growth** and often **TCP retransmits** as downstream consequences ([[queueing-theory]]).
- **SYN retransmits** point at **handshake-stage loss/backlog pressure** (accept path / listener queue / middlebox)—still queueing-story vocabulary, not a moral final root cause ([[queueing-theory]]).
- **Receive-queue pruning / socket buffer overrun counters** tie application socket memory + kernel buffering to **packet drops**: fixing often means **more consume-side throughput** or buffer tuning—still grounded in [[resource-vs-implementation-bottleneck]] framing.
- **Monitoring plumbing**: unstable counter names/output typos argue for reading canonical sources (`/proc/net/snmp`)—invoke [[measurement-validity]] **scope/semantics** when dashboards parse fragile text.

## Decision clarity

**Decision:** choose **direct `/proc/net/snmp` ingestion** over **fragile `netstat -s` parsing** when you must build durable metrics that survive formatting quirks ([[measurement-validity]]).

## Application validation

- **Incidents:** if `RX-DRP/OVR` grows while CPU is fine, prioritize **NIC/driver queue + interrupt budget** hypotheses before blaming app code—drops inflate **retransmit-driven tail latency** ([[use-method]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[use-method]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[counters-statistics-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[use-method]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[counters-statistics-metrics]], [[systems-performance]]
