# network-algorithmics-8-5-pathfinder-factoring-out-common-checks (chunk 000001)

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
