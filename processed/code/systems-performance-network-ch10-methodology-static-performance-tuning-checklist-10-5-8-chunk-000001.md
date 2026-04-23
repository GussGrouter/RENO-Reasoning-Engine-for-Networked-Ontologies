# Systems Performance — Ch.10 §10.5.8 Static performance tuning (network checklist)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2372–2407** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Static tuning audits **configured environment** before chasing dynamic behavior: interfaces in use, max vs negotiated speed/duplex, MTU/trunking, routing/DNS, firmware/driver/stack versions, firewalls, and **imposed throughput limits** (common in cloud).
- Treat negotiated downshifts, MTU/path fragmentation surprises, and “hidden caps” as **capacity/policy ceilings** that can saturate upstream queues; **retransmits/drops/delays are often the visible queueing consequences**, not the explanatory label you stop on.
- The checklist ends by explicitly asking for **software-imposed throughput limits** (resource controls), which matters most when “the NIC looks fine” but the path still tops out early.
