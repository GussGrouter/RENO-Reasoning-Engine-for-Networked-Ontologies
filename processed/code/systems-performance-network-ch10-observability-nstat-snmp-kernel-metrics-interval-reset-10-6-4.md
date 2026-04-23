# Systems Performance — Ch.10 §10.6.4 nstat (SNMP-named kernel metrics)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2694–2750** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- `nstat` surfaces kernel network metrics using **SNMP-like names**, enabling comparison to MIB docs and cross-tool consistency.
- **Default behavior resets counters** unless you use `-s` (“summary since boot” without reset)—surprise resets break baseline comparisons; recovery flag `-rs` exists if you slip.
- **Delta-friendly workflow**: run twice around a reproduction window to see **which counters moved** (interval-style interpretation without needing a daemon).
- Optional **daemon mode** prints an extra column for **interval stats**.
- Highlights include **TcpRetransSegs vs TcpOutSegs** (retransmit intensity) among many TCP/IP counters.
