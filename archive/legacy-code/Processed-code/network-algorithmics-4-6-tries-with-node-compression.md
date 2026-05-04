# Network Algorithmics — 4.6 Tries with node compression (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 112
- Slice: from `4.6 Tries with node compression` up to next detected section heading

---

4.6 Tries with node compression
A trie is a data structure that is a tree of nodes, where each node is an array of M elements. Fig. 4.10
shows a simple example with M = 8. Each array can hold either a key (e.g., KEY 1, KEY 2, or KEY 3
in Fig. 4.10) or a pointer to another trie node (e.g., the first element in the topmost trie node of Fig. 4.10,
which is the root). The trie is used to search for exact matches (and longest-prefix matches) with an
input string. Tries are useful in networking for such varied tasks as IP address lookups (Chapter 11),
bridge lookups (Chapter 10), and demultiplexing filters (Chapter 8).




FIGURE 4.10
Trie storing three keys. Notice the wasted space in the trie nodes.

86       Chapter 4 Principles in action



    The exact trie algorithms do not concern us here. All one needs to know is how a trie is searched.
Let c = log2 M be the chunk size of a trie. To search the trie, search first breaks the input string into
chunks of size c. Search uses successive chunks, starting from the most significant, to index into nodes
of the trie, starting with the root node. When search uses chunk j to index into position i of the current
trie node, position i could contain either a pointer or a key. If position i contains a nonnull pointer to
node N , the search continues at node N with chunk j + 1; otherwise, the search terminates.
    To summarize, each node is an array of pointers or keys, and the search process needs to index
into these arrays. However, if many trie nodes are sparse, there is considerable wasted space (P1). For
example, in Fig. 4.10, only 4 out of 16 locations contain useful information. In the worst case, each
trie node could contain 1 pointer or key and there could be a factor of M in wasted memory. Assume
M ≤ 32 in what follows. Even if M is this small, a 32-fold increase in memory can greatly increase the
cost of the design.
    An obvious approach is to replace each trie node by a linear list of pairs of the form (i, val), where
val is the nonempty value (either pointer or key) in position i of the node. For example, the root trie
node in Fig. 4.10 could be replaced by the list (1, ptr1); (7, KEY 1), where ptr1 is the pointer to the
bottom trie node. Unfortunately, this can slow down trie search by a factor of M, because the search
of each trie node may now have to search through a list of M locations, instead of a single indexing
operation. This leads to the following problem.

Problem
How can trie nodes be compressed to remove null pointers without slowing down search by more than
a small factor?
Hint: Despite compressing the nodes, array indexing needs to be efficient. If the nodes are com-
pressed, how might information about which array elements are removed be represented? Consider
leveraging off the fact that M is small by following P14 (exploit the small integer size) and P4a
(exploit locality).

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
