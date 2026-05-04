# Systems Performance — Ch.10 §10.4.1 Protocols (TCP: duplicate ACK detection + retransmits + TLP)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2149–2186** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Duplicate ACKs enable fast loss detection (fast retransmit/recovery) without waiting for long timers.
- Retransmits can be timer-based (RTO, exponential backoff) or fast (dup ACK driven).
- Tail Loss Probe (TLP) reduces “last-packet lost” stalls by probing after a short timeout.

