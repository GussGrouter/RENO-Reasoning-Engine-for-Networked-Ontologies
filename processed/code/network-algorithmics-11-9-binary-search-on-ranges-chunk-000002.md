# network-algorithmics-11-9-binary-search-on-ranges (chunk 000002)

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
