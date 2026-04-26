# Systems Performance — Ch.10 §10.6.15 Other tools (part B — Linux sources + monitoring)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3835–3838** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Lists additional common sources: **strace** for socket syscalls (high overhead warning), **lsof** for open sockets by PID, **nfsstat**, **ifpps**, **iftop** (host throughput sniffer), **perf** for network tracepoints/functions, **`/proc/net`**, **BPF iterators exporting custom stats** under `/sys/fs/bpf`.
- Notes ecosystem reality: many **SNMP/custom-agent** monitoring stacks exist—operational coverage matters as much as single-host CLI skill.
