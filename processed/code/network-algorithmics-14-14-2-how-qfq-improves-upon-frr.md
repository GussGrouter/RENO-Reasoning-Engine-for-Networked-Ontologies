# Network Algorithmics — 14.14.2 How QFQ improves upon FRR (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 447
- Slice: from `14.14.2 How QFQ improves upon FRR` up to next detected section heading

---

14.14.2 How QFQ improves upon FRR
QFQ improves upon FRR by reducing its technically O(1) (actually O(G log G)) time complexity to
true O(1), or in other words getting rid of its dependence on G, through three modifications. The first
modification is that it makes use of an approximate virtual time function V (t) proposed in what was
called WF2 Q+ (Bennett and Zhang, 1996a). WF2 Q+ is pretty much the same algorithm as WF2 Q except
that its V (t) only approximately tracks the GPS clock (whereas that of WF2 Q does so exactly). This
approximation, combined with the third modification to be described shortly, allows the WF2 Q+ clock
to be tracked with true O(1) (independent of both n and G) time complexity. The tradeoff (P3b) is that
its fairness guarantee, as measured by T-WFI, is slightly worse than that of WF2 Q.
     The second modification is that it assigns a flow Fk to a group based not only on its weight φk ,
but also on its maximum packet size Lk . More precisely, it assigns a flow Fk to flow group i, where
i = log2 (Lk /φk ) (with base C = 2). It was shown in Checconi et al. (2013) that the use of WF2 Q+
clock with this modification leads to the following nice property of QFQ that is key to its true O(1)
time complexity: The difference between the WF2 Q+ virtual finish times of the HOL packets of any
two flows in the system is bounded by a small universal constant δ, no matter what the traffic arrival
pattern is. A weaker version of this property is called the Globally Bounded Timestamp (GBT) property
in Bennett and Zhang (1996a).
     The third modification is that for the purpose of sorting (the WF2 Q+ virtual finish times of HOL
packets), in each group i, the WF2 Q+ virtual finish times are rounded to the multiples of a certain
unit value σi . For each group index i, the value of σi is defined to be 2i (bits). With this σi -integral
rounding, the rounded WF2 Q+ virtual finish time of any HOL packet can only take a small number
of possible values thanks to the GBT property described above. Hence the sorting of rounded WF2 Q+
virtual finish times (to decide which flow shall have its HOL packet transmitted) within any group
can be done in O(1) time using bucket sorting (P14). In the rest of this section, we drop the qualifier
“rounded WF2 Q+” with the understanding that all virtual finish and start times referred to below has
this qualifier.
     For any flow Fk that belongs to a group i ∗ , its maximum normalized packet length Lk /φk is less than
2σi ∗ as a result of how we assign flows to groups as described above. This property in turn guarantees
that the virtual finish time of any packet is no later than its virtual start time by more than 2σi . For
each group i, define s (i) to be the earliest virtual start time among all flows (their HOL packets) in

                                                          14.14 Quick fair queueing (QFQ)                421



group i. This s (i) is called the virtual start time of group i, and the corresponding packet is called
the HOL packet of group i. Let f (i) be the virtual finish time of this HOL packet. To achieve O(1)
time complexity, QFQ makes the following simplifying assumption: f (i) is assumed to be s (i) + 2σi .
Arguably, this assumption is a bit unfair for the HOL packet of a group i if the length of this packet is
much smaller than the maximum packet length of the flow this packet belongs to. However, the overall
degradation of fairness due to this assumption is typically small (P3b), since within each group, packets
are still served in the order of their actual virtual finish times.
    The QFQ scheduling policy can now be precisely stated as follows: Whenever the link becomes
idle, the QFQ policy picks, among the eligible groups (those that should have started service under the
WF2 Q+ clock), the group that has the earliest virtual finish time to service next. Intuitively, as in the
implementation of the WF2 Q policy, a scheduling algorithm that implements the QFQ policy needs to
do both the sorting (of virtual finish times) and the eligibility checks.
    The QFQ algorithm manages to do both checks in O(1) time. The key idea is to partition (at any
time) the (set of) G groups into four subsets according to whether a group is ready (R) to receive ser-
vice or blocked (B), and whether a group is eligible (E) or ineligible (I), with invariants maintained for
these four subsets (at any time). Since G ≤ 64, we can represent these G groups by G ≤ 64 different
locations; hence each subset (of these G groups) can be encoded as a 64-bit-long bitmap (P14), with
the value of each bit indicating whether or not the corresponding group is in the subset. With these
invariants maintained at all times, the QFQ algorithm boils down to performing the following basic op-
eration, a few times, per scheduling or maintenance event: identify the group with the smallest index in
one of these four subsets. But this is equivalent to “finding first one” (FFO, mentioned in Section 13.16)
in the 64-bit integer (bitmap) that encodes the subset. Since most modern CPUs have a built-in FFO
instruction (P4c) that completes in one clock cycle, the QFQ algorithm can process each scheduling or
maintenance event in a few clock cycles. For a scheduling event, after the QFQ algorithm identifies the
group with the smallest index (using FFO), it identifies the flow within this group that has the smallest
virtual finish time again in true O(1) time using bucket sorting.
    The first subset is the ER (eligible and ready) subset. Whenever the QFQ algorithm picks the next
group to service it picks from this subset. Two invariants are maintained for ER at any time t. First, it
contains the “right” group, say group i ∗ , to pick (at time t) in the sense group i ∗ both is eligible and has
the earliest virtual finish time among all eligible groups. Second, the virtual finish times of all groups in
ER are sorted by their group indices in the following sense: For any i1 , i2 ∈ ER and i1 < i2 , the virtual
finish time of group i1 is no later than that of group i2 . With these two invariants, to find the “right”
group, the QFQ algorithm needs only to perform FFO on the 64-bit-long ER bitmap.
    However, without additional “magic”, apparently something is wrong with the second invariant:
There can certainly be an eligible group whose index is smaller than i ∗ , and in this case FFO would not
locate the “right” group i ∗ . The ingenious idea of QFQ is to block all such groups, and push them to
the second subset, named EB (eligible and blocked). Compared to the ER subset, the EB subset does
not contain the “right” group i ∗ , satisfies the second invariant above as proven in Checconi et al. (2013)
(in Theorem 5). The other two subsets are IB (ineligible     and blocked) and IR (ineligible and ready). It
was shown in Checconi et al. (2013) that groups in IB IR satisfy two invariants: (1) The virtual start
times of these groups are sorted by their group indices; and (2) The virtual finish times of these groups
are sorted by their group indices. Note (1) and (2) can both be true simultaneously since we assume
f (i) = s (i) + 2σi as explained above.

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
