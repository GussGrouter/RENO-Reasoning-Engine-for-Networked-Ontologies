# network-algorithmics-11-7-lulea-compressed-tries (chunk 000003)

uncompressed index must be mapped to an index into the compressed node. This mapping is accom-
plished by counting bits within the node bitmap.
    Consider the data structure on the right of Fig. 11.12 and a search for an address that starts with
100111. If we were dealing with just the uncompressed node on the left of Fig. 11.12, we could use 100
to index into the fifth array element to get ptr1. However, we must now obtain the same information
from the compressed-node representation on the right of Fig. 11.12.
    Instead, we use the first three bits (100) to index into the root-node bitmap. Since this is the second
bit set (the algorithm needs to count the bits set before a given bit), the algorithm indexes into the
second element of the compressed node. This produces a pointer ptr1 to the rightmost trie node. Next,
imagine the rightmost leaf node of Fig. 11.7 (after leaf pushing) also compressed in the same way. The
node contains the sequence P7, P6, P6, P6, P8, P8, P8, P8. Thus the corresponding bitmap is 11001000,
and the compressed sequence is P7, P6, P8.
    Thus in the rightmost leaf node, the algorithm uses the next 3 bits (111) of the destination address
to index into bit 8. Since this bit is a 0, the search terminates: There is no pointer to follow in the
equivalent uncompressed node. However, to retrieve the best matching prefix (if any) at this node, the
algorithm must find any prefix stored before this entry.
    This would be trivial with expansion because the value P8 would have been expanded into the 111
entry, but since the expanded sequence of P8 values has been replaced by a single P8 value in the
compressed version, the algorithm has to work harder. Thus the Lulea algorithm counts the number
of bits set before position 8 (which happens to be 3) and then indexes into the third element of the
compressed sequence. This gives the correct result P8.
    The Lulea paper (Degermark et al., 1997) describes a trie that uses fixed strides of 16, 8, and 8. But
how can the algorithm efficiently count the bits set in a large bitmap, say of 64K bits in size, that a
16-bit stride needs to use? Before you read on, try to answer this question using principles P12 (adding
state for speed) and P2a (precomputation).
    To speed up counting set bits, the algorithm accompanies each bitmap with a summary array that
contains a cumulative count (precomputed) of the number of set bits associated with fixed-size chunks
of the bitmap. Using 64-bit chunks, the summary array takes negligible storage. Counting the bits set
up to position i now takes two steps. First, access the summary array at position j , where j is the chunk
containing bit i. Then access chunk j and count the bits in chunk j up to position i. The sum of the two
values gives the count.
    While the Lulea paper uses 64-bit chunks, the example in Fig. 11.13 uses 8-bit chunks. The large
bitmap is shown from left to right, starting with 10001001, as the second array from the top. Each 8-bit
chunk has a summary count that is shown as an array above the bitmap. The summary count for chunk
i counts the cumulative bits in the previous chunks of the bitmap (not including chunk i).
    Thus the first chunk has count 0, the second has count 3 (because 10001001 has three bits set), and
the third has count 5 (because 10000001 has two bits set, which added to the previous chunk’s value of
3 gives a cumulative count of 5).
    Consider searching for the bits set up to position X in Fig. 11.13, where X can be written as J011.
Clearly, X belongs to chunk J . The algorithm first looks up the summary count array to retrieve
numSet[J ]. This yields the number of bits set up to but not including chunk J . The algorithm then
retrieves chunk J itself (10011000) and counts the number of bits set until the third position of chunk
J . Since the first three bits of chunk J are 100, this yields the value 1. Finally, the desired overall bit
count is numSet[J ] + 1.
