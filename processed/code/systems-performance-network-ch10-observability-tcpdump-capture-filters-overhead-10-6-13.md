# Systems Performance — Ch.10 §10.6.13 tcpdump (packet capture)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3736–3786** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Prefer **writing captures to disk** over live STDOUT when rates are high; live summaries are often impractical at real packet rates.
- Capture output reports **packets captured**, **packets received by filter**, and **packets dropped by kernel**—the drop counter is a **saturation signal** (capture path could not keep up), not an application bug by itself.
- **In-kernel BPF filtering** (pcap-filter) focuses work before userspace (except ancient Linux note).
- **Timestamps**: per-packet absolute time with microsecond resolution; options switch to **inter-packet deltas** (`-ttt`) or **elapsed since first packet** (`-ttttt`)—these are still per-event timestamps, not “rates” unless you derive rates yourself.
- **Verbose / link-layer / hex dumps** trade readability vs volume; checksum “incorrect” notices often reflect **offloads** (interpretation caveat).
- Capture is **CPU + storage expensive**; keep runs short and prefer **higher-level BPF tools** when they answer the question.
- **tshark** called out as CLI sibling with richer filtering/output (Wireshark ecosystem).
