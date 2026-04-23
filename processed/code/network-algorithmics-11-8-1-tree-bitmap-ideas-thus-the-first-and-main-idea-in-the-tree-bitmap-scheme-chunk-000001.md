# network-algorithmics-11-8-1-tree-bitmap-ideas-thus-the-first-and-main-idea-in-the-tree-bitmap-scheme (chunk 000001)

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
