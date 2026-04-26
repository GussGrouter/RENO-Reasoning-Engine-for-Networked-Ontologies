# Network Algorithmics — 13.9 Parallel iterative matching (PIM) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 373
- Slice: from `13.9 Parallel iterative matching (PIM)` up to next detected section heading

---

13.9 Parallel iterative matching (PIM)
Strictly speaking, PIM is an approximate maximal matching algorithm in the sense that it outputs a
maximal matching only with high probability, and the same can be said about iSLIP. PIM is a random-
ized algorithm (P3a). In particular, it can be viewed as an adaptation of the randomized (approximate)
maximal matching algorithm proposed in Israel and Itai (1986) to switching. In PIM the scheduling
needs of any input port takes a bitmap of only N bits, where N is the size of the switch. In the bitmap,
a 1 in position i implies that there is at least one cell destined for output port i. Thus if each of N input
ports communicates an N -bit vector describing its scheduling needs, the scheduler needs to process
only N 2 bits. For small N ≤ 32, this is not many bits to communicate via control buses or to store in
control memories.
    The communicating of requests is indicated in the top left diagram of Fig. 13.7 by showing a line
sent from each input port to each output port for which it has a nonempty VOQ. Notice A does not have
a line to port 4 because it has no cell for port 4. Notice also that input port C sends a request for the
cell destined for output port 4 in input port C, while the same cell is the last cell in input queue C in
the single-input-queue scenario of Fig. 13.5.
    What is still required is a scheduling algorithm that matches resources to needs. Although the
scheduling algorithm is clever, it is the author’s opinion that the real breakthrough was observing that,
using VOQs, input-queue scheduling without HOL blocking is feasible to think about. To keep the ex-
ample in Fig. 13.7 corresponding to Fig. 13.5, assume that every packet in the scenario of Fig. 13.5 is
converted into a single cell in Fig. 13.7.
    To motivate the scheduling algorithm used in PIM, observe that on the top left diagram of Fig. 13.7,
output port 1 gets three requests from A, B, and C but can service only one in the next slot. A simple
way to choose between requests is to choose randomly (P3a). Thus in the Grant phase (top middle
diagram of Fig. 13.7) output port 1 chooses B randomly. Similarly, assume that port 2 randomly chooses
A (from A and B), port 3 randomly chooses A (from A, B, and C), and finally port 4 chooses its only
requester, C.
    However, resolving output-port contention is insufficient because there is also input-port contention.
Two output ports can randomly grant to the same input port, which must choose exactly one to send
a cell to. For example, on the top middle diagram of Fig. 13.7 A has an embarrassment of riches by
getting grants from outputs 2 and 3. Thus a third, Accept, phase is necessary, in which each input port

                                                      13.10 Avoiding randomization with iSLIP                       347



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
