# network-algorithmics-11-7-lulea-compressed-tries (chunk 000004)

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
