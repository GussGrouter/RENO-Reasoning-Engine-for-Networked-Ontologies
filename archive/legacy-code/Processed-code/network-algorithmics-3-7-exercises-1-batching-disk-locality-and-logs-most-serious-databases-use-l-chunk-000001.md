# network-algorithmics-3-7-exercises-1-batching-disk-locality-and-logs-most-serious-databases-use-l (chunk 000001)

# Network Algorithmics — 3.7 Exercises 1. Batching, Disk Locality, and Logs: Most serious databases use log files for performance. Because (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 98
- Slice: from `3.7 Exercises 1. Batching, Disk Locality, and Logs: Most serious databases use log files for performance. Because` up to next detected section heading

---

3.7 Exercises
1. Batching, Disk Locality, and Logs: Most serious databases use log files for performance. Because
   writes to disk are expensive, it is cheaper to update only a memory image of a record. However,
   because a crash can occur at any time, the update must also be recorded on disk. This can be done
   by directly updating the record location on disk, but random writes to disk are expensive (see P4a).
   Instead, information on the update is written to a sequential log file. The log entry contains the
   record location, the old value (undo information), and the new value (redo information).
   • Suppose a disk page of 4000 bytes can be written using one disk I/O and that a log record is
     50 bytes. If we apply batching (2c), what is a reasonable strategy for updating the log? What
     fraction of a disk I/O should be charged to a log update?
   • Before a transaction that does the update can commit (i.e., tell the user it is done), it must be
     sure the log is written. Why? Explain why this leads to another form of batching, group commit,
     where multiple transactions are committed together.

72       Chapter 3 Fifteen implementation principles
