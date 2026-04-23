# network-algorithmics-16-3-a-randomized-counter-scheme (chunk 000002)

In a nutshell, RS works as follows. Each logical counter is represented by a 5-bit counter in SRAM,
backed up by a 64-bit counter in DRAM. Increments to a logical counter happen first to its 5-bit SRAM
counter until it reaches the overflow value 32, at which point the value of this SRAM counter (i.e.,
32) needs to be flushed to the corresponding DRAM counter. Since updates to DRAM counters take
much longer (more specifically b = 21 times) than to SRAM counters, multiple SRAM counters may
overflow during the time it takes to update just one DRAM counter.
    In RS the solution is to maintain in SRAM a small FIFO buffer between the SRAM counters and
the DRAM counters to temporarily hold the “flush requests” that need to be made to the DRAM in the
future. With the parameter settings in this case (b = 21 and c = 5), this FIFO buffer, viewed as a simple
queueing system with births (arrivals of new flush-to-DRAM requests) and deaths (completed flushings
of overflowed counters to DRAM), has a moderate load factor (birth rate divided by death rate) of only
b/32 ≈ 65.6% (where 32 = 25 ).
    Hence, intuition from queueing theory suggests that only a small buffer is needed to ensure that this
FIFO queue does not overflow with overwhelming probability. However, while this intuition is correct
“in the average case” (i.e., when the arrival process is “smooth”), it is not in the worst case, as we
elaborate next.
    Let A[1..N] and B[1..N] be the SRAM array and the DRAM counter array, respectively. Simply
setting A[i] and B[i], i = 1, 2, ..., N , to 0 at the beginning of a measurement (counting) interval is
a standard way of assigning initial values. However, it would not work well in this scheme for the
following reason. In the worst case, an adversary (not in the context of security or cryptography) could
choose the sequence of the indices of the counters to be increased to be 1, 2, ..., N , 1, 2, ..., N, ... (the
repetition of the subsequence “1, 2, 3, ..., N ” over and over).
    At the end of the 31st repetition, the values of A[i], i = 1, 2, ..., N , will all become 31. Then, during
the next repetition, A[i], i = 1, 2, ..., N will overflow one by one after each increment, resulting in a
“burst arrival” of O(N ) flushing-to-DRAM requests to the FIFO queue. The FIFO queue has to be
made very large (in fact, much larger than the SRAM counter array A) to be able to accommodate this
burst, which would defeat the very purpose of combining DRAM and SRAM (that is, to save SRAM).
    This example shows that, in this queueing system, the arrival rate can far exceed the departure rate
for an extended period of time in the worst case, even when the aforementioned necessary condition (for
stability) 21 < 25 is met. However, from queuing theory, we know such a situation cannot happen when
the arrival process is “smooth”. Hence, a key innovation of RS is to guarantee that the arrival process
(of the counter overflows) is fairly smooth, even in the worst case, through a simple randomization of
seed SRAM counter values as follows.
    Each SRAM counter A[i] is assigned a random seed value uniformly distributed over {0, 1, 2, ..., 31}.
We need to somehow remember this seed value since it should be subtracted from the observed counter
value at the end of a measurement (counting) interval. This is achieved by setting the initial value of
B[i] to −A[i], for i = 1, 2, ..., N.
    Using large deviation theory, Zhao et al. (2006b) shows that a small FIFO buffer (say a few hundred
slots) is large enough to ensure that the probability for it to be filled up by flush requests (so that an
arriving flushing request would be tail-dropped) is vanishingly small, even when there are millions of
counters and the sequence of counters to be incremented is arbitrary. Here, each slot holds a counter
index to be flushed, which is usually shorter than 4 bytes. This translates into the aforementioned  bits
per counter when the cost of hundreds of buffer slots is amortized over millions of counters.
