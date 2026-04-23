# network-algorithmics-4-14-binary-search-of-long-identifiers (chunk 000002)

Solution
The trick is to add state to each element in each column, which can constrain the binary search to stay
within a guard range. This is shown in Fig. 4.27. In the figure, for each word like B in the leftmost
(most significant) column, add a pointer to the range of all other words that also contain B in this
position. Thus the first probe of the binary search for BMW starts with the B in BN X. On equality,
the search moves to the second column, as before. However, search also keeps track of the guard range
corresponding to the B’s in the first column. The figure shows that the guard range includes only rows
4 through 7. This guard range is stored with the first B compared (see arrows in Fig. 4.27).
    Thus when the search moves to column 2 and finds that M in BMW is less than the N in BN X,
it attempts to halve the range as before and to try a second probe at the third entry (the M in AMW).
However, the third entry is lower than the high point of the current guard range (4 through 7, assuming

4.15 Video conferencing via asynchronous transfer mode                         105

the first element is numbered 1). So without doing a compare, the search tries to halve the binary search
range again. This time the search tries entry 4, which is in the guard range. The search finds equality,
moves to the right, and finds BMW , as desired.
    In general, every multiword entry W1 , W2 , . . . , Wn will store a precomputed guard range. The range
for Wi points to the range of entries that have W1 , W2 , . . . , Wi in the first i words. This ensures that on a
match with Wi in the ith column, the binary search in column i + 1 will search only in this guard range.
For example, the N entry in BN Y (second column) has a guard range of 5–7, because these entries all
have BN in the first two words.
    The resulting search strategy takes log2 N + W probes if there are N identifiers. The cost is the
addition of two 16-bit pointers to each word. Since most word sizes are at least 32 bits, this results in
adding 32 bits of pointer space for each word, which can at most double memory usage. Besides adding
state, a second dominant idea is to use precomputation (P2a) to trade a slower insertion time for a faster
search. The idea is due to Butler Lampson.

Exercise

• (This is harder than the usual exercises.) The naive method of updating the binary search data struc-
  ture requires rebuilding the entire structure (especially because of the precomputed ranges) when
  a new entry is added or deleted. However, the whole scheme can be elegantly represented by a bi-
  nary search tree, with each node having the usual > and < pointers but also an = pointer, which
  corresponds to moving to the next column to the right, as shown earlier. The subtree corresponding
  to the = pointer naturally represents the guard range. The structure now looks like a trie of binary
  search trees. Use this observation and standard update techniques for balanced binary trees and tries
  to obtain logarithmic update times.
