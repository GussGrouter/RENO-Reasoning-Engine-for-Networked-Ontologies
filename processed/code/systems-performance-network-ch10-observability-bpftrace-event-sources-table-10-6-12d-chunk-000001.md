# Systems Performance — Ch.10 §10.6.12 bpftrace (part D — Table 10.6 event sources)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3325–3735** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Table 10.6 maps **network phenomena** (app protocols, sockets, TCP/UDP, IP/ICMP, packets, qdisc/driver queues, XDP, NIC drivers) to typical **instrumentation layers** (uprobes, syscall tracepoints, tcp tracepoints/kprobes, skb tracepoints/kprobes, qdisc/net tracepoints, xdp tracepoints, driver probes).
- Guiding rule repeated: **prefer tracepoints** where available for stability.
