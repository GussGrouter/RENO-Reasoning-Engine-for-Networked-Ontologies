# Systems Performance — Ch.10 §10.6.9 tcplife (TCP session lifespan)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3186–3239** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Summarizes each TCP session at **CLOSE**: duration (ms), endpoints, TX/RX KB, PID/comm when known—useful workload characterization (“who talks to whom,” short vs long flows).
- Implementation tracks **TCP socket state transitions**, which are far less frequent than packets—much lower overhead than sniffing everything; text notes production viability as a lightweight flow logger (paired with open-session snapshots elsewhere).
- Filtering knobs include local/remote ports and single-PID focus—supports drilling into suspect services without full packet capture.
