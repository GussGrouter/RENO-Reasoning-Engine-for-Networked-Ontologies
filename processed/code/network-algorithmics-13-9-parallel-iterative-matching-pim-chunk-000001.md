# network-algorithmics-13-9-parallel-iterative-matching-pim (chunk 000001)

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
