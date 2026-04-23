# Systems Performance — Ch.10 §10.8.3 Configuration (jumbo frames, link aggregation, firewall DSCP)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4492–4502** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- **Jumbo frames (MTU ~9000)** can improve throughput if the infrastructure supports it.
- **Link aggregation** combines multiple NICs into one logical interface with combined bandwidth; requires switch support and correct configuration.
- **Firewall / egress marking** can set IP ToS/DSCP based on rules (e.g., via iptables or BPF at egress) to prioritize traffic by port/other criteria.

