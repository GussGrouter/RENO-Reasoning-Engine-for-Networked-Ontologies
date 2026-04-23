# Systems Performance — Ch.10 §10.8.1 System-wide tuning (part B — buffers, backlogs, device backlog)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4555–4621** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- **`net.core.somaxconn`**: maximum length of the **listen backlog** for `listen(2)` (default often 128).
- **`net.core.netdev_max_backlog`**: maximum length of the **device input queue** (packets awaiting delivery to user-level processes).
- **`net.ipv4.tcp_max_syn_backlog`**: maximum length of the **SYN backlog** (half-open connections).
- **`net.core.rmem_max` / `wmem_max`**: maximum **receive/send buffer sizes** for sockets.
- **`net.ipv4.tcp_rmem` / `tcp_wmem`**: min/default/max **TCP receive/send buffer sizes** (three values each).
