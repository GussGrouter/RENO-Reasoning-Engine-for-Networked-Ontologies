# Systems Performance — Ch.10 §10.5.7 TCP analysis (buffers/backlog/cwnd; TIME_WAIT + port collisions)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2349–2371** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- TCP analysis targets specific behaviors: buffer usage, backlog usage/drops, congestion window signals.
- A scalability failure mode: high connection rates can exhaust ephemeral ports due to TIME_WAIT holding ports; new SYNs can collide and be rejected/misidentified.
- Mitigations include fast reuse/recycle (kernel behavior), using multiple IPs, or socket options affecting close behavior.

