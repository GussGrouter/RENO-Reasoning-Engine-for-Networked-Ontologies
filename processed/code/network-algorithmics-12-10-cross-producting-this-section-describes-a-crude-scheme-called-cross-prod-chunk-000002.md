# network-algorithmics-12-10-cross-producting-this-section-describes-a-crude-scheme-called-cross-prod (chunk 000002)

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
