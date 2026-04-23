# network-algorithmics-3-3-3-speeding-up-routines (chunk 000001)

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
