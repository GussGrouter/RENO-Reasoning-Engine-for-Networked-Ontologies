# Systems Performance — Ch.9 §9.9.3 Disk controller tunables

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2459–2493** (printed ~494–495).

## Summary

- **Vendor-specific firmware settings** (**rebuild**, **parity**, **cache flush intervals**, **throttle**, **spin-up grouping**, …)—illustrative **MegaCli** dump only.
- Each knob has vendor meaning; tune only with **matching workload + failure-mode** rationale.

## Measurement-validity

- **Representation:** firmware counters/tunables explain **policy delays** invisible to **`iostat`** alone—still not a substitute for **trace-backed** latency work.
