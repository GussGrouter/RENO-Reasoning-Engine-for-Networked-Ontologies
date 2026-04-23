# network-algorithmics-14-15-2-universal-packet-scheduler (chunk 000001)

# Network Algorithmics — 14.15.2 Universal packet scheduler (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 450
- Slice: from `14.15.2 Universal packet scheduler` up to next detected section heading

---

14.15.2 Universal packet scheduler
Programmable packet scheduling implies that when the switch packet scheduling algorithm changes
for say a new bandwidth allocation criterion, the switch must be reprogrammed. However, reprogram-
ming switches frequently can disrupt the high-speed operations of a production network. The Universal
Packet Scheduler paper (Mittal et al., 2015) studied whether a change in the fairness criteria necessar-
ily requires switch reprogramming. Does there exist a universal packet scheduler S that can emulate
(called replay) the bandwidth allocation behavior of any packet scheduling algorithm? If the answer to
this question is yes, then we need to program only S on programmable switches once and for all, and
never need to reprogram it thereafter.
    To provide a short introduction to the concept of a universal packet scheduler, we have to introduce
some terms and notation. Consider a network of routers connected by links, with a boundary comprised
of ingress and egress routers. Every router uses a certain packet scheduling algorithm for scheduling
packets along its output links, and different routers may use different packet scheduling algorithms.
We denote the set of packet scheduling algorithms these routers use as {Aα } in the sense router α uses
algorithm Aα . Consider a packet arrival instance {(p, i(p), path(p))|p ∈ P } to the ingress routers,
where P is a set of packets, i(p) is the arrival time of p to an ingress router, and path(p) is the
path p takes through the network to the egress router. Let o(p) be the departure time of p (from the
network), or when p leaves the corresponding egress router. Then {(path(p), i(p), o(p))|p ∈ P } is
called a schedule.

424       Chapter 14 Scheduling packets
