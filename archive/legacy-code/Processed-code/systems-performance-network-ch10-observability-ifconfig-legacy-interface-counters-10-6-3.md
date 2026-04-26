# Systems Performance — Ch.10 §10.6.3 ifconfig (legacy interface stats)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2660–2693** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Linux `ifconfig` still prints **interface configuration + RX/TX counters** aligned with `ip`’s story (errors/drops/overruns/etc.).
- On Linux, `ifconfig` is treated as **obsolete** vs `ip` from **iproute2**—operational reality: many hosts still have it; engineering reality: prefer maintained tooling when you need newest semantics.
- Footnote caveat: **`txqueuelen`** is not uniformly honored by drivers (notifier path); **BQL** may auto-tune queues—don’t treat the number as a guaranteed knob effect.
