# Systems Performance — Ch.10 §10.3.11 Local connections (loopback/UDS) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1299–1613**; file rebuilt 2026-04-20)
- Scope: choose IPC transport when components co-reside

## Processed artifacts

- `processed/code/systems-performance-network-ch10-concepts-local-connections-loopback-uds-10-3-11.md`

## Extracted ideas

- When “network latency” is actually intra-host IPC, changing the transport can remove protocol-stack overheads (an implementation bottleneck, not a resource limit) ([[resource-vs-implementation-bottleneck]]).

## Application validation

If a service mesh sidecar and app share a host and localhost traffic is hot, consider UDS for high-frequency control paths before tuning TCP.

## Decision clarity

**Decision:** choose **UDS** over **localhost TCP/IP** when endpoints are on the same host and profiling suggests TCP/IP stack overhead is a material fraction of request time ([[resource-vs-implementation-bottleneck]]).

## Concepts reused / refined / created

- Reused: [[resource-vs-implementation-bottleneck]], [[throughput-latency-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[resource-vs-implementation-bottleneck]], [[throughput-latency-metrics]], [[systems-performance]]

