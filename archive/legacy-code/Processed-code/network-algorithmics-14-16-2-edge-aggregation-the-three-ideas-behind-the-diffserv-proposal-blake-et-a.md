# Network Algorithmics — 14.16.2 Edge aggregation The three ideas behind the DiffServ proposal (Blake et al., 1998) are: relaxing system requirements (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 452
- Slice: from `14.16.2 Edge aggregation The three ideas behind the DiffServ proposal (Blake et al., 1998) are: relaxing system requirements` up to next detected section heading

---

14.16.2 Edge aggregation
The three ideas behind the DiffServ proposal (Blake et al., 1998) are: relaxing system requirements
(P3) by aggregating flows into classes at the cost of a reduced ability to discriminate between flows;
shifting the mapping to classes from core routers to edge routers (P3c, shifting computation in space);
and passing the aggregate class information from the edge to core routers in the IP header (P10, passing
hints in protocol headers).
    Thus edge routers aggregate flows into classes and mark the packet class by using a standardized
value in the IP TOS field. The IP type-of-service (TOS) field was meant for some such use, but it was
never standardized; vendors such as Cisco used it within their networks to denote traffic classes, such
as voice over IP, but there was no standard definition of traffic classes. The DiffServ group generalizes
and standardizes such vendor behavior, reserving values for classes that are being standardized. One
class being discussed is so-called expedited service, in which a certain bandwidth is reserved for the
class. Another is assured service, which is given a lower drop probability for RED in output queues.
    However, the key point is that backbone routers have a much easier job in DiffServ. First, they map
flows to classes based on a small number of field values in a single TOS field. Second, the backbone
router has to manage only a small number of queues, mostly one for each class and sometimes one
for each subclass within a class; for example, assured service currently specifies three levels of service
within the class. Edge routers, though, have to map flows to classes based on ACL-like rules and
examination of possibly the entire header. This is, however, a good trade-off because edge routers
operate at slower speeds.

426       Chapter 14 Scheduling packets




FIGURE 14.24
If flows F 1 and F 2 are aggregated by the time they reach the core router CR, how can the core router realize that F 1
is oversubscribing without keeping state for each (unaggregated) flow?
