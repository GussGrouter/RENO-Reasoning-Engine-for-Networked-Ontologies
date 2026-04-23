# Network Algorithmics — 11.11 Binary search on prefix lengths (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 305
- Slice: from `11.11 Binary search on prefix lengths` up to next detected section heading

---

11.11 Binary search on prefix lengths
In this section we adapt another classical exact-match scheme, hashing, to longest prefix matching.
Binary search on prefix lengths finds the longest match using log2 W hashes, where W is the maximum
prefix length. This can provide a very scalable solution for 128-bit IPv6 addresses. For 128-bit prefixes,
this algorithm takes only seven memory accesses, as opposed to 16 memory accesses using a multibit
trie with 8-bit strides. To do so, the algorithm first segregates prefixes by length into separate hash
tables. More precisely, it uses an array L of hash tables such that L[i] is a pointer to a hash table
containing all prefixes of length i.
    Assume the same tiny routing table, with only two prefixes, P4 = 1* and P1 = 101*, of lengths 1
and 3, respectively, that was used in Fig. 11.15. Recall that this is a small subset of Fig. 11.6. The array
of hash tables is shown horizontally in the top frame (A) of Fig. 11.16. The length-1 hash table storing
P4 is shown vertically on the left and is pointed to by position 1 in the array; the length-3 hash table
storing P1 is shown on the right and is pointed to by position 3 in the array; the length-2 hash table is
empty because there are no prefixes of length 2.
    Naively, a search for address D would start with the greatest-length hash table l (i.e., 3), would
extract the first l bits of D into Dl , and then search the length-l hash table for Dl . If search succeeds,
the best match has been found; if not, the algorithm considers the next smaller length (i.e., 2). The
algorithm moves in decreasing order among the set of possible prefix lengths until it either finds a
match or runs out of lengths.
    The naive scheme effectively does linear search among the distinct prefix lengths. The analogy
suggests a better algorithm: binary search (P15). However, unlike binary search on prefix ranges, this is
binary search on prefix lengths. The difference is major. With 32 lengths, binary search on lengths takes
five hashes in the worst case; with 32,000 prefixes, binary search on prefix ranges takes 16 accesses.

                                                        11.11 Binary search on prefix lengths       279




FIGURE 11.16
From naive linear search on the possible prefix lengths to binary search.


    Binary search must start at the median prefix length, and each hash must divide the possible prefix
lengths in half. A hash search gives only two values: found and not found. If a match is found at length
m, then lengths strictly greater than m must be searched for a longer match. Correspondingly, if no
match is found, search must continue among prefixes of lengths strictly less than m.
    For example, in Fig. 11.16, part (A), suppose search begins at the median length-2 hash table for an
address that starts with 101. Clearly, the hash search does not find a match. But there is a longer match
in the length-3 table. Since only a match makes search move to the right half, an “artificial match,” or
marker, must be introduced to force the search to the right half when there is a potentially longer match.
    Thus part (B) introduces a bolded marker entry 10, corresponding to the first two bits of prefix P1
= 101, in the length-2 table. In essence, state has been added for speed (P12). The markers allow probe
failures in the median to rule out all lengths greater than the median.
    Search for an address D that starts with 101 works correctly. Search for 10 in the length-2 table
(in part (B) of Fig. 11.16) results in a match; search proceeds to the length-3 table, finds a match with

280      Chapter 11 Prefix-match lookups



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
