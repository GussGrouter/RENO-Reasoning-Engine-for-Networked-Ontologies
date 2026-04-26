# Network Algorithmics — 11.2.3 Status of tag switching, flow switching, and multiprotocol label switching (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 284
- Slice: from `11.2.3 Status of tag switching, flow switching, and multiprotocol label switching` up to next detected section heading

---

11.2.3 Status of tag switching, flow switching, and multiprotocol label switching
While tag switching and IP switching were originally introduced to speed up lookups, IP switching has
died away. However, tag switching in the more general form of multi-protocol-label switchings (MPLS)
(IETF MPLS Charter, 1997) has reinvented itself as a mechanism for providing flow differentiation to
provide quality of service. Just as a VCI provides a simple label to quickly distinguish a flow, a label
allows a router to easily isolate a flow for special service. In effect, MPLS uses labels to finesse the
need for packet classification (Chapter 12), a much harder problem than prefix lookups. Thus although
prefix matching is still required, MPLS is also de rigueur for a core router today.

258      Chapter 11 Prefix-match lookups



    Briefly, the required MPLS fast path forwarding is as follows. A packet with an MPLS header
is identified, a 20-bit label is extracted, and the label is looked up in a table that maps the label to
a forwarding rule. The forwarding rule specifies a next hop and also specifies the operations to be
performed on the current set of labels in the MPLS packet. These operations can include removing
labels (“popping the label stack”) or adding labels (“pushing on to the label stack”).
    Router MPLS implementations have to impose some limits on this general process to guarantee
wire speed forwarding. Possible limits include requiring that the label space be dense, supporting a
smaller number of labels than 220 (this allows a smaller amount of lookup memory while avoiding a
hash table), and limiting the number of label-stacking operations that can be performed on a single
packet.
