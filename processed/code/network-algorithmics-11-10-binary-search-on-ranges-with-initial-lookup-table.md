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



the tables that are pointed to by root entries that match P . This translates into a huge savings since a
full build is much more costly than an incremental update: The cost of a full build for a 16-bit initial
table is reported to be 70 msec and goes up to 300 msec for a 20-bit initial stride (Zec and Mikuc,
2017), whereas that of an incremental update is reported to be only 10s of microseconds on average for
random tests (Zec et al., 2012).
    There seems to be two fundamental reasons why DXR does so well. First, the bigger reason is that
careful compression allows it to fit into the cache hierarchy; as the table size grows, the cache size of
modern processors should also grow. Second, the seemingly long time taken for binary search seems to
be hidden by thread parallelism. A recent updated Zec and Mikuc (2017) suggests that as CPUs scale
to more hardware threads (say 36 threads) this could easily double the throughput of DXR.
    Despite its success for IPv4, it is unlikely that DXR will work well as is for IPv6 because of 128-bit
keys and a more sparse address space. However, it is worth pointing out that the original paper Lampson
et al. (1998) suggests a multicolumn binary search for binary search of long identifiers (see the Exercise
in this chapter on Multicolumn search). Multicolumn search with multithreading (and the compression
ideas used in DXR) may be the basis for a fast software IPv6 implementation but more work is needed.
    The code for DXR is available online and has been integrated into FreeBSD which allows it to be
used as part of a Network Function Virtualization device based on FreeBSD.
