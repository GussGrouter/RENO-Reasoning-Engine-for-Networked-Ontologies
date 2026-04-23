# network-algorithmics-12-11-equivalenced-cross-producting (chunk 000001)

# Network Algorithmics — 12.11 Equivalenced cross-producting (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 347
- Slice: from `12.11 Equivalenced cross-producting` up to next detected section heading

---

12.11 Equivalenced cross-producting
Gupta and McKeown (1999a) have invented a scheme called recursive flow classification (RFC), which
is an improved form of cross-producting that significantly compresses the cross-product table, at a
slight extra expense in search time. We prefer to call their scheme equivalenced cross-producting, for
the following reason. The scheme works by building larger cross products from smaller cross products;
the main idea is to place the smaller cross products into equivalence classes before combining them to
form larger cross products. This equivalencing of partial cross products considerably reduces memory
requirements, because several original cross-product terms map into the same equivalence class.
    Recall that in simple cross-producting when a header H arrives, the individual field matches are
immediately concatenated to form a cross product that is then looked up in a cross-product table. By
contrast, equivalenced cross-producting builds the final cross product in several pairwise combining
steps instead of in one fell swoop.
    For example, one could form the destination–source cross product and separately form the destina-
tion port–source port cross product. Then, a third step can be used to combine these two cross products
into a cross product on the first four fields, say, C  . A fourth step is then needed to combine C  with
the protocol field to form the final cross product, C. The actual combining sequence is defined by a
combining tree, which can be chosen to reduce overall memory.
    Just forming the final cross product in several pairwise steps does not reduce memory below N K .
What does reduce memory is the observation that when two partial cross products are combined, many
of these pairs are equivalent: Geometrically, they correspond to the same region of space; algebraically,
they have the same set of compatible rules.
    Thus the main trick is to give each class a class number and to form the larger cross products using
the class numbers instead of the original matches. Since the algebraic view is easier for computation, we
will describe an example of equivalencing using the first two columns of Fig. 12.10 under the algebraic
view.

12.11 Equivalenced cross-producting                     321

FIGURE 12.13
Forming the partial cross products of the first two columns in Fig. 12.10 and then assigning these cross products into
the same equivalence class if they have the same rule set (rule bitmap). Notice that 16 partial cross products form
only eight classes.

Fig. 12.13 shows the partial cross products formed by only the destination and source columns in
Fig. 12.10. For each pair (e.g., M, S), we compute the set of rules that are compatible with such a pair
of matches exactly, as in the bit vector linear search scheme. In fact, we can find the bit vector of any
pair, such as M, S, by taking the intersection of the rule bitmaps for M and S in Fig. 12.11. Thus from
Fig. 12.11, since the rule bitmap for M is 11110111 and the bitmap for S is 11110011, the intersection
bitmap for M, S is 11110011, as shown in Fig. 12.13.
    Doing this for each possible pair, we soon see that several bitmaps repeat themselves. For example,
M, T O, and M, ∗ (second and fourth entries in Fig. 12.13) have the same bitmap. Two rules that have
the same bitmap are assigned to the same equivalence class, and each class is given a class number.
Thus in Fig. 12.13, the classes are numbered starting with 1; the table-building algorithm increments

322      Chapter 12 Packet classification

FIGURE 12.14
The combining tree used in the example.
