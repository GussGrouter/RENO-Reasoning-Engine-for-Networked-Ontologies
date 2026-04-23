# Network Algorithmics — 11.9 Binary search on ranges (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 302
- Slice: from `11.9 Binary search on ranges` up to next detected section heading

---

11.9 Binary search on ranges
So far, all our schemes (unibit tries, expanded tries, LC tries, Lulea tries, tree bitmaps) have been
trie variants. Are there other algorithmic paradigms (P15) to the longest-matching-prefix problem?
Now, exact matching is a special case of prefix matching. Both binary search and hashing (Cormen et
al., 1990) are well-known techniques for exact matching. Thus we should consider generalizing these
standard exact-matching techniques to handle prefix matching. In this section we examine an adaptation
of binary search; in the next section we look at an adaptation of hashing.
     In binary search on ranges (Lampson et al., 1998), each prefix is represented as a range, using the
start and end of the range. Thus the range endpoints for N prefixes partition the space of addresses
into 2N + 1 disjoint intervals. The algorithm (Lampson et al., 1998) uses binary search to find the
interval in which a destination address lies. Since each interval corresponds to a unique prefix match,
the algorithm precomputes this mapping and stores it with range endpoints. Thus prefix matching takes
log2 (2N ) memory accesses.
     Consider a tiny routing table with only two prefixes, P4 = 1* and P1 = 101*. This is a small subset
of the database used in Fig. 11.6. Fig. 11.15 shows how the binary search data structure is built as a
table (left) and as a binary tree (right).
     The starting point for this scheme is to consider a prefix as a range of addresses. To keep things
simple, imagine that addresses are 4 bits instead of 32 bits. Thus P4 = 1* is the range 1000 to 1111,
and P1 = 101* is the range 1010 to 1011. Next, after adding in the range for the entire address space
(0000 to 1111), the endpoints of all ranges are sorted into a binary search table, as shown on the left of
Fig. 11.15.
     In Fig. 11.15, the range endpoints are drawn vertically on the left. The figure also shows the ranges
covered by each of the prefixes. Next, two next-hop entries are associated with each endpoint. The
leftmost entry, called the > entry, is the next hop corresponding to addresses that are strictly greater
than the endpoint but strictly less than the next range endpoint in sorted order. The rightmost entry,
called the = entry, corresponds to addresses that are exactly equal to the endpoint.
     For example, it should be clear from the ranges covered by the prefixes that any addresses
greater than or equal to 0000 but strictly less than 1000 do not match any prefix. Hence the entries

276        Chapter 11 Prefix-match lookups




FIGURE 11.15
Binary search on values of a tiny subset of the sample database, consisting of only prefixes P4 = 1* and P1 = 101*.


corresponding to 0000 are −, to denote no next hop.3 Similarly, any address greater than or equal to
1000 but strictly less than 1010 must match prefix P4 = 1*.
    The only subtle case, which illustrates the need for two separate entries for > and =, is the entry
for 1011. If an address is strictly greater than 1011 but strictly less than the next entry, 1111, then the
best match is P4. Thus the > pointer is P 4. On the other hand, if an address is exactly equal to 1011,
its best match is P1. Thus the = pointer is P1.
    The entire data structure can be built as a binary search table, where each table entry has three
items, consisting of an endpoint, a > next-hop pointer, and a = next-hop pointer. The table has at most
2N entries, because each of N prefixes can insert two endpoints. Thus after the next-hop values are
precomputed, the table can be searched in log2 2N time using binary search on the endpoint values.
Alternatively, the table can be drawn as a binary tree, as shown on the right in Fig. 11.15. Each tree
node contains the endpoint value and the same two next-hop entries.
    The description so far shows that binary search on values can find the longest prefix match after
log2 2N time. However, the time can be reduced using binary trees of higher radix, such as B-trees.
While such trees require wider memory accesses, this is an attractive trade-off for DRAM-based mem-
ories, which allow fast access to consecutive memory locations (P4a).
    Computational geometry (Preparata and Shamos, 1985) offers a data structure called a range tree
for finding the narrowest range. Range trees offer fast insertion times as well as fast O(log2 N ) search
times. However, there seems to be no easy way to increase the radix of range trees to obtain O(logM N )
search times for M > 2.
    As described, this data structure can easily be built in linear time using a stack and an additional
trie. It is not hard to see that even with a balanced binary tree (see exercises), adding a short prefix can
change the > pointers of a large number of prefixes in the table. A trick to allow fast insertions and
deletions in logarithmic time is described in Warkhede et al. (2001).
    Naively done, binary search on prefix values is somewhat slow when compared to multibit tries.
However, unlike the other trie schemes, all of which are subject to patents, binary search is free of such
restrictions. Thus at least a few vendors have implemented this scheme into hardware. In hardware, the


3 In a core router, no prefix match implies that the message should be dropped; in a router within a domain no prefix match is
often sent to the so-called default route.

                            11.10 Binary search on ranges with Initial Lookup Table                   277



use of a wide memory access (to reduce the base of the logarithm) and pipelining (to allow one lookup
per memory access) can make this scheme sufficiently fast.
    The original paper (Lampson et al., 1998) written in 1998 suggests two optimizations to improve
speed even in software. First, it suggests improving “the worst-case number of memory accesses of the
basic binary search scheme with a precomputed table of best-matching prefixes for the first bits . . . if
there are prefixes of longer length with that prefix the array element stores a pointer to a binary search
table/tree that contains all such prefixes” (Lampson et al., 1998). The paper shows that this simple trick
of using an array as a front-end reduces the maximum number of prefixes in each partitioned table from
over 38000 to 336, reducing the worst case binary table size to 336, which makes binary search faster
(10 memory accesses versus log2 N + 1 where N is the size of the original table). Second, it suggests
using larger radixes instead of binary trees and exploiting the cache line size of a Pentium processor to
make such k-way searh efficient in software.
    Best of all, a highly optimized form of the original binary search on prefix ranges paper with initial
table lookup (Lampson et al., 1998) called DXR (Zec et al., 2012) first suggested in 2021 currently
appears to offer the fastest software implementations of over 2.5 Billion IP lookups per second on
a commodity CPU (AMD R7-1700) with 8 cores in 2022. This makes it a good building block for
Network Function Virtualization devices. We now describe the new optimizations in DXR.
