# network-algorithmics-12-4-5-passing-labels-recall-from-chapter-11-that-one-way-to-finesse-lookups-is (chunk 000001)

# Network Algorithmics — 12.4.5 Passing labels Recall from Chapter 11 that one way to finesse lookups is to pass a label from a previous-hop router (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 330
- Slice: from `12.4.5 Passing labels Recall from Chapter 11 that one way to finesse lookups is to pass a label from a previous-hop router` up to next detected section heading

---

12.4.5 Passing labels
Recall from Chapter 11 that one way to finesse lookups is to pass a label from a previous-hop router
to a next-hop router. One of the most prominent examples of such a technology is multiprotocol la-
bel switching (MPLS) (IETF MPLS Charter, 1997). While IP lookups have been able to keep pace
with wire speeds, the difficulties of algorithmic approaches to packet classification have ensured an
important niche for MPLS. Refer to Chapter 11 for a description of tag switching and MPLS.
    Today MPLS is useful mostly for traffic engineering. For example, if Web traffic between two sites
A and B is to be routed along a special path, a label-switched path is set up between the two sites.
Before traffic leaves site A, a router does packet classification and maps the Web traffic into an MPLS
header. Core routers examine only the label in the header until the traffic reaches B, at which point the
MPLS header is removed.

304      Chapter 12 Packet classification

The gain from the MPLS header is that the intermediate routers do not have to repeat the packet-
classification effort expended at the edge router; simple table lookup suffices. The DiffServ (Blake et
al., 1998) proposal for QoS is actually similar in this sense. Classification is done at the edges to mark
packets that deserve special quality of service. The only difference is that the classification information
is used to mark the Type of Service (TOS) bits in the IP header, as opposed to an MPLS label. Both are
examples of Principle P10, passing hints in protocol headers.
     Despite MPLS and DiffServ, core routers still do classification at the very highest speeds. This is
largely motivated by security concerns, for which it may be infeasible to rely on label switching. For
example, Singh et al. (2004a) describe a number of core router classifiers, the largest of which contained
2000 rules.
