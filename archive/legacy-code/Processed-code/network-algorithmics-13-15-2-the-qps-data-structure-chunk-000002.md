# network-algorithmics-13-15-2-the-qps-data-structure (chunk 000002)

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
