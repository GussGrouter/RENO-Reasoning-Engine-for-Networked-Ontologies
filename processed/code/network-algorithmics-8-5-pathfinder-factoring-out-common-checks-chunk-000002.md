# network-algorithmics-8-5-pathfinder-factoring-out-common-checks (chunk 000002)

A data structure for this purpose is shown in Fig. 8.5. The basic idea is to superimpose the CFGs
for each filter in BPF so that all comparisons on the same field are placed in a single node. Finally,
each node is implemented as a hash table containing all comparison values to replace linear search with
hashing.
    Fig. 8.5 shows an example with at least four filters, two of which specify TCP packets with des-
tination port numbers 2 and 5; for now, ignore the dashed line to TCP port 17, which will be used as
an example of filter insertion in a moment. Besides the TCP filters, there are one or more filters that
specify ARP packets and one or more filters that specify packets that use the OSI protocol.
    The root node corresponds to the Ethernet type field; the hash table contains values for each possible
Ethernet type field value used in the filters. Each node entry has a value and a pointer. Thus the ARP
entry points to nodes that further specify what type of ARP packets must be received; the OSI entry
does likewise. Finally, the Ethernet type field corresponding to IP points to a node corresponding to the
IP protocol field.
    In the IP protocol field node one of the values corresponding to TCP (which has value 6) will point
to the TCP node. In the TCP node there are three values pointing to the three possible destination
port values of 2 and 5 (recall that the 17 has not been inserted yet). When a TCP packet arrives,
demultiplexing proceeds as follows.
    Search starts at the root, and the Ethernet type field is hashed to find a matching value corresponding
to IP. The pointer of this value leads to the IP node, where the IP protocol type field is hashed to find a

204      Chapter 8 Demultiplexing
