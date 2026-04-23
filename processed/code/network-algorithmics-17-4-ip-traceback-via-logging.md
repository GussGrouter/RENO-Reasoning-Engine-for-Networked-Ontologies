# Network Algorithmics — 17.4 IP traceback via logging (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 526
- Slice: from `17.4 IP traceback via logging` up to next detected section heading

---

17.4 IP traceback via logging
A problem with the edge-sampling approach of the previous section is that it requires changes to the
IP header to update marks and does not work for single-packet attacks like the Teardrop attack. The

500       Chapter 17 Network security




FIGURE 17.6
Using a packet log to trace an attack packet P backward from the victim V to the attacker A by having the currently
traced node ask all its neighbors (the dotted lines) if they have seen P (solid line).



following approach, traceback via logging (Snoeren et al., 2001), avoids both problems by adding more
storage at routers to maintain a compressed packet log.
    As motivations, neither of the difficulties the logging approach gets around is very compelling. This
is because the logging approach still requires modifying router forwarding, even though it requires no
header modification. This is due to the difficulty of convincing vendors (who have already committed
forwarding paths to silicon) and ISPs (who wish to preserve equipment for, say, 5 years) to make
changes. Similarly, single-packet attacks are not very common and can often be filtered directly by
routers.
    However, the idea of maintaining compressed searchable packet logs may be useful as a general
building block. It could be used, more generally, for, say, a network monitor that wishes to maintain
such logs for forensics after attacks. But even more importantly, it introduces an important technique
called Bloom filters.
    Given an efficient packet log at each router, the high-level idea for traceback is shown in Fig. 17.6.
The victim V first detects an attack packet P ; it then queries all its neighboring routers, say, R8 and
R9 , to see whether any of them have P in their log of recently sent packets. When R9 replies in the
affirmative, the search moves on to R9 , who asks its sole neighbor, R7 . Then R7 asks its neighbors R5
and R4 , and the search moves backward to A.

                                                                  17.4 IP traceback via logging                501




FIGURE 17.7
A Bloom filter represents a set element by setting k bits in a bitmap using k independent hash functions applied to
the element. Thus the element John sets the second (using H 1) and next-to-last (using H 2) bits. When searching for
Jonas, Jonas is considered a member of the set only if all bit positions hashed to by Jonas have set bits.


    The simplest way to implement a log is to reuse one of the techniques in trajectory sampling (Chap-
ter 16). Instead of logging a packet, we log a 32-bit hash of invariant content (i.e., exclude fields that
change from hop to hop, such as the TTL) of the packet. However, 32 bits per packet for all the packets
sent in the last 10 minutes is still huge at 10 Gbps. Bloom filters, described next, allow a large reduction
to around 5 bits per packet.
