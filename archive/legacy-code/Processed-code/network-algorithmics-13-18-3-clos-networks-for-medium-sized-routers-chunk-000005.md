# network-algorithmics-13-18-3-clos-networks-for-medium-sized-routers (chunk 000005)

370      Chapter 13 Switching

re-sequencing capability of modern NICs at end hosts is cleverly exploited to keep the percentage of
out-of-order packets to a minimum.
    An alternative load-balancing approach, known as TCP hashing (Keslassy, 2004), does not have
this packet reorder problem. In this approach all packets belonging to the same TCP flow must take the
same path (i.e., links and switches) through the Clos network. At each input port of a switch at the first
level, this can be achieved by hashing on the TCP flow identifier (source and destination IP addresses,
source and destination ports, and protocol identification) of every incoming packet to obtain a value
between 1 and N , which corresponds to the output port of this switch to which this packet should be
forwarded. However, while eliminating the packet-reorder problem, TCP hashing can lead to severe
load-imbalance. For example, all packets in an elephant flow, which travel the same path, will congest
the links and switches along the path. Hence, recently, in an LBS scheme (to be described in Sec-
tion 13.18.5) called safe randomized switching (SRS) (Yang et al., 2017b), the TCP hashing approach
was enhanced with two safety mechanisms to effectively mitigate this load-imbalance problem.
