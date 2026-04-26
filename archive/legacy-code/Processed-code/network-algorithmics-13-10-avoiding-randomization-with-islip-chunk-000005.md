# network-algorithmics-13-10-avoiding-randomization-with-islip (chunk 000005)

iterations appear to take at least 2K time steps because the grant-and-accept steps of each iteration take
one time step. At first glance, the architecture appears to specify that the grant phase of iteration k + 1
be started after the accept phase of iteration k. This is because one needs to know whether an input port
I has been accepted in iteration k so as to avoid doing a grant for such an input in iteration k + 1.
    What makes partial pipelining possible is a simple observation (Gupta and McKeown, 1999b): if
input I receives any grant in iteration k, then I must accept exactly one and so be unavailable in iteration
k + 1. Thus the implementation specification can be relaxed (P3) to allow the grant phase of iteration
k + 1 to start immediately after the grant phase of iteration k, thus overlapping with the accept phase
of iteration k. To do so, we simply use the OR of all the grants to input I (at the end of iteration k) to
mask out all of I ’s requests (in iteration k + 1).
    This reduces the overall completion time by nearly a factor of two time steps for k iterations, from
2k to k + 1. For example, the Tiny Tera iSLIP implementation (Gupta and McKeown, 1999b) does three
iterations of iSLIP in 51 nanoseconds (roughly OC-192 speeds) using a clock speed of 175 MHz; given
that each clock cycle is roughly 5.7 nanoseconds, iSLIP has roughly nine clock cycles to complete.
Since each grant and accept step takes two clock cycles, the pipelining is crucial for being able to
handle three iterations in nine clock cycles; the naive iteration technique would have taken at least 12
clock cycles.
