7.3.2

Software

Software for memory management includes the virtual memory system, address translation,
swapping, paging, and allocation. The topics most related to performance are included in this
section: freeing memory, the free list, page scanning, swapping, the process address space, and
memory allocators.

Freeing Memory
When the available memory on the system becomes low, there are various methods that the kernel can use to free up memory, adding it to the free list of pages. These methods are pictured in
Figure 7.6 for Linux, in the general order in which they are used as available memory decreases.
These methods are:
■

■

Free list: A list of pages that are unused (also called idle memory) and available for immediate allocation. This is usually implemented as multiple free page lists, one for each locality
group (NUMA).
Page cache: The file system cache. A tunable parameter called swappiness sets the
degree to which the system should favor freeing memory from the page cache instead
of swapping.

315

316

Chapter 7 Memory

Figure 7.6 Linux memory availability management
■

■

■

Swapping: This is paging by the page-out daemon, kswapd, which finds not recently used
pages to add to the free list, including application memory. These are paged out, which
may involve writing to either a file system-based swap file or a swap device. Naturally, this
is available only if a swap file or device has been configured.
Reaping: When a low-memory threshold is crossed, kernel modules and the kernel slab
allocator can be instructed to immediately free any memory that can easily be freed. This
is also known as shrinking.
OOM killer: The out-of-memory killer will free memory by finding and killing a sacrificial
process, found using select_bad_process() and then killed by calling oom_kill_process().
This may be logged in the system log (/var/log/messages) as an “Out of memory: Kill process” message.

