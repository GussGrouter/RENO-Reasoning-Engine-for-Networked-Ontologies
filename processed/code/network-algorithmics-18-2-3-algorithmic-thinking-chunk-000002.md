# network-algorithmics-18-2-3-algorithmic-thinking (chunk 000002)

header prediction (Chapter 9) optimizes the expected case when the next packet is from the same
connection and is the next data packet or ack. If this is indeed the expected case, there is no need
for fancy connection lookup structures (a simple one-element cache) or fancy structures to deal with
sequence number bookkeeping. However, if there are several concurrent connections, as in a server, a
hash table may be better for connection lookup. Similarly, if packets routinely arrive out of order, then
more fancy sequence number bookkeeping schemes (Thomas et al., 1992) may be needed.
    Principle P12, adding state for speed, is a simple technique used often in standard algorithmic de-
sign. However, it is quite common for just this principle by itself (without fancy additional algorithmic
machinery) to help remove systems bottlenecks. For example, the major bottleneck in the select() call
implementation is the need to repeatedly check for data in network connections known not to be ready.
By simply keeping state across calls, this key bottleneck can be removed. By contrast, the bottlenecks
caused by the bitmap interface can be removed by algorithmic means, but these are less important.
    Having framed the appropriate problem using P11, P12, and P13, Principles P14 and P15 can be
used to guide the search for solutions.
    Principle P14 asks whether there are any important special cases, such as the use of finite universes,
that can be leveraged to derive a more efficient algorithm. For example, the McKenney buffer-stealing
algorithm of Chapter 9 provides a fast heap with O(1) operations for the special case when elements to
the heap change by at most 1 on each call.
    Finally, Principle P15 asks whether there are algorithmic methods that can be adapted to the sys-
tem. It is dangerous to blindly adapt existing algorithms because of the following possibilities that can
mislead the designer.

• Wrong Measures: The measure for most systems implementations is the number of memory accesses
  and not the number of operations. For example, the fast ufalloc() operation uses a selection tree on
  bitmaps instead of a standard heap, leveraging off the fact that a single read can access W bits, where
  W is the size of a word. Again, the important measure in many IP lookup algorithms is search speed
  and not update speed.
• Asymptotic Complexity: Asymptotic complexity hides constants that are crucial in systems. When
  every microsecond counts, surely constant factors are important. Thus the switch matching algo-
  rithms in Chapter 13 have much smaller constants than the best bipartite matching algorithms in the
  literature and hence can be implemented.
• Incorrect Cost Penalties: In timing wheels (Chapter 7) a priority heap is implemented using a bucket-
  sorting data structure. However, the cost of strolling through empty buckets, a severe cost in bucket
  sort, is unimportant because, on every timer tick, the system clock must be incremented anyway.
  As a second example, the dynamic programming algorithm to compute optimal lookup strides for
  multibit tries (Chapter 11) is O(N ∗ W 2 ), where N is the number of prefixes and W is the address
  width. While this appears to be quadratic, it is linear in the important term N (100,000 or more) and
  quadratic in the address width (32 bits, and the term is smaller in practice).

In spite of all these warnings algorithmic methods are useful in networking, ranging from the use of
Pathfinder-like tries in Chapter 8 to the use of tries and binary search (suitably modified) in Chapter 11.

524      Chapter 18 Conclusions
