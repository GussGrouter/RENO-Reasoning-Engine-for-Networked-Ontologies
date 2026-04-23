7.6.1 Tunable Parameters
This section describes tunable parameter examples for recent Linux kernels.
Various memory tunable parameters are described in the kernel source documentation in
Documentation/sysctl/vm.txt and can be set using sysctl(8). The examples in Table 7.7 are from
a 5.3 kernel, with defaults from Ubuntu 19.10 (those listed in the first edition of this book have
not changed since then).

**(Table 7.7 omitted here — example Linux `vm.*` / `kernel.*` tunable grid; see `Documentation/sysctl/vm.txt` and the book PDF.)**

The tunables use a consistent naming scheme that includes the units. Note that dirty_
background_bytes and dirty_background_ratio are mutually exclusive, as are dirty_bytes and
dirty_ratio (when one is set it overrides the other).

The size of vm.min_free_kbytes is set dynamically as a fraction of main memory. The algorithm
to choose this is not linear, as needs for free memory do not linearly scale with main memory size.
(For reference, this is documented in the Linux source in mm/page_alloc.c.) vm.min_free_kbytes
can be reduced to free up some memory for applications, but that can also cause the kernel to be
overwhelmed during memory pressure and resort to using OOM sooner. Increasing it can help
avoid OOM kills.
Another parameter for avoiding OOM is vm.overcommit_memory, which can be set to 2 to
disable overcommit and avoid cases where this leads to OOM. If you want to control the OOM
killer on a per-process basis, check your kernel version for /proc tunables such as oom_adj or
oom_score_adj. These are described in Documentation/filesystems/proc.txt.
The vm.swappiness tunable can significantly affect performance if it begins swapping application memory earlier than desired. The value of this tunable can be between 0 and 100, with high
values favoring swapping applications and therefore retaining the page cache. It may be desirable to set this to zero, so that application memory is retained as long as possible at the expense
of the page cache. When there is still a memory shortage, the kernel can still use swapping.
At Netflix, kernel.numa_balancing was set to zero for earlier kernels (around Linux 3.13) because
overly aggressive NUMA scanning consumed too much CPU [Gregg 17d]. This was fixed in
later kernels, and there are other tunables including kernel.numa_balancing_scan_size_mb for
adjusting the aggressiveness of NUMA scanning.

