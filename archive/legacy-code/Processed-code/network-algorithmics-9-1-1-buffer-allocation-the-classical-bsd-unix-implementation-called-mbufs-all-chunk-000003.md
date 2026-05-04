# network-algorithmics-9-1-1-buffer-allocation-the-classical-bsd-unix-implementation-called-mbufs-all (chunk 000003)

Batch allocator
One alternative idea for memory allocation, which has an even simpler hardware implementation than
Kingsley’s allocator, leverages batching (P2c). The idea, shown in Fig. 9.1, is for the allocator to work in
large chunks of memory. Each chunk is allocated sequentially. A pointer Curr is kept to the point where
the last allocation is terminated. A new request of size B is allocated after Curr, and Curr increases to
Curr + B. This is extremely fast, handles variable sizes, and does not waste any memory—up to the
point, that is, when the chunk is used up.
    The idea is that when the chunk is used up, another chunk is immediately available. Of course,
there is no free lunch, while the second chunk is being used, some spare chunk must be created in
the background. The creation of this spare chunk can be done by software, while allocates can easily
be done in hardware. Similar ideas were presented in the context of the MIT J-machine (Dally et al.,
1987), which relied on an underlying fast messaging service.
    Creating a spare chunk can be done in many ways. The problem, of course, is that deallocates may
not be done in the same order as allocates, thus creating a set of holes in the chunks that need somehow
to be coalesced. Three alternatives for coalescing present themselves. If the application knows that
eventually all allocated buffers will be freed, then using some more spare chunks may suffice to ensure
that before any chunk runs out, some chunk will be completely scavenged. However, this is a dangerous
game.

9.1 Buffer management                   215

FIGURE 9.1
Sequentially allocating from a large chunk and using a spare chunk. The magic comes from using the time it takes to
completely allocate a chunk to create a new chunk.

Second, if memory is accessed through a level of indirection, as in virtual memory, and the buffers
are allocated in virtual memory, it is possible to use page remapping to gather together many scattered
physical memory pages to appear as one contiguous virtual memory chunk. Finally, it may be worth
considering compaction. Compaction is clearly unacceptable in a general-purpose allocator like UNIX,
where any number of pieces of memory may point to a memory node. However, in network applications
using buffers or other treelike structures, compaction may be feasible using simple local compaction
schemes (Sikka and Varghese, 2000).

9.1.2 Sharing buffers
If buffer allocation was not hard enough, consider making it harder by asking also for a fairness con-
straint.2 Imagine that an implementation wishes to fairly share a group of buffers among a number of
users, each of whom may wish to use all the buffers. The buffers should be shared roughly equally
among the active users that need these buffers. This is akin to what in economics is called Pareto op-
timality and also to the requirements for fair queuing in routers studied in Chapter 14. Thus it is not
surprising that the following buffer-stealing algorithm was invented (McKenney, 1991) in the context
of a stochastic fair queuing (SFQ) algorithm.
