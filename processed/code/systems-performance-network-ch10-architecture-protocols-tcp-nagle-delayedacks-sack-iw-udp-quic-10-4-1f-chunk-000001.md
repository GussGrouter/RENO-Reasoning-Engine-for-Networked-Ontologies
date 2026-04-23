# Systems Performance — Ch.10 §10.4.1 Protocols (TCP Nagle/delayed ACK/SACK/IW; UDP; QUIC)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2149–2186** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- **Nagle** reduces small packets via coalescing (can add latency).
- **Delayed ACKs** coalesce ACKs (can add latency); Nagle + delayed ACK interaction can require disabling one.
- **SACK/FACK/RACK-TLP** improve loss recovery (avoid retransmitting whole windows; better loss detection).
- **Initial window (IW)** trades faster short-flow completion against congestion/drop risk when many flows start simultaneously.
- **UDP** is simple and low-overhead but unreliable and lacks congestion avoidance; it can contribute to congestion.
- **QUIC** builds on UDP to provide multiplexing, optional reliability per stream, connection resumption, encryption, and 0-RTT for previously known peers.

