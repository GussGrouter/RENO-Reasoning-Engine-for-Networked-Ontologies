# Systems Performance — Ch.10 §10.5.9 Resource controls (network)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2408–2433** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- OS-level controls can cap or shape traffic by connection/process/group: **bandwidth limits**, **QoS/priority marking**, and **injected latency** (test harnesses).
- Mixed-traffic environments often need **isolation/throttling of low-priority bulk** (backups, monitoring) so production traffic keeps headroom—implemented as limits/priority, not “more NIC”.
- The book’s PDF layout inserts the **§10.6 Observability Tools** heading inside this subsection; the substantive resource-control narrative ends before **§10.5.10 Micro-Benchmarking**.
