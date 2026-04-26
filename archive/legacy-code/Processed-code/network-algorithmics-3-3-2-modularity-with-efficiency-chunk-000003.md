# network-algorithmics-3-3-2-modularity-with-efficiency (chunk 000003)

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
