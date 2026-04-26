# network-algorithmics-12-7-extending-two-dimensional-schemes (chunk 000002)

Unfortunately, it turns out that there is a delicacy about extending the grid of tries. In the grid of
tries, whenever one rule, R, is at least as specific in all fields as a second rule, R  , rule R  precomputes
its matching directive to be that of R if R is the lower cost of the two rules. This allows the traversal
through the grid of tries to safely skip rule R when encountering rule R  . While this works correctly
with two-field rules, it requires some further modifications to handle the general case.
    One solution, equivalent to precomputing rule costs, is to precompute the list for R  to include all
the list elements for R. Unfortunately, this approach can increase storage because each rule is no longer
represented exactly once. A more sophisticated solution, called the extended grid of tries (EGT) and
described in Singh et al. (2004b), is based on extra traversals beyond the standard grid of tries.
    The performance of EGT can be described as follows.
Assumption: The extension of two-dimensional schemes depends critically on observation O5.
Performance: The scheme takes at least one grid-of-tries traversal plus the time to linearly search c
      rules, where c is the constant embodied in observation O5. Assuming linear storage, the search
      performance can increase (Singh et al., 2004b) by an additive factor representing the time to
      search for less specific rules. The addition of a new rule R requires only rebuilding of the indi-
      vidual two-dimensional structure of which R is a part. Thus rule update should be fairly fast.
