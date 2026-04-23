8.4.3

File System Caches

Unix originally had only the buffer cache to improve the performance of block device access.
Nowadays, Linux has multiple different cache types. Figure 8.8 gives an overview of file system
caches on Linux, showing generic caches available for standard file system types.

Figure 8.8 Linux file system caches

373

374

Chapter 8 File Systems

Buffer Cache
Unix used a buffer cache at the block device interface to cache disk device blocks. This was a separate, fixed-size cache and, with the later addition of the page cache, presented tuning problems
when balancing different workloads between them, as well as the overheads of double caching
and synchronization. These problems have largely been addressed by using the page cache to
store the buffer cache, an approach introduced by SunOS and called the unified buffer cache.
Linux originally used a buffer cache as with Unix. Since Linux 2.4, the buffer cache has also
been stored in the page cache (hence the dotted border in Figure 8.8) avoiding the double
caching and synchronization overhead. The buffer cache functionality still exists, improving
the performance of block device I/O, and the term still appears in Linux observability tools
(e.g., free(1)).
The size of the buffer cache is dynamic and is observable from /proc.

Page Cache
The page cache was first introduced to SunOS during a virtual memory rewrite in 1985 and
added to SVR4 Unix [Vahalia 96]. It cached virtual memory pages, including mapped file system
pages, improving the performance of file and directory I/O. It was more efficient for file access
than the buffer cache, which required translation from file offset to disk offset for each lookup.
Multiple file system types could use the page cache, including the original consumers UFS and
NFS. The size was dynamic: the page cache would grow to use available memory, freeing it again
when applications needed it.
Linux has a page cache with the same attributes. The size of the Linux page cache is also
dynamic, with a tunable to set the balance between evicting from the page cache and swapping
(swappiness; see Chapter 7, Memory).
Pages of memory that are dirty (modified) and are needed for use by a file system are flushed
to disk by kernel threads. Prior to Linux 2.6.32, there was a pool of page dirty flush (pdflush)
threads, between two and eight as needed. These have since been replaced by the flusher threads
(named flush), which are created per device to better balance the per-device workload and
improve throughput. Pages are flushed to disk for the following reasons:
■

After an interval (30 seconds)

■

The sync(2), fsync(2), msync(2) system calls

■

Too many dirty pages (the dirty_ratio and dirty_bytes tunables)

■

No available pages in the page cache

If there is a system memory deficit, another kernel thread, the page-out daemon (kswapd, also
known as the page scanner), may also find and schedule dirty pages to be written to disk so that it
can free the memory pages for reuse (see Chapter 7, Memory). For observability, the kswapd and
flush threads are visible as kernel tasks from operating system performance tools.
See Chapter 7, Memory, for more details about the page scanner.

