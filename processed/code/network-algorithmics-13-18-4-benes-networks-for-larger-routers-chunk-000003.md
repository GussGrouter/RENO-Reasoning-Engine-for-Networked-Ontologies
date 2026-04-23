# network-algorithmics-13-18-4-benes-networks-for-larger-routers (chunk 000003)

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
