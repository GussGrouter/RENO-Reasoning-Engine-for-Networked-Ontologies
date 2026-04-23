# network-algorithmics-12-9-bit-vector-linear-search (chunk 000003)

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
