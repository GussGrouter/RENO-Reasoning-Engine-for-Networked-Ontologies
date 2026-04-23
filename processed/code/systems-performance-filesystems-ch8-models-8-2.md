8.2 Models

8.2

Models

The following simple models illustrate some basic principles of file systems and their performance.

8.2.1

File System Interfaces

A basic model of a file system is shown in Figure 8.1, in terms of its interfaces.

Figure 8.1 File system interfaces
The locations where logical and physical operations occur are also labeled in the figure. See
Section 8.3.12, Logical vs. Physical I/O, for more about these.
Figure 8.1 shows generic object operations. Kernels may implement additional variants: for
example, Linux provides readv(2), writev(2), openat(2), and more.
One approach for studying file system performance is to treat it as a black box, focusing on
the latency of the object operations. This is explained in more detail in Section 8.5.2, Latency
Analysis.

8.2.2

File System Cache

A generic file system cache stored in main memory is pictured in Figure 8.2, servicing a read
operation.
The read returns data either from cache (cache hit) or from disk (cache miss). Cache misses are
stored in the cache, populating the cache (warming it up).
The file system cache may also buffer writes to be written (flushed) later. The mechanisms for
doing this differ for different file system types, and are described in Section 8.4, Architecture.
Kernels often provide a way to bypass the cache if desired. See Section 8.3.8, Raw and Direct I/O.

361

362

Chapter 8 File Systems

Figure 8.2 File system main memory cache

8.2.3

Second-Level Cache

Second-level cache may be any memory type; Figure 8.3 shows it as flash memory. This cache
type was first developed by myself in 2007, for ZFS.

Figure 8.3 File system second-level cache
