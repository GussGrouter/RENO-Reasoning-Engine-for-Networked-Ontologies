# network-algorithmics-13-17-combined-input-and-output-queueing (chunk 000001)

# Network Algorithmics — 13.17 Combined input and output queueing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 389
- Slice: from `13.17 Combined input and output queueing` up to next detected section heading

---

13.17 Combined input and output queueing
A switch architecture called Combined Input and Output Queueing (CIOQ) was studied in late 1990s
and early 2000s (Prabhakar and McKeown, 1997) (Stoica and Zhang, 1998) (Chuang et al., 1999) (Iyer
et al., 2002) (Yang and Zheng, 2003) (Giaccone et al., 2004) (Firoozshahian et al., 2007). CIOQ was
motivated by the need to provide Quality of Service (QoS) guarantees via performing packet scheduling
(topic of the next chapter) at output ports. In CIOQ, packets are queued at both input and output ports,
which gives the architecture its name. The design objective of CIOQ is to fully emulate the effect of
output queueing, as far as the packet scheduling at output ports is concerned, without paying for the
aforementioned high cost (of N -fold speedup at the output ports as explained in Section 13.6) of output
queueing.
    We now elaborate on the concept of “full emulation”. For an output-queued switch to provide a cer-
tain QoS guarantee, each output port j needs to enforce a certain packet scheduling policy P (common
to all output ports) among the N Virtual Input Queues (VIQs) at output port j , where the i th VIQ (at
output port j ) holds all the packets that arrived from input port i. In an output-queued switch, given any
packet arrival instance, P completely determines the service order of these packets, since each packet
can “fly” directly to its output port upon arrival without any delay as guaranteed by an output-queued
switch. A switch is said to fully emulate output queueing if, given any packet arrival instance, it pro-
duces exactly the same packet service order as an output-queued switch, no matter what P is used by
both switches (at the output ports for packet scheduling).
    A CIOQ switch is very different than an input-queued switch in that the former computes a very
different matching than the latter. In a CIOQ switch, the matching between input and output ports at
any given time (cycle) is decided based on the deadlines or priority scores assigned to the HOL packets
of the N 2 VOQs or VIQs by P; and a matching π thus computed must be a stable matching (Gale and
Shapley, 1962) in the sense there does not exist a pair of input and output ports that both prefer (to
pair with) each other (according to these deadlines or priority scores) to their current pairing under π.
In contrast, no crossbar scheduling algorithms described in the previous sections for an input-queued
switch has anything to do with such a P, or computes a stable matching.
    The CIOQ technology has never taken off, likely because its cost is high in two aspects. First, CIOQ
scheduling algorithms generally have a high time complexity of O(N 2 ) (per cycle) since these N 2
deadlines or priority scores need to be somehow sorted out for a stable matching to be computed (Gale
and Shapley, 1962). Second, they can only guarantee 50% throughput (Chuang et al., 1999) (Dai and

13.18 Scaling to larger and faster switches             363
