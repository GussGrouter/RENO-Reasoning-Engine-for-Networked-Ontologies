# network-algorithmics-11-5-2-variable-stride-tries (chunk 000001)

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
