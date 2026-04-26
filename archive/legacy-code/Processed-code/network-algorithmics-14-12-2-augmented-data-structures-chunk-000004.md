# network-algorithmics-14-12-2-augmented-data-structures (chunk 000004)

14.12 The data structure and algorithm for efficient GPS clock tracking                          415

searches. For example, in the case of the insertion of a new leaf node with a certain key value, which
will be described in the next subsection, such range information guides the search down the tree to the
appropriate leaf position to insert. Second, the width of such a range, or more precisely the difference
between the two key values, is used for calculating an important quantity called area that is an additional
(w.r.t. the base data structure) data field of the augmented data structure. Since only leaf nodes contain
keys, the algorithmic steps for maintaining the balance of the tree, such as various rotation operations
(e.g., RR, RL, LR, LL rotations in an AVL tree), need to be suitably modified as in say B+ trees.
