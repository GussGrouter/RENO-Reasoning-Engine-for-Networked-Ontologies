# Systems Performance — Ch.10 §10.3.7 Connection backlog (SYN queue)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1229–1241** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- TCP keeps a **backlog** for incoming SYNs before user-land accepts.
- If accepts can’t keep up, backlog hits a limit, SYNs drop, and clients retransmit → **higher connect latency**.
- Backlog drops and SYN retransmits are indicators of **host overload** (endpoint, not necessarily the network path).

