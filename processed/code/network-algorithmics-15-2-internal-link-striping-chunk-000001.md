# network-algorithmics-15-2-internal-link-striping (chunk 000001)

# Network Algorithmics — 15.2 Internal Link Striping (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 462
- Slice: from `15.2 Internal Link Striping` up to next detected section heading

---

15.2 Internal Link Striping
Flow control within routers is motivated by the twin forces of increasingly large interconnect length
and increasing speeds. On the other hand, internal link striping within a router is motivated by slow
interconnect speeds. If serial lines are not fast enough, a designer may resort to striping cells internally
across multiple serial links.
    Besides serial link striping, designers often resort to striping across slow DRAM banks (as we
will see in the next section) to gain memory bandwidth, and across switch fabrics, to scale scheduling
algorithms like iSLIP. We saw these trends in Chapter 13. In each case the designer distributes cells
across multiple copies of a slow resource, called a channel.
    In most applications the delay across each channel is variable; there is some large skew between the
fastest and slowest times to send a packet on each channel. Thus the goals of a good striping algorithm
are FIFO delivery in the face of arbitrary skew, routers should not reorder packets because of internal
mechanisms, and robustness in the face of link bit errors.
    To understand why this combination of goals may be difficult, consider round-robin striping. The
sender sends packets in round-robin order on the channels. Round-robin, however, does not provide
FIFO delivery without packet modification. The channels may have varying skews, and so the physical
arrival of packets at the receiver may differ from their logical ordering. Without sequencing information,
packets may be persistently misordered.
    Round-robin schemes can be made to guarantee FIFO delivery by adding a packet sequence number
that can be used to resequence packets at the receiver. However, many implementations would prefer
not to add a sequence number because it adds to cell overhead and reduces the effective throughput of
the router.
