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


is 0), then the input is routed to the upper N/2 Delta Network; if the output is in the lower half (i.e.,
MSB = 1), the input is routed to the lower N/2 Delta network.
    To economize on the first stage of two-input switches, group the inputs into consecutive pairs, each
of which shares a two-input switch, as in Fig. 13.18. Thus if the two input cells in a pair are going
to different output halves, they can be switched in parallel; otherwise, one will be switched and the
other is either dropped or buffered. Of course, the same process can be repeated recursively for both of
the smaller (N/2)-size Delta networks, breaking them up into a layer of 2-by-2 switches followed by
four N/4 switches, and so on. The complete expansion of a Delta network is shown in the first half of
Fig. 13.19. Notice how the recursive construction in Fig. 13.18 can be seen in the connections between
the first and second stages in Fig. 13.19.
    Thus to reduce the problem to 2 × 2 switches takes log N stages; since each stage has N/2 cross-
points, the binary Delta network has N log N crosspoint and link complexity. Clearly, we can also
construct a Delta network by using d-by-d switches in the first stage and breaking up the initial net-
work into d Delta networks of size N/d each. This reduces the number of stages to logd N and link
complexity to n logd N. Given VLSI costs, it is cheaper to construct a switching chip with as large a
value of d as possible to reduce link costs.
    The Delta network, as do many of its close relatives (see Section A.4) such as the Banyan and the
Butterfly, has a nice property called the self-routing property. For a binary Delta network, one can find
the unique path from a given input to a given output o = o1 , o2 , . . . , os expressed in binary by following
the link corresponding to the value of oi in stage i. This should be clear from Fig. 13.18, where we use
the MSB at the first stage, the second bit at the second stage, and so on. For d ≥ 2, write the output
address as a radix-d number, and follow successive digits in a similar fashion.
    An interesting property that one can intuitively see in Fig. 13.18 is that the Delta network is re-
versible. It is possible to trace a path from an output to an input by following bits of the input in the

372       Chapter 13 Switching




FIGURE 13.19
The first half is a Delta network (Fig. 13.18), and the second half is a mirror-reversed Delta network. The first half
distributes load and the second routes.


same way. Thus in Fig. 13.18 notice that, in going from outputs to inputs, the next-to-last bit of the input
selects between two consecutive first-stage switches, and the last bit selects the input. This reversibility
property is important because it allows the use of a mirror-reversed version of the Delta (see the second
half of Fig. 13.19) with similar properties as the original Delta.
    One problem with the Delta network is congestion. Since there is a unique path from each input
to each output, the Delta network is emphatically not a permutation network. For example, if each
successive pair of inputs wishes to send a cell to the same output half, only half of the cells can proceed
to the second stage; if this repeats, only a quarter can proceed to the third stage; and so on. Thus there
are combinations of output requests for which the Delta network throughput can reduce to that of one
link, as opposed to N links.
    Clearly, one way to make the Delta network less susceptible to congestion for arbitrary permutations
of input requests is to add more paths between an input and an output. Generalizing the ideas in a Clos
network (Fig. 13.16), one can construct a Benes network (Fig. 13.19) that consists of two (log N )-depth
networks: the left half is a standard Delta network, and the right half is a mirror-reversed Delta network.
Look at the right half backwards, going left from the outputs: notice that the connections from the last
stage to the next-to-last stage are identical to those between the first and second stages.
    One can also visualize a Benes network recursively (P15) by extending Fig. 13.18 by adding a
third stage of 2-by-2 switches and by connecting these third stages to the two (N/2)-sized networks in
the middle, in the same way as the first-stage switches are connected to the two middle (N/2)-sized
networks (Fig. 13.20). Observe that this recursion can be used to directly create Fig. 13.19 without
creating two separate Delta networks.
    Observe the similarity between the recursive version of the Benes network in Fig. 13.20 and the
Clos network of Fig. 13.16. This similarity can be exploited to prove that the Benes can route any

                                             13.18 Scaling to larger and faster switches               373




FIGURE 13.20
Recursively constructing a Benes network.


permutation of output requests in a manner similar to our proof (see the earlier box) of the rearrangeably
nonblocking property of a Clos network.
    In each of two iterations start by doing a perfect matching between the first and last stages of
Fig. 13.20, as before, and pick one of the two middle switches. However, rather than stopping here
as in the Clos proof, the algorithm must recursively follow the same routing procedure in the (N/2)-
sized Benes network. Alternatively, the whole process can be formulated using edge coloring. The final
message is that it is possible to perfectly route arbitrary permutations in a Benes network; however,
doing so is fairly complex and is unlikely to be accomplished cheaply in a minimum packet arrival
time.
    However, recall the earlier argument that a randomized strategy works well, in an expected sense,
for Clos networks instead of a more complex and deterministic edge-coloring scheme. Analogous to
picking a random middle switch in the Clos network, returning to Fig. 13.19, one can pick a random
destination for each cell in the first half. One can then route from the random intermediate destination
to the actual cell destination (using reverse Delta routing) in the second half. The roots of this idea of
using random intermediate destinations go back to Valiant (Valiant, 1990), who first used it to route in
a (single-copy) hypercube.
    As in the case of a Clos network using a random choice of middle switches, it can be shown that
(in an expected sense) no internal link gets congested as long as no input or output link is congested.
Intuitively, the load-splitting half takes all the traffic destined for any output link from any input and
spreads it evenly over all the N output links of the first half of Fig. 13.19. In the second half because of
the mirror-image structure, all the traffic of the link fans is back to the destined output links.
    For example, consider the upper link coming into the first switch in the last stage of Fig. 13.19. An
important claim is that this upper link will carry half of the traffic to output link 1. This is because this
upper link carries all the traffic destined for output link 1 from the top half of the input nodes in the
route-and-copy network (mirror-reversed Delta). And, by the load-splitting property of the distribute

374       Chapter 13 Switching




FIGURE 13.21
Generic load-balanced switch. (Adapted from (Ding et al., 2014).)



network (the first half of the Delta network), this is half of the traffic destined for output link 1. Similarly,
it is possible to argue that the upper link carries half the traffic going to output link 2. Thus if output
links 1 and 2 are not saturated, neither will the upper link to switch 1 in the last stage be. One can make
a similar argument for any internal link in the second half.
