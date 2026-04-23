# network-algorithmics-13-15-1-the-qps-algorithm-this-algorithm-consists-of-two-steps-in-the-first-step (chunk 000001)

# Network Algorithmics — 13.15.1 The QPS algorithm This algorithm consists of two steps. In the first step we sample a packet, out of all packets currently (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 384
- Slice: from `13.15.1 The QPS algorithm This algorithm consists of two steps. In the first step we sample a packet, out of all packets currently` up to next detected section heading

---

13.15.1 The QPS algorithm
This algorithm consists of two steps. In the first step we sample a packet, out of all packets currently
queued at the input port, uniformly at random. Specifically, if there are a total of m packets across all
N VOQs at the input port, each packet is sampled with probability 1/m. With such uniform sampling,
the j th VOQ that has length mj will have one of the packets sampled with probability mj /m. This is
precisely the QPS behavior.
    Suppose a packet is thus sampled. A part of the second step is to find out which VOQ this packet
belongs to so that the input port can propose to the corresponding output port with its queue length.
However, more effort is still required. Since all switching algorithms serve packets in a VOQ strictly in
the FIFO order, if this proposal is successful (i.e., accepted by the output port), and the input and output
port pair is eventually a part of the final matching, the HOL packet of this VOQ, which may or may not
be the sampled packet, needs to be located and serviced. Hence, the other part of the second step is to
locate the HOL packet of this VOQ.
    Before going into the details, we list two other basic operations that this data structure needs also
to support. The first operation is that any new incoming packet must be recorded in the data structure
so that it is logically “added to the end of the VOQ that it belongs to.” The second operation is that,
when the scheduling algorithm eventually decides to pair the input port with a different output port than
was proposed to, which could happen due to either the proposal being rejected or the initially accepted
proposal being overridden by the scheduling algorithm (e.g., during SERENA’s MERGE operation in
the case of QPS-SERENA), the HOL packet of the (new) corresponding VOQ needs to be located and
removed for receiving the switching service. Both operations can be supported with O(1) complexity,
as will be shown next.
