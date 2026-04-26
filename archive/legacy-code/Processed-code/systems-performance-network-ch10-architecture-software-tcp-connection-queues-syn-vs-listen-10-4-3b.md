# Systems Performance — Ch.10 §10.4.3 Software (TCP connection queues: SYN vs listen backlog)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1737–1931** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Linux uses two backlog queues: one for **incomplete handshakes (SYN backlog)** and one for **established sessions waiting accept (listen backlog)**.
- Two-queue design reduces SYN flood vulnerability by staging potentially bogus connections before promoting them.
- SYN cookies can bypass the first queue; queue sizes are tunable; the listen backlog can be set by the application.

