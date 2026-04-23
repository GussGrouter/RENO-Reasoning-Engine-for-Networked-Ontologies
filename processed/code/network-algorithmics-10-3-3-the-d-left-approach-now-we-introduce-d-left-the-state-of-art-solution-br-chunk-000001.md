# network-algorithmics-10-3-3-the-d-left-approach-now-we-introduce-d-left-the-state-of-art-solution-br (chunk 000001)

# Network Algorithmics — 10.3.3 The d-left approach Now we introduce d-left, the state of art solution (Broder and Mitzenmacher, 2001) to the exact-match (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 272
- Slice: from `10.3.3 The d-left approach Now we introduce d-left, the state of art solution (Broder and Mitzenmacher, 2001) to the exact-match` up to next detected section heading

---

10.3.3 The d-left approach
Now we introduce d-left, the state of art solution (Broder and Mitzenmacher, 2001) to the exact-match
problem that has been used in Cisco switch products. The objective of this approach is similar to that of
perfect hashing: to minimize the maximum number of objects hashed into any bucket in a hash table.
However, when a random hash function is used, this maximum is known to be much larger than the
average (Gonnet, 1981). More precisely, when n objects are hashed into n buckets, the expectation of
this maximum is (1 + o(1)) log n/ log log n (with high probability). As explained earlier, the objective
of perfect hashing is to reduce this maximum to a small number (say 2 or 3) so that every bucket can
fit into a memory block, using a hash function that is perfect for the set of keys to be inserted into the
hash table; as a result, much precomputation is needed to find such a perfect hash function.
     d-left is a variation of a slightly older idea called d-random that is now widely known as “the
power of d choices” (Mitzenmacher, 1996). The original idea of d-random is to use d > 1 random hash
functions (say h1 , h2 , · · · , hd ) instead of one. Given a hash key x, there are d candidate hash buckets

246      Chapter 10 Exact-match lookups
