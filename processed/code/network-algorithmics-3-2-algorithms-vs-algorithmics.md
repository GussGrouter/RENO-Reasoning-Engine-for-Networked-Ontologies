# Network Algorithmics — algorithms vs algorithmics (3.2) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 82 -l 111 -layout
- Slice: from `3.2 Algorithms versus algorithmics` up to (excluding) `3.3.1`

---

3.2 Algorithms versus algorithmics                          55



prefixes,1 creating a hole at the end of the length-2 prefixes, etc., until we create a hole at the end of the
length-i prefixes. Thus the worst-case time is 32 − i memory accesses, which is around 32 for small i.
    Are we done? No, we can do better by further exploiting degrees of freedom. First, in Fig. 3.5 we
assumed that the free space was at the top of the CAM. But the free space could be placed anywhere. In
particular, it can be placed after the length-16 prefixes. This reduces the worst-case number of memory
accesses by a factor of 2 (Shah and Gupta, 2001).
    A more sophisticated degree of freedom is as follows. So far, the specification of the CAM insertion
algorithm required that “a prefix of length i must occur before a prefix of length j if i > j .” Such
a specification is sufficient for correctness but is not necessary. For example, 010* can occur before
111001* because there is no address that can match both prefixes!
    Thus a less exacting specification is “if two prefixes P and Q can match the same address, then P
must come before Q in the CAM if P is longer than Q.” This is used in Shah and Gupta (2001) to
further reduce the worst-case number of memory accesses for insertion for some practical databases.
    While the last improvement is not worth its complexity, it points to another important principle. We
often divide a large problem into subproblems and hand over the subproblem for a solution based on a
specification. For example, the CAM hardware designer may have handed over the update problem to
a microcoder, specifying that longer prefixes be placed before shorter ones.
    But, as before, such a specification may not be the only way to solve the original problem. Thus
changes to the specification (principle P3) can yield a more efficient solution. Of course, this requires
curious and confident individuals who understand the big picture or who are brave enough to ask dan-
gerous questions.



3.2 Algorithms versus algorithmics
It may be possible to argue that the previous example is still essentially algorithmic and does not
require system thinking. One more quick example will help clarify the difference between algorithms
and algorithmics.

Security forensics problem
In many intrusion detection systems, a manager often finds that a flow (defined by some packet header,
for example, a source IP address) is likely to be misbehaving based on some probabilistic check. For
example, a source doing a port scan may be identified after it has sent 100,000 packets to different
machines in the attacked subnet.
    While there are methods to identify such sources, one problem is that the evidence (the 100,000
packets sent by the source) has typically disappeared (i.e., been forwarded from the router) by the time
the guilty source is identified. The problem is that the probabilistic check requires accumulating some
state (in, say, a suspicion table) for every packet received over some period of time before a source can
be deemed suspicious. Thus if a source is judged to be suspicious after 10 seconds, how can one go
back in time and retrieve the packets sent by the source during those 10 seconds?


1 For simplicity, this description has assumed that the CAM contains prefixes of all lengths; it is easy to modify the algorithm to
avoid this assumption.

---

## PDF page 83

56        Chapter 3 Fifteen implementation principles




FIGURE 3.6
Keeping a queue of the last 100,000 packets that contains forensic information about what suspicious flows have
been sent in the past.


    To accomplish this, in Fig. 3.6 we keep a queue of the last 100,000 packets that were sent by the
router. When a packet is forwarded, we also add a copy of the packet (or just keep a pointer to the
packet) to the head of the queue. To keep the queue bounded, when the queue is full, we delete from
the tail as well.
    The main difficulty with this scheme is that when a guilty flow is detected, there may be lots of
the flow’s packets in the queue (Fig. 3.6). All of these packets must be placed in the forensic log for
transmission to a manager. The naive method of searching through a large DRAM buffer is very slow.
    The textbook algorithms approach would be to add some index structure to search quickly for flow
IDs. For example, one might maintain a hash table of flow IDs that maps every flow to a list of pointers
to all packets with that flow ID in the queue. When a new packet is placed in the queue, the flow ID is
looked up in the hash table and the address of the new packet in the queue is placed at the end of the
flow’s list. Of course, when packets leave the queue, their entries must be removed from the list, and
the list can be long. Fortunately, the entry to be deleted is guaranteed to be at the head of the queue for
that flow ID.
    Despite this, the textbook scheme has some difficulties. It adds more space to maintain these extra
queues per flow ID, and space can be at a premium for a high-speed implementation. It also adds some
extra complexity to packet processing to maintain the hash table and requires reading out all of a flow’s
packets to the forensic log before the packet is overwritten by a packet that arrives 100,000 packets
later. Instead, the following “systems” solution may be more elegant.

Solution
Do not attempt to immediately identify all of a flow F ’s packets when F is identified, but lazily identify
them as they reach the end of the packet queue. This is shown in Fig. 3.7. When we add a packet to the
head of the queue, we must remove a packet from the end of the queue (at least when the queue is full).

---

## PDF page 84
