# Network Algorithmics — 11.13 Memory allocation in compressed schemes (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 310
- Slice: from `11.13 Memory allocation in compressed schemes` up to next detected section heading

---

11.13 Memory allocation in compressed schemes
With the exception of binary search and fixed-stride multibit tries, many of the schemes described in
this chapter need to allocate memory in different sizes. Thus if a compressed trie node grows from
two to three memory words, the insertion algorithm must deallocate the old node of size 2 and allocate
a new node of size 3. Memory allocation in operating systems is a somewhat heuristic affair, using
algorithms, such as best-fit and worst-fit, that do not guarantee worst-case properties.
    In fact, all standard memory allocators can have a worst-case fragmentation ratio that is very bad. It
is possible for allocates and deallocates to conspire to break up memory into a patchwork of holes and
small allocated blocks. Specifically, if Max is the size of the largest memory allocation request, the
worst-case scenario occurs when all holes are of size Max − 1 and all allocated blocks are of size 1.
This can occur by allocating all of the memory using requests of size 1, followed by the appropriate
                                              1
deallocations. The net result is that only Max    of memory is guaranteed to be used, because all future
requests may be of size Max.
    The allocator’s use of memory translates directly into the maximum number of prefixes that a lookup
chip can support. Suppose that—ignoring the allocator—one can show that 20 MB of on-chip memory
can be used to support 640,000 prefixes in the worst case. If one takes the allocator into account and
Max = 32, the chip can guarantee supporting only 20,000 prefixes!

284      Chapter 11 Prefix-match lookups



    Matters are not helped by the fact that CAM vendors at the time of writing were advertising a
worst-case number of 100,000 prefixes, with 10-nanoseconds search times and microsecond update
times. Thus, given that algorithmic solutions to prefix lookup often compress data structures to fit into
SRAM, algorithmic solutions must also design memory allocators that are fast and that minimally
fragment memory.
    There is an old result (Robson, 1974) that says that no allocator that does not compact memory
can have a utilization ratio better than log 1Max . For example, this is 20% for Max = 32. Since this is
                                            2
unacceptable, algorithmic solutions involving compressed data structures must use compaction. Com-
paction means moving allocated blocks around to increase the size of holes.
    Compaction is hardly ever used in operating systems for the following reason. If you move a piece of
memory M, you must correct all pointers that point to M. Fortunately, most lookup structures are trees,
in which any node is pointed to by at most one other node. By maintaining a parent pointer for every
tree node, nodes that point to a tree node M can be suitably corrected when M is relocated. Fortunately,
the parent pointer is needed only for updates and not for search. Thus the parent pointers can be stored
in an off-chip copy of the database used for updates in the route processor, without consuming precious
on-chip SRAM.
    Even after this problem is solved, one needs a simple algorithm that decides when to compact a
piece of memory. The existing literature on compaction is in the context of garbage collection (e.g.,
Refs. Wilson, 1992; Lai and Baker, 1996) and tends to use global compactors that scan through all
of the memory in one compaction cycle. To bound insertion times, one needs some form of local
compactor that compacts only a small amount of memory around the region affected by an update.
