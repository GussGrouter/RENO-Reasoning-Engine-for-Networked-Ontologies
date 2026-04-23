# network-algorithmics-13-5-head-of-line-blocking (chunk 000001)

# Network Algorithmics — 13.5 Head-of-line blocking (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 367
- Slice: from `13.5 Head-of-line blocking` up to next detected section heading

---

13.5 Head-of-line blocking
Forgetting about the internal mechanics of Fig. 13.5, observe that there were nine potential transmission
opportunities in three iterations (three input ports and three iterations), but, after the connection depicted
in the diagram at the bottom right, there is one packet in B’s queue and two in C’s queue. Thus only
six of potentially nine packets have been sent, thereby taking limited advantage of parallelism.
    This focus on only input–output behavior is sketched in Fig. 13.6. The figure shows the packets sent
in each packet time at each output port. Each output port has an associated timeline labeled with the

13.5 Head-of-line blocking                341

FIGURE 13.6
Example of HOL blocking caused by schemes like take-a-ticket. For each output port, a horizontal time scale is
drawn labeled with the input port that sent a packet to that output port during the corresponding time period or a
blank mark if there is none. Note the large number of blanks, showing potentially wasted opportunities that limit
parallelism.
