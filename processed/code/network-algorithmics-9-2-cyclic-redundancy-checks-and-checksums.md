# Network Algorithmics — 9.2 Cyclic redundancy checks and checksums (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 244
- Slice: from `9.2 Cyclic redundancy checks and checksums` up to next detected section heading

---

9.2 Cyclic redundancy checks and checksums
Once a TCP packet is buffered, typically a check is performed to see whether the packet has been
corrupted in flight or in a router’s memory. Such checks are performed by either checksums or CRCs.
In essence, both CRCs and checksums are hash functions H on the packet contents. They are designed
so that if errors convert a packet P to corrupted packet P  , then H (P ) = H (P  ) with high probability.
    In practice, every time a packet is sent along a link, the data link header carries a link level CRC. But
in addition, TCP computes a checksum on the TCP data. Thus a typical TCP packet on a wire carries
both a CRC and a checksum. While this may appear to be obvious waste (P1), it is a consequence of
layering. The data link CRC covers the data link header, which changes from hop to hop. Since the data
link header must be recomputed at each router on the path, the CRC does not catch errors caused within
routers. While this may seem unlikely, routers do occasionally corrupt packets (Stone and Partridge,
2000) because of implementation bugs and hardware glitches.
    Given this, the CRC is often calculated in hardware by the chip (e.g., Ethernet receiver) that receives
the packet, while the TCP checksum is calculated in software in BSD UNIX. This division of labor
explains why CRC and checksum implementations are so different. CRCs are designed to be powerful
error-detection codes, catching link errors such as burst errors. Checksums, on the other hand, are less

218      Chapter 9 Protocol processing



adept at catching errors; however, they tend to catch common end-to-end errors and are much simpler
to implement in software.
    The rest of this section describes CRC and then checksum implementation. The section ends with
a clever way, used in Infiniband implementations, to finesse the need for software checksums by using
two CRCs in each packet, both of which can easily be calculated by the same piece of hardware.
