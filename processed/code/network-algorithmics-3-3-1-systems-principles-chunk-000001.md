# network-algorithmics-3-3-1-systems-principles (chunk 000001)

# Network Algorithmics — fifteen principles: systems principles (3.3.1) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 84 -l 111 -layout
- Slice: from `3.3.1 Systems principles` up to (excluding) `3.3.2 Principles for modularity with efficiency`

---

3.3.1 Systems principles
The first five principles exploit the fact that we are building systems.

P1: Avoid obvious waste in common situations
In a system, there may be wasted resources in special sequences of operations. If these patterns occur
commonly, it may be worth eliminating the waste. This reflects an attitude of thriftiness toward system
costs.
    For example, Chef Charlie has to make a trip to the pantry to get the ice cream maker to make ice
cream and to the pantry for a pie plate when he makes pies. But when he makes pie à la mode, he has
learned to eliminate the obvious waste of two separate trips to the pantry.
    Similarly, optimizing compilers look for obvious waste in terms of repeated subexpressions. For
example, if a statement calculates i = 5.1 ∗ n + 2 and a later statement calculates j := (5.1 ∗ n + 2) ∗ 4,
the calculation of the common subexpression 5.1 ∗ n + 2 is wasteful and can be avoided by computing
the subexpression once, assigning it to a temporary variable t, and then calculating i := t and j := t ∗ 4.
A classic networking example, described in Chapter 5, is avoiding making multiple copies of a packet
between the operating system and user buffers.
    Notice that each operation (e.g., walk to pantry, line of code, single packet copy) considered by
itself has no obvious waste. It is the sequence of operations (two trips to the pantry, two statements
that recompute a subexpression, two copies) that have obvious waste. Clearly, the larger the exposed
context, the greater the scope for optimization. While the identification of certain operation patterns as
being worth optimizing is often a matter of designer intuition, optimizations can be tested in practice
using benchmarks.

P2: Shift computation in time
Systems have an aspect in space and time. The space aspect is represented by the subsystems, possibly
geographically distributed, into which the system is decomposed. The time aspect is represented by
the fact that a system is instantiated at various time scales, from fabrication time to compile time to
parameter-setting times to run time. Many efficiencies can be gained by shifting computation in time.
Here are three generic methods that fall under time-shifting.
• P2a: Precompute. This refers to computing quantities before they are actually used, to save time at
  the point of use. For example, Chef Charlie prepares crushed garlic in advance to save time during
  the dinner rush. A common systems example is table-lookup methods, where the computation of an
  expensive function f in run time is replaced by the lookup of a table that contains the value of f
  for every element in the domain of f . A networking example is the precomputation of IP and TCP
  headers for packets in a connection; because only a few header fields change for each packet, this
  reduces the work to write packet headers (Chapter 9).
• P2b: Evaluate Lazily. This refers to postponing expensive operations at critical times, hoping that
  either the operation will not be needed later or a less busy time will be found to perform the opera-

---

## PDF page 86

3.3 Fifteen implementation principles—categorization and description                               59

FIGURE 3.8
Easing the implementation of Subsystem 1 by weakening its specification from S to, say, W , at the cost of making
Subsystem 2 do more work.
