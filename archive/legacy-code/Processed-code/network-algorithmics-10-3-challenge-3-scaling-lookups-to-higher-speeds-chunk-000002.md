# network-algorithmics-10-3-challenge-3-scaling-lookups-to-higher-speeds (chunk 000002)

chip on the line cards that would implement a hashing-based algorithm for lookups. The Gigaswitch
article (Souza et al., 1994) states that each bridge lookup makes at most four reads from memory.
    Now, every student of algorithms (Cormen et al., 1990) knows that hashing, on average, is much
faster (constant time) than binary search (logarithmic time). However, the same student also knows that
hashing is much slower in the worst case, potentially taking linear time because of collisions. How,
then, can the Gigaswitch hash lookups claim to take at most four reads to memory in the worst case
even for bridge databases of size 64K, whereas binary search would require 16 memory accesses?
    The Gigaswitch trick has its roots in an algorithmic technique (P15) called perfect hashing (Diet-
zfelbinger et al., 1988; Belazzougui et al., 2009; Limasset et al., 2017). The idea is to use a param-
eterized hash function, where the hash function can be changed by varying some parameters. Then
appropriate values of the parameters can be precomputed (P2a) to obtain a hash function such that the
worst-case number of collisions is small and bounded.
    While finding such a good hash function may take (in theory) a large amount of time, this is a good
trade-off because this new station’s addresses do not get added to local area networks at a very rapid
rate. On the other hand, once the hash function has been picked, lookup can be done at wire speeds.
    Specifically, the Gigaswitch hash function treats each 48-bit address as a 47-degree polynomial
in the Galois field of order 2, GF(2). While this sounds impressive, this is the same arithmetic used
for calculating CRCs; it is identical to ordinary polynomial arithmetic, except that all additions are
done mod 2. A hashed address is obtained by the equation A(X) ∗ M(X) mod G(X), where G(X) is
the irreducible polynomial X 48 + X 36 + X 25 + X 10 + 1, M(X) is a nonzero, 47-degree programmable
hash multiplier, and A(X) is the address expressed as a 47-degree polynomial.
    The hashed address is 48 bits. The bottom 16 bits of the hashed address is then used as an index
into a 64K-entry hash table. Each hash table entry [see Fig. 10.3 as applied to the destination address
lookup, with D(x) being used in place of A(x)] points to the root of a balanced binary tree of height at
most 3. The hash function has the property that it suffices to use only the remaining high-order 32 bits
of the hashed address to disambiguate collided keys.
    Thus the binary tree is sorted by these 32-bit values, instead of the original 48-bit keys. This saves
16 bits to be used for associated lookup information. Thus any search is guaranteed to take no more
than four memory accesses, one to lookup the hash table and three more to navigate a height-3 binary
tree.
    It turns out that picking the multiplier is quite easy in practice. The coefficients of M(x) are picked
randomly. Having picked M(x), it sometimes happens that a few buckets have more than seven colliding

244       Chapter 10 Exact-match lookups
