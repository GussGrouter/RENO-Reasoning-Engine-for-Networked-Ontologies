8.3.3

Random vs. Sequential I/O

A series of logical file system I/O can be described as random or sequential, based on the file offset
of each I/O. With sequential I/O, each I/O offset begins at the end of the previous I/O. Random
I/O have no apparent relationship between them, and the offset changes randomly. A random
file system workload may also refer to accessing many different files at random.

363

364

Chapter 8 File Systems

Figure 8.4 Sequential and random file I/O
Figure 8.4 illustrates these access patterns, showing an ordered series of I/O and example file
offsets.
Due to the performance characteristics of certain storage devices (described in Chapter 9, Disks),
file systems have historically attempted to reduce random I/O by placing file data on disk
sequentially and contiguously. The term fragmentation describes what happens file systems do
this poorly, causing files to be scattered over a drive, so that sequential logical I/O yields random
physical I/O.
File systems may measure logical I/O access patterns so that they can identify sequential workloads, and then improve their performance using prefetch or read-ahead. This is helpful for
rotational disks; less so for flash drives.

8.3.4

Prefetch

A common file system workload involves reading a large amount of file data sequentially, for
example, for a file system backup. This data may be too large to fit in the cache, or it may be read
only once and is unlikely to be retained in the cache (depending on the cache eviction policy).
Such a workload would perform relatively poorly, as it would have a low cache hit ratio.
Prefetch is a common file system feature for solving this problem. It can detect a sequential read
workload based on the current and previous file I/O offsets, and then predict and issue disk reads
before the application has requested them. This populates the file system cache, so that if the
application does perform the expected read, it results in a cache hit (the data needed was already
in the cache). An example scenario is as follows:
1. An application issues a file read(2), passing execution to the kernel.
2. The data is not cached, so the file system issues the read to disk.
3. The previous file offset pointer is compared to the current location, and if they are
sequential, the file system issues additional reads (prefetch).
4. The first read completes, and the kernel passes the data and execution back to the
application.
5. Any prefetch reads complete, populating the cache for future application reads.
6. Future sequential application reads complete quickly via the cache in RAM.
This scenario is also illustrated in Figure 8.5, where application reads to offsets 1 and then 2
trigger prefetch of the next three offsets.

8.3

Concepts

Figure 8.5 File system prefetch
When prefetch detection works well, applications show significantly improved sequential read
performance; the disks keep ahead of application requests (provided they have the bandwidth
to do so). When prefetch detection works poorly, unnecessary I/O is issued that the application
does not need, polluting the cache and consuming disk and I/O transport resources. File systems
typically allow prefetch to be tuned as needed.
