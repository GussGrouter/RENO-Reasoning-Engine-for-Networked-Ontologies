# Network Algorithmics — 12.9 Bit vector linear search (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 343
- Slice: from `12.9 Bit vector linear search` up to next detected section heading

---

12.9 Bit vector linear search
Consider doing a match in one of the individual columns in Fig. 12.10, say, the destination address
field, and finding a bit string S as the longest match. Clearly, this lookup result eliminates any rules
that do not match S in this field. Then the search algorithm can do a linear search in the set of all
remaining rules that match S. The logical extension is to perform individual matches in each field; each
field match will prune away a number of rules, leaving a remaining set. The search algorithm needs to
search only the intersection of the remaining sets obtained by each field lookup.
    This would clearly be a good heuristic for optimizing the average case if the remaining sets are
typically small. However, one can guarantee performance even in the worst case (to some extent) by
representing the remaining sets as bitmaps and by using wide memories to retrieve a large number of
set members in a single memory access (P4a, exploit locality).
    In more detail, as in Section 12.8, divide-and-conquer is used to slice the database, as in Fig. 12.10.
However, in addition with each possible value M of field i, the algorithm stores the set of rules S(M)
that match M in field i as a bit vector. This is easy to do when building the sliced table. The algorithm
that builds the data structure scans through the rules linearly to obtain the rules that match M using the
match rule (e.g., exact, prefix, or range) specified for the field.
    For example, Fig. 12.11 shows the sliced database of Fig. 12.10 together with bit vectors for each
sliced field value. The bit vector has 8 bits, one corresponding to each of the eight possible rules in
Fig. 12.2. Bit j is set for value M in field i if value M matches Rule j in field i.
    Consider the destination prefix field and the first value M in Fig. 12.11. If we compare it to Fig. 12.2,
we see that the first four rules specify M in this field. The fifth rule specifies T I (which does not
match M), and the sixth and eighth rules specify a wildcard (which matches M). Finally, the seventh
rule specifies the prefix N et (which matches M, because N et is assumed to be the prefix of the company
network in which M is the mail gateway). Thus the bitmap for M is 11110111, where the only bit not
set is the fifth bit. This is because the fifth rule has T I , which does not match M.

                                                                      12.9 Bit vector linear search                317




FIGURE 12.11
The sliced database of Fig. 12.10 together with bit vectors for every possible sliced value. The bit vector has 8 bits,
one corresponding to each of the eight possible rules in Fig. 12.2. Bit j is set for value M in field i if value M
matches Rule j in field i.


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



linear search can be parallelized, using N -way parallelism; what matters are the amount of parallelism
that can be employed at a reasonable cost.
    Using our old example, consider a lookup for a packet to M from S with UDP destination port
equal to 53 and source port equal to 1029 in the database of Fig. 12.2, as represented by Fig. 12.11.
This packet matches Rules 2, 3, and 8 but must be allowed through because the first matching rule is
Rule 2.
    Using the bit vector algorithm just described (see Fig. 12.11), the longest match in the destination
field (i.e., M) yields the bitmap 11110111. The longest match in the source field (i.e., S) yields the
bitmap 11110011. The longest match in the destination port field (i.e., 53) yields the bitmap 01100111.
The longest match in the source port field (i.e., the wildcard) yields the bitmap 11110111; the longest
match in the protocol field (i.e., U DP ) yields the bitmap 11111101. The AND of the five bitmaps is
01100001. This bitmap corresponds to matching Rules 2, 3, and 8. The index of the first bit set is 2.
This corresponds to the second rule, which is indeed the correct match.
    The bit vector algorithm was described in detail in Lakshman and Stidialis (1998) and also in a
few lines in a paper on network monitoring (Malan and Jahanian, 1998). The first paper (Lakshman
and Stidialis, 1998) also describes some trade-offs between search time and memory. A later paper
(Baboescu and Varghese, 2001) shows how to add more state for speed (P12) by using summary bits.
For every W bits in a bitmap, the summary is the OR of the bits. The main intuition is that if, say, W 2
bits are zero, this can be ascertained by checking W summary bits.
    The bit vector scheme is a good one for moderate-size databases. However, since the heart of the
algorithm relies on linear search, it cannot scale to both very large databases and very high speeds.
    The performance of this scheme can be described as follows.
Assumption: The number of rules will stay reasonably small or will grow only in proportion to
      increases in bus width and parallelism made possible by technology improvements.
Performance: The number of memory accesses is N · (K + 1)/W plus the number of memory ac-
      cesses for K longest-matching-prefix or narrowest-range operations. The memory required is
      that for the K individual field matches (see schemes in Chapter 11) plus potentially N 2 K bits.
      Recall that N is the number of rules, K is the number of fields, and W is the width of a memory
      access. Updating rules is slow and generally requires rebuilding the entire database.
