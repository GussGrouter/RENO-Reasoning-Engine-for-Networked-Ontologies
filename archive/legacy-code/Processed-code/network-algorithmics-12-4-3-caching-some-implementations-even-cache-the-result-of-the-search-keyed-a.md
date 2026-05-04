# Network Algorithmics — 12.4.3 Caching Some implementations even cache the result of the search keyed against the whole header. There are (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 329
- Slice: from `12.4.3 Caching Some implementations even cache the result of the search keyed against the whole header. There are` up to next detected section heading

---

12.4.3 Caching
Some implementations even cache the result of the search keyed against the whole header. There are
two problems with this scheme. First, the cache hit rate of caching full IP addresses in the backbones is
often small. Early studies show a hit rate of at most 80%–90% (Partridge, 1996; Newman et al., 1997).
Part of the problem is Web accesses and other flows that send only a small number of packets; if a Web
session sends just five packets to the same address, then the cache hit rate is 80%. Since caching full
headers takes a lot more memory, this should have an even worse hit rate (for the same amount of cache
memory).
    Second, even with a 90% hit rate cache, a slow linear search of the rule space will result in poor
performance.2 For example, suppose that a search of the cache costs 100 nanoseconds (one memory

2 This is an application of a famous principle in computer architecture called Amdahl’s law.

                                                                       12.4 Simple solutions           303



access) and that a linear search of 10,000 rules costs 1,000,000 nanoseconds = 1 millisecond (one mem-
ory access per rule). Then the average search time with a cache hit rate of 90% is still 0.1 millisecond,
which is very slow.
    However, caching could be combined with some of the fast algorithms in this chapter to improve the
expected search time even further. An investigation of the use of caching for classification can be found
in Xu et al. (2000). As a more recent example, Open vSwitch (Pfaff et al., 2015) combines Tuple Space
search with caching in clever ways. In particular, the Open vSwitch implementation does caching not
of full IP and TCP headers of a TCP connection (which they call microflows) but instead for larger
aggregates (that they call macroflows). Macroflow caching requires some more complexity to handle
correctly (Pfaff et al., 2015).
