# Network Algorithmics — 7.3 Simplest timer schemes (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 209
- Slice: from `7.3 Simplest timer schemes` up to next detected section heading

---

7.3 Simplest timer schemes
The two simplest schemes for timer implementation are, in fact, commonly used. In the first scheme
STARTTIMER finds a memory location and sets that location to the specified timer interval. Every
T units, PERTICKBOOKKEEPING will decrement each outstanding timer; if any timer becomes zero,
EXPIRYPROCESSING is called.
    This scheme is extremely fast for all but PERTICKBOOKKEEPING. It also uses one record per out-
standing timer, the minimum space possible. It is appropriate if there are only a few outstanding timers,
if most timers are stopped within a few ticks of the clock, and if PERTICKBOOKKEEPING is done with
suitable performance by special-purpose hardware.
    Note that instead of doing a Decrement, we can store the absolute time at which timers expire
and do a Compare. This option is valid for all timer schemes we describe; the choice between them
will depend on the size of the time-of-day field, the cost of each instruction, and the hardware on the
machine implementing these algorithms. In this chapter we will use the Decrement option, except when
describing Scheme 2.
    In a second simple scheme, used in older versions of UNIX, PERTICKBOOKKEEPING latency is
reduced at the expense of STARTTIMER performance. Timers are stored in an ordered list. Unlike
Scheme 1, we will store the absolute time at which the timer expires, not the interval before expiry.
The timer that is due to expire at the earliest time is stored at the head of the list. Subsequent timers are
stored in increasing order, as shown in Fig. 7.1. In Fig. 7.1 the lowest timer is due to expire at absolute
time 10 hours, 23 minutes, and 12 seconds.
    Because the list is sorted, PERTICKBOOKKEEPING need only increment the current clock time and
compare it with the head of the list. If they are equal or if the time of day is greater, it deletes that list
element and calls EXPIRYPROCESSING. It continues to delete elements at the head of the list until the
expiry time of the head of the list is strictly less than the time of day. STARTTIMER searches the list to

                                                                           7.4 Timing wheels           183



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
