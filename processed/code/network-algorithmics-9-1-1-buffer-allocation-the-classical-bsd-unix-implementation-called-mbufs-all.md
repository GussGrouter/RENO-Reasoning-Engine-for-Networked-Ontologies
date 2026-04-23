# Network Algorithmics — 9.1.1 Buffer allocation The classical BSD UNIX implementation, called mbufs, allowed a single packet to be stored as a linear (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 239
- Slice: from `9.1.1 Buffer allocation The classical BSD UNIX implementation, called mbufs, allowed a single packet to be stored as a linear` up to next detected section heading

---

9.1.1 Buffer allocation
The classical BSD UNIX implementation, called mbufs, allowed a single packet to be stored as a linear
list of smaller buffers, where a buffer is a contiguous area of memory.1 The motivation for this technique

1 Craig Partridge attributes the invention of mbufs to Rob Gurwitz (Partridge et al., 2004).

                                                                  9.1 Buffer management             213



is to allow the space allocated to the packet to grow and shrink (for example, as it passes up and down
the stack). For instance, it is easy to grow a packet by prepending a new mbuf to the current chain of
mbufs. For even more flexibility, BSD mbufs come in three flavors: two small sizes (100 and 108 bytes)
and one large size (2048 bytes, called a cluster).
    Besides allowing dynamic expansion of a packet’s allocated memory, mbufs make efficient use
of memory, something that was important around 1981, when mbufs were invented. For example, a
packet of 190 bytes would be allocated two mbufs (wasting around 20 bytes), while a packet of 450
bytes would be allocated five mbufs (wasting around 50 bytes).
    However, dynamic expansion of a packet’s size may be less important than it sounds because the
header sizes for important packet paths (e.g., Ethernet, IP, TCP) are well known and can be preallocated.
Similarly, saving memory may be less important in workstations today than increasing the speed of
packet processing. On the other hand, the mbuf implementation makes accessing and copying data
much harder because it may require traversing the list.
    Thus very early on, Van Jacobson designed a prototype kernel that used what we called pbufs. As
Jacobson puts it in an email note (Jacobson, 1993): “There is exactly one, contiguous, packet per pbuf
(none of that mbuf chain stupidity).”
    While pbufs have sunk into oblivion, the Linux operating system currently uses a very similar idea
(Cox, 1996) for network buffers called sk_buf. These buffers, like pbufs, are linear buffers with space
saved in advance for any packet headers that need to be added later. At times, this will incur wasted
space to handle the worst-case headers, but the simpler implementation makes this worthwhile. Both
sk_bufs and pbufs relax the specification of a buffer to avoid unnecessary generality (P7) and trade
memory for time (P4b).
    Given that the use of linear buffer sizes, as in Linux, is a good idea, how do we allocate memory for
packets of various sizes? Dynamic memory allocation is a hard problem in general because users (e.g.,
TCP connections) deallocate at different times, and these deallocations can fragment memory into a
patchwork of holes of different sizes.
    The standard textbook algorithms, such as First-Fit and Best-Fit (Wilson et al., 1995), effectively
stroll through memory, looking for a hole of the appropriate size. Any implementor of a high-speed net-
working implementation, say, TCP, should be filled with horror at the thought of using such allocators.
Instead, the following three allocators should be considered.

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

Buffer stealing
One way to provide roughly Pareto optimality among users is as follows. When all buffers are used
up and a new user (whose allocated buffers are smaller than the highest current allocation) wishes one
more buffer, steal the extra buffer from the highest buffer user. It is easy to see that even if one user
initially grabs all the buffers when other users become active, they can get their fair share by stealing.
    The problem is that a general solution to the problem of buffer stealing uses a heap. A heap has
O(log n) cost, where n is the number of users with current allocations. How can this be made faster?
    Once again, as is often the case in algorithmics versus algorithms, the problem is caused by reading
too much into the specification. If allocations keep changing in arbitrary increments and the algorithm


2 However, to make things easier in return, this section assumes constant-size buffer allocation with all its potential memory
wastage.

216       Chapter 9 Protocol processing




