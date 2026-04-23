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



indicating the priority of a packet relative to other packets. For example, in WFQ the timestamp of
a packet is its GPS virtual finish time. Hence, in this context, a PIFO is precisely a standard priority
queue. However, the term PIFO is used (rather than call it a priority queue) for three reasons. First, in
the context of packet scheduling, PIFO is more than just an abstract data structure: It also embodies the
aforementioned invariant property that the service order of existing packets do not change with future
packet arrivals. Second, as explained in Sivaraman et al. (2016a), for non-work-conserving algorithms
that have this invariant property, a PIFO is a calendar queue instead. Third, the term PIFO was first
introduced in Chuang et al. (1999) for describing the proposed combined input and output queueing
(CIOQ) switching algorithm (described in Section 13.17), in which PIFO means only this invariant
property (but not the data structure). In the sequel, we refer to a work-conserving packet scheduling
algorithm that has this property as PIFO-compatible.
    For each supported PIFO-compatible algorithm, there is only one parameter to be specified under
this programmable packet scheduling framework: a callback procedure that assigns a timestamp to
each packet right upon its arrival. Such a callback procedure is called scheduling transaction in Sivara-
man et al. (2016b). For example, the scheduling transaction in WFQ can be implemented using the
efficient GPS clock tracking algorithm (Valente, 2004) described in Section 14.12. For another ex-
ample, the scheduling transaction in FIFO (first in first out) is trivial: The timestamp of a packet is
simply the arrival time of the packet. It was shown in Sivaraman et al. (2016a) that this programmable
packet scheduling framework supports, besides WFQ and FIFO, several other well-known algorithms
(including those that are non-work-conserving) such as Token Bucket Filtering (described in Sec-
tion 14.4), Hierarchical Packet Fair Queueing (aka. WF2 Q+) (Bennett and Zhang, 1996a), Least-Slack
Time-First (Leung, 1989), the Rate Controlled Service Disciplines (Zhang and Ferrari, 1994), and fine-
grained priority scheduling (e.g., Shortest Job First).
