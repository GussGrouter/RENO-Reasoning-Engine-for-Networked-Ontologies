# Systems Performance — Ch.10 §10.7.1 ping (ICMP RTT)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4042–4068** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- `ping` reports **per-packet RTT samples** plus a summary **min/avg/max/mdev**—useful coarse latency distribution and loss% (per run totals in the summary line).
- Older user-space timing inflated RTT slightly; newer stacks use **kernel timestamps** for more faithful RTT reporting.
- Caveat: ICMP may be **lower priority** than application traffic on some networks → **higher variance / optimistic or pessimistic bias** relative to TCP/UDP SLO paths (footnote notes exceptions).
