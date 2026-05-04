# Network Algorithmics — 18.2.3 Algorithmic thinking (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 549
- Slice: from `18.2.3 Algorithmic thinking` up to next detected section heading

---

18.2.3 Algorithmic thinking
Algorithmic thinking refers to thinking about networking bottlenecks the way algorithm designers ap-
proach problems. Overall, algorithmic approaches are less important than other systems approaches, as
embodied by Principles P1 through P10. Also, it is dangerous to blindly reuse existing algorithms.
    The first problem that must be confronted in using algorithmic thinking is how to frame the problem
that must be solved. By changing the problem, one can often find more effective solutions. Consider
the following problem, which we avoided in Chapter 11.
Example (Pipelining and Memory Allocation). A lookup engine is using a trie. The lookup engine
must be pipelined for speed. The simplest solution is to pipeline the trie by level. The root is at the first
stage, the children of the root are assigned to the second stage, the nodes at height 2 to the third stage,
etc. Unfortunately, the memory needs for each stage can vary as prefixes are inserted and deleted. There
is the following spectrum of approaches.

• Centralized memory: All the processing stages share a single memory. Memory allocation is easy,
  but the centralized memory becomes a bottleneck.
• One memory per stage: Each processing stage has its own memory, minimizing memory contention.
  However, since the memory is statically allocated at fabrication time, any memory unused by a stage
  cannot be used by another stage.
• Dynamically allocate small 1-port memories to stages: As suggested in Chapter 11, on-chip memory
  is divided into M SRAMs, which are connected to stage processors via a crossbar. As a processor
  requires more or less memory, crossbar connections can be changed to allocate more or fewer mem-
  ories to each stage. This scheme requires a large M to avoid wasting memory, but a large M can
  lead to high capacitive loads.
• Dynamically allocate medium-size 2-port memories to stages: The setting is identical to the last
  approach, except that each memory is now a 2-port memory that can be allocated to two processors.
  Using this, it is possible to show that N memories are sufficient for N processors, with almost no
  memory wastage.
• Dynamically change the starting point in the pipeline: In a conventional linear pipeline all lookups
  start at the first stage and leave at the last. Florin Baboescu has suggested an alternative: Using
  a lookup table indexed on the first few bits, assign each address to a different first processor in
  the pipeline. Thus different addresses have different start and end processors. However, this gives
  considerably more flexibility in allocating memory to processors by changing the assignment of
  addresses to processors.
• Pipeline by depth: Instead of pipelining a tree by height, consider pipelining by depth. All leaves
  are assigned to the last stage, K, all parents of the leaves to stage K − 1, etc.

   These approaches represent the interplay between Principles P13 (optimizing degrees of freedom)
and P5 (add hardware). However, each approach results in a different algorithmic problem! Thus a far
more important skill than solving a hard problem is the skill required to frame the right problems that
balance overall system needs.
   Principles P11 and P13 help choose the right problem to solve. The pipelining example shows that
choosing the degrees of freedom (P13) can change the algorithmic problem solved.
   Similarly, Principle P11, optimizing the expected case, can sometimes help decide what the right
measure is to optimize. This in turn influences the choice of algorithm. For example, simple TCP

                                               18.2 What network algorithmics is about               523



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
