# Systems Performance — Ch.10 §10.3.10 Utilization (network interfaces)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1278–1298** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Network interface utilization can be computed as throughput / maximum bandwidth, but negotiation (speed/duplex) complicates the denominator.
- For full duplex, utilization is per-direction; systems are often asymmetric (servers TX-heavy, clients RX-heavy).
- Some tools report packet counts rather than bytes; since packet size varies, packet counts cannot be reliably converted to throughput/utilization without size information.

