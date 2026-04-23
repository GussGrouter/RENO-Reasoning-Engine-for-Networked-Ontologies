8.5.1

Disk Analysis

A common troubleshooting strategy has been to ignore the file system and focus on disk performance instead. This assumes that the worst I/O is disk I/O, so by analyzing only the disks you
have conveniently focused on the expected source of problems.
With simpler file systems and smaller caches, this generally worked. Nowadays, this approach
becomes confusing and misses entire classes of issues (see Section 8.3.12, Logical vs. Physical I/O).

8.5.2 Latency Analysis
For latency analysis, begin by measuring the latency of file system operations. This should
include all object operations, not just I/O (e.g., include sync(2)).
operation latency = time (operation completion) - time (operation request)
These times can be measured from one of four layers, as shown in Table 8.4.

(Stopped before **Table 8.4** in this batch; table omitted here — see PDF. Next extract continues the layer taxonomy.)
