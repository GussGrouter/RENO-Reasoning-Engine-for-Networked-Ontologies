# Systems Performance — Ch.10 §10.7.2 traceroute (TTL path experiment)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4076–4225** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Mechanism: increment **TTL** hop-by-hop to elicit **ICMP time exceeded** responses and reveal gateways—**experimental route discovery**, not passive counters.
- Each hop prints multiple **RTT samples** (often three) usable as coarse latency statistics; same ICMP priority caveats as ping.
- **`* * *` gaps** can mean **no ICMP return**, **rate limiting**, or **firewall blocking**—not automatically “dead hop”; TCP-mode workarounds (`-T`, `tcptraceroute`, `astraceroute`) exist when ICMP is unreliable.
- **Path dynamics**: route can change **during** a run; output rules print new addresses when they change.
- Pointer to deeper traceroute interpretation literature.
