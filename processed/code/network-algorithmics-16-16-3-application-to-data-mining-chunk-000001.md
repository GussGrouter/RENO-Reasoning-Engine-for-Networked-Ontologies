# network-algorithmics-16-16-3-application-to-data-mining (chunk 000001)

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
