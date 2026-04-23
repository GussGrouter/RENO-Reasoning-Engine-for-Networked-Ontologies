# Systems Performance — Ch.9 §9.7.4 Offset heat maps

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2214–2233** (printed ~490).

## Summary

- **Axes:** **time × disk offset (LBA)**—pixel intensity encodes **I/O density** in each cell.
- **Read visually:** **dark streaks** ≈ **sequential crawl** across media; **diffuse clouds** ≈ **random** access—useful for **spatial access shape** separate from **latency-only** views.
- **Tools:** historical **taztool** lineage; **seekwatcher** on Linux mentioned.

## Measurement-validity

- **Representation:** figure caption text mixes **“time and latency range”** with **offset-on-y** description—**trust axis labels** over a loose phrase when interpreting pixels (**representation** risk if labels absent).
