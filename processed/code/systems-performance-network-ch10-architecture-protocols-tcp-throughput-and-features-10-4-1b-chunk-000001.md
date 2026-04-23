# Systems Performance — Ch.10 §10.4.1 Protocols (TCP: throughput + key features)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2149–2186** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- TCP sustains throughput on high-latency paths via **buffering + sliding window**, and avoids congestion collapse via **congestion control**.
- Performance-relevant features include slow start, SACK, fast retransmit/recovery, fast open, timestamps (RTT measurement), and SYN cookies (backlog defense).

