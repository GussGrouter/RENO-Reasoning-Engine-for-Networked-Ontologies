7.3.2 (continued) — Free lists, reaping, page scanning

Free List(s)
The original Unix memory allocator used a memory map and a first-fit scan. With the introduction of paged virtual memory in BSD, a free list and a page-out daemon were added [Babaoglu 79].
The free list, pictured in Figure 7.7, allows available memory to be located immediately.

Figure 7.7 Free list operations
Memory freed is added to the head of the list for future allocations. Memory that is freed by the
page-out daemon—and that may still contain useful cached file system pages—is added to the
tail. Should a future request for one of these pages occur before the useful page has been reused,
it can be reclaimed and removed from the free list.
A form of free list is still in use by Linux-based systems, as pictured in Figure 7.6. Free lists are
typically consumed via allocators, such as the slab allocator for the kernel, and libc malloc() for
user-space (which has its own free lists). These in turn consume pages and then expose them via
their allocator API.
Linux uses the buddy allocator for managing pages. This provides multiple free lists for differentsized memory allocations, following a power-of-two scheme. The term buddy refers to finding
neighboring pages of free memory so that they can be allocated together. For historical background, see [Peterson 77].
The buddy free lists are at the bottom of the following hierarchy, beginning with the per-memory node pg_data_t:
■

■

4

Nodes: Banks of memory, NUMA-aware
Zones: Ranges of memory for certain purposes (direct memory access [DMA],4 normal,
highmem)

■

Migration types: Unmovable, reclaimable, movable, etc.

■

Sizes: Power-of-two number of pages

Although ZONE_DMA may be removed [Corbet 18a].

Allocating within the node free lists improves memory locality and performance. For the most
common allocation, single pages, the buddy allocator keeps lists of single pages for each CPU to
reduce CPU lock contention.

Reaping
Reaping mostly involves freeing memory from the kernel slab allocator caches. These caches
contain unused memory in slab-size chunks, ready for reuse. Reaping returns this memory to
the system for page allocations.
On Linux, kernel modules can also call register_shrinker() to register specific functions for
reaping their own memory.

Page Scanning
Freeing memory by paging is managed by the kernel page-out daemon. When available main
memory in the free list drops below a threshold, the page-out daemon begins page scanning. Page
scanning occurs only when needed. A normally balanced system may not page scan very often
and may do so only in short bursts.
On Linux, the page-out daemon is called kswapd, which scans LRU page lists of inactive and
active memory to free pages. It is woken up based on free memory and two thresholds to provide
hysteresis, as shown in Figure 7.8.

Figure 7.8 kswapd wake-ups and modes
Once free memory has reached the lowest threshold, kswapd runs in the foreground, synchronously freeing pages of memory as they are requested, a method sometimes known as directreclaim [Gorman 04]. This lowest threshold is tunable (vm.min_free_kbytes), and the others are
scaled based on it (by 2x for low, 3x for high). For workloads with high allocation bursts that
outpace kswap reclamation, Linux provides additional tunables for more aggressive scanning,
vm.watermark_scale_factor and vm.watermark_boost_factor: see Section 7.6.1, Tunable
Parameters.
The page cache has separate lists for inactive pages and active pages. These operate in an LRU fashion, allowing kswapd to find free pages quickly. They are shown in Figure 7.9.

Figure 7.9 kswapd lists
kswapd scans the inactive list first, and then the active list, if needed. The term scanning refers
to checking of pages as the list is walked: a page may be ineligible to be freed if it is locked/dirty.
The term scanning as used by kswapd has a different meaning than the scanning done by the
original UNIX page-out daemon, which scans all of memory.
