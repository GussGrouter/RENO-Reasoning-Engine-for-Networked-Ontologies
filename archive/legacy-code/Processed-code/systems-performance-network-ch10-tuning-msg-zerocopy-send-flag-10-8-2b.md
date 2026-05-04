# Systems Performance — Ch.10 §10.8.2 Socket Options (part B — MSG_ZEROCOPY send flag)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4440–4491** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Linux 4.14 added **`MSG_ZEROCOPY`** for `send(2)`: lets user-space buffer be used during transmission to avoid copying into kernel space.
- **Constraint:** `send(2)` may return before data is actually sent; the application must wait for a kernel notification before freeing/reusing that buffer.

