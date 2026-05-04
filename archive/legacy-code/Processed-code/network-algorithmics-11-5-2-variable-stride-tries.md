# Network Algorithmics — 11.5.2 Variable-stride tries (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 290
- Slice: from `11.5.2 Variable-stride tries` up to next detected section heading

---

11.5.2 Variable-stride tries
In Fig. 11.7 the leftmost leaf node needs to store the expansions of P3 = 11001*, while the rightmost
leaf node needs to store P6 (1000*) and P7 (100000*). Thus because of P7 the rightmost leaf node
needs to examine 3 bits. However, there is no reason for the leftmost leaf node to examine more than

264       Chapter 11 Prefix-match lookups




FIGURE 11.7
Expanded trie (which has two strides of 3 bits each) corresponding to the prefix database of Fig. 11.6.


2 bits because P3 contains only 5 bits, and the root stride is 3 bits. There is an extra degree of freedom
that can be optimized (P13).
    In a variable-stride trie, the number of bits examined by each trie node can vary, even for nodes at
the same level. To do so, the stride of a trie node is encoded with the pointer to the node. Fig. 11.7 can
be transformed into a variable-stride trie (Fig. 11.8) by replacing the leftmost node with a four-element
array and encoding length 2 with the pointer to the leftmost node. The stride encoding costs 5 bits.
However, the variable stride trie of Fig. 11.8 has four fewer array entries than the trie of Fig. 11.7.
    Our example motivates the problem of picking strides to minimize the total amount of trie memory.
Since expansion trades memory for time, why not minimize the memory needed by optimizing a degree
of freedom (P13), the strides used at each node? To pick the variable strides, the designer first specifies
the worst-case number of memory accesses. For example, with 40-byte packets at 1-Gbps and 80-
nanosecond DRAM, we have a time budget of 320 nanoseconds, which allows only four memory
accesses. This constrains the maximum number of nodes in any search path (four in our example).
    Given this fixed height, the strides can be chosen to minimize storage. This can be done using
dynamic programming (Srinivasan and Varghese, 1999) in a few seconds, even for large databases of
150,000 prefixes. A degree of freedom (the strides) is optimized to minimize the memory used for a
given worst-case tree height.
    A trie is said to be optimal for height h and a database D if the trie has the smallest storage among all
variable-stride tries for database D, whose height is no more than h. It is easy to prove (see exercises)
that the trie of Fig. 11.8 is optimal for the database on the left of Fig. 11.6 and height 2.
    The general problem of picking an optimal stride trie can be solved recursively (Fig. 11.9). Assume
the tree height must be h. The algorithm first picks a root with stride s. The y = 2s possible pointers in

                                                                                     11.5 Multibit tries               265




FIGURE 11.8
Transforming the fixed-stride trie of Fig. 11.7 into a variable-stride trie by encoding the stride of each trie node
along with a pointer to the node. Notice that the leftmost leaf node now only contains four locations (instead of
eight), thus reducing the number of locations from 24 to 20.




FIGURE 11.9
Picking an optimum variable-stride trie via dynamic programming.



the root can lead to y nonempty subtries T1 , . . . Ty . If the s-bit pointer pi leads to subtrie Ti , then all
prefixes in the original database D that start with pi must be stored in Ti . Call this set of prefixes Di .
    Suppose we could recursively find the optimal Ti for height h − 1 and database Di . Having used
up one memory access at the root node, there are only h − 1 memory accesses left to navigate each
subtrie Ti . Let Ci denote the storage cost required, counted in array locations, for the optimal Ti . Then
for a fixed root stride s, the cost of the resulting optimal trie C(s) is 2s (cost of root node in array

266      Chapter 11 Prefix-match lookups


                 y
locations) plus i=1 Ci . Thus the optimal value of the initial stride is the value of s, where 1 ≤ s ≤ 32,
that minimizes C(s).
     A naive use of recursion leads to repeated subproblems. To avoid repeated subproblems, the algo-
rithm first constructs an auxiliary 1-bit trie. Notice that any subtrie Ti in Fig. 11.9 must be a subtrie N
of the 1-bit trie. Then the algorithm uses dynamic programming to construct the optimal cost and trie
strides for each subtrie N in the original 1-bit trie for all values of height from 1 to h, building bottom-
up from the smallest-height subtries to the largest-height subtries. The final result is the optimal strides
for the root (of the 1-bit subtrie) with height h. Details are described in Srinivasan and Varghese (1999).
     The final complexity of the algorithm is easily seen to be O(N ∗ W 2 ∗ h), where N is the number
of original prefixes in the original database, W is the width of the destination address, and h is the
desired worst-case height. This is because there are N ∗ W subtries in the 1-bit trie, each of which must
be solved for heights that range from 1 to h, and each solution requires a minimization across at most
W possible choices for the initial stride s. Note that the complexity is linear in N (the largest number,
around 150,000 at the time of writing) and h (which should be small, at most 8), but quadratic in the
address width (currently 32). In practice, the quadratic dependence on address width is not a major
factor.
     For example, Srinivasan and Varghese (1999) show that using a height of 4, the optimized MAE-
East database required 423 KB of storage, compared to 2003 KB for the unoptimized version. The
unoptimized version uses the “natural” stride lengths 8, 8, 8, 8. The dynamic program took 1.6 seconds
to run on a 300-MHz Pentium Pro. The dynamic program is even simpler for fixed-stride tries and takes
only 1 milliseconds to run. However, the use of fixed strides requires 737 KB instead of 423 KB.
     Clearly, 1.6 seconds are much too long to let the dynamic program be run for every update and
still allow millisecond updates (Labovitz et al., 1997). However, backbone instabilities are caused by
pathologies in which the same set of prefixes S are repeatedly inserted and deleted by a router that
is temporarily swamped (Labovitz et al., 1997). Since we had to allocate memory for the full set,
including S, anyway, the fact that the trie is suboptimal in its use of memory when S is deleted is
irrelevant. On the other hand, the rate at which new prefixes get added or deleted by managers seems
more likely to be on the order of days. Thus a dynamic program that takes several seconds to run every
day seems reasonable and will not unduly affect worst-case insertion and deletion times while still
allowing reasonably optimal tries.
