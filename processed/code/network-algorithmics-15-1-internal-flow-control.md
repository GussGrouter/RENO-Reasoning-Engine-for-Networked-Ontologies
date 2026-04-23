# Network Algorithmics — 15.1 Internal flow control (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 457
- Slice: from `15.1 Internal flow control` up to next detected section heading

---

15.1 Internal flow control
As noted in Chapter 13, packaging technology and switch size are forcing switches to expand beyond
single racks. These multichassis systems interconnect various components with serial links that span
relatively large distances of 5–20 m. At the speed of light, a 20-m link contributes a round-trip link
delay of 60 nanoseconds. On the other hand, at OC-768 speeds, a 40-byte minimum-size packet takes
8 nanoseconds to transmit. Thus eight packets can be simultaneously in transit on such a link.
    What is worse, link signals propagate slower than the speed of light; also, there are other delays,
such as serialization delay, that make the number of cells that can be in flight on a single link even
larger. This is quite similar to a stream of packets in flight on a transatlantic link. A single router is now
a miniature Internet.
    TCP and other transport protocols already solve the problem of flow control. If the receiver has
finite buffers, sender flow control ensures that any packet sent by the sender has a buffer available when

                                                                   15.1 Internal flow control          431




FIGURE 15.1
Basic credit-based flow control.


it arrives at the receiver. Chip-to-chip links also require flow control. It is considered bad form to drop
packets or cells (we will use cells in what follows) within a router for reasons other than output-link
congestion.
    It is possible to reuse directly the TCP flow control mechanisms between chips. But, TCP is com-
plex to implement. Disentangling mechanisms, TCP is complex because it does error control and flow
control, both using sequence numbers. However, within a chip-to-chip link, errors on the link are rare
enough for recovery to be relegated to the original source computer. Thus it is possible to apply fairly
recent work on flow control (Kung et al., 1994; Ozveren et al., 1994) that is not intertwined with error
control.
    Fig. 15.1 depicts a simple credit flow control mechanism (Ozveren et al., 1994) for a chip-to-chip
link within a router. The sender keeps a credit register (CR) that is initialized to the number of buffers
allocated at the receiver. The sender sends cells only when the CR is positive and decrements the CR
after a cell is sent. At the receiving chip, whenever a cell is removed from the buffer, the receiver sends
a credit to the sender. Finally, when a credit message arrives, the sender increments the CR.
