# network-algorithmics-10-3-3-the-d-left-approach-now-we-introduce-d-left-the-state-of-art-solution-br (chunk 000002)

into which x can be inserted: buckets indexed by h1 (x), h2 (x), · · · , hd (x) respectively. Among them,
x is inserted into the bucket that is least occupied; ties are broken randomly (which gives the d-random
scheme its name). The objective of such a greedy insertion strategy is to keep the number of objects
inside each hash bucket as even as possible across the hash table, and as a result, to make the maximum
number of objects in any bucket as small as possible. Indeed, it was shown in Broder and Mitzenmacher
(2001) that, in d-random, given the same workload above of inserting n objects into a hash table with
n buckets, the expectation of this maximum number is reduced to (log log n/ log d) + O(1), from (1 +
o(1)) log n/ log log n when only a single random hash function is used.
    There are only two slight differences between d-left and d-random. First, in d-left, the hash table
is partitioned into d equal-sized (in number of buckets) logically independent subtables, each of which
contains n/d buckets (with indices 1, 2, · · · , n/d); in comparison, there is no such partitioning in d-
random. These d subtables are numbered 1, 2, · · · , d and arranged from left to right, so that subtable 1
is the leftmost, subtable 2 is the second leftmost, and so on. When an object x is to be inserted, each
of the d hash functions h1 , h2 , · · · , hd maps x to a hash value in the range [1, n/d]. The d candidate
buckets where x can be inserted are the bucket indexed by h1 (x) in subtable 1, the bucket indexed by
h2 (x) in the subtable 2, . . . , and the bucket indexed by hd (x) in subtable d. As in d-random, among
these d buckets, the one that is least occupied is where x should be inserted.
    Second, in d-left, a tie is broken in a very different way. In d-left if there are more than one least
occupied buckets among the d buckets where an object x should be inserted into, then x will be inserted
into the leftmost one among them (i.e., the one in the leftmost subtable). This tie-breaking strategy of
“going as left as possible” gives d-left its name.
    It has been shown that this tie-breaking strategy outperforms, in terms of resulting in a stochastically
smaller maximum (occupancy) number, other tie-breaking strategies such as the standard strategy of
breaking ties (uniformly) randomly. This finding is perhaps counterintuitive, or even surprising, to some
readers. In particular, how can an asymmetric strategy of “always going left” when there is a tie beat a
symmetric strategy of breaking ties randomly? We refer readers to Broder and Mitzenmacher (2001) for
an intuitive answer to this question, which is still quite subtle. Note that this “going left” tie-breaking
strategy performs better only when the performance metric is the maximum occupancy of any bucket.
For example, if the performance metric is instead the maximum total occupancy (number of objects in)
of any subtable, the random tie-breaking strategy performs better.
    Finally, we provide a brief comparison between d-left and perfect hashing. In practice, d-left can
achieve a similar maximum occupancy (of any bucket) as perfect hashing. In doing so, d-left does not
have to recompute the hash function from time to time (when the set of MAC addresses changes),
whereas perfect hashing does. As this recomputation can take a long time for a large set of MAC
addresses (e.g., minutes as reported in Broder and Mitzenmacher, 2001), perfect hashing may not be
suitable for a LAN environment where the set of MAC addresses “attached” to a switch changes fre-
quently, such as in a campus WiFi network. Compared to perfect hashing, the only obvious disadvantage
of d-left is that, when searching for an object x, all the d buckets where x may possibly appear have
to be probed. However, since these d buckets belong to logically independent subtables, the probing of
these d buckets can be performed in a parallel or pipelined manner (P5a), if these d subtables are put
in physically independent memory or cache modules.
