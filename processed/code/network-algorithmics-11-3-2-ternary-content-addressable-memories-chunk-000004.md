# network-algorithmics-11-3-2-ternary-content-addressable-memories (chunk 000004)

262      Chapter 11 Prefix-match lookups

leaves of the trie, instead of within nodes, as shown in Fig. 11.5. The result is that prefix matching can,
in the worst case, result in backtracking up the trie for a worst case of 64 memory accesses (32 down
the tree and 32 up).
    Given the simple alternative of using text strings to avoid backtracking, doing skip counts is a bad
idea. In essence, this is because the skip count transformation does not preserve information, while
the text string transformation does. However, because of the enormous influence of BSD, a number of
vendors and even other algorithms (e.g., Ref. Nilsson and Karlsson, 1998) have used skip counts in
their implementations.
