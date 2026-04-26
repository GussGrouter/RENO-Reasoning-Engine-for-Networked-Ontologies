7.3.3 (continued) — jemalloc (book overview)

jemalloc
Originating as the FreeBSD user-level libc allocator, libjemalloc is also available for Linux. It
uses techniques such as multiple arenas, per-thread caching, and small object slabs to improve
scalability and reduce memory fragmentation. It can use both mmap(2) and sbrk(2) to obtain
system memory, preferring mmap(2). Facebook use jemalloc and have added profiling and other
optimizations [Facebook 11].
