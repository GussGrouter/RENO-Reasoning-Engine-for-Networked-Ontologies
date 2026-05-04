# Network Algorithmics — 10.3 Challenge 3: scaling lookups to higher speeds (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 269
- Slice: from `10.3 Challenge 3: scaling lookups to higher speeds` up to next detected section heading

---

10.3 Challenge 3: scaling lookups to higher speeds
First, let’s understand why binary search forwarding does not scale to FDDI speeds. Binary search takes
log2 N memory accesses to look up a bridge database, where N is the size of the database. As bridges
grew popular, marketing feedback indicated that the database size needed to be increased from 8 K to
64 K. Thus using binary search, each search would take 16 memory accesses. Doing a search for the
source and destination addresses using 100-nanosecond DRAM would then take 3.2 microsecond.
    Unlike Ethernet, where small packets are padded to ensure a minimum size of 64 bytes, a minimum-
size packet consisting of FDDI, routing, and transport protocol headers could be as small as 40 bytes.
Given that a 40-byte packet can be received in 3.2 microsecond at 100 Mbps, two binary search lookups
would use up all of the packet-processing budget for a single link, leaving no time for other chores, such
as inserting and removing from link chip queues.
    One simple approach to meet the challenge of wire speed forwarding is to retain binary search but
to use faster hardware (P5). In particular, faster SRAM (Chapter 2) could be used to store the database.
Given a factor of 5–10 decrease in memory access time using SRAM in place of DRAM, binary search
will easily scale to wire speed FDDI forwarding.
    However, this approach is unsatisfactory for two reasons. First, it is more expensive because SRAM
is more expensive than DRAM. Second, using faster memory gets us lookups at FDDI speeds but will
not work for the next speed increment (e.g., Gigabit Ethernet). What is needed is a way to reduce the
number of memory accesses associated with a lookup so that bridging can scale with link technology.
Of the two following approaches to bridge-lookup scaling, one is based on hashing and the other on
hardware parallelism.


10.3.1 Scaling via hashing
In the 1990s DEC decided to build a fast crossbar switch connecting up to 32 links, called the Gi-
gaswitch (Souza et al., 1994). The switch-arbitration algorithms used in this switch will be described
in Chapter 13. This chapter concentrates on the bridge-lookup algorithms used in the Gigaswitch. The
vision of the original designers, Bob Simcoe and Bob Thomas, was to have the Gigaswitch be a switch
connecting point-to-point FDDI links without implementing bridge forwarding and learning. Bridge
lookups were considered to be too complex at 100-Mbps speeds.
    Into the development arena strode a young software designer who changed the product direction.
Barry Spinney, who had implemented an Ada compiler in his last job, was determined to do hardware
design at DEC. Barry suggested that the Gigaswitch be converted to a bridge interconnecting FDDI
local area networks. To do so, he proposed designing an FDDI-to-Gigaswitch network controller (FGC)

                                     10.3 Challenge 3: scaling lookups to higher speeds                      243




FIGURE 10.3
Gigaswitch hashing uses a hash function with a programmable multiplier, a small, balanced binary tree in every hash
bucket, and a backup CAM to hold the rare case of entries that result in more than seven collisions.


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



addresses. In such a case these entries are stored in a small hardware lookup database called a content
addressable memory or CAM (studied in more detail in Chapter 11).
    The CAM lookup occurs in parallel with the hash lookup. Finally, in the extremely rare case when
several dozen addresses are added to the CAM (say, when new station addresses are learned that cause
collisions), the central processor initiates a rehashing operation and distributes the new hash function
to the line cards. It is perhaps ironic that rehashing occurred so rarely in practice that one might worry
whether the rehashing code was adequately tested!
    The Gigaswitch became a successful product, allowing up to 22 FDDI networks to be bridged to-
gether with other link technologies, such as ATM. Barry Spinney was assigned US patent 5,920,900,
“Hash-based translation method and apparatus with multiple-level collision resolution.” While tech-
niques based on perfect hashing (Dietzfelbinger et al., 1988) have been around for a while in the
theoretical community, Spinney’s contribution was to use a pragmatic version of the perfect hashing
idea for high-speed forwarding.
