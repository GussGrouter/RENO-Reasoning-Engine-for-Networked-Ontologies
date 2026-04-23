# network-algorithmics-12-9-bit-vector-linear-search (chunk 000001)

# Network Algorithmics — 12.9 Bit vector linear search (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 343
- Slice: from `12.9 Bit vector linear search` up to next detected section heading

---

12.9 Bit vector linear search
Consider doing a match in one of the individual columns in Fig. 12.10, say, the destination address
field, and finding a bit string S as the longest match. Clearly, this lookup result eliminates any rules
that do not match S in this field. Then the search algorithm can do a linear search in the set of all
remaining rules that match S. The logical extension is to perform individual matches in each field; each
field match will prune away a number of rules, leaving a remaining set. The search algorithm needs to
search only the intersection of the remaining sets obtained by each field lookup.
    This would clearly be a good heuristic for optimizing the average case if the remaining sets are
typically small. However, one can guarantee performance even in the worst case (to some extent) by
representing the remaining sets as bitmaps and by using wide memories to retrieve a large number of
set members in a single memory access (P4a, exploit locality).
    In more detail, as in Section 12.8, divide-and-conquer is used to slice the database, as in Fig. 12.10.
However, in addition with each possible value M of field i, the algorithm stores the set of rules S(M)
that match M in field i as a bit vector. This is easy to do when building the sliced table. The algorithm
that builds the data structure scans through the rules linearly to obtain the rules that match M using the
match rule (e.g., exact, prefix, or range) specified for the field.
    For example, Fig. 12.11 shows the sliced database of Fig. 12.10 together with bit vectors for each
sliced field value. The bit vector has 8 bits, one corresponding to each of the eight possible rules in
Fig. 12.2. Bit j is set for value M in field i if value M matches Rule j in field i.
    Consider the destination prefix field and the first value M in Fig. 12.11. If we compare it to Fig. 12.2,
we see that the first four rules specify M in this field. The fifth rule specifies T I (which does not
match M), and the sixth and eighth rules specify a wildcard (which matches M). Finally, the seventh
rule specifies the prefix N et (which matches M, because N et is assumed to be the prefix of the company
network in which M is the mail gateway). Thus the bitmap for M is 11110111, where the only bit not
set is the fifth bit. This is because the fifth rule has T I , which does not match M.

12.9 Bit vector linear search                317

FIGURE 12.11
The sliced database of Fig. 12.10 together with bit vectors for every possible sliced value. The bit vector has 8 bits,
one corresponding to each of the eight possible rules in Fig. 12.2. Bit j is set for value M in field i if value M
matches Rule j in field i.
