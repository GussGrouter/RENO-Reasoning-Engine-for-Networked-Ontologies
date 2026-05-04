# network-algorithmics-5-2-2-using-copy-on-write-while-the-basic-idea-in-the-witless-approach-can-be (chunk 000001)

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
