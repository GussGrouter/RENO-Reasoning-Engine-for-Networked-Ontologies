# network-algorithmics-15-2-2-rescuing-reliability (chunk 000001)

# Network Algorithmics — 15.2.2 Rescuing reliability (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 463
- Slice: from `15.2.2 Rescuing reliability` up to next detected section heading

---

15.2.2 Rescuing reliability
Synchronization between sender and receiver can be lost due to the loss of a single cell. In the round-
robin example shown earlier if cell A is lost in a large stream of cells sent over three links (Fig. 15.3),
the receiver will deliver the packet sequence D, B, C, G, E, F, . . . and permanently reorder cells.
    For switch fabrics and some links, one may be able to assume that cell loss is very rare (say, once
a year). Still, such an assumption should make the designer queasy, especially if one loss can cause
permanent damage from that point on. To prevent permanent damage after a single cell loss, the sender
must periodically resynchronize with the receiver.
    To do so, define a round as a sequence of visits to consecutive channels before returning to the
starting channel. In each round, the sender sends data over all channels. Similarly, in each round, the
receiver receives data from all channels. To enable resynchronization, the sender maintains the round
number (initialized to R0) of all channels, and so does the receiver.
    Thus in Fig. 15.3 after sending A, B, and C, all the sender channel numbers are at R1. However,
only channel 1 at the receiver is at R1, while the other channels are at R0 because the second and third

15.2 Internal Link Striping          437
