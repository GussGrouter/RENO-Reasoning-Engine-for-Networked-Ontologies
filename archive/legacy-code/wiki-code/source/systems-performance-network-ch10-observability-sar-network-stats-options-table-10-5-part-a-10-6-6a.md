# Systems Performance — Ch.10 §10.6.6 sar — options + Table 10.5 (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2911–3075**; file rebuilt 2026-04-20)
- Scope: sar as **rate-capable** network reporting + what Table 10.5 is for (taxonomy absorbed into counters/SAR workflow, not new concepts)

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-sar-network-stats-options-table-10-5-part-a-10-6-6a.md`

## Extracted ideas

- **USE alignment**: DEV/EDEV emphasize **throughput + error/drop proxies**; ETCP emphasizes **retransmit intensity**—again, interpret **retransmits** as usually **loss/queueing/congestion consequences**, then localize the queue ([[queueing-theory]], [[use-method]]).
- **SOCK group surfaces concurrency shape** (TCP sockets in use, TIME_WAIT inventory): pairs with **port-space / churn** stories without needing deep tracing ([[resource-limits-method]] when contention becomes limiting).
- **%ifutil** is an **interface utilization heuristic** (full duplex: max of rx/tx direction): useful, but remember **representation** limits—link utilization ≠ end-to-end app SLA ([[measurement-validity]] **representation**, only when you’re deciding capacity from `%ifutil` alone).

## Decision clarity

**Decision:** choose **`sar -n DEV` interval samples** over raw cumulative `/proc` scraping when you need **built-in rate columns** for busy interfaces during incidents ([[counters-statistics-metrics]]).

## Application validation

- **Capacity fights:** rising `%ifutil` with rising **rxerr/txdrop** suggests **hardware/driver saturation**; rising `%ifutil` with clean counters points to **goodput vs serialization** questions before chasing CPU ([[use-method]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[use-method]], [[resource-limits-method]], [[measurement-validity]], [[counters-statistics-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[use-method]], [[resource-limits-method]], [[measurement-validity]], [[counters-statistics-metrics]], [[systems-performance]]
