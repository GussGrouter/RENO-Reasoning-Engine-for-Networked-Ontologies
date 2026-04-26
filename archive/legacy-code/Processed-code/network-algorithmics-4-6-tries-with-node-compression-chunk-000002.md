# network-algorithmics-4-6-tries-with-node-compression (chunk 000002)

Solution
Since M < 32, a bitmap of size 32 can easily fit into a computer word (P14 and P4a). Thus null pointers
are removed after adding a bitmap with zero bits indicating the original positions of null pointers. This
is shown in Fig. 4.11. The trie node can now be replaced with a bitmap and a compressed trie node.
A compressed trie node is an array that consists only of the nonnull values in the original node. Thus in
Fig. 4.11, the original root trie node (on the top) has been replaced with the compressed trie node (on
the bottom). The bitmap contains a 1 in the first and seventh positions, where the root node contains
nonnull values. The compressed array now contains only two elements, the first pointer and KEY 3.
This still begs the question: How should a trie node be searched?
    Since both uncompressed and compressed nodes are arrays and the search process starts with an
index I into the uncompressed node, the search process must consult the bitmap to convert the uncom-
pressed index I into a compressed index C into the compressed node. For example, if I is 1 in Fig. 4.11,
C should be 1; if I is 7, C should be 2. If I is any other value, C should be 0, indicating that there is
only a null pointer.
    Fortunately, the conversion from I to C can be accomplished easily by noting the following. If
position I in the bitmap contains a 0, then C = 0. Otherwise, C is the number of 1’s in the first I bits of
the bitmap. Thus if I = 7, then C = 2, since there are two bits set in the first seven bits of the bitmap.

4.7 Packet filtering in routers                  87

FIGURE 4.11
Compressing a trie node using a bitmap and bit counting to efficiently translate from an uncompressed index to a
compressed index.

This computation requires at most two memory references: one to access the bitmap (because the
bitmap is small [P4a]) and one to access the compressed array. The calculation of the number of bits
set in a bitmap can be done using internal registers (in software) or combinatorial logic (in hardware).
Thus the effective slowdown is slightly more than a factor of 2 in software and exactly 2 in hardware.

Exercises

• How could you use table lookup (P14, P2a) to speed up counting the number of bits set in software?
  Would this necessarily require a third memory reference?
• Suppose the bitmap is large (say, M = 64 K). It would appear that counting the number of bits set
  in such a large bitmap is impossibly slow in hardware or software. Can you find a way to speed up
  counting bits in a large bitmap (principles P12 and P2a) using only one extra memory access? This
  will be extremely useful in Chapter 11.
