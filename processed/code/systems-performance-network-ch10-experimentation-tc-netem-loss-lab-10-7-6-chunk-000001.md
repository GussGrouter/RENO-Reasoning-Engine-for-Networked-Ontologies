# Systems Performance — Ch.10 §10.7.6 tc (netem loss experiment)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4484–4517** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- `tc qdisc show` inspects current root qdisc; example starts from `noqueue`.
- Adds **`netem` loss** on an interface for experimentation/simulation; subsequent I/O experiences configured loss.
- `tc -s qdisc show` prints **counters** including **Sent bytes/packets** and **dropped** counts—these are **cumulative totals since the qdisc was installed** (not rates) until you sample deltas over time.
- Removal restores prior configuration; points reader to per-qdisc man pages (`tc-netem(8)` for netem).
