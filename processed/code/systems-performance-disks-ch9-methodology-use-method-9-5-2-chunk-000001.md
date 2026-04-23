# Systems Performance — Ch.9 §9.5.2 USE method (disks + controllers)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1531–1605** (PDF ~451–452).

## Summary

- **Per disk device:** **utilization**, **saturation**, **errors** ([[use-method]]).
- **Errors first:** redundant pools can **mask slow failure modes**—use **OS counters + SMART-class** probes where applicable.
- **Virtual disk caveat:** **util ≠ physical util** (**§9.3.9** pointer).
- **Per controller:** **utilization** framed as **throughput/IOPS vs card limits** (not only **time-busy**); **saturation** when controller queues throttle; **errors**.
- **Transports** (host↔controller, controller↔disk): same **USE** pattern.
- **Tool gap:** OS tools often **per-disk only**—**sum per controller** when topology known; **plateau at fixed IOPS/BW** across workloads hints **controller/transport ceiling**.

## Application validation

If **aggregate disk metrics** flatline below raw **drive capability**, split **controller vs HBA vs fabric** before buying more spindles.
