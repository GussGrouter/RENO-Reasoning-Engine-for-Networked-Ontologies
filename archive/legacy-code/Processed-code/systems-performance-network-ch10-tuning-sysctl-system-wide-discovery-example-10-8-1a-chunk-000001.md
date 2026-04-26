# Systems Performance — Ch.10 §10.8.1 System-wide tuning (part A — sysctl discovery + example profile)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4164–4223** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Linux system-wide knobs live under **`sysctl` / `/etc/sysctl.conf` / `/proc/sys/net`**; `sysctl -a | grep tcp` is a pragmatic discovery pattern (example shows many `net.ipv4.tcp_*` keys on a 5.3 kernel).
- Notes many parameters exist beyond TCP (IP, Ethernet, routing, interfaces).
- Includes a **Netflix cloud sysctl excerpt** as a **point-in-time example** (explicitly not a universal recipe) and mentions pending tweaks after review/non-regression testing.
