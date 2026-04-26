# network-algorithmics-14-6-a-quick-detour-into-reservation-protocols (chunk 000001)

# Network Algorithmics — 14.6 A quick detour into reservation protocols (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 419
- Slice: from `14.6 A quick detour into reservation protocols` up to next detected section heading

---

14.6 A quick detour into reservation protocols
This chapter focuses on packet-scheduling mechanisms. However, before we go deeper into scheduling
queues, it may help to see the big picture. Thus we briefly discuss reservation protocols that actually
set up the parameters that control scheduling. While we do so to make this chapter self-contained, the
reader should refer to the original sources (e.g., Boyle, 1997) for a more detailed description.
    First, note that reservations are crucial for any form of absolute performance guarantee for flows
passing through a router. Consider an ISP router with a 100-Mbs output link. If the ISP wishes to
provide some customer flows with a 10-Mbps-bandwidth guarantee, it clearly cannot provide this guar-
antee to more than 10 flows. It follows that there must be some mechanism to request the router for
bandwidth guarantees for a given flow. Clearly, the router must do admission control and be prepared
to reject further requests if further requests are beyond its capacity.
    Thus if we define QoS as the provision of performance guarantees for flows, it can be said that QoS
requires reservation mechanisms and admission control (to limit the set of flows we provide QoS to)
together with scheduling (to enforce performance guarantees for the selected flows). Quality of service

14.7 Providing bandwidth guarantees               393

is a sufficiently vague term, and the implied performance guarantees can refer to the bandwidth, delay,
or even a variation in delay.
    One way to make reservations is for a manager to make reservations for each router in the path
of a flow. However, this is tedious and would require the work to be done each time the route of the
flow changes and whenever the application that requires reservations is stopped and restarted. One
standard that has been proposed is the Resource Reservation Protocol (RSVP) (Boyle, 1997), which
allows applications to make reservations.
    This protocol works in the context of a multicast tree between a sender and a set of receivers (and
works for one receiver). The idea is that the sender sends a periodic PATH message along the tree
that allows routers and receivers to know in which direction the sender is. Then, each receiver that
wants a reservation of some resource (say, bandwidth) sends a Resource Reservation Protocol (RSV)
message up to the next router in the path. Each router accepts the RSV message if the reservation is
feasible, merges the RSV messages of all receivers, and then sends it to its parent router. This continues
until all reservations have been set up or failure notifications are sent back. Reservations are timed out
periodically, so RSV messages must be sent periodically if a receiver wishes to maintain its reservation.
    While RSVP appears simple from this description, it has a number of tricky issues. First, it can allow
reservations across multiple senders and can include multiple modes of sharing. For shared reservations,
it improves scalability by allowing reservations to be merged; for example, for a set of receivers that
want differing bandwidths on the same link for the same conference, we can make a single reservation
for the maximum of all requests. Finally, we have to deal with the possibility that the requests of a
subset of receivers are too large but that the remaining subset can be accommodated. This is handled
by creating blockade state in the routers. The resulting specification is quite complex.
