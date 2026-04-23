# Network Algorithmics — 11.12.1 Using Bloom Filters to compress prefix bitmaps (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 308
- Slice: from `11.12.1 Using Bloom Filters to compress prefix bitmaps` up to next detected section heading

---

11.12.1 Using Bloom Filters to compress prefix bitmaps
Observe that the bitmaps, especially at larger lengths will be very sparse. Thus each bitmap can be
compressed by what is called a Bloom Filter (Bloom, 1970). In a Bloom Filter any entry x is hashed a
small constant number of times (often 3 times) with independent hash functions (say h1 (x) = i, h2 (x) =
j, h3 (x) = k, and bits i, j , k are set in the bitmap. Thus if there are NL prefixes at length L, the theory
shows that the NL prefixes require cNL bits, where c is a small constant.
    While we will study Bloom filters later in this book when we survey techniques for measurement
and security, for now it is worth noting that Bloom filters have no false negatives, but can have false
positives. It may happen that when doing a lookup for entry y that is not present, the corresponding
indices h1 (y), h2 (y), h3 (y) are all set, leading search to incorrectly conclude that y exists in that Bloom
Filter. However, if c is sufficiently large, the probability of a false positive is low.
    A paper by Dharmapurikar et al. (2003) suggests using 32 Bloom Filters to compress all the stored
prefixes stored at each length on-chip, followed by off-chip lookups. If i is the longest length Bloom
Filter that matches, an off-chip access is made to off-chip Hash Table i. However, the Bloom filter may
rarely have a false positive, in which case the chip will try the next smallest Bloom filter length that
matched, and so on. While in the worst case there can be several DRAM accesseses (such pathological
IP addresses can be cached), the expected number of DRAM accesses is close to 1. Nevertheless, this
lack of deterministic performance leads to the next proposal called SAIL.
