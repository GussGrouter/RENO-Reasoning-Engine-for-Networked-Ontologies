# network-algorithmics-11-11-binary-search-on-prefix-lengths (chunk 000001)

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
