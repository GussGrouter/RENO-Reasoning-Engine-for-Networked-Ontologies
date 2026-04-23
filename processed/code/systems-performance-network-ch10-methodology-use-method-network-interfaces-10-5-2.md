# Systems Performance — Ch.10 §10.5.2 USE method (network)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2093–2136** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Apply USE per interface and per direction (TX/RX):
  - **Errors** first (quick, interpretable)
  - **Utilization** as throughput / negotiated speed (include protocol headers; consider imposed limits)
  - **Saturation** is harder: infer from blocked send time, overruns, and retransmits (but retransmits can be anywhere along the path)
- Extend USE to controllers/transports by topology inference (sum per-port throughput vs max controller capacity).

