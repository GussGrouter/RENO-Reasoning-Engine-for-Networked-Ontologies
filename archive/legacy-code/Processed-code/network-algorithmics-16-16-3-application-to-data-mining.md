# Network Algorithmics — 16.16.3 Application to data mining (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 506
- Slice: from `16.16.3 Application to data mining` up to next detected section heading

---

16.16.3 Application to data mining
In this section, we first state the problem of association
                                                            rule mining and then explain how to reduce it
to the problem just described of estimating |A B|. Association rule mining (Agrawal et al., 1993) is
arguably the most classical and fundamental problem in data mining (Kamber and Han, 2000). It can be
best described using the following application. Let us organize the transactions of customers shopping
at Walmart as a two-dimensional table shown in Table 16.2. Each column except the 0th corresponds
to a type of merchandise (say milk), and each row corresponds to a transaction (made by a customer at
the time of checkout). The cell at the intersection of the ith row and j th column takes value 1 if the ith
transaction has the j th type of merchandise in it and takes value 0 otherwise. The 0th column contains
the customer-transaction identifiers that are distinct for each customer transaction.
     Let us say Walmart is interested in finding all pairs of merchandise that are more frequently bought
together by customers (say milk and cereal) than if the purchases of these two merchandises are sta-
tistically uncorrelated. Such a positive statistical correlation is called an association in the data-mining
literature. For example, if roughly 1/2 of the customer transactions contain milk and roughly 1/3 of
customer transactions contain cereal, then an association between milk and cereal is established if much
more than 1/2 ∗ 1/3 = 1/6 of the customer transactions contain both milk and cereal.
     Given any pair of columns (merchandises), to check if there is an association between them is a
straightforward counting problem: to count the number of rows (customer transactions) in which the
two corresponding cells both have value 1 (contain both merchandises). This suggests a straightforward
but naive algorithm: Do this counting for every pair of columns. However, this naive algorithm is
extremely time-consuming if the numbers of rows and columns in the table are both large. For example,
suppose Walmart (table) has 50,000 different merchandises (columns) and 1 billion transactions (rows).
Then, to do this counting for a pair of columns takes roughly  a second on a gigahertz processor. To do
this counting for every two columns takes roughly 50000     2    ≈ 1.25 billion seconds, which is roughly
39.64 years. Such a slow solution is not going to help with Walmart’s business.

480      Chapter 16 Measuring network traffic



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
