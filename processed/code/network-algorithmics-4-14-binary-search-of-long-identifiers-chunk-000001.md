# network-algorithmics-4-14-binary-search-of-long-identifiers (chunk 000001)

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
