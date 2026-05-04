# network-algorithmics-11-12-2-sail-uncompressed-bitmaps-up-to-a-pivot-level (chunk 000001)

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
