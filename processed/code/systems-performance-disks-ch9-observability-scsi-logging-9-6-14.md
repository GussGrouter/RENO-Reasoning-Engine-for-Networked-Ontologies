# Systems Performance — Ch.9 §9.6.14 SCSI logging

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2078–2111** (printed ~486–487).

## Summary

- Linux **SCSI logging** via **`sysctl`** / **`/proc`**—**octal bitfield** selects verbosity **per event class**; **`scsi_logging_level`** helper exists.
- **Risk:** max logging can **flood logs** under load—time-box experiments.
- **Limit:** **`dmesg` timestamps** lack pairing IDs—**hard to turn into precise latency distributions** vs BPF/trace frameworks.

## Measurement-validity

- **Perturbation:** verbose SCSI logging can **disturb** production (**log I/O**, **CPU**).
