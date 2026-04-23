# Systems Performance — Ch.10 §10.4.3 Software (other optimizations: pacing, TSQ, BQL, EDT)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1737–1931** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- **Pacing** reduces bursts to avoid queueing delay/drops (micro-bursts, incast).
- **TCP Small Queues (TSQ)** limits queued data in the stack to reduce bufferbloat.
- **Byte Queue Limits (BQL)** auto-sizes driver queues to reduce latency and avoid TX descriptor exhaustion.
- **EDT** orders NIC-bound packets by timestamps (timing wheel vs FIFO), enabling policy/rate control.
- These mechanisms compose: multiple layers can shape a packet before it reaches the NIC.

