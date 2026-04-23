# Systems Performance — Ch.10 §10.6 Table 10.4 (traditional stats tools)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3839–3900** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- “Traditional stats” family covers **socket inventory**, **interface/route counters**, **kernel network stack counters**, and **historical summaries**—the first line of evidence for utilization/saturation stories.
- This is the low-cost layer for answering: **how many connections**, **what queues are growing**, and **what interfaces are busy**—before tracing/capture.
