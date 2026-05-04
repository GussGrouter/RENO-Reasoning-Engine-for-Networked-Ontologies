# Systems Performance — Ch.10 §10.5.6 Packet sniffing (overhead + last resort)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2279–2328** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Packet capture inspects protocol headers/payload packet-by-packet; treat as late-stage because it can be expensive in CPU/storage.
- To reduce overhead: ring buffers/shared-memory paths; or out-of-band capture (tap/mirror) when available.
- Kernel filtering reduces overhead by dropping unwanted packets before user-space transfer; classic BPF compilation is used for filters.
- Capture can drop packets under overload; include drop counts when interpreting results.

