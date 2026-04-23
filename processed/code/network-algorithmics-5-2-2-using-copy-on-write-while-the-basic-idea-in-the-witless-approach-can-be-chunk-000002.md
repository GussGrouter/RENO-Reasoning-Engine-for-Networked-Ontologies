# network-algorithmics-5-2-2-using-copy-on-write-while-the-basic-idea-in-the-witless-approach-can-be (chunk 000002)

For any virtual address, the high-order bits (e.g., 20 bits) form the page number, and the low-order
bits (e.g., 12 bits) form the location within a page. Main memory is also divided into physical pages
such that (say) every group of 212 memory words is a physical page. Recall that a virtual address is
mapped to a physical address by mapping the corresponding VP to a physical page number by looking
up a page table indexed by the VP number. If the desired page is not memory resident, the hardware
generates an exception that causes the operating system to read the page from disk into main memory.
Recall also that the overhead of reading page tables from memory can be avoided in the common case
using a TLB (translation look-aside buffer), which is a processor resident cache.
    Looking under the hood, VM is the basis for the COW scheme. Suppose virtual page X is pointing to
a physical memory–resident page P . Suppose that the operating system wishes to replicate the contents
of X onto a new VP, Y . The hard way to do this would be to allocate a new physical page, P  , to copy
the contents of P to P  , and then to point Y to P  in the page table. The simpler way, embodied in
COW, is to map the new VP, Y , back to the old physical page, P , by changing a page table entry. Since
most modern operating systems use large page sizes, changing a page table entry is more efficient than
copying from one physical page to another.
    In addition, the kernel also sets a COW protection bit as part of the page table entry for the original
VP, X. If the application tries to write to page X, the hardware will access the page table for X, notice
the bit set, and generate an exception that calls the operating system. At this point the operating system
will copy the physical page, P , to another location, P  , and then make X point to P  , after clearing
the COW bit. Y continues to point to the old physical page, P . While this is every bit as expensive as

5.2 Reducing copying via local restructuring            119

FIGURE 5.4
Basic operations involved in making a copy of a page using VM.

physical page copying, the point is that this expense is incurred only in the (hopefully) rare case when
an application writes to a COW page.
    The explanation of how COW works should present the following opportunity. While operating
systems such as UNIX and Windows do not offer COW, they still offer VM. VM presents a level of
indirection that can be exploited by changing page table entries to finesse physical copying. Thus much
of the core idea behind Fig. 5.3 can be reused in most operating systems. All that remains is to find an
alternate way to protect against application Writes in place of COW protection.
