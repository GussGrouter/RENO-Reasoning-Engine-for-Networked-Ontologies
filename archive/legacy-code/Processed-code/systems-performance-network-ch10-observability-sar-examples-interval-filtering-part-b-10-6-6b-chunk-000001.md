# Systems Performance — Ch.10 §10.6.6 sar (part B — examples, naming, filtering)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2911–3075** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- After the table, the text explains **SNMP name mapping** (e.g., `ipInReceives` ↔ `irec/s`)—helps crosswalk kernel counters to MIB/docs and other tools.
- Worked example: `sar -n TCP 1` shows per-second **active/passive** connection rates plus segment rates—useful workload and churn signals.
- **Interface reports** often need **filtering one IFACE**; example uses awk to isolate `ens5` from the all-interfaces listing.
- Reminder: other tools (e.g., `atop`) can **archive** similar stats—choose based on fleet standards, not novelty.
