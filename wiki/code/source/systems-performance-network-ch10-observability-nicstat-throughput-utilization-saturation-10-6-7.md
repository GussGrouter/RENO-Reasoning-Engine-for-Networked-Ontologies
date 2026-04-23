# Systems Performance — Ch.10 §10.6.7 nicstat (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3076–3121**; file rebuilt 2026-04-20)
- Scope: NIC-level utilization framing for USE + tail implications when links approach ceilings

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-nicstat-throughput-utilization-saturation-10-6-7.md`

## Extracted ideas

- **Utilization near the NIC** increases **queueing delay** on that hop: even before “errors,” you can get **latency inflation** and **retransmits** as consequences when buffers and scheduling interact with bursts ([[queueing-theory]]).
- `%Util` is a **compact headroom signal**, but it’s still a **metric representation** of busy-ness—pair with drops/retransmits and application SLAs before declaring “network is full” ([[measurement-validity]] **representation**, conditional).
- **Sat column** + throughput columns help separate **mostly idle NIC** vs **actually busy** interfaces on dense servers—reduces blind spots ([[streetlight-anti-method]]).

## Decision clarity

**Decision:** choose **`nicstat` interval rows** over one-shot cumulative counters when you must answer **“is this NIC actually busy?”** quickly during an outage ([[use-method]]).

## Application validation

- **Noisy neighbors on host:** one interface pegged (`%Util` climbing) while others idle suggests **local egress/inbound saturation**—next step is correlating **drops + qdisc/driver queues**, not rewriting app threads first ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[use-method]], [[measurement-validity]], [[streetlight-anti-method]], [[throughput-latency-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[use-method]], [[measurement-validity]], [[streetlight-anti-method]], [[throughput-latency-metrics]], [[systems-performance]]
