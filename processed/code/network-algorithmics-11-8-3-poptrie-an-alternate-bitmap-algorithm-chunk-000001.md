# network-algorithmics-11-8-3-poptrie-an-alternate-bitmap-algorithm (chunk 000001)

# Network Algorithmics — 11.8.3 PopTrie: an alternate bitmap algorithm (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 301
- Slice: from `11.8.3 PopTrie: an alternate bitmap algorithm` up to next detected section heading

---

11.8.3 PopTrie: an alternate bitmap algorithm
Many years after the initial Lulea and Tree bitmap algorithms, a new bitmap algorithm called Pop-
trie (Asai and Ohara, 2015) was proposed. The algorithm gets its name from the population count
instruction (called popcount) that can count the number of bits set (in say a 64-bit machine word) on
a modern CPU. The setting is for a software implementation, perhaps for Network Function Virtual-
ization. The motivation is that since the Tree bitmap of stored prefixes is not a simple linear bitmap
it cannot be calculated easily in software. The Poptrie paper (Asai and Ohara, 2015) describes some
experiments to suggest that Tree bitmap is fairly slow in software, and suggests an alternative.
    The alternative to Tree bitmap is again to use an aggressive form of leaf-pushing so insertion is
again slow compared to Tree bitmap. In Poptrie, every leaf stores an associated prefix (corresponding
to its most specific ancestor prefix). Thus every multibit trie element either is a null pointer with an
associated leaf-pushed prefix, or contains a pointer to a descendant node. Thus each node has a basic
bitmap where the 1’s represent valid pointers to descendants and the 0’s represent stored prefixes. Thus
each trie node has the basic bitmap and two base pointers: the first base pointer (base0) points to the
start of the stored prefix array, and the second (base1) to the start of the descendant pointer array.
    Poptrie breaks an IP address into 6-bit chunks (a uniform stride of 6 bits) so each basic bitmap is 64
bits. During search, when indexing into the bitmap using the current chunk of the address, if the bit is 1,
then there is a descendant node. In that case, search continues by counting the number of 1’s and using
the count to index into the compressed array of pointers whose start is base1. If the indexed bit is a 0,
search terminates with a stored prefix. Search now ends by counting the number of 0’s and indexing
into the base0 array to retrieve the next hop associated with the longest match. Because Poptrie uses 64
bit bitmaps, the counting can be done efficiently in software by a popcount instruction in 1 cycle.
    The basic scheme as described takes a tremendous amount of storage because of the very aggressive
leaf pushing. But many of the consecutive entries have the same stored prefix. As in our description of

11.9 Binary search on ranges             275

Lulea, one can do a form of run-length encoding using a second bitmap, called the LeafVector. Thus if
there is a run of consecutive stored prefixes say P4, P4, P4, P5. ., in the base0 array this is replaced by
one copy of P4 and a LeafVector bitmap 1001 ...
    In summary, all three schemes use different but closely related semantics for bitmaps. Lulea uses a
single bitmap and large strides, but uses a summary bitmap to recover speed. Tree bitmap does not do
leaf pushing, but uses two bitmaps, one for compressing pointers and one Tree bitmap that represents
the stored prefixes. Poptrie does aggressive leaf pushing, and uses two bitmaps: one that distinguishes
pointers from prefixes, and one that compresses consecutive stored prefixes.
    While the Poptrie paper shows better performance than Tree bitmap in software, there are two
concerns. First, it is not clear that Lulea cannot simulate the forwarding performance of Poptrie with
smaller (say 6-bit) strides and using the popcount instruction to count bits. Second, as we will see
below, the current fastest method in software uses a different strategy, based on binary search on prefix
ranges.
