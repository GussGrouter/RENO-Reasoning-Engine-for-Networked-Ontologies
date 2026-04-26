# network-algorithmics-11-5-3-incremental-update-simple-insertion-and-deletion-algorithms-exist-for-mu (chunk 000001)

# Network Algorithmics — 11.5.3 Incremental update Simple insertion and deletion algorithms exist for multibit tries. Consider the addition of a prefix P. The (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 293
- Slice: from `11.5.3 Incremental update Simple insertion and deletion algorithms exist for multibit tries. Consider the addition of a prefix P. The` up to next detected section heading

---

11.5.3 Incremental update
Simple insertion and deletion algorithms exist for multibit tries. Consider the addition of a prefix P. The
algorithm first simulates search on the string of bits in the new prefix P up to and including the last
complete stride in prefix P. Search will terminate either by ending with the last (possibly incomplete)
stride or by reaching a nil pointer. Thus for adding P10 = 1100* to the database of Fig. 11.7, search
follows the 110-pointer and terminates at the leftmost leaf trie node X.
    For the purposes of insertion and deletion, for each node X in the multibit trie, the algorithm main-
tains a corresponding 1-bit trie, with the prefixes stored in X. This auxiliary structure need not be in fast
memory. Also, for each node array element, the algorithm stores the length of its present best match.
After determining that P10 must be added to node X, the algorithm expands P10 to the stride of X. Any
array element to which P10 expands (which is currently labeled with a prefix of a length smaller than
P10) must be overwritten with P10.

11.6 Level-compressed (LC) tries                    267

FIGURE 11.10
The level-compressed (LC) trie scheme decomposes the 1-bit trie recursively into full subtries of the largest size
possible (left). The children in each full subtrie (shown by the dotted boxes) are then placed in a trie node to form a
variable-stride trie that is specific to the database chosen.

Thus in adding P10 = 1100*, the algorithm must add the expansions of 0* into node X. In particular,
the 000 and 001 entries in node X must be updated to be P10.
    If the search ends before reaching the last stride in the prefix, the algorithm creates new trie nodes.
For example, if the prefix P11 = 1100111* is added, search fails at node X when a nil pointer is found
at the 011 entry. The algorithm then creates a new pointer at this location that is made to point to a new
trie node that contains P11. P11 is then expanded in this new node.
    Deletion is similar to insertion. The complexity of insertion and deletion is the time to perform a
search (O(W )) plus the time to completely reconstruct a trie node (O(S), where S is the maximum
size of a trie node). For example, using 8-bit trie nodes, the latter cost will require scanning roughly
28 = 256 trie node entries. Thus to allow for fast updates, it is crucial to also limit the size of any trie
node in the dynamic program described earlier.
