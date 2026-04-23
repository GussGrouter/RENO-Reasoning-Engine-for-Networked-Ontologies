8.3.13

Operations Are Not Equal

As is clear from the previous sections, file system operations can exhibit different performance
based on their type. You can’t tell much about a workload of “500 operations/s” from the rate
alone. Some operations may return from the file system cache at main memory speeds; others
may return from disk and be orders of magnitude slower. Other determinant factors include
whether operations are random or sequential, reads or writes, synchronous writes or asynchronous writes, their I/O size, whether they include other operation types, their CPU execution cost
(and how CPU-loaded the system is), and the storage device characteristics.
It is common practice to micro-benchmark different file system operations to determine these
performance characteristics. As an example, the results in Table 8.2 are from a ZFS file system,
on an otherwise idle Intel Xeon 2.4 GHz multi-core processor.

**(Table 8.2 omitted — example micro-benchmark latencies by syscall pattern; see book PDF.)**

These tests did not involve the storage devices but are a test of the file system software and CPU
speed. Some special file systems never access persistent storage devices.
These tests were also single-threaded. Parallel I/O performance may be affected by the type and
organization of file system locks in use.

