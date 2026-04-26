Slab allocation has been adopted by various operating systems. BSD has a kernel slab allocator
called the universal memory allocator (UMA), which is efficient and NUMA-aware. A slab allocator was also introduced to Linux in version 2.2, where it was the default option for many years.
Linux has since moved to SLUB as an option or as the default.

SLUB
The Linux kernel SLUB allocator is based on the slab allocator and is designed to address various
concerns, especially regarding the complexity of the slab allocator. Improvements include the
removal of object queues, and per-CPU caches—leaving NUMA optimization to the page allocator (see the earlier Free List(s) section).
The SLUB allocator was made the default option in Linux 2.6.23 [Lameter 07].
