# network-algorithmics-14-14-2-how-qfq-improves-upon-frr (chunk 000003)

422      Chapter 14 Scheduling packets

Conceivably, as time evolves, a group needs to move from one subset to another, and each such
move corresponds to an aforementioned maintenance event. As shown in Checconi et al. (2013), there
are four types of moves: (1) IB→IR; (2) IR→ER; (3) IB→EB; and (4) EB→ER. The QFQ algorithm
has two remarkable properties: (1) All four invariants concerning these four subsets can be maintained
in the event of any such move, and (2) the maintenance cost (time complexity) of each such move is true
O(1) (as it involves mostly a FFO operation). As shown in Checconi et al. (2013), both properties result
from (1) the the assumption that f (i) = s (i) + 2σi ; (2) the aforementioned GBT property; and (3) the
grouping rule i = log2 (Lk /φk ). Due to its true O(1) time complexity and excellent QoS guarantee
(that is close to that of WF2 Q), the QFQ algorithm has been integrated into the Linux kernel (QFQ
source code in Linux Kernels, 2012).
