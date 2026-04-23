# Network Algorithmics — 11.12 Linear search on prefix lengths with hardware assist (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 307
- Slice: from `11.12 Linear search on prefix lengths with hardware assist` up to next detected section heading

---

11.12 Linear search on prefix lengths with hardware assist
The last section shows we can make binary search on prefix lengths work by adding markers and other
mechanisms. Unfortunately, this adds complexity and makes insertion slow. The idea in this section
is to revisit naive linear search on prefix lengths (that we discarded in the last section), but add some
hardware assistance to make it practical.
    Assume the setting is hardware with on-chip memory (with say 1 nsec access time) of a few Mbytes
and a massive amount of slower DRAM (with say 50 nsec access time). How can we do IP Lookups

                          11.12 Linear search on prefix lengths with hardware assist                      281



with a small number (say 1 or 2) of sequential DRAM accesses? We can easily also afford up to to 32
on-chip memory accesses because the on-chip accesses are dwarfed by a single DRAM access. We will
describe two such schemes, both based on using bitmaps to represent the stored prefixes at each length.
Since these bitmaps are compact, they can be stored in on-chip memory; a corresponding hash table for
each length is stored in off-chip DRAM using a scheme such as d-left (Broder and Mitzenmacher, 2001)
(described in Section 10.3.3). For example, if there are just two prefixes P 4 = 1∗ and P 1 = 100∗. The
length-1 bitmap would be 10 (first bit set corresponding to P 4 , the length-2 bitmap would be 0000,
and the length-3 bit map would be 00010000 (fourth bit is set corresponding to P 1).
    The skeleton idea, then, is to search on-chip either sequentially or in parallel to find the longest
matching length, say L. Then a hash table access is made to an off-chip DRAM hash table that stores
all L bit prefixes using the first L bits of the address as a key to retrieve the next hop. Clearly, a naive use
of indexed bitmaps does not work well because at prefix lengths such as 32 the corresponding bitmap
is of size 232 which is too large to fit into on-chip memory. We will describe two schemes that show
how to deal with this memory explosion caused by larger length bitmaps.
