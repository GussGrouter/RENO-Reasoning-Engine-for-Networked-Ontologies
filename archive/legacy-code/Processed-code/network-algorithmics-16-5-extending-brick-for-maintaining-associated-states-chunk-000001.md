# network-algorithmics-16-5-extending-brick-for-maintaining-associated-states (chunk 000001)

# Network Algorithmics — 16.5 Extending BRICK for maintaining associated states (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 488
- Slice: from `16.5 Extending BRICK for maintaining associated states` up to next detected section heading

---

16.5 Extending BRICK for maintaining associated states
The approach of combining randomized bundling and rank indexing has also been used for a similar but
different application: memory- and computation-efficient storage and lookup of exact or approximate
states associated with flow labels. The resulting scheme is called Rank Indexed Hashing (RIH) (Hua et
al., 2008a). In Section 10.3.3 we have already described a hash-table-based scheme that can be adapted

462       Chapter 16 Measuring network traffic

FIGURE 16.6
Buckets and hash-chain locations.

for maintaining such states: d-Left hashing (Broder and Mitzenmacher, 2001). Compared to d-Left,
RIH is more memory-efficient and, by taking advantage of built-in CPU instructions such as popcount,
is similarly computationally efficient, as shown in Hua et al. (2008a).
    The design of RIH is based on the same two key ideas as that of BRICK: randomized bundling
and rank-indexed chaining. Hence, we provide only a brief description, in this new context, of both
innovations using a few figures. Conceptually, the starting point of RIH is a conventional chaining-
based hash-table scheme. As also shown in Fig. 16.6 its first key idea is to randomly bundle a decent
number of hash buckets (with chaining) together so that the number of hash nodes in each bundle (called
hash-chain locations in Hua et al. (2008a)) is not far from the average number statistically, like that is
shown in Fig. 16.3 (the “BRICK wall”). In this way we only need to allocate a fixed amount of memory
that is slightly more than the average amount to each “hash bundle” to satisfy its resource needs with
high probability.
    In a chaining-based hash table maintaining a 32- or 64-bit pointer for each hash node is costly,
especially when the hash key and the associated state are both short in length, which, as shown in Hua
et al. (2008a), can happen in practice. In Fig. 16.7(A) the fingerprints are 7 bits long; the associated state
is not shown in Fig. 16.7(A) to better convey the main idea. The second key idea of RIH, illustrated
in Fig. 16.7, is a rank indexing method, similar to that in BRICK, that allows us to efficiently realize
dynamic chaining without storing and paying the large cost of full-size pointers.
    Instead, like subcounters that comprise a counter in BRICK, consecutive hash nodes in a bucket
are linked together using single-bit “rank index pointers,” as shown in Fig. 16.7(B). However, whereas
in BRICK sub-counters of a counter can have various lengths, in RIH each hash node, including the
signature (the hash value of the flow label by a different hash function than that for the hash table oper-
tion) and the associated state, has the same length. This allows us to “collapse” all hash nodes into one
pile and the corresponding single-bit “rank index pointers” into another, as illustrated in Fig. 16.7(C).

16.5 Extending BRICK for maintaining associated states   463

FIGURE 16.7
Rank-indexed hashing.

464      Chapter 16 Measuring network traffic

Such a collapse facilitates more efficient storage of these contents and pointers and faster read access
to them. Finally, like in BRICK, we can accommodate the insertion and deletion of hash nodes in RIH
in a computationally efficient manner.
