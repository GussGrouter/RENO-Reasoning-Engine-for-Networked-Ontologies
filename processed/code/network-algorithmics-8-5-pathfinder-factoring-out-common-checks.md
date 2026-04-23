# Network Algorithmics — 8.5 Pathfinder: factoring out common checks (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 228
- Slice: from `8.5 Pathfinder: factoring out common checks` up to next detected section heading

---

8.5 Pathfinder: factoring out common checks
BPF is a more refined adaptation than CSPF because it increases speed for a single filter. However,
every packet must still be compared with each filter in turn. Thus the processing time grows with
the number of filters. Fortunately, this is not a problem for typical BPF usage. For example, a typical
tcpdump application may provide only a few filters to BPF.
    However, this is not true if early demultiplexing is used to discriminate between a large number
of packet streams or paths. In particular, each TCP connection may provide a filter, and the number

202       Chapter 8 Demultiplexing




FIGURE 8.4
Packets arriving on a link are sent to both BPF (for potential logging) and the protocol stack (for normal protocol
processing). BPF applies all currently specified filters and queues the packet to the appropriate buffer if the filter
indicates a match.



of concurrent TCP connections in a busy server can be large. The need to deal with this change in
environment (user-level networking) led to another successful mutation called Pathfinder (Bailey et al.,
1994). Pathfinder goes beyond BPF by providing composability. This allows scaling to a large number
of users.
    To motivate the Pathfinder solution, imagine there are 500 filters, each of which is exactly the same
(Ethernet type field is IP, IP protocol type is TCP) except that each specifies a different TCP port
pair. Doing each filter sequentially would require comparing the Ethernet type of the packet 500 times
against the (same) IP Ethernet type field and comparing the IP protocol field 500 times against the
(same) TCP protocol value. This is wasteful (P1).
    Next, comparing the TCP port numbers in the packet to each of the 500 port pairs specified in each
of the 500 filters is not obvious waste. However, this is exactly analogous to a linear search for exact
matching. This suggests that integrating all the individual filters into a single composite filter can con-
siderably reduce unnecessary comparisons when the number of individual filters is large. Specifically,
this can be done using hashing (P15, using efficient data structures) to perform an exact search; this can
replace 500 comparisons with just a few comparisons.
    As we have said repeatedly at the start of this chapter, if one only has TCP this notion of hashing is
already implemented by receive packet steering mechanisms. A more complex data structure is needed
if one wishes to do flexible demultiplexing of general protocols.

                                               8.5 Pathfinder: factoring out common checks                          203




FIGURE 8.5
The Pathfinder data structure integrates several versions of the BPF CFG integrated into a composite structure. In the
composite structure all the different field values specified in different filters for a given header field are placed in a
single node. Rather than searching these values linearly, the header field values are placed in a hash table.



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



matching value corresponding to TCP. The value pointer leads to the TCP node, where the destination
port value in the packet is hashed to lead to the final matching filter.
    The Pathfinder data structure has a strong family resemblance to a common data structure called a
trie, which is more fully described in Chapter 11. Briefly, a trie is a tree in which each node contains an
array of pointers to subtries; each array contains one pointer for each possible value of a fixed-character
alphabet.
    To search the trie for a keyword, the keyword is broken into characters, and the ith character is used
to index into the ith node on the path, starting with the root. Searching in this way at node i yields a
pointer that leads to node i + 1, where search continues recursively. One can think of the Pathfinder
structure as generalizing a trie by using packet header fields (e.g., Ethernet type field) as the successive
characters used for search and by using hash tables to replace the arrays at each node.
    It is well known that tries provide fast insertions of new keys. Given this analogy, it is hardly
surprising that Pathfinder has a fast algorithm to insert or delete a filter. For instance, consider inserting
a new filter corresponding to TCP port 17. As in a trie, the insert algorithm starts with a search for the
longest matching prefix (Chapter 11) of this new filter.
    This longest match corresponds to the path Ethernet Type = IP and IP Protocol = TCP. Since
this path has already been created by the other two TCP filters, it need not be replicated. The insertion
algorithm only has to add branches (in this case a single branch) corresponding to the portion of the
new filter beyond the longest match. Thus the hash table in the TCP node need only be updated to add
a new pointer to the port 17 filter.
    More precisely, the basic atomic unit in Pathfinder is called a cell. A cell specifies a field of bits in
a packet header (using an offset, length, and a mask), a comparison value, and a pointer. For example,
ignoring the pointer, the cell that checks whether the protocol field in the IP header is (9, 1, 0xff,
6)—the cell specifies that the tenth byte of the IP header should be masked with all 1’s and compared
to the value 6, which specifies TCP.
    Cells of a given user are strung together to form a pattern for that user. Multiple patterns are super-
imposed to form the Pathfinder trie by not recreating cells that already exist. Finally, multiple cells that
specify identical bit fields but different values are coalesced using a hash table.
    Besides using hash tables in place of arrays, Pathfinder also goes beyond tries by making each node
contain arbitrary code. In effect, Pathfinder recognizes that a trie is a specialized state machine that can
be generalized by performing arbitrary operations at each node in the trie. For instance, Pathfinder can
handle fragmented packets by allowing loadable cells in addition to the comparison cells described
earlier. This is required because for a fragmented packet, only the first fragment specifies the TCP
headers; what links the fragments together is a common packet ID described in the first fragment.
    Pathfinder handles fragmentation by placing an additional loadable cell (together with the nor-
mal IP comparison cell specifying, say, a source address) that is loaded with the packet ID after the
first fragment arrives. A cell is specified as loadable by not specifying the comparison value in a
cell.
    The loadable cell is not initially part of the Pathfinder trie but is instead an attribute of the IP
cells. If the first fragment matches, the loaded cell is inserted into the Pathfinder trie and now matches
subsequent fragments based on the newly loaded packet ID. After all fragments have been removed,
this newly added cell can be removed. Finally, Pathfinder handles the case when the later fragments
arrive before the first fragment by postponing their processing until the first fragment arrives.

                                   8.6 Dynamic packet filter: compilers to the rescue                205



    Although Pathfinder has been described so far as a tree, the data structure can be generalized to
a directed acyclic graph (DAG). A DAG allows two different filters to initially follow different paths
through the Pathfinder graph and yet come together to share a common path suffix. This can be useful,
for instance, when providing a filter for TCP packets for destination port 80 that can be fragmented
or unfragmented. While one needs a separate path of cells to specify fragmented and unfragmented IP
packets, the two paths can point to a common set of TCP cells.
    Finally, Pathfinder also allows the use of OR links that lead from a cell. The idea is that each of the
OR links specify a value, and each of the OR links is checked to find a value that matches and then that
link is followed.
    In order to prioritize packets during periods of congestion, as in Chapter 6, the demultiplexing
routine must complete in the minimum time it takes to receive a packet. Software implementations of
Pathfinder are fast but are typically unable to keep up with line speeds. Fortunately, the Pathfinder state
machine can be implemented in hardware to run at line speeds. This is analogous to the way IP lookups
using tries can be made to work at line speeds (Chapter 11).
    The hardware prototype described in Bailey et al. (1994) trades functionality for speed. It works
in 16-bit chunks and implements only the most basic cell functions; it does, however, implement frag-
mentation in hardware. The limited functionality implies that the Pathfinder hardware can only be used
as a cache to speed up Pathfinder software that handles the less common cases. A prototype design
running at 100 MHz was projected to take 200 nanoseconds to process a 40-byte TCP message, which
is sufficient for 1.5 Gbps. The design can be scaled to higher wire speeds using faster clock rates, faster
memories, and a pipelined traversal of the state machine.
