# Network Algorithmics — 11.12.2 SAIL: Uncompressed Bitmaps up to a pivot level (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 308
- Slice: from `11.12.2 SAIL: Uncompressed Bitmaps up to a pivot level` up to next detected section heading

---

11.12.2 SAIL: Uncompressed Bitmaps up to a pivot level
SAIL (Yang et al., 2014) starts by observing that up to some length (which they refer to as a pivot
length) one can easily store all the bitmaps without further compression. In particular, they suggest
                                                   24 2i = 32 Mbits. Thus their implementation pivots at
that storing all bitmaps up to 24 requires only i=1
length 24, but this could be changed. While 4 Mbytes is large, it is feasible in on-chip SRAM. Better
still, the amount of required on-chip memory remains constant even as the IPv4 database increases
arbitrarily. They also observe that prefixes of length greater than 24 bits are rare: hence they use prefix
expansion to store all such prefixes in 256 element multibit trie nodes indexed by their 24-bit prefix in

282      Chapter 11 Prefix-match lookups



off-chip DRAM. Note that we need 256 element trie nodes for these rare cases because the expansion
of a 24-bit prefix results in up to 256 32-bit entries.
    Because SAIL is also designed to work in software, SAIL starts lookup at length 24. SAIL first
determines whether the longest match is exactly 24 bits, less than 24 bits, or possibly greater than 24
bits. If the match is 24 bits, SAIL terminates by a lookup into the 24-bit next hop table in DRAM. If the
match is less than 24 bits, search continues sequentially from 23 to 1, trying each bitmap on-chip until
the longest match length is found at say W ; this is followed by a lookup to the W length hash table in
DRAM. Finally, if the match is greater than 24 (this should occur rarely), SAIL uses the last 8 bits of
the IP address to index into the corresponding multibit trie node in DRAM corresponding to the first
24-bits of the address.
    The key mechanism then is to efficiently implement a predicate that determines whether the longest
match is equal to 24, < 24, or possibly greater than 24. This is trickier than it may seem. Consider the
conceptual unibit trie level corresponding to the pivot length 24. Let the first 24 bit prefix of the address
being looked up be P .
    There are four cases to consider. If there is no trie node corresponding to the path P , then the
longest match must be less than 24. Second, if there is a trie node but it is a pure pointer, then search
must continue at levels greater than 24. But Case 2 can fail as a match is not guaranteed to be found at
longer lengths (as in binary search on prefix lengths). The third case is that the corresponding trie node
is a stored prefix but not a pointer; but in this case search terminates with a 24-bit match). The fourth
case is that the corresponding trie node is both a stored prefix and a pointer.
    For example, consider a smaller version of our earlier database with P 4 = 1∗, P 2 = 101∗, P 3 =
11001∗, P 7 = 1000000∗ and a new prefix P 10 = 100∗. If we assume the pivot level is 3, Case 1 occurs
say when the first bits of the address are 000, and Case 2 occurs when the first 3 bits are 110 (a pure
pointer pointing to P 3). Further, Case 3 occurs when the first 3 bits being matched are 101 (they match
P 2 and no longer prefix. Finally, Case 4 occurs when the first 3 bits being matched are 100 (they match
P 10 and also potentially the longer match P 7.
    A single bitmap at the pivot level cannot distinguish these four cases because a single indexed bit
has only 2 possible values. Thus SAIL uses an idea called pivot pushing to reduce four cases to three
cases. For example, case 4 (which should be rare) can be eliminated by pushing the stored prefix to
length 25 by expansion; thus, the prefix can be stored in an off-chip multibit trie node. That still leaves
3 cases. Case 1 is distinguished by a corresponding 0 in the 24-bit on-chip bitmap. However, Case 2
and Case 3 both correspond to a 1 in the bitmap. They are distinguished by one more lookup to the
corresponding next hop array of Length 24 bit prefixes. If there is a match (Case 3), search terminates
with a 24-bit match.
    If there is no match in the 24-bit next hop array and there is a 1 in the corresponding bit in the Length
24 bitmap, we are in Case 2 (pure pointer) and search must proceed to an off-chip multibit trie node.
But as in binary search on prefix lengths this can cause us to hare off on a wild goose chase when the
best match is actually at lengths less than 24. SAIL fixes this problem as usual using precomputation.
The longest match corresponding to the pointer is pushed to Level 25 in case no other longer match
works. Again just as in Case 4, such pushing should be done rarely, because prefixes greater than 24
are rare.
    The overall performance of SAIL in a hardware model requires 2 DRAM accesses in the (rare)
worst case for a match that is longer than 24-bits. This is because it requires a DRAM access into the

                                    11.13 Memory allocation in compressed schemes                       283



24-bit next hop table (to distinguish Case 2 and Case 3) followed by a lookup into the multibit trie node
(for Case 2).
    While SAIL was possibly designed in this way to make the software implementation fast, we have
already seen that DXR is likely to outperform SAIL on modern CPUs because of its smaller cache
footrpint. By contrast, SAIL requires 4 Mbytes of cache. Thus the SAIL ideas seem more relevant
for hardware settings with on-chip memory and cheap and large off-chip DRAM. If that is indeed the
setting, then SAIL can be simplified as follows.
    First, we can segregate the DRAM into 2 separate parallel banks that can be looked up in parallel.
The first DRAM bank can be used to store next hops for prefixes of all lengths strictly less than or equal
to 24, while a second bank can contain all the multibit trie nodes for prefixes of lengths greater than
24. If these two lookups can be done in parallel in one DRAM access time there is no need for pivot
pushing. The bit map corresponding to Length 24 is treated like the other bit maps of length < 24, with
bits set only for valid prefixes of that length (and not for pointers to greater length prefixes as in vanilla
SAIL). Instead, a hardware thread searches through all the bitmaps on-chip of lengths less than or equal
to 24 looking for the longest match length; a second parallel thread looks up the multibit trie node (if
it exists) corresponding to the full 32 bits, using the first 24 bits as a key. It is easy to combine all the
results since Thread 2 results (if any) are more specific than Thread 1 results.
    Finally, all the next hop tables can be indexed using say d-left hashing described in the chapter
on exact matching (more specifically in Section 10.3.3). The resulting hardware requires less DRAM
(at most the size of the prefix database instead of the indexed arrays used in the SAIL paper (Yang
et al., 2014). It is also easier and faster to add and delete prefixes because the pivot pushing has been
eliminated. This simplification was probably not considered in the SAIL paper (Yang et al., 2014)
because of the need to do a software implementation. However, given the existence of DXR, a simplified
SAIL seems most useful in a pure hardware setting with on-chip SRAM and off-chip DRAM.
