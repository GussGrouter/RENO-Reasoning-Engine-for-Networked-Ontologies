# network-algorithmics-12-11-equivalenced-cross-producting (chunk 000002)

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
