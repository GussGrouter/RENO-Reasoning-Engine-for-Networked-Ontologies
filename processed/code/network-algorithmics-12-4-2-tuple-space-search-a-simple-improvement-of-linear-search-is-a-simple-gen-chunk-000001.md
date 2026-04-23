# network-algorithmics-12-4-2-tuple-space-search-a-simple-improvement-of-linear-search-is-a-simple-gen (chunk 000001)

# Network Algorithmics — 12.4.2 Tuple space search A simple improvement of linear search is a simple generalization of IP lookups using hash tables where (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 328
- Slice: from `12.4.2 Tuple space search A simple improvement of linear search is a simple generalization of IP lookups using hash tables where` up to next detected section heading

---

12.4.2 Tuple space search
A simple improvement of linear search is a simple generalization of IP lookups using hash tables where
prefixes were partitioned by length, and all prefixes of the same length are placed in a common hash
table. While this requires 32 memory accesses in the worst case for IPv4, recall that the previous chapter
described a major improvement, binary search on prefix lengths that could perform IPv4 lookups in
log2 32 = 5 memory accesses.
    While the use of binary search does not generalize from IP lookups to packet classification as far
as we know, the idea of using linear search on hash tables does and was first called tuple space search
(TSS) by Srinivasan et al. (1998). Consider a simple packet classifier with four rules on IPv4 Destination
(D) and Source (S) fields. Ignoring the directive fields, assume that R1 must match D = 01∗, S = 10∗;

302        Chapter 12 Packet classification
