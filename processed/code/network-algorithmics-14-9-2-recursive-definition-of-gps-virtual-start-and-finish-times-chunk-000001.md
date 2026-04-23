# network-algorithmics-14-9-2-recursive-definition-of-gps-virtual-start-and-finish-times (chunk 000001)

# Network Algorithmics — 14.9.2 Recursive definition of GPS virtual start and finish times (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 429
- Slice: from `14.9.2 Recursive definition of GPS virtual start and finish times` up to next detected section heading

---

14.9.2 Recursive definition of GPS virtual start and finish times
Although GPS cannot be used directly as a realistic scheduler as explained earlier, some concepts as-
sociated with GPS are important in specifying, reasoning about, and implementing realistic schedulers,
such as WFQ, WF2 Q (Bennett and Zhang, 1996a), and WFQ+ (Bennett and Zhang, 1997). One such
concept is the GPS virtual finish time of a packet pi,k , defined as the virtual time when this packet
finishes service under GPS and denoted as fi,k . For example, in Fig. 14.16 the GPS virtual finish time
of packet p3,2 is 4 (bits). Similarly, the GPS virtual start time of a packet pi,k is defined as the virtual
time at which the packet starts to receive service under GPS and denoted as si,k . For example, the GPS
virtual start time of p3,2 is 3. In general, the virtual start and the virtual finish times of any packet can
be computed from the following simple recursive formulae:

si,k = max{fi,k−1 , V (ai,k )},                                 (14.1)
                                                       li,k
                                         fi,k = si,k +      .                                            (14.2)
                                                        φi
Here, V (ai,k ) is the virtual time that corresponds to ai,k , the real arrival time of pi,k . For example, when
packet p3,2 arrives at time a3,2 = 3, the corresponding virtual time V (3) = 13 because there are three
backlogged flows sharing GPS service during the real time interval [0, 1], and each receives 13 bits of
service. As stated in (14.1), the virtual start time of the packet pi,k is defined as the larger of fi,k−1 , the
virtual finish time of its previous packet pi,k−1 , and V (ai,k ). This is because, per GPS policy, a packet
pi,k cannot start receiving service under GPS until pi,k−1 , the previous packet in the same flow, finishes

14.9 Generalized processor sharing               403
