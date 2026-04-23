# network-algorithmics-12-12-decision-tree-approaches (chunk 000004)

326      Chapter 12 Packet classification

with different heuristics to achieve a good trade-off between number of trees (lookup time) and storage
(redundancy).
     Using a publicly available benchmark of synthetic and other classifiers called ClassBench (Taylor
and Turner, 2007), the authors show that for comparable performance EffiCuts needs 57 times less
memory than HyperCuts and 4-8 times less power than a TCAM. The last experiment is notable because
unlike earlier papers that informally claimed that algorithmic schemes used less power than TCAMs,
this is one of the few papers to quantify the comparison using a hardware model called CACTI (Wilton
and Jouppi, 1996) to model CAM and RAM. However, the benchmarks used (Taylor and Turner, 2007)
are mostly synthetic ones; thus a more modern benchmark of real classifiers would be ideal to compare
all these schemes.
     HiCuts, HyperCuts, and Efficuts all use manually created heuristics to build decision trees – in other
words, to decide how to partition rules among multiple trees and how to perform cuts at each node in
a tree. A later paper, NeuroCuts (Liang et al., 2019), further advances the state-of-the-art in decision
trees by using Reinforcement Learning. First, note that using a neural network for classification, is
problematic because a neural classification network cannot guarantee correct results (the answers are
correct only with high probability). Further, neural networks are resource intensive, making it hard to
guarantee results in time to forward a packet. Instead, NeuroCuts uses deep Reinforcement Learning
to build efficient decision tree, pushing the cost of the neural network to the time when new rules are
added to the classifier.
     Thus, while previous approaches attempt to heuristically meet performance objective (e.g., reduce
storage), Reinforcement Learning explicitly maximizes the given performance objective. Fortunately,
the learning time to evaluate a large number of models, which is one of main drawbacks of RL, is
not very high for packet classification. Using synthetic workloads generated using ClassBench, the
authors (Liang et al., 2019) show that NeuroCuts outperforms existing hand-tuned decisions in both
classification time and memory footprint. More specifically, NeuroCuts improves median classification
time by 18%, and reduces both time and memory usage by up to a factor of 3.
     In conclusion, the decision tree approach described by (Woo, 2000), (Gupta and McKeown, 1999b),
(Singh et al., 2004a), (Vamanan et al., 2010) and (Liang et al., 2019) is best viewed as a framework that
encompasses a number of potential algorithms. However, experimental evidence (Singh et al., 2004a;
Vamanan et al., 2010) shows that this approach works well in practice. The performance of this scheme
can be summarized as follows.
Assumption: The scheme assumes there is a sufficient number of distinct fields to make reasonable
      cuts without much storage replication. This rather general observation needs to be sharpened.
Performance: The memory required can be kept to roughly linear in the number of rules using var-
      ious heuristics. The tree can be of relatively small height if it is reasonably balanced. Search
      can easily be pipelined to allow O(1) lookup times. Finally, the updates are likely to be slow if
      sophisticated heuristics are used to build the decision tree.
