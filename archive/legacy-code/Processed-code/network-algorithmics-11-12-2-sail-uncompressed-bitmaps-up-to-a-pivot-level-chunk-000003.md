# network-algorithmics-11-12-2-sail-uncompressed-bitmaps-up-to-a-pivot-level (chunk 000003)

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
