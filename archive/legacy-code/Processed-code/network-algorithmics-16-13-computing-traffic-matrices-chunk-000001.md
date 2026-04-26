# network-algorithmics-16-13-computing-traffic-matrices (chunk 000001)

# Network Algorithmics — 16.13 Computing traffic matrices (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 499
- Slice: from `16.13 Computing traffic matrices` up to next detected section heading

---

16.13 Computing traffic matrices
While the DCU solution is useful only for accounting, a generalization of some of the essential ideas
can help in solving the traffic matrix problem. This is a problem of great interest to many ISPs.

3 It can also be made sensitive to the type of service by also using the DiffServ byte to determine the class.

16.13 Computing traffic matrices                    473

To define the traffic matrix problem, consider a network (e.g., Z in Fig. 16.13) such as those used
by ISPs Sprint and AT&T. The network can be modeled as a graph with links connecting router nodes.
Some of the links from a router in ISP Z go to routers belonging to other ISPs (E2, E3) or cus-
tomers (E1, E4, E5). Let us call such links external links. Although we have lumped them together
in Fig. 16.13, external links directed toward the ISP router are called input links, and external links
directed away from an ISP router are called output links.
    The traffic matrix of a network enumerates the amount of traffic that was sent (in some arbitrary
period, say, a day) between every pair of input and output links of the network. For example, the traffic
matrix could tell managers of ISP Z in Fig. 16.13 that 60 Mbits of traffic entered during the day from
Customer A, of which 20 Mbits exited on the peering link E2 to ISP X, and 40 Mbps left on link E5
to Customer B.
    Network operators find traffic matrices (over various time scales ranging from hours to months)
indispensable. They can be used to make more optimal routing decisions (working around suboptimal
routing by changing OSPF weights or setting up MPLS tunnels), for knowing when to set up circuit-
switched paths (avoiding hot spots), for network diagnosis (understanding causes of congestion), and
for provisioning (knowing which links to upgrade on a longer time scale of months).
    Unfortunately, existing legacy routers provide only a single aggregate counter (the SNMP link byte
counter) of all traffic traversing a link, which aggregates traffic sent between all pairs of input and
output links that traverse the link. Inferring the traffic matrix from such data is problematic because
there are O(V 2 ) possible traffic pairs in the matrix (where V is the number of external links), and many
sparse networks may have only, say, O(V ) links (and hence O(V ) counters). Even after knowing how
traffic is routed, one has O(V ) equations for O(V 2 ) variables, which makes deterministic inference (of
all traffic pairs) impossible. This dilemma has led to two very different solution approaches. We now
describe these two existing solutions and a proposed new approach.
