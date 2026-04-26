# Network Algorithmics — 13.15.2 The QPS data structure (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 384
- Slice: from `13.15.2 The QPS data structure` up to next detected section heading

---

13.15.2 The QPS data structure
We show that the two steps of the QPS proposing strategy can be performed in O(1) time, at any input
port, via a main and an auxiliary data structures, that are the same for all input ports. Fig. 13.13(A)
and (B) present the data structures, at a single input port, before and after the HOL packet of its j th
VOQ is chosen for (switching) service. The top half and bottom half of the figures show the main and
the auxiliary data structures, respectively.
The main data structure. The main data structure is an array of N records, corresponding to the N
VOQs at the input port. Each record j (i.e., array entry j ) is associated with a linked list that corresponds
to (pointers to) packets queued at a VOQ in the order they arrived, starting with the HOL packet. Each
node in the linked list contains two pointers encoded as “letter” (e.g., A); one points to the actual
packet (e.g., packet A) in the packet buffer (not shown in the figure) and the other to the corresponding
entry (e.g., entry A) in the auxiliary data structure, which we refer to as a back pointer.
    For simplicity Fig. 13.13 shows only record j (corresponding to VOQ j ). Each record contains a
head and tail pointers that point to the head node and the tail node of the linked list, respectively. The

358       Chapter 13 Switching




FIGURE 13.13
Illustrating the action of the QPS data structures on a single-input port. (Adapted from Gong et al., 2017.)


head pointer is needed for locating and for removing the head node (i.e., the HOL packet) in O(1) time;
it is also needed for locating and replacing the array entry that corresponds to the HOL packet in the
auxiliary data structure. The tail pointer is needed for inserting a newly arrived packet to the “end of
the VOQ” (i.e., the first basic operation) in O(1) time.
The auxiliary data structure. The bottom half of Fig. 13.13 shows the auxiliary data structure used
for performing the sampling. Suppose there are a total of m packets queued across all N VOQs at the
input port. The auxiliary data structure is simply an array of m entries, each of which is a pointer that
points to a distinct (packet) node (e.g., node A) in one of the N linked lists in the main data structure.
    Despite arrivals and departures of packets over time, the auxiliary data structure always occupies a
contiguous block of array entries, the boundaries of which are identified by a head and a tail pointer as
shown in the bottom half of Fig. 13.13. This contiguity allows an array entry (packet) to be sampled
uniformly at random in O(1) time, an aforementioned key step of QPS. Hence, this contiguity needs
to be maintained in the event of packet arrivals and departures. The case of a packet arrival is easier:
the entry corresponding to the new packet is inserted after the current tail position, and the tail pointer
updated. The case of a packet departure is only slightly trickier: if the departing packet leaves a “hole”
in the block, the tail entry is moved to fill this hole, and the tail pointer updated.
    In the case of a packet departure the (packet) node in the main data structure that is pointed to by
the former tail entry (now moved to “fill the hole”) needs to have its back pointer updated to the offset
of the former hole, where the former tail entry is now. This is clearly an O(1) procedure. A similar
procedure can be used to support the second basic operation in O(1) time.
An illustrative example. To see how the main and the auxiliary data structures work together to facili-
tate QPS, consider the example shown in Fig. 13.13 where the packet A was sampled out of m packets
in the auxiliary data structure. However, it is not the HOL packet, so its destination (output) port (i.e.,
VOQ identifier) is checked, which turns out to be j . By accessing the j th record in the main data struc-
ture that corresponds to VOQ j , the HOL packet is found to be packet B. Now, the input port proposes
to match with output port j . If the proposal is accepted by, and the input port is eventually matched to,
output port j , packet B will depart (for output port j ) in the current time slot. The head pointer in the
j th record of the main data structure is updated to (point to) E, the new HOL packet. These changes are

                                    13.16 Small-batch QPS and sliding-window QPS                   359



captured in Fig. 13.13(B). These operations, including the search for the HOL packet and the updates
to both data structures, all take O(1) time.
