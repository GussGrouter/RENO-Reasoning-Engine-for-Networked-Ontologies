# network-algorithmics-9-3-1-udp-processing-recall-that-udp-is-tcp-without-error-recovery-congestion (chunk 000001)

# Network Algorithmics — 9.3.1 UDP processing Recall that UDP is TCP without error recovery, congestion control, or connection management. As with (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 253
- Slice: from `9.3.1 UDP processing Recall that UDP is TCP without error recovery, congestion control, or connection management. As with` up to next detected section heading

---

9.3.1 UDP processing
Recall that UDP is TCP without error recovery, congestion control, or connection management. As with
TCP, UDP allows multiplexing and demultiplexing using port numbers. Thus UDP allows applications
to send IP datagrams without the complexity of TCP. Although TCP is by far the dominant protocol,
many important applications, such as videoconferencing, use UDP. Thus it is also important to optimize
UDP implementations.
    Because UDP is stateless, header prediction is not relevant: one cannot store past headers that can
be used to predict future headers. However, UDP shares with TCP two potentially time-consuming
tasks: demultiplexing to the right PCB, and checksumming, both of which can benefit from TCP-style
optimizations (Partridge and Pink, 1993).
    Caching of PCB entries is more subtle in UDP than in TCP. This is because PCBs may need to
be looked up using wildcarded entries for, say, the remote (called foreign) IP address and port. Thus
there may be PCB 1 that specifies local port L with all the other fields wildcarded, and PCB 2 that

9.4 Reassembly           227

specifies local port L and remote IP address X. If PCB 1 is cached and a packet arrives destined for
PCB 2, then the cache can result in demultiplexing the packet for the wrong PCB. Thus caching of
wildcarded entries is not possible in general; address prefixes cannot be cached for purposes of route
lookup (Chapter 11), for similar reasons.
    Partridge and Pink (1993) suggest a simple strategy to get around this issue. A PCB entry, such
as PCB 1, that can “hide” or match another PCB entry is never allowed to be cached. Subject to this
restriction, the UDP implementation of Partridge and Pink (1993) caches both the PCB of the last packet
received and the PCB of the last packet sent. The first cache handles the case of a train of received
packets, while the second cache handles the common case of receiving a response to the last packet
sent. Despite the cache restrictions, these two caches still have an 87% hit rate in the measurements of
Partridge and Pink (1993).
    Finally, Partridge and Pink (1993) also implemented a copy-and-checksum loop for UDP as in TCP.
In the BSD implementation UDP’s sosend was treated as a special case of sending over a connected
socket. Instead, Partridge and Pink propose an efficient special-purpose routine (P6) that first calculates
the header checksum and then copies the data bytes to the network buffer while updating the checksum.
(Some of these ideas allowed Cray machines to vectorize the checksum loop in the early 1990s.) With
similar optimizations used for receive processing, Partridge and Pink report that the checksum cost is
essentially zero for CPUs that are limited by memory access time and not processing.
