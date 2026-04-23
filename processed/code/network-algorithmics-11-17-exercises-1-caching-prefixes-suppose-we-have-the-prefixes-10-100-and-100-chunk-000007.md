# network-algorithmics-11-17-exercises-1-caching-prefixes-suppose-we-have-the-prefixes-10-100-and-100 (chunk 000007)

by three very different examples of algorithms based on divide-and-conquer: simple and aggregated
bit vector linear search (Section 12.9), cross-producting (Section 12.10), and RFC, or equivalenced
cross-producting (Section 12.11). Section 12.12 presents the most promising of the current algorithmic
approaches, an approach based on decision trees.
    This chapter will continue to exhibit the set of principles introduced in Chapter 3, as summarized
in Table 12.1. The chapter will also illustrate three general problem-solving strategies: solving simpler
problems first before solving a complex problem, collecting different viewpoints, and exploiting the
structure of input data sets.

Quick reference guide
  The most important lookup algorithms for an implementor today are as follows. If memory is not an issue, the fastest
  scheme is one called recursive flow classification (RFC), described in Section 12.11. If memory is an issue, a simple
  scheme that works well for classifiers up to around 5000 rules is the Lucent bit vector scheme (Section 12.9). For larger
  classifiers, the best trade-off between speed and memory is provided by decision tree schemes, such as HyperCuts and
  EffiCuts (Section 12.12). For software settings which require fast updates as in Hypervisor switches, then a good solution
  is Tuple Space Search and the improvements implemented in Open Vswitch (Pfaff et al., 2015). Unfortunately, all these
  algorithms are based on heuristics and cannot guarantee performance on all databases. If guaranteed performance is
  required for more than two field classifiers, there is no alternative but to consider hardware schemes such as ternary
  CAMs.
