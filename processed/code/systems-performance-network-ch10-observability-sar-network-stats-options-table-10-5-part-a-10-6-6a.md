# Systems Performance — Ch.10 §10.6.6 sar (Linux network statistics, part A — options + Table 10.5)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2911–3075** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- `sar` contributes **historical replay + interval rates** for network stacks (Chapter 4 tie-in): network observability spans live and archived reporting.
- Linux exposes many groups (`-n DEV`, `EDEV`, `IP`, `EIP`, `TCP`, `ETCP`, `SOCK`; text notes additional ICMP/NFS/SOFT and IPv6 variants exist—see manual).
- **Table 10.5** enumerates statistic names/units across those groups (packet/byte rates, errors, TCP connection churn, retransmits, socket counts, TIME_WAIT counts, IP fragments, etc.). Treat it as a **catalog of candidate signals**, not something to memorize row-by-row.
- Notable intent: column naming encodes direction/units (`rx` vs `tx`, `seg`, `err`, etc.), which supports consistent dashboard design.
