# Network Algorithmics — 15.2.1 Improving performance (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 462
- Slice: from `15.2.1 Improving performance` up to next detected section heading

---

15.2.1 Improving performance
To gain ordering without the expense of sequence numbers, the main idea is to exploit a hidden degree
of freedom (P13) by decoupling physical reception from logical reception. Physical reception is sub-
ject to skew-induced misordering. Logical reception eliminates misordering by using buffering and by
having the receiver remove cells using the same algorithm as the sender.
    For example, suppose the sender stripes cells in round-robin order using a round-robin pointer that
walks through the sending channels. Thus cell A is sent on Channel 1, after which the round-robin
pointer at the sender is incremented to 2. The next cell, B, is sent on Channel 2, and so on.
    The receiver buffers received cells but does not dequeue a cell when it arrives. Instead, the receiver
also maintains a round-robin pointer that is initialized to Channel 1. The receiver waits at Channel 1 to
receive a cell; when a cell arrives, that cell is dequeued, and the receiver moves on to wait for Channel 2.
Thus if skew causes cell B (that was sent on Channel 2 after cell A was sent on Channel 1) to arrive
before cell 1, the receiver will not dequeue cell B before cell A. Instead, the receiver will wait for cell

436       Chapter 15 Routers as distributed systems




FIGURE 15.3
Misordering and recovery: a play in six scenes. The final output at the receiver is D, B, C, E, F, G, H, I, and synchro-
nization is achieved after the logical reception of E.


A to arrive; after dequeuing cell A, the receiver will move on to Channel 2, where it will dequeue the
waiting cell, B.
