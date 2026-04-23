# network-algorithmics-14-12-2-augmented-data-structures (chunk 000008)

manner: The algorithm shall not only map t to V (t) “upon request” but also output the value of the
area (III) + (IV) in Fig. 14.23. Hence, our “induction hypothesis” is that this logic held true at time t0 ,
i.e., the algorithm output both v0 = V (t0 ) and the value of area (III) at time t0 . Based on this “induction
hypothesis,” we now show how the revised algorithm delivers the extended logic (of outputting both
V (t) and (III) + (IV) at time t).
     Recall that we can query the shape data structure that encodes this staircase for the line V (t) such
that the area under the staircase between V (tc ) and V (t) is equal to (I) + (II). Since the staircase is
solid to the right of the V (t0 ) line (because there was no new flow arrival between t0 and t), we have
(I I ) = t − t0 . However, the area of (I) is not necessarily equal to t0 − tc because the area under the
staircase between tc and t0 is not necessarily solid. Instead, the area of (I) can be calculated as the
area of the enclosing rectangle ((v0 − vc ) ∗ [1..m]) minus (III), where (III) is known thanks to the
“induction hypothesis.” Hence, our algorithm is to query the staircase for the virtual timeline v such
that the area below the staircase between vc and v is (v0 − vc ) ∗ [1..m] − (I I I ) + t − t0 . As just
explained, the shape data structure can handle this query because it corresponds to the first situation.
This v is the value of V (t) that we are looking for. Once we obtain the value of V (t), the area of (IV)
can be calculated as (V (t) − v0 ) ∗ [1..m] − (t − t0 ). Now, we have obtained the value of (III) + (IV)
as promised, so the “induction proof” is complete.
Invariant maintenance under insertions and deletions
In this section we first describe the two method calls that would destroy the invariant of the augmented
data fields, namely an insertion or deletion of a flow record, and how to repair the invariant. We then
describe how the GPS clocking tracking operation would trigger the two method calls.

418      Chapter 14 Scheduling packets
