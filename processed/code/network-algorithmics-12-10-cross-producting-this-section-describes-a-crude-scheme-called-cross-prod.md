# Network Algorithmics — 12.10 Cross-producting This section describes a crude scheme called cross-producting (Srinivasan et al., 1998). In the next (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 345
- Slice: from `12.10 Cross-producting This section describes a crude scheme called cross-producting (Srinivasan et al., 1998). In the next` up to next detected section heading

---

12.10 Cross-producting
This section describes a crude scheme called cross-producting (Srinivasan et al., 1998). In the next
section, we describe a crucial refinement we call equivalenced cross-producting (but called RFC by
the authors (Gupta and McKeown, 1999a)) that makes cross-producting more feasible. The top of each
column in Fig. 12.10 indicates the number of elements in the column. Consider a 5-tuple, formed by
taking one value from each column. Call this a cross product. Altogether, there are 4 ∗ 4 ∗ 5 ∗ 2 ∗ 3 =
480 possible cross products. Some sample cross products are shown in Fig. 12.12. Considering the
destination field to be most significant and the flags field to be least significant, and pretending that
values increase down a column, cross products can be ordered from the smallest to the largest, as in any
number system.
    A key insight into the utility of cross products is as follows.

                                                                          12.10 Cross-producting          319




FIGURE 12.12
A sample of the cross products obtained by cross-producting the individual prefix tables of Fig. 12.10.


Given a packet header H , if the longest-matching-prefix operation for each field H [i] is con-
catenated to form a cross product C, then the least-cost rule matching H is identical to the
least-cost rule matching C.
    Suppose this were not true. Since each field in C is a prefix of the corresponding field in H , every
rule that matches C also matches H . Thus the only case in which H has a different matching rule is if
there is some rule R that matches H but not C. This implies that there is some field i such that R[i] is
a prefix of H [i] but not of C[i], where C[i] is the contribution of field i to cross product C. But since
C[i] is a prefix of H [i], this can happen only if R[i] is longer than C[i]. But that contradicts the fact
that C[i] is the longest-matching prefix in column/field i.
    Thus, the basic cross-producting algorithm (Srinivasan et al., 1998) builds a table of all possible
cross products and precomputes the least-cost rule matching each cross product. This is shown in
Fig. 12.12. Then, given a packet header, the search algorithm can determine the least-cost matching
rule for the packet by performing K longest-matching-prefix operations, together with a single hash
lookup of the cross-product table. In hardware, each of the K prefix lookups can be done in parallel.
    Using our example, consider matching a packet with header (M, S, UDP, 53, 57) in the database
of Fig. 12.2. The cross product obtained by performing best-matching prefixes on individual fields is
(M, S, UDP, 53, default). It is easy to check that the precomputed rule for this cross product is Rule
2—although Rules 3 and 8 also match the cross product, Rule 2 has the least cost.
    The naive cross-producting algorithm suffers from a memory explosion problem: In the worst case,
the cross-product table can have N K entries, where N is the number of rules and K is the number of
fields. Thus, even for moderate values, say, N = 100 and K = 5, the table size can reach 1010 , which is
prohibitively large.

320      Chapter 12 Packet classification



    One idea to reduce memory is to build the cross products on demand (P2b, lazy evaluation)
(Srinivasan et al., 1998): Instead of building the complete cross-product table at the start, the algo-
rithm incrementally adds entries to the table. The prefix tables for each field are built as before, but the
cross-product table is initially empty. When a packet header H arrives, the search algorithm performs
longest-matching prefixes on the individual fields to compute a cross-product term C.
    If the cross-product table has an entry for C, then of course the associated rule is returned. However,
if there is no entry for C in the cross-product table, the search algorithm finds the best-matching rule
for C (possibly using a linear search of the database) and inserts that entry into the cross-product table.
Of course, any subsequent packets with cross product C will yield fast lookups.
    On-demand cross-producting can improve both the building time of the data structure and its storage
cost. In fact, the algorithm can treat the cross-product table as a cache and remove all cross products
that have not been used recently. Caching based on cross products can be more effective than full header
caching because a single cross product can represent multiple headers (see Exercises). However, a more
radical improvement of cross-producting comes from the next idea, which essentially aggregates cross
products into a much smaller number of equivalence classes.
