# Systems Performance — Ch.10 §10.8.1 System-wide tuning (part C — congestion control, TCP options, ECN)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4555–4621** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- **`net.ipv4.tcp_congestion_control`**: selects the **TCP congestion control algorithm** (example lists `reno`, `cubic`, `hybla`, `htcp`, `vegas`, `westwood`, `illinois`, `bbr`, `nv`, `dctcp`, `cdg`, `veno`, `scalable`, `lp`, `yeah`, `venus`, `newreno`, `ledbat`, `mlp01`, `mlp02`, `mlp03`, `nvidia_cc`, `nvidia_ll`).
- **`net.ipv4.tcp_available_congestion_control`**: lists algorithms available in the kernel.
- **`net.ipv4.tcp_slow_start_after_idle`**: enables/disables **slow start after idle** (default on).
- **`net.ipv4.tcp_tw_reuse`**: allows **reuse of TIME-WAIT sockets** for new connections when safe from protocol view (default off).
- **`net.ipv4.tcp_sack`**: enables **selective acknowledgments** (default on).
- **`net.ipv4.tcp_ecn`**: enables **ECN** (explicit congestion notification) for TCP (default off).
