# Systems Performance — Ch.10 §10.4.3 Software (CPU scaling: steering + softirq bottlenecks)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1737–1931** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- High packet rates need multi-CPU processing; steering methods distribute work (RSS/RPS/RFS/XPS).
- Without steering, one CPU can hit 100% (softirq time) and bottleneck packet processing.
- Affinity/locality-aware steering (e.g., RFS) can improve cache locality; irqbalance can spread IRQs.

