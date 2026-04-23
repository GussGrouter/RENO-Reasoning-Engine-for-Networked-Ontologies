# network-algorithmics-11-8-1-tree-bitmap-ideas-thus-the-first-and-main-idea-in-the-tree-bitmap-scheme (chunk 000002)

10*, 11*), and finally the length-3 prefixes. Bits are set when the corresponding prefixes occur within
the trie node.
    Thus in Fig. 11.14, the prefixes P8 and P9, which were leaf pushed in Fig. 11.12, have been resur-
rected and now correspond to bits 12 and 14 in the internal prefix bitmap. In general, for an r-bit trie
node, there are 2r+1 − 1 possible prefixes of lengths r or less, which requires the use of a (2r+1 − 1)
bitmap. The scheme gets its name because the internal prefix bitmap represents a trie in a linearized
format: Each row of the trie is captured top-down from left to right.
    The second idea in the tree bitmap scheme is to keep the trie nodes as small as possible to reduce
the required memory access size for a given stride. Thus a trie node is of fixed size and contains only a
pointer bitmap, an internal prefix bitmap, and child pointers. But what about the next-hop information
associated with any stored prefixes?
    The trick is to store the next hops associated with the internal prefixes stored within each trie node
in a separate array associated with this trie node. Putting next-hop pointers in a separate result array
potentially requires two memory accesses per trie node (one for the trie node and one to fetch the result
node for stored prefixes).
    However, a simple lazy evaluation strategy (P2b) is not to access the result nodes until search
terminates. Upon termination, the algorithm makes a final access to the correct result node. This is the
result node that corresponds to the last trie node encountered in the path that contained a valid prefix.
This adds only a single memory reference at the end, in addition to the one memory reference required
per trie node.
    The third idea is to use only one memory access per node, unlike Lulea, which uses at least two
memory accesses. Lulea needs two memory accesses per node because it uses large strides of 8 or
16 bits. This increases the bitmap size so much that the only feasible way to count bits is to use an
additional chunk array that must be accessed separately. The tree bitmap scheme gets around this by
simply using smaller-stride nodes, say, of 4 bits. This makes the bitmaps small enough that the entire
node can be accessed by a single wide access (P4a, exploit locality). Combinatorial logic (Chapter 2)
can be used to count the bits.
