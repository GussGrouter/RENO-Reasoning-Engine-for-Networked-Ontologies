7.2.3

Demand Paging

Operating systems that support demand paging (most do) map pages of virtual memory to physical memory on demand, as shown in Figure 7.2. This defers the CPU overhead of creating the
mappings until they are actually needed and accessed, instead of at the time a range of memory
is first allocated.

Figure 7.2 Page fault example
The sequence shown in Figure 7.2 begins with a malloc() (step 1) that provides allocated memory,
and then a store instruction (step 2) to that newly allocated memory. For the MMU to determine
the main memory location of the store, it performs a virtual to physical lookup (step 3) for the
page of memory, which fails as there is not yet a mapping. This failure is termed a page fault (step 4),
which triggers the kernel to create an on-demand mapping (step 5). Sometime later, the page of
memory could be paged out to the swap devices to free up memory (step 6).
Step 2 could also be a load instruction in the case of a mapped file, which should contain data
but isn’t yet mapped to this process address space.
If the mapping can be satisfied from another page in memory, it is called a minor fault. This may
occur for mapping a new page from available memory, during memory growth of the process (as
pictured). It can also occur for mapping to another existing page, such as reading a page from a
mapped shared library.

Page faults that require storage device access (not shown in this figure), such as accessing an
uncached memory-mapped file, are called major faults.
The result of the virtual memory model and demand allocation is that any page of virtual memory
may be in one of the following states:
A. Unallocated
B. Allocated, but unmapped (unpopulated and not yet faulted)
C. Allocated, and mapped to main memory (RAM)
D. Allocated, and mapped to the physical swap device (disk)
State (D) is reached if the page is paged out due to system memory pressure. A transition from (B)
to (C) is a page fault. If it requires disk I/O, it is a major page fault; otherwise, a minor page fault.
From these states, two memory usage terms can also be defined:
■

Resident set size (RSS): The size of allocated main memory pages (C)

■

Virtual memory size: The size of all allocated areas (B + C + D)

Demand paging was added to Unix via BSD, along with paged virtual memory. It has become the
standard and is used by Linux.

