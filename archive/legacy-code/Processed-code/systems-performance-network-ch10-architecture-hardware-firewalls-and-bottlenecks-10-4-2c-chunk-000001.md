# Systems Performance — Ch.10 §10.4.2 Hardware (firewalls + performance bottlenecks)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1614–1736** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Firewalls enforce policy and can be hardware devices or kernel software.
- Stateful firewalls can become a bottleneck via per-connection state and memory load (DoS or heavy outbound churn).
- Firewalls can also complicate experimentation (rules may block tests).

