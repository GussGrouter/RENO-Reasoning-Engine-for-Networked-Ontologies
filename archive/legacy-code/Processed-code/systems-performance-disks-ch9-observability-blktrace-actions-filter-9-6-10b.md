# Systems Performance — Ch.9 §9.6.10 blktrace (action IDs, RWBS, filtering)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **4508–4677** (PDF ~477–478).

## Summary

- **Action identifiers** (`Q`,`G`,`I`,`D`,`C`,…) enumerate **what blktrace can observe**—reference **blkparse** man page for semantics (taxonomy omitted here).
- **`rwbs` string:** kernel-encoded **I/O flavor** shared across **blktrace family** tools—combinations like **`WM`** (metadata write).
- **Filtering:** **`-a issue`** ( **`D`** only), **`-a read`**, **`-a write`**, **`-a sync`** cuts noise when hunting **specific mechanisms**.

*(No separate concepts for letter tables.)*
