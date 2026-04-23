# Systems Performance — Ch.10 §10.5.1 Tools method (network: what to check)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2057–2092** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Tools method = iterate available tools/metrics; can be slow and miss invisible issues.
- Decision-relevant checks it suggests:
  - **Retransmits/out-of-order** rate (context depends on client quality).
  - **Interface errors/drops/overruns**.
  - **Per-socket limiter/bottleneck flags**.
  - **Bytes TX/RX rate** (throughput caps may reflect negotiated speed or external throttles).
- If you find something, use all fields for context; other methods cover other issue classes.

