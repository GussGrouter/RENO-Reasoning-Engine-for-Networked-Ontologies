# Systems Performance — Ch.9 §9.6.10 blktrace (intro + default trace)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **4366–4504** (PDF ~475–477).

## Summary

- **Stack:** **`blktrace`** captures kernel **blk** events; **`blkparse`** decodes; **`btrace`** runs **pipeline** equivalent to `blktrace … | blkparse`.
- **Granularity:** **multiple trace lines per logical I/O**—rich for diagnosis, heavy for humans.
- **Default column schema** (seven fields): **maj/min**, **CPU**, **sequence**, **time**, **PID**, **action letter**, **RWBS** (+ payload varies by action).
- Example single read produced **eight** action lines—shows **queue plug/unplug**, **merge**, **issue**, **completion** choreography.

## Measurement-validity

- **Scope/semantics:** raw **blktrace** is **event vocabulary**, not yet **end-to-end latency**—later **btt** aggregates stages (**perturbation:** volume / capture cost).
