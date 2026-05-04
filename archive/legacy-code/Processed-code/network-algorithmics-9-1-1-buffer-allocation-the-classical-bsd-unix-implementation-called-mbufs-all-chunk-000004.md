# network-algorithmics-9-1-1-buffer-allocation-the-classical-bsd-unix-implementation-called-mbufs-all (chunk 000004)

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
