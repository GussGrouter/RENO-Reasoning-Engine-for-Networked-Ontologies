# Systems Performance — Ch.9 §9.3.12–§9.3.13 Sync vs async; disk vs application I/O

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **645–693** (PDF ~434).

## Summary

### §9.3.12 Synchronous vs asynchronous

- **Disk latency ≠ app latency** when **async / write-back / prefetch / worker threads** decouple client path from media completion (**Ch.8** NIO, read-ahead, sync write sections).

### §9.3.13 Disk vs application I/O mismatch

Rates/volumes at **disk** may **not match** application expectations due to:

- **FS inflation/deflation / unrelated I/O** (**Ch.8 logical vs physical**).
- **Paging** pressure (**Ch.7**).
- **Driver rounding/fragmentation**.
- **RAID parity/mirror traffic**.

Understanding **architecture + measurement at both layers** resolves confusion.

## Notes

- §9.4 **Architecture** begins immediately after in book—**next ingest batch** starts there.
