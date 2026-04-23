# Systems Performance — Ch.9 §9.6.14 SCSI logging

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p482-560.txt`
- Scope: **§9.6.14**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-scsi-logging-9-6-14.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Kernel SCSI logging** trades **deep protocol visibility** for **log volume**—bounded trials only ([[instrumentation-overhead-and-perturbation]] **perturbation**).
- **dmesg lacks pairing IDs**—poor substitute for **structured latency tracing** when you need **distributions** ([[measurement-validity]] **representation**).

## Decision clarity

**Decision:** choose **BPF latency tools** over **SCSI syslog levels** when the question is **quantitative latency shape**, not **“did the HBA log a protocol oddity?”**

## Concepts reused / refined / created

- Reused: [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[event-tracing]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[event-tracing]], [[systems-performance]]
