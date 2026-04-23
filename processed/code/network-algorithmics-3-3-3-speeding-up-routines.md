# Network Algorithmics — fifteen principles: speeding up routines (3.3.3) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 88 -l 126 -layout
- Slice: from `3.3.3 Principles for speeding up routines` up to (excluding) `3.4 Design versus implementation principles`

---

3.3.3 Principles for speeding up routines
While the previous principles exploited system structure, we now consider principles for speeding up
system routines considered in isolation.

P11: Optimize the expected case
While systems can exhibit a range of behaviors, the behaviors often fall into a smaller set called the
“expected case” (Hennessey and Patterson, 1996). For example, well-designed systems should mostly
operate in a fault- and exception-free regime. A second example is a program that exhibits spatial
locality by mostly accessing a small set of memory locations. Thus it pays to make common behaviors
efficient, even at the cost of making uncommon behaviors more expensive.
    Heuristics such as optimizing the expected case are often unsatisfying for theoreticians, who (natu-
rally) prefer mechanisms whose benefit can be precisely quantified in an average or worst-case sense.
In defense of this heuristic, note that every computer in existence optimizes the expected case (see
Chapter 2) at least a million times a second.
    For example, with the use of paging, the worst-case number of memory references to resolve a
PC instruction that accesses memory can be as bad as four (read instruction from memory, read first-
level page table, read second-level page table, fetch operand from memory). However, the number of
memory accesses can be reduced to 0 using caches. In general, caches allow designers to use modular
structures and indirection, with gains in flexibility, and yet regain performance in the expected case.
Thus it is worth highlighting caching.

P11a: Use caches
Besides caching, there are subtler uses of the expected-case principle. For example, when you wish to
change buffers in the EMACS editor, the editor offers you a default buffer name, which is the last buffer
you examined. This saves typing time in the expected case when you keep moving between two buffers.
The use of header prediction (Chapter 9) in networks is another example of optimizing the expected

---

## PDF page 92

           3.3 Fifteen implementation principles—categorization and description                       65



case: The cost of processing a packet can be greatly reduced by assuming that the next packet received
is closely related to the last packet processed (for example, by being the next packet in sequence) and
requires no exception processing.
    Note that determining the common case is best done by measurements and by schemes that auto-
matically learn the common case. However, it is often based on the designer’s intuition. Note that the
expected case may be incorrect in special situations or may change with time.

P12: Add or exploit state to gain speed
If an operation is expensive, consider maintaining additional but redundant state to speed up the op-
eration. For example, Charlie keeps track of the tables that are busy so that he can optimize waiter
assignments. This is not absolutely necessary, for he can always compute this information when needed
by walking around the restaurant.
    In database systems, a classic example is the use of secondary indices. Bank records may be stored
and searched using a primary key, say, the customer’s Social Security number. However, if there are
several queries that reference the customer name (e.g., “Find the balance of all Cleopatra’s accounts in
the Thebes branch”), it may pay to maintain an additional index (e.g., a hash table or B-tree) on the
customer name. Note that maintaining additional state implies the need to potentially modify this state
whenever changes occur.
    However, sometimes this principle can be used without adding state by exploiting the existing state.
We call this out as Principle P12a.

P12a: Compute incrementally
When a new customer comes in or leaves, Charlie increments the board on which he notes waiter
assignments. As a second example, strength reduction in compilers (see example in P4c) incrementally
computes the new loop index from the old using additions instead of computing the absolute index using
multiplication. An example of incremental computation in networking is the incremental computation
of IP checksums (Chapter 9) when only a few fields in the packet change.

P13: Optimize degrees of freedom
It helps to be aware of the variables that are under one’s control and the evaluation criteria used to
determine good performance. Then the game becomes one of optimizing these variables to maximize
performance. For example, Charlie first used to assign waiters to tables as they became free, but he
realized he could improve waiter efficiency by assigning each waiter to a set of contiguous tables.
    Similarly, compilers use coloring algorithms to do register assignment while minimizing register
spills. A networking example of optimizing degrees of freedom is multibit trie IP lookup algorithms
(Chapter 11). In this example, a degree of freedom that can be overlooked is that the number of bits
used to index into a trie node can vary, depending on the path through the trie, as opposed to being fixed
at each level. The number of bits used can also be optimized via dynamic programming (Chapter 11)
to demand the smallest amount of memory for a given speed requirement.

P14: Use special techniques for finite universes such as integers
When dealing with small universes, such as moderately sized integers, techniques like bucket sorting,
array lookup, and bitmaps are often more efficient than general-purpose sorting and searching algo-
rithms.

---

## PDF page 93

66         Chapter 3 Fifteen implementation principles



    To translate a virtual address into a physical address, a processor first tries a cache called the TLB.
If this fails, the processor must look up the page table. A prefix of the address bits is used to index into
the page table directly. The use of table lookup avoids the use of hash tables or binary search, but it
requires large page table sizes. A networking example of this technique is timing wheels (Chapter 7),
where an efficient algorithm for a fixed timer range is constructed using a circular array.

P15: Use algorithmic techniques to create efficient data structures
Even where there are major bottlenecks, such as virtual address translation, systems designers finesse
the need for clever algorithms by passing hints, using caches, and performing table lookup. Thus a
major system designer is reported to have told an eager theoretician: “I don’t use algorithms, son.”
    This book does not take this somewhat antiintellectual position. Instead, it contends that, in context,
efficient algorithms can greatly improve system performance. In fact, a fair portion of the book will be
spent describing such examples. However, there is a solid kernel of truth to the “I don’t use algorithms”
putdown. In many cases, Principles P1 through P14 need to be applied before any algorithmic issues
become bottlenecks.
    Algorithmic approaches include the use of standard data structures as well as generic algorithmic
techniques, such as divide-and-conquer and randomization. The algorithm designer must, however, be
prepared to see his clever algorithm become obsolete because of changes in system structure and tech-
nology. As described in the introduction, the real breakthroughs may arise from applying algorithmic
thinking as opposed to merely reusing existing algorithms.
    Examples of the successful use of algorithms in computer systems are the Lempel–Ziv compression
algorithm employed in the UNIX utility gzip, the Rabin–Miller primality test algorithm found in public
key systems, and the common use of B-trees (due to Bayer–McCreight) in databases (Cormen et al.,
1990). Networking examples studied in this text include the Lulea IP-lookup algorithm (Chapter 11)
and the RFC scheme for packet classification (Chapter 12).
