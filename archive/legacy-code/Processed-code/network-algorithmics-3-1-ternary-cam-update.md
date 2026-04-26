# Network Algorithmics — motivating principles: ternary CAM updates (3.1) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 75 -l 91 -layout
- Slice: from `3.1 Motivating the use of principles` up to (excluding) `3.2 Algorithms versus algorithmics`

---

3.1 Motivating the use of principles—updating ternary
    content-addressable memories
Call a string ternary if it contains characters that are either 0, 1, or *, where * denotes a wildcard that
can match both a 0 and a 1. Examples of ternary strings of length 3 include S1 = 01* and S2 = *1*;
the actual binary string 011 matches both S1 and S2, while 111 matches only S2. A ternary content-
addressable memory (CAM) is a memory containing ternary strings of a specified length together with
associated information; when presented with an input string, the CAM will search all its memory loca-
tions in parallel to output (in one cycle) the lowest memory location whose ternary string matches the
specified input key.
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00008-7
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                       51

---

## PDF page 79

52       Chapter 3 Fifteen implementation principles




FIGURE 3.1
Summary of Principles 1–5—systems thinking.




FIGURE 3.2
Summary of Principles 6–10—recovering efficiency while retaining modularity.



   Fig. 3.4 shows an application of ternary CAMs to the longest-matching prefix problem for Internet
routers. For every incoming packet, each Internet router must extract a 32-bit destination IP address
from the incoming packet and match it against a forwarding database of IP prefixes with their corre-
sponding next hops. An IP prefix is a ternary string of length 32 where all the wildcards are at the end.
We will change notation slightly and let * denote any number of wildcard characters, so 101* matches
10100 and not just 1010.

---

## PDF page 80

                                                        3.1 Motivating the use of principles        53




FIGURE 3.3
Summary of Principles 11–15—speeding up key routines.




FIGURE 3.4
Example of using a ternary CAM for prefix lookups.


    Thus in Fig. 3.4 a packet sent to a destination address that starts with 010001 matches the prefixes
010001* and 01* but should be sent to Port P5 because Internet forwarding requires that packets be
forwarded using the longest match. We will have more to say about this problem in Chapter 11. For now,
note that if the prefixes are arranged in a ternary CAM such that all longer prefixes occur before any
shorter prefixes (as in Fig. 3.4), the ternary CAM provides the matching next hop in one memory cycle.
    While ternary CAMs are extremely fast for message forwarding, they require that longer prefixes
occur before shorter prefixes. But routing protocols often add or delete prefixes. Suppose in Fig. 3.4
that a new prefix, 11*, with next hop Port 1 must be added to the router database. The naive way to do
insertion would make space in the group of length-2 prefixes (i.e., create a hole before 0*) by pushing
up by one position all prefixes of length 2 or higher.
    Unfortunately, for a large database of around 100,000 prefixes kept by a typical core router, this
would take 100,000 memory cycles, which would make it very slow to add a prefix. We can obtain a

---

## PDF page 81

54        Chapter 3 Fifteen implementation principles




FIGURE 3.5
Finding a spot for the new prefix by moving X to Y ’s position recursively requires us to find a spot to move Y .



better solution systematically by applying the following two principles (described later in this chapter
as principles P13 and P15).

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
