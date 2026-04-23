# network-algorithmics-9-1-1-buffer-allocation-the-classical-bsd-unix-implementation-called-mbufs-all (chunk 000002)

Segregated pool allocator
One of the fastest allocators, due to Chris Kingsley, was distributed along with BSD 4.2 UNIX. Kings-
ley’s malloc() implementation splits all of memory into a set of segregated pools of memory in powers
of 2. Any request is rounded up to its closest power of 2, a table lookup is done to find the correspond-
ing pool list, and a buffer is allocated from the head of that list if available. The pools are said to be
segregated because when a request of a certain size fails, there is no attempt made to carve up available
larger buffers or to coalesce contiguous smaller buffers.
    Such carving up and coalescing is actually done by a more classical scheme called the buddy system
(see Wilson et al., 1995 for a thorough review of memory allocators). Refraining from doing so clearly
wastes memory (P4b, trading memory for speed). If all the requests are for exactly one pool size, then
the other pools are wasted. However, this restraint is not as bad as it seems because allocators using the
buddy system have a far more horrible worst case.

214      Chapter 9 Protocol processing

Suppose, for example, that all requests are for size 1 and that every alternate buffer is then deallo-
cated. Then, using the buddy system, memory degenerates into a series of holes of size 1 followed by
an allocation of size 1. Half of the memory is unused, but no request of size greater than 2 can be sat-
isfied. Notice that this example cannot happen with the Kingsley allocator because the size-1 requests
will only deplete the size-1 pool and will not affect the other pools. Thus trafficking between pools may
help improve the expected memory utilization but not the worst-case utilization.

Linux allocator
The Linux allocator (Chelf, 2001), originally written by Doug Lea, is sometimes referred to as dlmal-
loc(). Like the Kingsley allocator, the memory is broken into pools of 128 sizes. The first 64 pools
contain memory buffers of exactly one size each, from 16 through 512 bytes in steps of 8. Unlike the
case of power-of-2 allocation, this prevents more than 8 bytes of waste for the common case of small
buffers. The remaining 64 pools cover the other, higher sizes, spaced exponentially.
    The Linux allocator (Chelf, 2001) does merge adjacent free buffers and promotes the coalesced
buffer to the appropriate pool. This is similar to the buddy system and hence is subject to the same
fragmentation problem of any scheme in which the pools are not segregated. However, the resulting
memory utilization is very good in practice.
    A useful trick to tuck away in your bag of tricks concerns how pools are linked together. The naive
way would be to create separate free lists for each pool using additional small nodes that point to the
corresponding free buffer. But since the buffer is free, this is obvious waste (P1). Thus the simple trick,
used in Linux and possibly in other allocators, is to store the link pointers for the pool free lists in the
corresponding free buffers themselves, thereby saving storage.
    The Lea allocator uses memory more efficiently than the Kingsley allocator but is more complex
to implement. This may not be the best choice for a wire-speed TCP implementation that desires both
speed and the efficient use of memory.
