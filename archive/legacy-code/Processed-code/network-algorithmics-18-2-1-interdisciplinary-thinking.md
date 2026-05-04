# Network Algorithmics — 18.2.1 Interdisciplinary thinking (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 546
- Slice: from `18.2.1 Interdisciplinary thinking` up to next detected section heading

---

18.2.1 Interdisciplinary thinking
Network algorithmics represents the intersection of several disciplines within computer science that
are often taught separately. Endnode algorithmics is a combination of networking, operating systems,
computer architecture, and algorithms. Router algorithmics is a combination of networking, hardware
design, and algorithms. Fig. 18.3 provides examples of uses of these disciplines that are studied in the
book.
    For example, in Fig. 18.3 techniques such as header prediction (Chapter 9) require a deep network-
ing knowledge of TCP to optimize the expected case, while internal link striping (Chapter 15) requires
knowing how to correctly design a striping protocol. On the other hand, application device channels
(Chapter 6) require a careful understanding of the protection issues in operating systems.
    Similarly, locality-driven receiver processing requires understanding the architectural function and
limitations of the instruction cache. Finally, in router algorithmics it is crucial to understand hardware




FIGURE 18.3
Examples of disciplines used in this book along with sample applications.

520      Chapter 18 Conclusions



design. Arbiters like iSLIP and PIM were designed to allow scheduling decisions in a minimum packet
arrival time.
    Later in this chapter we argue that other disciplines, such as statistics and learning theory, will also
be useful for network algorithmics.
