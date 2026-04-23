# network-algorithmics-11-10-binary-search-on-ranges-with-initial-lookup-table (chunk 000001)

# Network Algorithmics — 11.10 Binary search on ranges with Initial Lookup Table (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 304
- Slice: from `11.10 Binary search on ranges with Initial Lookup Table` up to next detected section heading

---

11.10 Binary search on ranges with Initial Lookup Table
The core idea in DXR (Zec et al., 2012) is still binary search on ranges with an initial table. Thus rather
than have 1 binary search, if the root has N pointers there can be pointers to N different binary search
tables. Once again, each prefix is converted to a range (start and end address).
    DXR, however, goes beyond the original binary search on ranges idea with an initial table (Lampson
et al., 1998) using multithreading and careful compression to fit into the cache hierarchy of a modern
CPU in clever ways. First, they use a multithreaded implementation so the apparent cost of binary
search can be hidden by increasing the number of hardware threads. Second, they use several com-
pression ideas to reduce memory to make it more likely for the database to fit into the L2/L3 caches.
Neighboring address ranges that resolve to the same next hop are merged. Next, the end address can be
derived from the start of the next interval. Thus each entry only needs the start address (2 bytes, because
the first 16 or more bits have already been resolved by direct lookup), and the next hop (1 or 2 bytes
to index a next hop table). A further twofold compression can be achieved for chunks which reference
only 8-bit next hop indices and correspond to prefix lengths up to 24 bits. For these, the range start can
be compressed to 8 bits or less, which is a big savings. Finally, they experiment with initial table sizes
beyond 216 and find better numbers by using anywhere from 16 to 21 bits.
    Using a 16 bit initial table, for instance, is compact and takes “less than 2 bytes per prefix, and
exceeds 100 million lookups per second (Mlps) on a single commodity CPU core in synthetic tests
with uniformly random queries” (DXR, 2022). Using 21 bits, allows “200 Mlps per CPU core at the
cost of increased memory footprint, and deliver aggregate throughputs exceeding two billion lookups
per second” (DXR, 2022) using 8 cores. A version of DXR merged in FreeBSD uses a two-stage trie
with a 16-4 split before proceeding with binary search.
    Note that partitioning (into multiple prefix search tables) also reduces the cost of updates because
a prefix addition or the deletion of a prefix P does not affect all the partitioned tables, but affects only

278      Chapter 11 Prefix-match lookups
