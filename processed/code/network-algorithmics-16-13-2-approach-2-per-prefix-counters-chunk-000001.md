# network-algorithmics-16-13-2-approach-2-per-prefix-counters (chunk 000001)

# Network Algorithmics — 16.13.2 Approach 2: per-prefix counters (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 501
- Slice: from `16.13.2 Approach 2: per-prefix counters` up to next detected section heading

---

16.13.2 Approach 2: per-prefix counters
Designers of modern routers have considered other systems solutions to the traffic matrix problem
based on changes to router implementations and (sometimes) changes to routing protocols (see the
DCU scheme described earlier). For example, one solution being designed into some routers built at
Cisco (2001a) and some start-ups is to use per-prefix counters. Recall that prefixes are used to aggregate
route entries for many millions of Internet addresses into, say, 100,000–150,000 prefixes at the present
time.
    A router has a forwarding engine for each input line card that contains a copy of the forwarding
prefix table. Suppose each prefix P has an associated counter that is incremented (by the number of
bytes) for each packet entering the line card that matches P . Then, by pooling the per-prefix counters
kept at the routers corresponding to each input link, a tool can reconstruct the traffic matrix. To do so,
the tool must associate prefix routes with the corresponding output links using its knowledge of routes
computed by a protocol, such as OSPF. In Fig. 16.13, if R1 keeps per-prefix counters on traffic entering
from link E1, it can sum the 10,000 counters corresponding to prefixes advertised by ISP X to find the
traffic between Customer A and ISP X.
    One advantage of this scheme is that it provides perfect traffic matrices. A second advantage is that
it can be used for differential traffic charging based on the destination address, as in the DCU proposal.
The two disadvantages are the implementation complexity of maintaining per-prefix counters (and the
lack thereof in legacy routers) and the large amount of data that needs to be collected and synthesized
from each router to form traffic matrices.
