# network-algorithmics-14-15-1-push-in-first-out-pifo-framework (chunk 000002)

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
