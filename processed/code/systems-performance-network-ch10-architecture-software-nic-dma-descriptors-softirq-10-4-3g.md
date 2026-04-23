# Systems Performance — Ch.10 §10.4.3 Software (NIC send/receive: DMA + descriptor limits)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1737–1931** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- NICs use DMA to read outgoing frames from kernel memory and to place incoming frames into ring buffers.
- TX descriptor exhaustion pauses transmission until the NIC catches up.
- RX interrupts trigger softirq processing (or may be coalesced/ignored under NAPI behavior).

