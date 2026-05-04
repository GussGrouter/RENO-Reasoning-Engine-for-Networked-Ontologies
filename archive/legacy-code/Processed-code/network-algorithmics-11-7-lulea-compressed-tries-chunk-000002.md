# network-algorithmics-11-7-lulea-compressed-tries (chunk 000002)

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
