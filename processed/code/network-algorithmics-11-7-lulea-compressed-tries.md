# Network Algorithmics — 11.7 Lulea-compressed tries (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 295
- Slice: from `11.7 Lulea-compressed tries` up to next detected section heading

---

11.7 Lulea-compressed tries
Though LC tries and variable-stride tries attempt to compress multibit tries by varying the stride at
each node, both schemes have problems. While the use of full arrays allows LC tries not to waste any
memory because of empty array locations, it also increases the height of the trie, which cannot then be
tuned. On the other hand, variable-stride tries can be tuned to have short height, at the cost of wasted
memory because of empty array locations in trie nodes. The Lulea approach (Degermark et al., 1997),
which we now describe, is a multibit-trie scheme that uses fixed-stride trie nodes of large stride but uses
bitmap compression to reduce storage considerably.
   We know that a string with repetitions (e.g., AAAABBAAACCCCC) can be compressed using a
bitmap denoting repetition points (i.e., 10001010010000) together with a compressed sequence (i.e.,

                                                                 11.7 Lulea-compressed tries             269




FIGURE 11.12
Compressing the root node of Fig. 11.7 (after leaf pushing) using the Lulea bitmap compression scheme.


ABAC). Similarly, the root node of Fig. 11.7 contains a repeated sequence (P5, P5, P5, P5) caused by
expansion.
    The Lulea scheme (Degermark et al., 1997) avoids this obvious waste by compressing repeated
information using a bitmap and a compressed sequence without paying a high penalty in search time.
For example, this scheme used only 160 KB of memory to store the MAE-East database. This allows
the entire database to fit into expensive SRAM or on-chip memory. It does, however, pay a high price
in insertion times.
    Some expanded trie entries (e.g., the 110 entry at the root of Fig. 11.7) have two values, a pointer
and a prefix. To make compression easier, the algorithm starts by making each entry have exactly one
value by pushing prefix information down to the trie leaves. Since the leaves do not have a pointer, we
have only next-hop information at leaves and only pointers at nonleaf nodes. This process is called leaf
pushing.
    For example, to avoid the extra stored prefix in the 110 entry of the root node of Fig. 11.7, the P9
stored prefix is pushed to all the entries in the leftmost trie node, with the exception of the 010 and 011
entries (both of which continue to contain P3). Similarly, the P8 stored prefix in the 100 root node entry
is pushed down to the 100, 101, 110, and 111 entries of the rightmost trie node. Once this is done, each
node entry contains either a stored prefix or a pointer but not both.
    The Lulea scheme starts with a conceptual leaf-pushed expanded trie and replaces consecutive iden-
tical elements with a single value. A node bitmap (with 0’s corresponding to removed positions) is used
to allow fast indexing on the compressed nodes.
    Consider the root node in Fig. 11.7. After leaf pushing, the root has the sequence P5, P5, P5, P5,
ptr1, P1, ptr2, P2 (ptr1 is a pointer to the trie node containing P6 and P7, and ptr2 is a pointer to the
node containing P3). After replacing consecutive values with the first value, we get P5, -, -, -, ptr1, P1,
ptr2, P2, as shown in the middle frame of Fig. 11.12. The rightmost frame shows the final result, with
a bitmap indicating removed positions (10001111) and a compressed list (P5, ptr1, P1, ptr2, P2).
    If there are N original prefixes and pointers within an original (unexpanded) trie node, the number
of entries within the compressed node can be shown never to be more than 2N + 1. Intuitively, this
is because N prefixes partition the address space into at most 2N + 1 disjoint subranges and each
subrange requires at most one compressed node entry.
    Search uses the number of bits specified by the stride to index into the current trie node, starting
with the root and continuing until a null pointer is encountered. However, while following pointers, an

270      Chapter 11 Prefix-match lookups



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

                                                                                     11.8 Tree bitmap             271




FIGURE 11.13
To allow fast counting of the bits set even in large bitmaps (e.g., 64 Kbits), the bitmap is divided into chunks and a
summary count of the bits set before each chunk precomputed.


     Notice that the choice of the chunk size is a trade-off between memory size and speed. Making
a chunk equal to the size of the bitmap will make counting very slow. On the other hand, making a
chunk equal to a bit will require more storage than the original trie node! Choosing a 64-bit chunk size
makes the summary array size only 1/64 the size of the original node, but this requires counting the bits
set within a 64-bit chunk. Counting can easily be done using special instructions in software and via
combinational logic in hardware.
     Thus search of a node requires first indexing into the summary table, then indexing into the cor-
responding bitmap chunk to compute the offset into the compressed node, and finally retrieving the
element from the compressed node. This can take three memory references per node, which can be
quite slow.
     The final Lulea scheme also compresses entries based on their next-hop values (entries with the
same next-hop values can be considered the same even though they match different prefixes). Overall
the Lulea scheme has very compact storage. Using an early (1997) snapshot of the MAE-East database
of around 40,000 entries, the Lulea paper (Degermark et al., 1997) reports compressing the entire
database to around 160 KB, which is roughly 32-bits per prefix.
     This is a very small number, given that one expects to use at least one 20-bit pointer per prefix in the
database. The compact storage is a great advantage because it allows the prefix database to potentially
fit into limited on-chip SRAM, a crucial factor in allowing prefix lookups to scale to OC-768 speeds.
     Despite compact storage, the Lulea scheme has two disadvantages. First, counting bits requires at
least one extra memory reference per node. Second, leaf pushing makes worst-case insertion times
large. A prefix added to a root node can cause information to be pushed to thousands of leaves. The full
tree bitmap scheme, which we study next, overcomes these problems by abandoning leaf pushing and
using two bitmaps per node.
