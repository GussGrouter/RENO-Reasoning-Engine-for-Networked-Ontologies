# network-algorithmics-12-11-equivalenced-cross-producting (chunk 000003)

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
