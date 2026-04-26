# Systems Performance — Ch.9 §9.6.4 pidstat (disk)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **2720–2899** (PDF ~464–465).

## Summary

- **`pidstat -d`:** per-process **read/write throughput** plus **`iodelay`** (time blocked on disk I/O in **clock ticks**).
- **Example narrative:** reader (`tar`) shows **`iodelay`**; writer (`gzip`) may show none until **write-back flush** shows up under **`kworker`** flush—illustrates **async write path** vs **attribution**.
- **Permissions:** non-root **cannot** see other users’ **`/proc/PID/io`** stats.

## Measurement-validity

- **Representation:** **`iodelay`** captures **blocked time**, not just **bytes moved**—better “pain” signal than rates alone for some issues.
