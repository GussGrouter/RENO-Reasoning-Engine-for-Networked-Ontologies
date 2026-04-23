# network-algorithmics-13-9-parallel-iterative-matching-pim (chunk 000002)

chooses an output port randomly (since randomization was used in the Grant phase, why not use it
again?).
    Thus in the top right diagram of Fig. 13.7, A randomly chooses port 2. B and C have no choice and
choose ports 1 and 4, respectively. Crossbar connections are made, and the packets from A to port 2, B
to port 1, and C to port 4 are transferred. While in this case, the corresponding match found happened to
be a maximal matching, in some cases the random choices may result in a matching that is not maximal.
For example, in the unlikely event that ports 1, 2, and 3, all choose A, and the matching size will only
be of size 2.
    In such cases although not shown in the figure, it may be worthwhile for the algorithm to mask
out all matched inputs and outputs and iterate more times (for the same forthcoming time slot). If the
matching on the current iteration is not maximal, a further iteration will improve the size of the matching
by at least 1. Note that subsequent iterations cannot worsen the match because existing matchings are
preserved across iterations. While the worst-case time to reach a maximal matching for N inputs is N
iterations, a simple argument shows that the expected number of matchings is closer to log N . The DEC
AN-2 implementation (Anderson et al., 1993) used three iterations for a 30-port switch.
    Our example in Fig. 13.7, however, uses only one iteration for each match (matching). The middle
row shows the second match for the second time slot, in which, for example, A and C both ask for port
1 (but not B because the B-to-1 cell was sent in the last time slot). Port 1 randomly chooses C, and the
final match is A, 3, B, 2, and C, 1. The third row shows the third match, this time of size 2. At the end
of the third match, only the cell destined for port 3 in input queue B is not sent. Thus in four time slots
(of which the fourth time slot is sparsely used and could have been used to send more traffic) all the
traffic is sent. This is clearly more efficient than the take-a-ticket example of Fig. 13.5.
