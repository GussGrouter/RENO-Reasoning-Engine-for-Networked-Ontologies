# Systems Performance — Ch.10 §10.4.1 Protocols (TCP handshake + states/timers)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2149–2186** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- TCP connections start with a **three-way handshake**; dropped packets add timer-based retransmit latency.
- TCP has multiple connection states; performance analysis often focuses on **ESTABLISHED**.
- Some states have long timers (e.g., TIME_WAIT), which can create resource pressure (ports) at high churn.

