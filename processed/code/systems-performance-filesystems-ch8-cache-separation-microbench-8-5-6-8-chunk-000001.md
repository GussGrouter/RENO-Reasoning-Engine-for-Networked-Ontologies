8.5.6

Cache Tuning

The kernel and file system may use many different caches, including a buffer cache, directory
cache, inode cache, and file system (page) cache. Various caches were described in Section 8.4,
Architecture. These can be examined and often tuned, depending on the tunable options
available.

8.5.7

Workload Separation

Some types of workloads perform better when configured to use their own exclusive file systems
and disk devices. This approach has been known as using “separate spindles,” since creating random I/O by seeking between two different workload locations is particularly bad for rotational
disks (see Chapter 9, Disks).
For example, a database may benefit from having separate file systems and disks for its log files
and its database files. The installation guide for the database frequently contains advice on the
placement of its data stores.

8.5.8 Micro-Benchmarking
Benchmark tools for file system and disk benchmarking (of which there are many) can be used
to test the performance of different file system types or settings within a file system, for given
workloads. Typical factors that may be tested include operation types, I/O sizes, sequential vs
random offsets (and randomness distributions), synchronous vs asynchronous writes, working
set size vs cache residency, concurrency, mmap vs read/write paths, cold vs warm cache state,
and FS tunables such as compression or deduplication.

(Omitted in this processed extract: the per-factor bullet list — see PDF.)

Common combinations include random read, sequential read, random write, and sequential
write. I have not included direct I/O in this list, as its intent with micro-benchmarking is to
bypass the file system and test disk device performance (see Chapter 9, Disks).
A critical factor when micro-benchmarking file systems is the working set size (WSS): the volume
of data that is accessed. Depending on the benchmark, this may be the total size of the files in
use. A small working set size may return entirely from the file system cache in main memory
(DRAM), unless a direct I/O flag is used. A large working set size may return mostly from storage
devices (disks). The performance difference can be multiple orders of magnitude. Running a
benchmark against a newly mounted file system and then a second time after caches have been
populated and comparing the results of the two is often a good illustration of WSS. (Also see
Section 8.7.3, Cache Flushing.)
