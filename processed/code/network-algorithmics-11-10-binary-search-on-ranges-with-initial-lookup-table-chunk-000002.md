# network-algorithmics-11-10-binary-search-on-ranges-with-initial-lookup-table (chunk 000002)

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
