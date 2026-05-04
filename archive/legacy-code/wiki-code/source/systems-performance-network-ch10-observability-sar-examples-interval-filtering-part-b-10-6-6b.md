# Systems Performance — Ch.10 §10.6.6 sar — examples + rate thinking (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2911–3075**; file rebuilt 2026-04-20)
- Scope: converting sar’s interval output into actionable “rates of change” narratives

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-sar-examples-interval-filtering-part-b-10-6-6b.md`

## Extracted ideas

- **Connection arrival rates** (`active/s`, `passive/s`) are **workload intensity** indicators: sudden step changes often precede **queue growth** elsewhere (listen queues, SYN processing, ephemeral port pressure) ([[resource-analysis-vs-workload-analysis]]).
- **Filtering to one interface** is a drill-down discipline: prevents “streetlight averaging” hiding a hot NIC on multi-homed hosts ([[streetlight-anti-method]]).
- **SNMP crosswalk** supports consistent naming between `sar`, `nstat`, and MIB docs—reduces **representation** mismatches between dashboards ([[measurement-validity]]).

## Decision clarity

**Decision:** choose **one-interface `sar` streams** over **whole-table eyeballing** when the host has many NICs/VLANs and a single interface is on the critical path ([[drill-down-analysis]]).

## Application validation

- **Burst traffic:** if `passive/s` spikes while p99 latency spikes, correlate with **SYN backlog / accept queue** behaviors (often shows up as SYN retransmits elsewhere)—still a **queueing** story ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[resource-analysis-vs-workload-analysis]], [[streetlight-anti-method]], [[measurement-validity]], [[drill-down-analysis]], [[queueing-theory]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[resource-analysis-vs-workload-analysis]], [[streetlight-anti-method]], [[measurement-validity]], [[drill-down-analysis]], [[queueing-theory]], [[systems-performance]]