FIGURE 9.2
The McKenney algorithm for buffer stealing finesses the need for logarithmic heap overhead by relying on the fact
that buffer values change by at most 1 on any operation.


wishes always to find the highest allocation, a logarithmic heap implementation is required. However,
if we can relax the specification (and this seems reasonable in practice) to assume that a user steals one
buffer at a time, then the allocated amounts change not in arbitrary amounts but only by +1 or −1.
This observation results in a constant-time algorithm (the McKenney algorithm, Fig. 9.2), which also
assumes that buffer allocations fall in a bounded set. For each allocation size i, the algorithm maintains
a list of processes that have size exactly i. The algorithm maintains a variable called Highest that points
to the highest amount allocated to any process.
    When a process P wishes to steal a buffer, the algorithm finds a process Q with the highest alloca-
tion at the head of the list pointed to by Highest. While doing so, process P gains a buffer and Q loses
a buffer. The books are updated as follows.
    When process P gets buffer i + 1, P is removed from list i and added to list i + 1, updating Highest
if necessary. When process Q loses buffer i + 1, Q is removed from list i + 1 and added to list i,
updating Highest = i if the Highest list becomes empty.
    Notice this could become arbitrarily inefficient if P and Q could change their allocations by sizes
larger than 1. If Q could reduce its allocation by, say, 100 and there are no other users with the same
original allocation, then the algorithm would require stepping through 100 lists, looking for the next
possible value of highest. Because the maximum amount an allocation can change by is 1, the algorithm
moves through only one list. In terms of algorithmics, this is an example of the special opportunities
created by the use of finite universes (P14 suggests the use of bucket sorting and bitmaps for finite
universes).

Dynamic thresholds
Limiting access by any one flow to a shared buffer is also important in shared memory switches (Chap-
ter 13). In the context of shared memory switches Choudhury and Hahne describe an algorithm similar
to buffer stealing that they call Pushout. However, even using the buffer-stealing algorithm due to
McKenney (1991), Pushout may be hard to implement at high speeds.
    Instead, Choudhury and Hahne (1998) propose a useful alternative mechanism called dynamic buffer
limiting. They observe that maintaining a single threshold for every flow is either overly limiting (if

                                        9.2 Cyclic redundancy checks and checksums                     217



the threshold is too small) or unduly dangerous (if the threshold is too high). Using a static value of
threshold is no different from using a fixed window size for flow control. But TCP uses a dynamic
window size that adapts to congestion. Similarly, it makes sense to exploit a degree of freedom (P13)
and use dynamic thresholds.
    Intuitively, TCP window flow control increases a connection’s window size if there appears to be
unused bandwidth, as measured by the lack of packet drops. Similarly, the simplest way to adapt to
congestion in a shared buffer is to monitor the free space remaining and to increase the threshold
proportional to the free space. Thus user i is limited to no more than cF bytes, where c is a constant
and F is the current amount of free space. If c is chosen to be a power of 2, this scheme only requires
the use of a shifter (to multiply by c) and a comparator (to compare with cF ). This is far simpler than
even the buffer-stealing algorithm.
    Choudhury and Hahne recommend a value of c = 1. This implies that a single user is limited to
taking no more than half the available bandwidth. This is because when the user takes half, the free
space is equal to the user allocation and the threshold check fails. Similarly, if c = 2, any user is limited
to no more than 2/3 of the available buffer space. Thus unlike buffer stealing, this scheme always holds
some free space in reserve for new arrivals, trading slightly suboptimal use of memory for a simpler
implementation.
    Now suppose there are two users and that c = 1. One might naively think that since each user is
limited to no more than half, two active users are limited to a quarter. The scheme does better, however.
Each user can now take 1/3, leaving 1/3 free. Next, if two new users arrive and the old users do not
free their buffers, the two new users can get up to 1/9 of the buffer space.
    Thus, unlike buffer stealing, the scheme is not fair in a short-term sense. However, if the same set
of users is present for sufficiently long periods, the scheme should be fair in a long-term sense. In the
previous example after the buffers allocated to the first two users are deallocated, a fairer allocation
should result.
