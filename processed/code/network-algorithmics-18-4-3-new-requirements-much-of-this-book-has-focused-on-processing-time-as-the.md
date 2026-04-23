# Network Algorithmics — 18.4.3 New requirements Much of this book has focused on processing time as the main metric to be optimized while minimizing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 554
- Slice: from `18.4.3 New requirements Much of this book has focused on processing time as the main metric to be optimized while minimizing` up to next detected section heading

---

18.4.3 New requirements
Much of this book has focused on processing time as the main metric to be optimized while minimizing
dollar cost. Storage was also an important consideration because of limited on-chip storage and the
expense of SRAM. However, even minimizing storage was related to speed, in order to maximize the
possibility of storing the entire data structure in high-speed storage.
    The future may bring new requirements. Two important such requirements are (mechanical) space
and power. Space is particularly important in PoPs and hosting centers, because rack space is limited.
Thus routers with small form factors are crucial. It may be that optimizing space is mostly a matter of
mechanical design together with the use of higher and higher levels of integration. However, engineer-
ing routers (and individual sensors in sensor networks) for power may require attention to algorithmics.
    Today power per rack is limited to a few kilowatts, and routers that need more power do so by
spreading out across multiple racks. Power is a major problem in modern router design. It may be
possible to rethink lookup, switching, and fair queuing algorithms in order to minimize power. Such
power-conscious designs have already appeared in the computer architecture and operating systems
community. It is logical to expect this trend to spread to router design.

528      Chapter 18 Conclusions
