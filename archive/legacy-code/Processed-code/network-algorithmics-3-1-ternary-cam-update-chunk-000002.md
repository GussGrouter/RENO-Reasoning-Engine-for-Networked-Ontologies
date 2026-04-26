# network-algorithmics-3-1-ternary-cam-update (chunk 000002)

Understand and exploit degrees of freedom
In looking at the forwarding table on the left of Fig. 3.4 we see that all prefixes of the same length are
arranged together and all prefixes of length i occur after all prefixes of length j > i. However, in the
figure all prefixes of the same length are also sorted by value. Thus 00* occurs before 01*, which occurs
before 10*. But it is unnecessary for the CAM to correctly return longest matching prefixes: We only
require ordering between prefixes of different lengths; we do not require ordering between prefixes of
the same length.
    In looking at the more abstract view of Fig. 3.4 shown in Fig. 3.5, we see that if we are to add an
entry to the start of the set of length-i prefixes, we have to create a hole at the end of the length-(i + 1)
set of prefixes. Thus we have to move the entry X, already at this position, to another position. If we
move X one step up, we will be forced into our prior inefficient solution.
    However, our observation about degrees of freedom says that we can place X anywhere adjacent to
the other length-(i + 1) prefixes. Thus, an alternative idea is to move X to the position held by Y , the
last length-(i + 2) prefix. But this forces us to find a new position for Y . How does this help? We need
a second principle.

Use algorithmic techniques
Again, recursion suggests itself: We solve a problem by reducing the problem to a “smaller” instance
of the same problem. In this case, the new problem of assigning Y a new position is “smaller” because
the set of length-(i + 2) prefixes is closer to the free space at the top of the CAM than the set of length-
(i + 1) prefixes. Thus we move Y to the end of the length-(i + 3) set of prefixes, etc.
    While recursion is a natural way to think, a better implementation is to unwind the recursion by
starting from the top of the CAM and working downward by creating a hole at the end of the length-1

---

## PDF page 82
