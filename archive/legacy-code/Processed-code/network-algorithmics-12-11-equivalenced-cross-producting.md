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


the class number whenever it encounters a new bitmap. Thus, there are only eight distinct class numbers,
compared to 16 possible cross products, because there are only eight distinct bitmaps.
    Now assume we combine the two port columns to form six classes from 10 possible cross products.
When we combine the port pairs with the destination–source pairs, we combine all possible combi-
nations of the destination–source and port pair class numbers and not the original field matches. Thus
after combining all four columns, we get 6 ∗ 8 = 48 cross products. Note that in Fig. 12.10, naive cross-
producting will form 4 ∗ 4 ∗ 5 ∗ 2 = 160 cross products from the first four columns. Thus we have saved
a factor of nearly 3 in memory.
    Of course, we do not stop here. After combining the destination–source and port pair class numbers,
we equivalence them again using the same technique. When combining class number C with class
number C  , the bitmap for C, C  is the intersection of the bitmaps for C and C  . Once again, pairs with
identical bitmaps are equivalenced into groups. After this is done, the final cross product is formed by
combining the classes corresponding to the first four columns with the matches in the fifth column.
    Our example combined fields 1 and 2, then fields 3 and 4, and then the first four and finally combined
in the fifth (Fig. 12.14). Clearly, other pairings are possible, as defined by a binary tree with the fields
as nodes and edges representing pairwise combining steps. One could choose the optimal combining
tree to reduce memory.
    The search process is similar to cross-producting, except the cross products are calculated pairwise
(just as they are built) using the same tree. Each pairwise combining uses the two class numbers as
input into a table that outputs the class number of the combination. Finally, the class number of the root
of the tree is looked up in a table to yield the best-matching rule. Since each class has the same set of
matching rules, it is easy to precompute the lowest-cost matching rule for the final classes. Note that
the search process does not need to access the rule bitmaps, as is needed for the bit vector linear search
scheme. The bitmaps are used only to build the structure.
    Clearly, each pairwise combining step can take O(N 2 ) memory because there can be N distinct
field values in each field. However, the total memory falls very short of the N K worst-case memory for
real rule databases. To see why this might be the case, we return to the geometric view.
    Using a survey of 8000 rule databases, Gupta and McKeown (1999a) observe that all databases
studied have only O(N ) classification regions, instead of the N K worst-case number of classification

                                                             12.12 Decision tree approaches                  323



regions. It is not hard to see that when the number of classification regions is N K , then the number of
cross products in the equivalenced scheme and in the naive scheme is also N K .
    But when the number of classification regions is linear, equivalenced cross-producting can do better.
However, it is possible to construct counterexamples where the number of classification regions is lin-
ear, but equivalenced cross-producting takes exponential memory. Despite such potentially pathological
cases, the performance of RFC can be summarized as follows.
Assumption: There is a series of subspaces of the complete rule space (as embodied by nodes in the
      combining tree) that all have a linear number of classification regions. Note that this is stronger
      than O4 and even O5. For example, if we combine two fields i and j first, we require that this
      intermediate two-dimensional subspace have a linear number of regions.
Performance: The memory required is O(N 2 ) ∗ T , where T is the number of nodes in the combining
      tree. The sequential performance (in terms of time) is O(T ) memory accesses, but the time
      required in a parallel implementation can be O(1) because the tree can be pipelined. Note that
      the O(N 2 ) memory is still very large in practice and would preclude the use of SRAM-based
      solutions.
