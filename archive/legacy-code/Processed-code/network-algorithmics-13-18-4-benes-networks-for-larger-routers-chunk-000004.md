# network-algorithmics-13-18-4-benes-networks-for-larger-routers (chunk 000004)

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
