Consider the general expectations for different benchmarks, which include the total size of the
files (WSS), in Table 8.5.

Table 8.5

File system benchmark expectations

System
Memory

Total File Size
(WSS)

Benchmark

Expectation

128 Gbytes

10 Gbytes

Random read

100% cache hits

128 Gbytes

10 Gbytes

Random read,
direct I/O

100% disk reads (due to direct I/O)

128 Gbytes

1,000 Gbytes

Random read

Mostly disk reads, with ~12% cache hits

128 Gbytes

10 Gbytes

Sequential read

100% cache hits

128 Gbytes

1,000 Gbytes

Sequential read

Mixture of cache hits (most due to
prefetch) and disk reads

8.6 Observability Tools

System
Memory

Total File Size
(WSS)

Benchmark

Expectation

128 Gbytes

10 Gbytes

Buffered writes

Mostly cache hits (buffering), with some
blocking on writes depending on file
system behavior

128 Gbytes

10 Gbytes

Synchronous
writes

100% disk writes

Some file system benchmark tools do not make clear what they are testing, and may imply a
disk benchmark but use a small total file size, which returns entirely from cache and so does not
test the disks. See Section 8.3.12, Logical vs. Physical I/O, to understand the difference between
testing the file system (logical I/O) and testing the disks (physical I/O).
Some disk benchmark tools operate via the file system by using direct I/O to avoid caching and
buffering. The file system still plays a minor role, adding code path overheads and mapping
differences between file and on-disk placement.
See Chapter 12, Benchmarking, for more on this general topic.
