# network-algorithmics-16-13-3-approach-3-class-counters (chunk 000001)

# Network Algorithmics — 16.13.3 Approach 3: class counters (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 501
- Slice: from `16.13.3 Approach 3: class counters` up to next detected section heading

---

16.13.3 Approach 3: class counters
Our idea is that each prefix is mapped to a small class ID of 8–14 bits (256–16,384 classes) using the
forwarding table. When an input packet is matched to a prefix P , the forwarding entry for P maps the
packet to a class counter that is incremented. For up to 10,000 counters, the class counters can easily be
stored in on-chip SRAM on the forwarding ASIC, allowing the increment to occur internally in parallel
with other functions.
     For accounting, the DCU proposal (Section 16.12) already suggests that routers use policy filters to
color routes by tariff classes and to pass the colors using the routing protocol. These colors can then be
used to automatically set class IDs at each router. For the traffic matrix, a similar idea can be used to
colorize routes based on the matrix equivalence class (e.g., all prefixes arising from the same external
link or network in one class).
     How can class counters be used? For example, many ISPs have points of presence (or PoPs) in major
cities, and just calculating the aggregate PoP-to-PoP traffic matrix is very valuable (Bhattacharyya et
al., 2001). Today, this is done by aggregating the complete router-to-router matrix to find this. This
can be done directly by classes by setting each PoP into a separate class. For example, in Fig. 16.13,
R4 and R5 may be part of the same PoP, and thus E4 and E5 would be mapped to the same class.
Measurement data from 2003 (Spring et al., 2002) indicates a great reduction in the number of classes,
with 150 counters sufficing to handle the largest ISP.
     The class-counter scheme is an example of Principle P4, leveraging existing system components. It
is also an example of Principle P3, relaxing system requirements (e.g., using only a small number of
aggregate classes).

16.14 Sting as an example of passive measurement                     475
