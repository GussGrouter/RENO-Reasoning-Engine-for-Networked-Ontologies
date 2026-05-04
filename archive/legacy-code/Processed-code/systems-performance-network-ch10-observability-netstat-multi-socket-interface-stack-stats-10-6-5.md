# Systems Performance — Ch.10 §10.6.5 netstat (multi-purpose stats)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2751–2910** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- `netstat` is intentionally a **multi-entry tool**: sockets (default / `-a`), stack stats (`-s`), interface stats (`-i`), routes (`-r`), plus naming/verbosity toggles.
- Interface columns include **drops/overruns/errors**—drops/overruns called out as **saturation indicators** alongside USE-style diagnosis.
- Continuous modes (`-c` with `-i`) expose **per-second snapshots of cumulative counters**, enabling packet-rate inference.
- Stack statistics include many TCP extended lines (examples: **segments retransmitted**, **SYN retransmits**, receive-queue pruning). Retransmits are framed as reliability/path pressure signals; SYN retransmits tied to **listen backlog pressure** narrative.
- Practical ops note: some human-readable labels contain typos; **`nstat`** SNMP names or direct **`/proc/net/snmp` + `/proc/net/netstat`** are preferable for programmatic monitoring.
