# Systems Performance — Ch.9 §9.6.2 sar (disk)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **2617–2700** (PDF ~463–464).

## Summary

- **`sar -d`:** disk summary with columns aligned to **`iostat -x`** family (**tps**, throughput, **aqu-sz**, **await**, **`%util`**).
- **Historical posture:** same metrics class as live **`iostat`**, but oriented to **archived**/**interval reporting** (see Ch.4 §4.4).
- **Legacy:** older **`svctm`** removed—over-simplified for **modern parallel** devices (ties to §9.3.1 service-time discussion).

## Measurement-validity

- **Representation:** treating **`svctm`** (when present in old builds) as “true service time” **fails** on parallel/queued devices—prefer **issue→complete** views (`await`, tracing).
