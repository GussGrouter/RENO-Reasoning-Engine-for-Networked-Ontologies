# network-algorithmics-17-4-2-bloom-filter-implementation-of-packet-logging (chunk 000001)

# Network Algorithmics — 17.4.2 Bloom filter implementation of packet logging (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 529
- Slice: from `17.4.2 Bloom filter implementation of packet logging` up to next detected section heading

---

17.4.2 Bloom filter implementation of packet logging
The Bloom filter implementation of packet logging in the SPIE system is shown in Fig. 17.8 (the picture
is courtesy of Sanchez et al. (2001)). Each line card calculates a 32-bit hash digest of the packet and
places it in a FIFO queue. To save costs, several line cards share, via a RAM multiplexer, a fast SRAM
containing the Bloom filter bitmap.
    As in the case of counters in Chapter 16, one can combine the best features of SRAM and DRAM to
reduce expense. One needs to use SRAM for fast front-end random access to the bitmap. Unfortunately,
the expense of SRAM would allow storing only a small number of packets. To allow a larger amount,
the Bloom filter bitmaps in SRAM are periodically read out to a large DRAM ring buffer. Because these
are no longer random writes to bits, the write to DRAM can be written in DRAM pages or rows, which
provide sufficient memory bandwidth.
