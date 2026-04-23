# network-algorithmics-14-14-2-how-qfq-improves-upon-frr (chunk 000002)

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
