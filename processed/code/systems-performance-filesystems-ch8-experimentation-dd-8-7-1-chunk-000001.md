8.7 Experimentation
This section describes tools for actively testing file system performance. See Section 8.5.8,
Micro-Benchmarking, for a suggested strategy to follow.
When using these tools, it is a good idea to leave iostat(1) continually running to confirm that
the workload reaches the disks as expected, which may mean not at all. For example, when testing a working set size that should easily fit in the file system cache, the expectation with a read
workload is 100% cache hits, so iostat(1) should not show substantial disk I/O. iostat(1) is covered
in Chapter 9, Disks.

8.7.1

Ad Hoc

The dd(1) command (device-to-device copy) can be used to perform ad hoc tests of sequential
file system performance. The following commands write, and then read a 1 Gbyte file named
file1 with a 1 Mbyte I/O size:
write: dd if=/dev/zero of=file1 bs=1024k count=1k
read: dd if=file1 of=/dev/null bs=1024k

The Linux version of dd(1) prints statistics on completion. For example:
$ dd if=/dev/zero of=file1 bs=1024k count=1k
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 0.76729 s, 1.4 GB/s

This shows a file system write throughput of 1.4 Gbytes/s (write-back caching is in use, so this
only dirtied memory and will be flushed later to disk, depending on the vm.dirty_* tunable
settings: see Chapter 7, Memory, Section 7.6.1, Tunable Parameters).
