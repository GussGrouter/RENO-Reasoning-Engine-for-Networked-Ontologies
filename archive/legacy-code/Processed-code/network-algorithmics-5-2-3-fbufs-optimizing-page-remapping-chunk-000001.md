# network-algorithmics-5-2-3-fbufs-optimizing-page-remapping (chunk 000001)

# Network Algorithmics — 5.2.3 Fbufs: optimizing page remapping (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 146
- Slice: from `5.2.3 Fbufs: optimizing page remapping` up to next detected section heading

---

5.2.3 Fbufs: optimizing page remapping
Even ignoring the aspect of protecting against application writes, Fig. 5.4 implies that a large buffer can
be transferred from application to kernel (or vice versa) with a Write to the page table. This simplistic
view of page remapping is somewhat naive and misleading.
    Fig. 5.4 shows a concrete example of page remapping. Suppose the operating system wishes to
make a fast copy of data of Process 1 (say, the application) in VP 10 to some virtual page (e.g., VP 8)
in the page table of Process 2’s (say, the kernel). Naively, this seems to require only changing the page
table entry corresponding to VP 8 in Process 2 to point to the packet data to which that VP table entry
10 in Process 1 already points. However, there are several additional pieces of overhead that are glossed
over by this simple description.
• Multiple-level page tables: Most modern systems use multiple levels of page table mappings because
  it takes too much page table memory to map from, say, 20 bits of a VP. Thus the real mapping may
  require changing mappings in at least a first- and a second-level page table. For portability, there
  are also both machine-independent and machine-dependent tables. Thus there are several Writes
  involved, not just one.
• Acquiring locks and modifying page table entries: Page tables are shared resources and thus must
  be protected using locks that must be acquired and released.
• Flushing translation look-aside buffers (TLBs): As we said earlier, to save translation time, com-
  monly used page table mappings are cached in the TLB. When a new VP location for VP 8 is
  written, any TLB entries for VP 8 must be found and flushed (i.e., removed) or corrected.

120        Chapter 5 Copying data

• Allocating VM in destination domain: While we have assumed that VM location 8 was the location
  for the destination page, some computation must be done to find a free page table entry in the
  destination process before the copy can take place.
• Locking the corresponding pages: Physical pages can be swapped out to disk to make room for other
  VPs currently on disk. To prevent pages from being swapped out, pages have to be locked, which is
  additional overhead.
    All these overheads are exacerbated in multiprocessor and multicore systems. The net result is that
while the page table mapping can seem very good (the mapping seems to take a constant time, indepen-
dent of the size of the packet data), the constant factors (see Q4 in the discussion of caveats) are actually
a big overhead. This was experimentally demonstrated by experiments performed by Druschel and Pe-
terson (1993) in the early 1990s. In the decade that followed, if anything, page mapping overheads have
only increased.
    Druschel and Peterson, however, did not stop with the experiments but invented an operating system
facility called fbufs (short for “fast buffers”), which actually removes most or all of the four sources of
page remapping overhead. Their idea can be described as follows in terms of the principles used in this
book.
