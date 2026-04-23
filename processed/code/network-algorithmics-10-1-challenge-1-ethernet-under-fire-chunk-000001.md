# network-algorithmics-10-1-challenge-1-ethernet-under-fire (chunk 000001)

# Network Algorithmics — 10.1 Challenge 1: Ethernet under fire (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 263
- Slice: from `10.1 Challenge 1: Ethernet under fire` up to next detected section heading

---

10.1 Challenge 1: Ethernet under fire
The first challenge arose in the late 1980s. Ethernet, invented in the 1970s as a low-cost, high-bandwidth
interconnect for personal computers, was attacked as behaving poorly at large loads and being incapable
of spanning large distances. Recall that if two or more nodes on an Ethernet send data at the same time,
a collision occurs on the shared wire. All senders then compute a random retransmission time and retry,
where the randomization is chosen to minimize the probability of further collisions.
    Theoretical analyses (e.g., Bux and Grillo, 1985) claimed that as the utilization of an Ethernet grew,
the effective throughput of the Ethernet dropped to zero because the entire bandwidth was wasted on
retransmissions. A second charge against Ethernet was its small distance limit of 1.5 km, much smaller
than the limits imposed by, say, the IBM token ring.
    While the limited-bandwidth charge turned out to be false in practice (Boggs et al., 1988), it re-
mained a potent marketing bullet for a long time. The limited-distance charge was, and remains, a true
limitation of a single Ethernet. In this embattled position network marketing people at Digital Equip-
ment Corporation (DEC) around 1980 pleaded with their technical experts for a technical riposte to

10.1 Challenge 1: Ethernet under fire   237

FIGURE 10.1
Toward designing a bridge connecting two Ethernets.
