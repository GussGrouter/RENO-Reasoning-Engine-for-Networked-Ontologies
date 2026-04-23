# network-algorithmics-11-9-binary-search-on-ranges (chunk 000003)

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
