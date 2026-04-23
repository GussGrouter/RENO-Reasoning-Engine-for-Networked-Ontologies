# Systems Performance — Ch.10 §10.6 Table 10.4 (traditional stats tools) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3839–3900**; file rebuilt 2026-04-20)
- Scope: what “stats-first” is for (not a tool tutorial)

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-traditional-stats-tools-table-10-6-a.md`

## Extracted ideas

- Use this family to operationalize **USE** on network interfaces and the stack: counters expose **utilization-ish proxies** (bytes/packets rates), **saturation** (drops, discards, overruns), and **errors**—the early classification inputs ([[use-method]], [[counters-statistics-metrics]]).
- Socket-level stats help separate “**too many concurrent conversations**” from “**too few bits/sec**”: growing receive/send queues are classic **queueing backlog** signals, while retransmits are often **downstream consequences** of loss/shaping/congestion—not a standalone diagnosis ([[queueing-theory]]).
- Prefer the maintained tool families called out by the text when you need **newest kernel semantics**; otherwise you risk blind spots that look like “no evidence” ([[streetlight-anti-method]]).

## Decision clarity

**Decision:** choose **stack/interface/socket counters** over **BPF tracing** when you still need to establish baseline utilization, error rates, and whether queues are accumulating ([[use-method]]).

## Application validation

- **Production noise:** if p95 latency rises but CPU is fine, start by checking whether **interface drops** or **socket queue growth** explains the tail—before turning on high-volume capture ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[use-method]], [[counters-statistics-metrics]], [[queueing-theory]], [[streetlight-anti-method]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[use-method]], [[counters-statistics-metrics]], [[queueing-theory]], [[streetlight-anti-method]], [[systems-performance]]
