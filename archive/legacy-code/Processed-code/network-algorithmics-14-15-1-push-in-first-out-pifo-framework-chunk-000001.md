# network-algorithmics-14-15-1-push-in-first-out-pifo-framework (chunk 000001)

# Network Algorithmics — 14.15.1 Push-In First-Out (PIFO) framework (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 449
- Slice: from `14.15.1 Push-In First-Out (PIFO) framework` up to next detected section heading

---

14.15.1 Push-In First-Out (PIFO) framework
Under the PIFO framework Sivaraman et al. (2016a), packet scheduling is programmable in the sense
that several different packet scheduling algorithms can be instantiated from a template via picking
different parameter values. For example, a data center network equipped with switches supporting such
a programmable capability can allow network operators to instantiate a supported packet scheduling
algorithm best suited for the network.
    The PIFO framework can support both work-conserving and non-work-conserving packet schedul-
ing algorithms. However, since the former is the focus of this chapter, in the rest of this section we
consider only the former and omit the qualifier “work-conserving” with the implicit understanding that
we are only referring to work-conserving algorithms. The design of PIFO is based on the observation
that a packet scheduling algorithm needs to make only one decision concerning packet arrivals: In what
order should existing packets (those currently in the packet queue) be served? For many algorithms, this
decision can be made when a packet is enqueued in the following sense. For any two exiting packets,
the relative order in which they should be served will not change with any future packet arrivals. For
example, this is the case in WFQ, since the QPS virtual finish time of any packet is determined as soon
as the packet has arrived. Not all work-conserving algorithms have this invariant property though. For
example, although the WF2 Q algorithm is work-conserving (see exercise problem 10 in Section 14.18),
it does not have this invariant property (see exercise problem 11 in Section 14.18).
    This invariant property is important, with respect to programmability, because a packet scheduling
algorithm having this property can be implemented using an abstract data structure called a push-in
first-out (PIFO) queue (Sivaraman et al., 2016a). A PIFO is a priority queue that allows elements to
be pushed to an arbitrary relative position based on an element’s rank, but always dequeues from the
head. In the context of packet scheduling using a work-conserving algorithm, this rank is a timestamp

14.15 Towards programmable packet scheduling                   423
