# network-algorithmics-11-17-exercises-1-caching-prefixes-suppose-we-have-the-prefixes-10-100-and-100 (chunk 000003)

entry in a trie node has pointer p and prefix P , we push P to the top of the node pointed to by
    p. Thus we would push the prefix P8 in the 100 entry of the root of Fig. 11.7 to the top of the
    rightmost trie node.
    • We cited leaf pushing as one of the reasons for slow insertion times in the Lulea scheme. Does
      next-node pushing allow incremental insertion for the Lulea scheme?
    • How would you modify trie search to take into account the fact that prefixes can be stored at
      the top of (potentially large) trie nodes? How would this increase the search time (in memory
      accesses) of the Lulea scheme?
 8. CAM Node Compression: Instead of using the Lulea scheme for compression, we could just
    store all the prefixes within a trie node without expansion. If we use small trie nodes (3- or 4-bit
    strides), a chip can potentially read all the entries in a node and internally do a comparison to find
    the best-matching prefix within the node. Describe the details of such a scheme.
 9. Tree Bitmap Algorithm: The tree bitmap algorithm described in the text requires rooting through
    the internal prefix bitmap to decide if there was a matching prefix at a trie node N before moving
    on. This requires a greater access width (to access the internal prefix bitmaps) and more time.
    Consider adding state to the next node in the search path (P12) and one more final memory access
    to avoid this overhead.
10. Multicolumn Binary Search: In Chapter 4 we saw how to efficiently use binary search when
    the identifiers were wide. Explain how to combine this idea with that of binary search on prefixes
    explained in this chapter in order to do IPv6 lookups (up to 128-bit prefixes). How does this scheme
    compare with the other schemes in terms of lookup performance for IPv6?
11. Binary Search with Fast Incremental Updates: (This is difficult.) Find a way to remove all the
    problems of updates to binary search. The key problem is that if a large prefix range R contains lots
    of disjoint prefix ranges R1 , . . . Rk , then the spaces between the ranges Rk must be precomputed
    to map to R. If we now add a new prefix range, R  , that is contained in R but still contains R1
    through Rk , then all the spaces between the ranges Rk must be changed to map to the new range,
    R  . Since k can be O(n), this could lead to a O(n) update. Try to avoid this problem by storing the
    binary search database as a tree and storing information about precomputed prefixes that cover the
    space between ranges as high as possible in the tree, as opposed to storing in the leaves. Details
    can be found in Warkhede et al. (2001).
12. Counterexamples for Binary Search on Prefix Lengths: Even in industry, it is often useful to
    show by counterexample that worst cases can actually exist. This ensures that we are not doing
    unnecessary work, and it also silences people who say that the worst case will never be too bad.
    Imagine that Hugh Hopeful is working for the same startup building an IP lookup chip. The com-
    pany is now considering using binary search on prefix lengths.
    • Suppose we use only markers and no precomputation. This would make insertion a lot faster.
      Hugh Hopeful suggests that backtracking can only lead to a logarithmic number of extra ac-
      cesses. Find an example that leads to linear time.
    • Hugh Hopeful finds that in practice real databases add only 25% extra marker storage, much
      less than the log2 W multiplicative factor that we claimed. This is important because he would
      like to boast of a larger number of prefixes that his chip can handle for the given amount of
      memory. Give a worst-case example to show that we can add log2 W entries per marker.
