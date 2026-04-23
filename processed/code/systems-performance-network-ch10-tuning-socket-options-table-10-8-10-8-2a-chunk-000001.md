# Systems Performance — Ch.10 §10.8.2 Socket Options (part A — setsockopt + Table 10.8)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4440–4474** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Per-socket tuning is done by applications via **`setsockopt(2)`**; it is often only feasible if you can **change/rebuild the app**.
- Socket options target different layers (socket vs TCP).
- Table 10.8 sample options and their intent:
  - **`SO_SNDBUF` / `SO_RCVBUF`**: per-socket send/receive buffers (bounded by system-wide limits).
  - **`SO_REUSEPORT`**: kernel distributes accepts across processes/threads binding same port (scalability).
  - **`SO_MAX_PACING_RATE`**: per-socket pacing ceiling (bytes/s).
  - **`SO_LINGER`**: can reduce TIME_WAIT latency in some patterns.
  - **`SO_TXTIME`**: time-based transmission deadlines (time-sensitive pacing).
  - **`TCP_NODELAY`**: disable Nagle; latency vs packetization/utilization trade.
  - **`TCP_CORK`**: delay sends until full packets; throughput vs latency trade (and system-wide autocork exists).
  - **`TCP_QUICKACK`**: ACK immediately (can increase send bandwidth).
  - **`TCP_CONGESTION`**: choose congestion control per socket.

