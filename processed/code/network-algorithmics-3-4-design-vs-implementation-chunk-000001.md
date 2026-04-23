# network-algorithmics-3-4-design-vs-implementation (chunk 000001)

# Network Algorithmics — design vs implementation principles (3.4) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 90 -l 106 -layout
- Slice: from `3.4 Design versus implementation principles` up to (excluding) `3.5 Caveats`

---

3.4 Design versus implementation principles
Now that we have listed the principles used in this book, three clarifications are needed. First, con-
scious use of general principles does not eliminate creativity and effort but instead channels them more
efficiently. Second, the list of principles is necessarily incomplete and can probably be categorized in a
different way; however, it is a good place to start.
    Third, it is important to clarify the difference between system design and implementation principles.
Systems designers have articulated principles for system design. Design principles include, for exam-
ple, the use of hierarchies and aggregation for scaling (e.g., IP prefixes), adding a level of indirection for
increased flexibility (e.g., mapping from domain names to IP addresses allows DNS servers to balance
the load between instances of a server), and virtualization of resources for increased user productivity
(e.g., virtual memory).5
    A nice compilation of design principles can be found in Lampson’s article (Lampson, 1989) and
Keshav’s book (Keshav, 1997). Besides design principles, both Lampson and Keshav include a few

5 The previous chapter briefly explains these terms (IP prefixes, DNS, and virtual memory).

---

## PDF page 94
