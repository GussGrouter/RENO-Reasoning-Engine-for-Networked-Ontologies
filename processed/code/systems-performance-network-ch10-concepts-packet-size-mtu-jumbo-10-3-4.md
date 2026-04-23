# Systems Performance — Ch.10 §10.3.4 Packet size (MTU, jumbo frames, fragmentation)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1071–1108** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Larger packets can improve **throughput** by reducing per-packet overhead.
- MTU commonly defaults to **1500 bytes**; jumbo frames (~9000 bytes) can improve throughput but introduce compatibility risks.
- Fragmentation and ICMP “can’t fragment” signaling can change performance; blocking ICMP can cause silent drops once packets exceed MTU.
- Hardware offloads (e.g., segmentation/large send) can narrow the performance gap without changing MTU.

