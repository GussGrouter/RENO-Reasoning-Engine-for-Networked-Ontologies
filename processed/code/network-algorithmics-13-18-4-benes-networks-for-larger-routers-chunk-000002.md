# network-algorithmics-13-18-4-benes-networks-for-larger-routers (chunk 000002)

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
