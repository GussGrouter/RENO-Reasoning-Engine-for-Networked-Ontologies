# network-algorithmics-14-10-weighted-fair-queueing (chunk 000002)

maximum-size packet at the full link rate r. For example, in the packet arrival instance, it is not hard to
verify that, for each of the seven packets, this difference is always upper-bounded by 7/1 = 7, where 7
is the maximum packet size and r = 1 is the link rate.
    Next, we briefly discuss the WFQ algorithm, the implementation of the WFQ policy. The WFQ
algorithm consists of two parts. The first part is the tracking of GPS clock, through which the GPS
virtual finish time of each packet can be determined. The second part is to have the GPS virtual finish
times of all packets currently in queue stored in a balanced priority queue data structure such as a heap,
so that “who is next” can be determined by making an ExtractMin() method call, which has O(log n)
time complexity per call (packet). Since the second part is straightforward, we only describe how to
implement the first part, GPS clock tracking, in detail in Section 14.12.
