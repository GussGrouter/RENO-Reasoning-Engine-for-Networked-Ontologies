# Network Algorithmics — 13.16.2 The SB-QPS algorithm (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 387
- Slice: from `13.16.2 The SB-QPS algorithm` up to next detected section heading

---

13.16.2 The SB-QPS algorithm
SB-QPS is a batch-switching algorithm that uses a small constant batch size T independent of N .
SB-QPS is a parallel iterative algorithm: the input and output ports run T QPS-like iterations (re-
quest–accept message exchanges) to collaboratively pack the joint calendar. The operation of each
iteration is extremely simple: Input ports request for cells in the joint calendar, and output ports accept
or reject the requests. More precisely, each iteration of SB-QPS, like that of QPS (Gong et al., 2017),
consists of two phases: a proposing phase and an accepting phase.
Proposing Phase. In this phase like in QPS, each input port i proposes to an output port j with a
probability proportional to the length of the corresponding VOQ. The content of the proposal (say from
i to j ) in SB-QPS, however, is slightly different than that in QPS. In QPS the proposal contains only the
VOQ length information, whereas, in SB-QPS, it also contains the following availability information
(of input port i): out of the T time slots in the batch, what (time slots) are still available for input port
i to pair with an output port? The time complexity of this QPS operation, carried out using the data
structure described in the previous section, is O(1) per input port.
Accepting Phase. In SB-QPS the accepting phase at an output port is quite different than that in QPS.
Whereas the latter allows at most one proposal to be accepted at any output port, the former allows an
output port to accept multiple (up to T ) proposals (as each output port has up to T cells in its calendar
to be filled). The operations at output port j depend on the number of proposals it receives. If output
port j receives exactly one proposal from an input port (say input port i), it tries to accommodate this
proposal using an accepting strategy called First Fit Accepting (FFA) (Meng et al., 2020). The FFA
strategy is to match in this case input port i and output port j at the earliest time slot (in the batch
of T time slots) during which both are still available (for pairing); if they have “schedule conflicts”
over all T time slots, this proposal is rejected. If output port j receives proposals from multiple input
ports, then it first sorts (with ties broken arbitrarily) these proposals in a descending order according
to their corresponding VOQ lengths, and then it tries to accept each of them using the FFA strategy. It

                                      13.16 Small-batch QPS and sliding-window QPS                     361




FIGURE 13.15
Sliding-window switching.(Adapted from Meng et al., 2020.)


was shown in Meng et al. (2020) that, when T is not too large (say T ≤ 64), this FFA operation can
be performed in one CPU cycle using a bitmap encoding (P14) of (a port’s availability during) these T
time slots, and the Find First One (FFO) instruction (to be described further in Section 14.14) available
on modern CPUs.
    The time complexity of SB-QPS is O(T ) per input or output port for the joint calendar consisting
of T matchings, since SB-QPS runs T iterations and each iteration has O(1) time complexity per input
or output port. Hence, the time complexity for computing each matching is O(1) per input or output
port.
