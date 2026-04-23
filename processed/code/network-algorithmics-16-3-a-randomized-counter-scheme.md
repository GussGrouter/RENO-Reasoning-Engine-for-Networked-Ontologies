# Network Algorithmics — 16.3 A randomized counter scheme (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 482
- Slice: from `16.3 A randomized counter scheme` up to next detected section heading

---

16.3 A randomized counter scheme
Both LCF and LR are deterministic algorithms and both guarantee that no counter update will be
lost. However, in most real-world network measurement operations, missing some counter updates
“occasionally” (say once a few billion years) is acceptable (P3). This has motivated Zhao et al. to
design a randomized algorithm (P3a) that is better than both LCF and LR in virtually all aspects (Zhao
et al., 2006b). We call this algorithm RS (random seeding) for reasons that will become clear shortly.
RS can be proved to be unconditionally (among all possible schemes and not restricted to the “pick-a-
counter-to-flush” framework) near-optimal in terms of SRAM consumption, yet has very simple control
logic. RS has been used on Huawei router products since 2010.
     With the same assumption (that the SRAM/DRAM speed difference b ≈ 21), RS requires only 5 + 
bits per counter, where each SRAM counter consumes 5 bits and its control logic consumes  bits per
counter. Here,  is typically a small number (e.g., 0.01). Clearly, in this case 5 bits per counter is the
absolute minimum for any algorithm/scheme since using 4 bits per counter would necessarily lead to
one DRAM access every 16 SRAM accesses, which would exceed the DRAM bandwidth (as b ≈ 21).
More generally, it can be shown that this absolute minimum is log2 (b + 1).
     Note that reducing the SRAM counter size from 8 to 5 bits per counter is 28−5 = 8 times harder
since overflows from an SRAM counter happen 8 times faster with the smaller overflow threshold (25
as compared to 28 ), requiring the “flushing” mechanism to operate 8 times more efficiently. Fortunately,
this improvement in the efficiency of RS is achieved with a simple counter-flushing technique that costs
only a small fraction of bits per counter, as compared to 20 bits per counter in LCF and 2 bits per
counter in LR.
     Like LCF and LR, the performance (in terms of not losing a counter update) guarantee of RS is
still worst case in nature in the sense that this guarantee holds under all possible sequences of counter
indices (to increment). Unlike LCF and LR, however, the guarantee is not with probability 1: With an
extremely small yet nonzero probability, RS may miss some increments to the counters.
     However, in practice, this probability can be made so small that even if a router operates continu-
ously for billions of years, the probability that a single loss of increment happens is less than one in a
billion. Note that router software/hardware failures and other unexpected or catastrophic events (e.g.,
earthquakes) that may disable a router happen with a probability many orders of magnitude higher.

456      Chapter 16 Measuring network traffic



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

                                           16.4 Maintain active counters using BRICK                 457



    We conclude this section using a numerical example from Zhao et al. (2006b). Let there be N =
1 million counters. The measurement epoch is set to n = 1012 (1 trillion) cycles with one counter
increment per cycle. This interval is a bit over two hours long if we assume each cycle is 8 anosecond
long as before. The SRAM/DRAM speed difference b is assumed to be 12 and, correspondingly, the
number of bits per SRAM counter is set to c = 4, the minimum that is needed (since 23 < 12).
    With this parameter setting, the load factor of the FIFO queue is 12/16 = 75%, a bit larger than
21/32 ≈ 65.6% in the earlier parameter setting. Suppose there are 300 slots in the FIFO buffer, which
costs 6000 bits (each index is 20 bits since N is 1 million) or  = 0.006 bits per counter. Under these
parameter settings, the probability for the FIFO queue to become full is less than 2.4 × 10−14 . This
translates into the FIFO queue dropping a flushing request every 10.57 billion years!
