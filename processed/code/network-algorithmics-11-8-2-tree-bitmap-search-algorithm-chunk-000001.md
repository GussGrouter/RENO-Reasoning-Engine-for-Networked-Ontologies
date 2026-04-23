# network-algorithmics-11-8-2-tree-bitmap-search-algorithm (chunk 000001)

# Network Algorithmics — 11.8.2 Tree bitmap search algorithm (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 300
- Slice: from `11.8.2 Tree bitmap search algorithm` up to next detected section heading

---

11.8.2 Tree bitmap search algorithm
The search algorithm starts with the root node and uses the first r bits of the destination address (cor-
responding to the stride of the root node, 3 in our example) to index into the pointer bitmap at the root
node at position P . If there is a 1 in this position, there is a valid child pointer. The algorithm counts
the number of 1’s to the left of this 1 (including this 1) and denotes this count by I . Since the pointer
to the start position of the child pointer block (say, y) is known, as is the size of each trie node (say, S),
the pointer to the child node can be calculated as y + (I ∗ S).
    Before moving on to the child, the algorithm must also check the internal bitmap to see if there
are one or more stored prefixes corresponding to the path through the multibit node to position P . For
example, suppose P is 101 and a 3-bit stride is used at the root node bitmap, as in Fig. 11.14. The
algorithm first checks to see whether there is a stored internal prefix 101*. Since 101* corresponds
to the 13th bit position in the internal prefix bitmap, the algorithm can check if there is a 1 in that
position (there is one in the example). If there was no 1 in this position, the algorithm would back up to
check whether there is an internal prefix corresponding to 10*. Finally, if there is not a 10* prefix, the
algorithm checks for the prefix 1*.

274      Chapter 11 Prefix-match lookups

This search algorithm appears to require a number of iterations, proportional to the logarithm of the
internal bitmap length. However, for bitmaps of up to 512 bits or so in hardware, this is just a matter of
simple combinational logic. Intuitively, such logic performs all iterations in parallel and uses a priority
encoder to return the longest matching stored prefix.
    Once it knows there is a matching stored prefix within a trie node, the algorithm does not imme-
diately retrieve the corresponding next-hop information from the result node associated with the trie
node. Instead, the algorithm moves to the child node while remembering the stored-prefix position and
the corresponding parent trie node. The intent is to remember the last trie node T in the search path that
contained a stored prefix, and the corresponding prefix position.
    Search terminates when it encounters a trie node with a 0 set in the corresponding position of the
extending bitmap. At this point, the algorithm makes a final access to the result array corresponding to
T to read off the next-hop information. Further tricks to reduce memory access width are described in
Eatherton’s MS thesis (Eatherton, 1995), which includes a number of other useful ideas.
    Intuitively, insertions in a tree bitmap are very similar to insertions in a simple multibit trie without
leaf pushing. A prefix insertion may cause a trie node to be changed completely; a new copy of the node
is created and linked in atomically to the existing trie. Compression results in Eatherton et al. (2004)
show that the tree bitmap has all the features of the Lulea scheme, in terms of compression and speed,
along with fast insertions. The tree bitmap also has the ability to be tuned for hardware implementations
ranging from the use of RAMBUS-like memories to on-chip SRAM.
