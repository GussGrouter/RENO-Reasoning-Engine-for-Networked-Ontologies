# Network Algorithmics — 11.2 Finessing lookups The first instinct for a systems person is not to solve complex problems (like longest matching prefix) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 281
- Slice: from `11.2 Finessing lookups The first instinct for a systems person is not to solve complex problems (like longest matching prefix)` up to next detected section heading

---

11.2 Finessing lookups
The first instinct for a systems person is not to solve complex problems (like longest matching prefix)
but to eliminate the problem.
    Observe that in virtual circuit networks such as ATM, when a source wishes to send data to a
destination, a call, analogous to a telephone call, is set up. The call number virtual circuit index [VCI]
at each router is a moderate-size integer that is easy to look up. However, this comes at the cost of a
round-trip delay for call setup before data can be sent.
    In terms of our principles, ATM has a previous hop switch pass an index (P10, pass hints in protocol
headers) into a next hop switch. The index is precomputed (P2a) just before data is sent by the previ-
ous hop switch (P3c, shifting computation in space). The same abstract idea can be used in datagram

                                                                          11.2 Finessing lookups               255




FIGURE 11.1
Replacing the need for a destination lookup in a datagram router by having each router pass an index into the next
router’s forwarding table.


networks such as the Internet to finesse the need for prefix lookups. We now describe two instantiations
of this abstract idea: tag switching (Section 11.2.1) and flow switching (Section 11.2.2).
