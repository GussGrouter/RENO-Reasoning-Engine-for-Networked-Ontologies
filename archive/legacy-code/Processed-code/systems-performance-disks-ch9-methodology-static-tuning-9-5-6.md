# Systems Performance — Ch.9 §9.5.6 Static performance tuning (disk-focused checklist)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1820–1890** (PDF ~455–456).

## Summary

- **Static tuning** here = **inventory configured reality** before chasing live queue theory (**[[static-performance-tuning]]**).
- **Checklist themes:** **device count/types/SMR/cell class**, **firmware levels**, **controller+HBA placement** (PCIe speed), **disks per HBA**, **BBU health**, **RAID layout/stripe**, **multipath**, **driver versions**, **RAM vs cache pressure**, **known driver bugs**, **I/O cgroup/throttle**.
- **Vendor bugs:** firmware/driver defects can dominate—“**latest vendor patch**” is a valid performance lever.
- **Case study:** **wide RAID-Z2 on half-JBOD** behaving like **single-disk throughput**—misconfiguration suspected **before** deep latency tracing (**[[resource-vs-implementation-bottleneck]]**).

## Application validation

“**Slow ZFS appliance**” triage: collect **pool topology + ashift + RAID width** on the **first** call—matches author’s phone-debug pattern.
