# network-algorithmics-7-3-simplest-timer-schemes (chunk 000002)

find the position to insert the new timer. In the example STARTTIMER will insert a new timer due to
expire at 10:24:01, between the second and third elements.
    The worst-case latency to start a timer is O(n). The average latency depends on the distribution
of timer intervals (from time started to time stopped) and on the distribution of the arrival process
according to which calls to STARTTIMER are made.
    STOPTIMER need not search the list if the list is doubly linked. When STARTTIMER inserts a timer
into the ordered list, it can store a pointer to the element. STOPTIMER can then use this pointer to delete
the element in O(1) time from the doubly linked list. This can be used by any timer scheme. This is an
application of P9, passing hints in layer interfaces. More precisely, the user passes a handle to the timer
in the STOPTIMER interface.
    If this scheme is implemented by a host processor, the interrupt overhead on every tick can be
avoided if there is hardware support to maintain a single timer. The hardware timer is set to expire at
the time at which the timer at the head of the list is due to expire. The hardware intercepts all clock ticks
and interrupts the host only when a timer actually expires. Unfortunately, some processor architectures
do not offer this capability.
    As for Space, Scheme 1 needs the minimum space possible; Scheme 2 needs O(n) extra space for
the forward and back pointers between queue elements.
    A linked list is one way of implementing a priority queue. For large n, tree-based data structures
are better. These include unbalanced binary trees, heaps, postorder and end-order trees, and leftist trees
(Cormen et al., 1990; Vaucher and Duval, 1975). They attempt to reduce the latency in Scheme 2
for STARTTIMER from O(n) to O(log(n)). In Myhrhaug (2001) it is reported that this difference is
significant for large n and that unbalanced binary trees are less expensive than balanced binary trees.
    Unfortunately, unbalanced binary trees easily degenerate into a linear list; this can happen, for in-
stance, if a set of equal timer intervals is inserted. It would, however, be a good idea to compare the
performance of timing wheels against an implementation using simple binary heaps. We will lump
these algorithms together as Scheme 3: tree-based algorithms. Linux high resolution timers (hrtimers)
use balanced (red-black) trees (Gleixner and Niehaus, 2006).
    Thus the three simple schemes take the time that is least logarithmic in the number of timers for
either STARTTIMER or PERTICKBOOKKEEPING. This is a problem for high-speed implementations.
The next section shows how to do better.
