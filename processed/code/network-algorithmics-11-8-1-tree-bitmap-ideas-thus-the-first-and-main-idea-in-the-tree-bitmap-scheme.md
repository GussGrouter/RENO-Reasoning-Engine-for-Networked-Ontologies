# Network Algorithmics — 11.8.1 Tree bitmap ideas Thus the first and main idea in the tree bitmap scheme is that there are two bitmaps per trie node, one (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 299
- Slice: from `11.8.1 Tree bitmap ideas Thus the first and main idea in the tree bitmap scheme is that there are two bitmaps per trie node, one` up to next detected section heading

---

11.8.1 Tree bitmap ideas
Thus the first and main idea in the tree bitmap scheme is that there are two bitmaps per trie node, one
for all the internally stored prefixes and one for the external pointers. Fig. 11.14 shows the tree bitmap
version of the root node in Fig. 11.12.
    Recall that in Fig. 11.12, the prefixes P8 = 100* and P9 = 110* in the original database are missing
from the picture on the left side because they have been pushed down to the leaves to accommodate the
two pointers (ptr1, which points to nodes containing longer prefixes such as P6 = 1000*, and ptr2,
which points to nodes containing longer prefixes such as P3 = 11001*). This results in the basic Lulea
trie node, in which each element contains either a pointer or a prefix but not both. This allows the use
of a single bitmap to compress a Lulea node, as shown on the extreme right of Fig. 11.12.
    By contrast, the same trie node in Fig. 11.14 is split into two compressed arrays, each with its own
bitmap. The first array, shown vertically, is a pointer array, which contains a bitmap denoting the (two)
positions where nonnull pointers exist and a compressed array containing the nonnull pointers, ptr1
and ptr2.
    The second array, shown horizontally, is the internal prefix array, which contains a list of all the
prefixes within the first 3 bits. The bitmap used for this array is very different from the Lulea encoding
and has one bit set for every possible prefix stored within this node. Possible prefixes are listed lexi-
cographically, starting from ∗, followed by 0∗ and 1∗, and then on to the length-2 prefixes (00*, 01*,

                                                                             11.8 Tree bitmap           273



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
