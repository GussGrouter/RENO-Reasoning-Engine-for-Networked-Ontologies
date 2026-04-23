# Network Algorithmics — 9.2.3 Finessing checksums The humble checksum’s reason for existence, compared to the more powerful CRC, is the relative ease (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 250
- Slice: from `9.2.3 Finessing checksums The humble checksum’s reason for existence, compared to the more powerful CRC, is the relative ease` up to next detected section heading

---

9.2.3 Finessing checksums
The humble checksum’s reason for existence, compared to the more powerful CRC, is the relative ease
of checksum implementation in software. However, if there is hardware that already computes a data
link CRC on every data link frame, an obvious question is: Why not use the underlying hardware to
compute another checksum on the data? Doing otherwise results in extra computation by the receiving
processor and appears to be obvious waste (P1). Once again, it is only obvious waste when looking
across layers; at each individual layer (data link, transport), there is no waste.
    Clearly, the CRC changes from hop to hop, while the TCP checksum should remain unchanged to
check for end-to-end integrity. Thus if a CRC is to be used for both purposes, two CRCs have to be
computed. The first is the usual CRC, and the second should be on some invariant portion of the packet
that includes all the data and does not change from hop to hop.
    One of the problems with exploiting the hardware (P4c) to compute the equivalent of the TCP
checksum is knowing which portion of the packet must be checksummed. For example, TCP and UDP
include some fields of the IP header4 in order to compute the end-to-end checksum. The TCP header
fields may also not be at a fixed offset because of potential TCP and IP options. Having a data link
hardware device understand details of higher-layer headers seems to violate layering.
    On the other hand, all the optimizations that avoid data copying and described in Chapter 5 also
violate layering in a similar sense. Arguably, it does not matter what a single endnode does internally
as long as the protocol behavior, as viewed externally by a black-box tester, meets conformance tests.
Further, there are creative structuring techniques (P8, not being tied to reference implementations) of
the endnode software that can allow lower layers access to this form of information.
    The Infiniband architecture (Infiniband Specification, 2000) does specify that end system hardware
compute two CRCs. The usual CRC is called the variant CRC; the CRC on the data, together with some
of the header, is called the invariant CRC. Infiniband transport and network layer headers are simpler
than those of TCP, and thus computing the invariant portion is fairly simple.
    However, the same idea could be used even for a more complex protocol, such as TCP or IP, while
preserving endnode software structure. This can be achieved by having the upper layers pass informa-
tion about offsets and fields (P9) to the lower layers through layer interfaces. A second option to avoid
passing too many field descriptions is to precompute the pseudoheader checksum/CRC as part of the
connection state (Jacobson, 1993) and instead to pass the precomputed value to the hardware.



4 These portions form what is called the TCP and UDP pseudoheader (Stevens, 1994).

224      Chapter 9 Protocol processing
