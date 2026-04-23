Allocators
There are a variety of user- and kernel-level allocators for memory allocation. Figure 7.11 shows
the role of allocators, including some common types.
6

Larger than the M_TRIM_THRESHOLD mallopt(3) parameter, which is 128 Kbytes by default.

Figure 7.11 User- and kernel-level memory allocators
Page management was described earlier in Section 7.3.2, Software, under Free List(s).
Memory allocator features can include:
■

■

■

■

Simple API: For example, malloc(3), free(3).
Efficient memory usage: When servicing memory allocations of a variety of sizes, memory usage can become fragmented, where there are many unused regions that waste memory.
Allocators can strive to coalesce the unused regions, so that larger allocations can make
use of them, improving efficiency.
Performance: Memory allocations can be frequent, and on multithreaded environments
they can perform poorly due to contention for synchronization primitives. Allocators can
be designed to use locks sparingly, and can also make use of per-thread or per-CPU caches
to improve memory locality.
Observability: An allocator may provide statistics and debug modes to show how it is
being used, and which code paths are responsible for allocations.

The sections that follow describe kernel-level allocators—slab and SLUB—and user-level
allocators—glibc, TCMalloc, and jemalloc.
