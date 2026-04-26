# Systems Performance — Ch.10 §10.3.5 Latency (measurement types)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1109–1183** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- “Network latency” has multiple operational definitions: **DNS/name resolution**, **ping (ICMP RTT)**, **connection establishment (TCP handshake)**, **first-byte (TTFB)**, **RTT**, and **connection life span**.
- Some measures include **server think time** (e.g., TTFB) while others aim to isolate the **network path** (e.g., ICMP RTT).
- Connection latency can include **retransmit latency** (e.g., SYN retransmits when backlog drops occur).
- Keep-alives can trade resource usage for avoiding repeated connection-setup latency.

