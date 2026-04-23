8.3.8

Raw and Direct I/O

These are other types of I/O that an application may use, if supported by the kernel or file system:
Raw I/O is issued directly to disk offsets, bypassing the file system altogether. It has been used
by some applications, especially databases, that can manage and cache their own data better
than the file system cache. A drawback is more complexity in the software, and administration
difficulties: the regular file system toolset can’t be used for backup/restore or observability.
Direct I/O allows applications to use a file system but bypass the file system cache, for example, by using the O_DIRECT open(2) flag on Linux. This is similar to synchronous writes (but
without the guarantees that O_SYNC offers), and it works for reads as well. It isn’t as direct as
raw device I/O, since mapping of file offsets to disk offsets must still be performed by file system
code, and I/O may also be resized to match the size used by the file system for on-disk layout (its
record size) or it may error (EINVAL). Depending on the file system, this may not only disable
read caching and write buffering but may also disable prefetch.

8.3.9

Non-Blocking I/O

Normally, file system I/O will either complete immediately (e.g., from cache) or after waiting
(e.g., for disk device I/O). If waiting is required, the application thread will block and leave CPU,

8.3

Concepts

allowing other threads to execute while it waits. While the blocked thread cannot perform
other work, this typically isn’t a problem since multithreaded applications can create additional
threads to execute while some are blocked.
In some cases, non-blocking I/O is desirable, such as when avoiding the performance or resource
overhead of thread creation. Non-blocking I/O may be performed by using the O_NONBLOCK
or O_NDELAY flags to the open(2) syscall, which cause reads and writes to return an EAGAIN
error instead of blocking, which tells the application to try again later. (Support for this depends
on the file system, which may honor non-blocking only for advisory or mandatory file locks.)
The OS may also provide a separate asynchronous I/O interface, such as aio_read(3) and aio_
write(3). Linux 5.1 added a new asynchronous I/O interface called io_uring, with improved ease
of use, efficiency, and performance [Axboe 19].
Non-blocking I/O was also discussed in Chapter 5, Applications, Section 5.2.6, Non-Blocking I/O.

8.3.10 Memory-Mapped Files
For some applications and workloads, file system I/O performance can be improved by mapping
files to the process address space and accessing memory offsets directly. This avoids the syscall
execution and context switch overheads incurred when calling read(2) and write(2) syscalls to
access file data. It can also avoid double copying of data, if the kernel supports directly mapping
the file data buffer to the process address space.
Memory mappings are created using the mmap(2) syscall and removed using munmap(2).
Mappings can be tuned using madvise(2), as summarized in Section 8.8, Tuning. Some applications provide an option to use the mmap syscalls (which may be called “mmap mode”) in their
configuration. For example, the Riak database can use mmap for its in-memory data store.
I’ve noticed a tendency to try using mmap(2) to solve file system performance issues without
first analyzing them. If the issue is high I/O latency from disk devices, avoiding the small syscall
overheads with mmap(2) may accomplish very little, when the high disk I/O latency is still present and dominant.
A disadvantage of using mappings on multiprocessor systems can be the overhead to keep each
CPU MMU in sync, specifically the CPU cross calls to remove mappings (TLB shootdowns).
Depending on the kernel and mapping, these may be minimized by delaying TLB updates (lazy
shootdowns) [Vahalia 96].

8.3.11

Metadata

While data describes the contents of files and directories, metadata describes information about
them. Metadata may refer to information that can be read from the file system interface (POSIX)
or information needed to implement the file system on-disk layout. These are called logical and
physical metadata, respectively.

367

368

Chapter 8 File Systems

Logical Metadata
Logical metadata is information that is read and written to the file system by consumers (applications), either:
■

■

Explicitly: Reading file statistics (stat(2)), creating and deleting files (creat(2), unlink(2))
and directories (mkdir(2), rmdir(2)), setting file properties (chown(2), chmod(2))
Implicitly: File system access timestamp updates, directory modification timestamp
updates, used-block bitmap updates, free space statistics

A workload that is “metadata-heavy” typically refers to logical metadata, for example, web
servers that stat(2) files to ensure they haven’t changed since caching, at a much greater rate
than reading file data contents.

Physical Metadata
Physical metadata refers to the on-disk layout metadata necessary to record all file system
information. The metadata types in use depend on the file system and may include superblocks,
inodes, blocks of data pointers (primary, secondary...), and free lists.
Logical and physical metadata are one reason for the difference between logical and physical I/O.
