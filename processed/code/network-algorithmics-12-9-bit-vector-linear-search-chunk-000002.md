# network-algorithmics-12-9-bit-vector-linear-search (chunk 000002)

When a packet header arrives with fields H [1] . . . H [K], the search algorithm first performs a
longest-matching-prefix lookup in each field i to obtain matches Mi and the corresponding set S(Mi )
of matching rules. The search algorithm then proceeds to compute the intersection of all the sets S(Mi )
and returns the lowest-cost element in the intersection set.
    But if rules are arranged in nondecreasing order of cost and all sets are bitmaps, then the intersection
set is the AND of all K bitmaps. Finally, the lowest-cost element corresponds to the index of the first
bit set in the intersection bitmap. But, the reader may object, since there are N rules, the intersected
bitmaps are N bits long. Hence, computing the AND requires O(N ) operations. So the algorithm is
effectively doing a linear search after slicing and doing individual field matches. Why not do simple
linear search instead?
    The reason is subtle and requires a good grasp of models and metrics. Basically, the preceding
argument above is correct but ignores the large constant-factor improvement that is possible using
bitmaps. Thus computing the AND of K bit vectors and searching the intersection bit vector is still an
O(K · N ) operation; however, the constants are much lower than doing naive linear search because we
are dealing with bitmaps. Wide memories (P4a) can be used to make these operations quite cheap, even
for a large number of rules.
    This is because the cost in memory accesses for these bit operations is N · (K + 1)/W memory
accesses, where W is the width of a memory access. Even with W = 32, this brings down the number
of memory accesses by a factor of 32. A specialized hardware classification chip can do much better.
Using wide memories and wide buses (the bus width is often the limiting factor), a chip can easily
achieve W = 1000 with today’s technology. As technology scales, one can expect even larger memory
widths.
    For example, using W = 1000 and k = 5 fields, the number of memory accesses for 5000 rules
is 5000 ∗ 6/1000 = 30. Using 10-nanosecond SRAM, this allows a rule lookup in 300 nanoseconds,
which is sufficient to process minimum-size (40-byte) packets at wire speed on a gigabit link. By using
K-fold parallelism, the further factor of K + 1 can be removed, allowing 30,000 rules. Of course, even

318      Chapter 12 Packet classification
