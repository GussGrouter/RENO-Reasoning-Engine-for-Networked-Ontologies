8.3.5 Read-Ahead
Historically, prefetch has also been known as read-ahead. Linux uses the read-ahead term for a
system call, readahead(2), that allows applications to explicitly warm up the file system cache.

8.3.6

Write-Back Caching

Write-back caching is commonly used by file systems to improve write performance. It works by
treating writes as completed after the transfer to main memory, and writing them to disk sometime later, asynchronously. The file system process for writing this “dirty” data to disk is called
flushing. An example sequence is as follows:
1. An application issues a file write(2), passing execution to the kernel.
2. Data from the application address space is copied to the kernel.
3. The kernel treats the write(2) syscall as completed, passing execution back to the
application.
4. Sometime later, an asynchronous kernel task finds the written data and issues disk writes.
The trade-off is reliability. DRAM-based main memory is volatile, and dirty data can be lost in
the event of a power failure. Data could also be written to disk incompletely, leaving a corrupted
on-disk state.
If file system metadata becomes corrupted, the file system may no longer load. Such a state may
be recoverable only from system backups, causing prolonged downtime. Worse, if the corruption
affects file contents that the application reads and uses, the business may be in jeopardy.
To balance needs for both speed and reliability, file systems can offer write-back caching by
default, and a synchronous write option to bypass this behavior and write directly to persistent
storage devices.

365

366

Chapter 8 File Systems

8.3.7 Synchronous Writes
A synchronous write completes only when fully written to persistent storage (e.g., disk devices),
which includes writing any file system metadata changes that are necessary. These are much
slower than asynchronous writes (write-back caching), since synchronous writes incur disk
device I/O latency (and possibly multiple I/O due to file system metadata). Synchronous writes
are used by some applications such as database log writers, where the risk of data corruption
from asynchronous writes is unacceptable.
There are two forms of synchronous writes: individual I/O, which is written synchronously, and
groups of previous writes, which are synchronously committed.

Individual Synchronous Writes
Write I/O is synchronous when a file is opened using the flag O_SYNC or one of the variants,
O_DSYNC and O_RSYNC (which as of Linux 2.6.31 are mapped by glibc to O_SYNC). Some file
systems have mount options to force all write I/O to all files to be synchronous.

Synchronously Committing Previous Writes
Rather than synchronously writing individual I/O, an application may synchronously commit
previous asynchronous writes at checkpoints in their code, using the fsync(2) system call. This
can improve performance by grouping the writes, and can also avoid multiple metadata updates
by use of write cancellation.
There are other situations that will commit previous writes, such as closing file handles, or when
there are too many uncommitted buffers on a file. The former is often noticeable as long pauses
when unpacking an archive of many files, especially over NFS.
