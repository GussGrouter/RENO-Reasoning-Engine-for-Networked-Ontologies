# network-algorithmics-16-16-3-application-to-data-mining (chunk 000002)

Now, we describe a much more efficient solution, based on the algorithm just described for esti-
          
mating |A     B|, that can find all associations in two weeks! To do so, we simply convert the counting
                                                                     
problem for a pair of columns to the problem of estimating |A            B| as follows. For each column of
cells in Table 16.2, except the 0th that contains customer-transactions identifiers, we perform the fol-
lowing transformation. If the value of the cell on row i (the ith customer transaction) is 1, we rewrite
the value of this cell to αi , the corresponding customer-transaction identifier; if the value of this cell is
0, we rewrite it to “empty.” The resulting table with the cell values rewritten is shown in Table 16.3.
    We view each column, except the 0th, in Table 16.3 as a set of customer-transactions identifiers. For
example, the “milk” column corresponds to the set of customer transactions, which we denote as A, that
contain the purchase of “milk.” We have A = {α1 , α3 , α4 , · · · } as shown in Table 16.3. Also, as shown
in Table 16.3, the “cereal” column corresponds to the set {α1 , α3 , ·  · · }, which wedenote as B. Then,
our counting problem is equivalent to the problem of estimating |A B| since A B is precisely the
set of customer transactions that contain both milk and cereal.
    This conversion naturally suggests the following data-streaming algorithm. The first step of this
algorithm is to take a one-pass scan over every column except the 0th. For each column, which cor-
responds to a set of customer transaction identifiers as just explained, the algorithm processes the set
into an array of 25 numbers using the min-hash algorithm described above. Suppose processing each
column to obtain a min-hash value (out of a total of 25 min-hash array elements) takes 1 second (1
nanosecond for processing each cell) as just explained, the preprocessing takes 1.25 million seconds,
or roughly two weeks, for the 50,000 columns.    The second step of the algorithm is, for every pair of
columns (sets) say A and B, to estimate |A B| using Formulae (16.3) and (16.4). Suppose process-
ing each such pair takes 50 nanoseconds     (2 nanoseconds   for each pair of array elements), the total
processing time of this step is only 50000    ∗ 50 ∗ 10 −9 ≈ 62.5 seconds!
                                          2
    Note that, unlike in network data streaming applications where the constraint of taking only a one-
pass scan over the data stream is imposed by the reality of networks, in this association rule mining
scenario, this constraint is self-imposed. Since all data items are in the database, the algorithm in theory
can scan the database as many times as it wishes. However, doing so comes at a high computational
cost (of close to 40 years) that this algorithm rightly avoids.

Table 16.2 The Walmart customer-transaction table be-
                      fore transformation.
                      Transaction ID     Milk     Cereal   Banana     Apple       ···
                           α1             1         1        0          1         ···
                           α2             0         0        1          1         ···
                           α3             1         1        1          1         ···
                           α4             1         0        1          1         ···
                            ..            ..        ..        ..        ..        .. .. ..
                             .             .         .         .         .         ...
