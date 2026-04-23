# network-algorithmics-2-4-2-virtual-memory (chunk 000002)

anisms of page table mapping and demand paging. Both these mechanisms are crucial to understand in
order to optimize data transfer costs in an endnode.
    Any virtual address must be mapped to a physical memory address. The easiest mapping is to use
an offset into physical memory. For example, a virtual array of 15,000 locations could be mapped into
physical memory from, say, 12,000 to 27,000. This has two disadvantages. First, when the program
runs, a block of 15,000 contiguous locations has to be found. Second, the programmer is limited to
using a total memory equal to the size of physical memory.
    Both problems can be avoided by a mapping based on table lookup. Since it takes too much memory
to implement a mapping from any virtual location to any physical location, a more restricted mapping
based on pages is used. Thus for any virtual address, let us say that the high-order bits (e.g., 20 bits)
form the page number and that the low-order bits (e.g., 12 bits) form the location within a page. All
locations within a virtual page are mapped to the same relative location, but individual virtual pages
can be mapped to arbitrary locations. Main memory is also divided into physical pages, such that every
group of 212 memory words is a physical page.
    To map a virtual into a physical address, the corresponding virtual page (i.e., high-order 20 bits) is
mapped to a physical page number while retaining the same location within the page. The mapping is
done by looking up a page table indexed by the virtual page number. A virtual page can be located on
any physical memory page. More generally, some pages (e.g., Virtual Page 2 in Fig. 2.13) may not be
memory resident and can be marked as being on disk. When such a page is accessed, the hardware will
generate an exception and cause the operating system to read the page from the disk page into a main
memory page. This second mechanism is called demand paging.
    Together, page mapping and demand paging solve the two problems of storage allocation and
bounded memory allocations. Instead of solving the harder variable size storage allocation problem,
the OS needs only to keep a list of fixed size free pages and to assign some free pages to a new pro-
gram. Also, the programmer can work with an abstraction of memory whose size is bounded only by
the size of the disk and the number of instruction address bits.
    The extra mapping can slow down each instruction considerably. A Read to virtual location X may
require two main memory accesses: a page table access to translate X to physical address P , followed
by a Read to address P . Modern processors get around this overhead by caching the most recently used
mappings between virtual and physical addresses in a translation look-aside buffer (TLB), which is
a processor-resident cache. The actual translation is done by a piece of hardware called the memory
management unit (MMU), as shown in Fig. 2.8.
    The page table mapping also provides a mechanism for protection between processes. When a
process makes a Read to virtual location X, unless there is a corresponding entry in the page table, the
hardware will generate a page fault exception. By ensuring that only the operating system can change
page table entries, the operating system can ensure that one process cannot read from or write to the
memory of another process in an unauthorized fashion.
    While router forwarding works directly on physical memory, all endnode and server networking
code works on virtual memory. While virtual memory is a potential cost (e.g., for TLB misses), it
also reflects a possible opportunity. For example, it offers the potential for packet copying between the
operating system and the application (see Example 8) to be done more efficiently by manipulating page
tables. This idea is explored further in Chapter 5.
