# Network Algorithmics — 5.2.2 Using copy-on-write While the basic idea in the Witless approach can be considered to be eliminating the kernel-to-adaptor (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 144
- Slice: from `5.2.2 Using copy-on-write While the basic idea in the Witless approach can be considered to be eliminating the kernel-to-adaptor` up to next detected section heading

---

5.2.2 Using copy-on-write
While the basic idea in the Witless approach can be considered to be eliminating the kernel-to-adaptor
copy, the alternate idea pursued in the next three subsections is to eliminate the application-to-kernel
copy (in most cases) using VM remappings. Recall that one reason for the separate copy was the
possibility that the application would modify the buffer and hence violate TCP semantics. A second
reason is that the application and kernel use different virtual address spaces.
    Some operating systems (notably Mach) offer a facility called copy-on-write (COW) that allows a
process to replicate a virtual page (VP) in memory at low cost. The idea is to make the copy point to
the original physical page P from which it was copied. This only involves updating a few descriptors
(a few words of memory) instead of copying a whole packet (say, 1500 bytes of data). However, the
nice thing about COW is that if the original owner of the data modifies the data, the OS will detect this
condition automatically and generate two separate physical copies, P and P  . The original owner now
points to P and can make modifications on P ; the owner of the copied page points to the old copy, P  .
This works fine if the vast majority of times pages are not modified (or only a few pages are modified)
by the original owner.
    Thus in a COW system, the application could make a COW copy for the kernel. In the hopefully rare
event that the application modifies its buffer, the kernel makes a (expensive) physical copy. However,
that should be uncommon. Clearly, we are using lazy evaluation (P2b) to minimize overhead in the
expected case (P11). Finally, in Fig. 5.3 the checksum can be piggybacked either with the copy to or
from adaptor memory or by using CRC hardware on the adaptor.
    Unfortunately, many operating systems, such as UNIX2 and Windows, do not offer COW. However,
much of the same effect can be obtained by understanding the basis behind the COW service, which is
the use of VM.

Implementing copy-on-write
Recall from Chapter 2 that most modern computers use VM. Recall that the programmer works with
an abstraction of infinite memory that is a linear array into which she (or more accurately her compiler)
assigns variable locations, so, say, location X would be location 1010 in this imaginary (or virtual)
array. These virtual addresses are then mapped into physical memory (which can reside on disk or in
main memory) using a page table (Chapter 2).


2 System V UNIX does implement COW when a process is forked. The pages shared between the child and the parent process
are shared with the COW bit set.

118      Chapter 5 Copying data




FIGURE 5.3
Using COW.


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
