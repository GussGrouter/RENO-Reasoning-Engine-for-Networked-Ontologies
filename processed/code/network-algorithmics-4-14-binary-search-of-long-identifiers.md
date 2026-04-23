# Network Algorithmics — 4.14 Binary search of long identifiers (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 130
- Slice: from `4.14 Binary search of long identifiers` up to next detected section heading

---

4.14 Binary search of long identifiers
The next-generation Internet (IPv6) plans to use larger, 128-bit addresses to accommodate more Internet
endpoints. Suppose the goal is to look up 128-bit addresses. Assume the algorithm works on a machine
whose natural word size is 32 bits. Then each comparison of two 128-bit numbers will take 128/32 = 4
operations to compare each word individually. In general, suppose each identifier in the table is W
words long. In our example, W = 4. Naive binary search will take W · log N comparisons, which is
expensive. Yet this seems obviously wasteful. If all the identifiers have the same first W − 1 words, then
clearly log N comparisons are sufficient. The problem is to modify binary search to take log N + W
comparisons. The strategy is to work in columns, starting with the most significant word and doing
binary search in that column until equality is obtained in that column. At that point, the algorithm
moves to the next word to the right and continues the binary search where it left off.
    Thus in Fig. 4.26, which has W = 3, consider a search for the three-word identifier BMW . Pretend
each character is a word. Start by comparing in the leftmost column in the middle element, as shown
by the arrow labeled 1.1 Since the B in the search string matches the B at the arrow labeled 1, the
search moves to the right (not shown) to compare the M in BMW with the N in the middle location of
the second column. Since N < M, the search performs the second probe at the quarter position of the
second column. This time the two M’s match and the search moves rightward and finds W , but (oops!)
the search has found AMW , not BMW as desired. This leads to the following problem.



1 Many implementors implement binary search to pick the fourth element from the top (i.e., the first B) as the middle and not
the fifth element as we have done. Keep this somewhat unusual convention in mind while following the example.

104       Chapter 4 Principles in action




FIGURE 4.26
Binary search of long identifiers can result in a multiplicative factor of W , the number of words in an identifier. The
naive method of reducing this to an additive factor by moving to the right on equality fails.




FIGURE 4.27
Adding a guard range to every element in a column to allow binary search to work correctly when switching
columns.


Problem
Find some state that can be added to each element in each column that can fix this algorithm to work
correctly in log N + W comparisons.
Hint: The problem is caused by the fact that when the search moved to the quarter position in
column 2, it assumed that all elements in the quarter of the second column begin with B. This
assumption is false in general. What state can be added to avoid making this false assumption, and
how can the search be modified to use this state?

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
