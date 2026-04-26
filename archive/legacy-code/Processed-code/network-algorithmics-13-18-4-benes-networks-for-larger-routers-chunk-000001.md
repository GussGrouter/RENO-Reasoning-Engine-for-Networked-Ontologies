# network-algorithmics-13-18-4-benes-networks-for-larger-routers (chunk 000001)

# Network Algorithmics — 13.18.4 Benes networks for larger routers (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 397
- Slice: from `13.18.4 Benes networks for larger routers` up to next detected section heading

---

13.18.4 Benes networks for larger routers
Just as the No. 1. ESS telephone switch switches 65,000 input links, Turner (1997); Chaney et al.
(1997) has made an eloquent case that the Internet should (at least eventually) be built of a few large
routers instead of several smaller routers. Such topologies can reduce the wasted links for router-to-
router connections between smaller routers and thus reduce cost; they can also reduce the worst-case
end-to-path length, reducing latency and improving √ user response times.
    Essentially, a Clos network has roughly N N scaling in terms of crosspoint complexity using
just three stages. This trade-off and general algorithmic experience (P15) suggest that one should be
able to get N log N crosspoint complexity, while increasing the switch depth to log N . Such switching
networks are indeed possible and have been known for years in theory, in telephony, and in the parallel
computing industry. Alternatives, such as Butterfly, Delta, Banyan, and Hypercube networks, are well-
known contenders.
    While the subject is vast, this chapter concentrates only on the Delta and Benes networks. Similar
networks are used in many implementations. For example, the Washington University Gigabit switch
(Chaney et al., 1997) uses a Benes network, which can be thought of as two copies of a Delta network.
Section A.4 in Appendix A outlines the (often small) differences between Delta networks and others of
the same ilk.
    In the following, we describe Delta and Benes networks only in the historical contexts of theory,
telephony, and parallel computing, where switches have no or little buffers. We will explain that, in
such contexts, the network designs need to address the congestion issues caused by pathological load
patterns. In the router context where the (small) switches have adequate amounts of buffers, however,
the buffers further alleviate such issues in a similar way as they do in the Clos network, which we have
explained in Section 13.18.3.

The Delta networks
The easiest way to understand a Delta network is recursively. Imagine that there are N inputs on the left
and that this problem is to be reduced to the problem of building two smaller (N/2)-size Delta networks.
To help in this reduction, assume a first stage of 2-by-2 switches. A simple scheme (Fig. 13.18) is to
inspect the output that every input wishes to speak to. If the output is in the upper half (MSB of output

13.18 Scaling to larger and faster switches                  371

FIGURE 13.18
Constructing a Delta network recursively by reducing the problem of constructing an N-input Delta network to the
problem of constructing two (N/2)-input Delta networks.
