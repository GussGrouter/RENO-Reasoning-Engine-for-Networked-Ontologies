# network-algorithmics-11-11-binary-search-on-prefix-lengths (chunk 000003)

P 1, and terminates. In general, a marker for a prefix P must be placed at all lengths that binary search
will visit in a search for P . This adds only a logarithmic number of markers. For a prefix of length 32,
markers are needed only at lengths 16, 24, 28, and 30.
    Unfortunately, the algorithm is still incorrect. While markers lead to potentially longer prefixes, they
can also cause search to follow false leads. Consider a search for an address D  whose first three bits
are 100 in part (B) of Fig. 11.16. Since the median table contains 10, search in the middle hash table
results in a match. This forces the algorithm to search in the third hash table for 100 and to fail. But the
correct best matching prefix is at the first hash table – i.e., P4 = 1*. Markers can cause the search to
go off on a wild goose chase! On the other hand, a backtracking search of the left half would result in
linear time.
    To ensure logarithmic time, each marker node M contains a variable M.bmp, where M.bmp is
the longest prefix that matches string M. This is precomputed when M is inserted into its hash table.
When the algorithm follows marker M and searches for prefixes of lengths greater than M, and if the
algorithm fails to find such a longer prefix, then the answer is M.bmp. In essence, the best matching
prefix of every marker is precomputed (P2a). This avoids searching all lengths less than the median
when a match is obtained with a marker.
    The final version of the database containing prefixes P4 and P1 is shown in part (C) of Fig. 11.16.
A bmp field has been added to the 10 marker that points to the best matching prefix of the string 10 (i.e.,
P4 = 1*). Thus when the algorithm searches for 100 and finds a match in the median length-2 table, it
remembers the value of the corresponding bmp entry P4 before it searches the length-3 table. When the
search fails (in the length-3 table), the algorithm returns the bmp field of the last marker encountered
(i.e., P4).
    A trivial algorithm for building the simple binary search data structure from scratch is as follows.
First determine the distinct prefix lengths; this determines the sequence of lengths to search. Then add
each prefix P in turn to the hash table corresponding to length(P ). For each prefix, also add a marker
to all hash tables corresponding to lengths L < length(P ) that binary search will visit (if one does not
already exist). For each such marker M, use an auxiliary 1-bit trie to determine the best matching prefix
of M. Further refinements are described in Waldvogel et al. (1997).
    While the search algorithm takes five hash table lookups in the worst case for IPv4, we note that in
the expected case most lookups should take two memory accesses. This is because the expected case
observation O1 shows that most prefixes are either 16 or 24 bits (at least today). Thus doing binary
search at 16 and then 24 will suffice for most prefixes.
    The use of hashing makes binary search on prefix lengths somewhat difficult to implement in hard-
ware. However, its scalability to large prefix lengths, such as IPv6 addresses, is notable.
