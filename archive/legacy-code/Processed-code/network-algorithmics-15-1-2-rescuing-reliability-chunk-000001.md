# network-algorithmics-15-1-2-rescuing-reliability (chunk 000001)

# Network Algorithmics — 15.1.2 Rescuing reliability (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 459
- Slice: from `15.1.2 Rescuing reliability` up to next detected section heading

---

15.1.2 Rescuing reliability
The protocol sketched in the last subsection uses limited receiver SRAM buffers very efficiently but
is not robust to failures. Before understanding how to make the more elaborate flow control protocol
robust against failures, it is wiser to start with the simpler credit protocol portrayed in Fig. 15.1.
    Intuitively, the protocol in Fig. 15.1 is like transferring money between two banks: the “banks” are
the sender and the receiver, and both credits and cells count as “money.” It is easy to see that, in the
absence of errors, the total “money” in the system is conserved. More formally, let CR be the credit
register, M the number of cells in transit from sender to receiver, C the number of credits in transit in
the other direction, and Q the number of cell buffers that are occupied at the receiver.
    Then, it is easy to see that (assuming proper initialization and that no cells or credits are lost on the
link), the protocol maintains the following property at any instant: CR + M + Q + C = B, where B is
the total buffer space at the receiver. The relationship is called an invariant because it holds at all times
when the protocol works correctly. It is the job of protocol initialization to establish the invariant and
the job of fault tolerance mechanisms to maintain the invariant.

15.1 Internal flow control          433
