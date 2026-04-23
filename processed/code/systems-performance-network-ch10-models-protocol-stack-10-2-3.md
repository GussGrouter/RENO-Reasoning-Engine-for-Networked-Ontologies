# Systems Performance — Ch.10 §10.2.3 Protocol stack (model)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **957–998** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Networking uses a **protocol stack**: messages move down (send) and up (receive).
- Layer terminology differs (OSI vs TCP/IP), and message names shift by layer (segment/datagram → packet → frame).
- Real deployments add layers (security/tunnels), which adds work and can change latency/throughput behavior.

