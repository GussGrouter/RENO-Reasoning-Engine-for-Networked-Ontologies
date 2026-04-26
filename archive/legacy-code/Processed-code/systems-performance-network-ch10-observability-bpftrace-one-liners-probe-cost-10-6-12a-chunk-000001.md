# Systems Performance — Ch.10 §10.6.12 bpftrace (part A — one-liners + probe cost)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3325–3735** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Positions bpftrace as a **fast custom layer** for following up hints from cheaper tools: syscalls, socket I/O, TCP/UDP message paths, retransmits, qdisc/NIC events, etc.
- One-liner gallery shows **incremental power** (counts, histograms, kstacks) and also **how cost explodes** when you attach to very hot code paths (e.g., `k:tcp_*` over every TCP function, or `k:ixgbevf_*` / `k:ieee80211_*` over whole subsystems).
- Footnote: some kprobes on send/recv paths are not in the originating process context, so **pid/comm can be misleading**—a common “attribution validity” footgun.
