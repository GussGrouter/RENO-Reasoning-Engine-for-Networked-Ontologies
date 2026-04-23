# network-algorithmics-16-2-reducing-sram-width-using-dram-backing-store (chunk 000002)

largest SRAM counter. With this strategy, Shah et al. (2002a) show that the SRAM counter width c can
be significantly smaller than M, the width of a DRAM counter.
                                             log b(N −1)
    More precisely, they show that 2c ≈ log(b/(b−1))     , where N is the total number of counters. Note
that this means that the SRAM counter width grows approximately as log log bN since b/(b − 1) can
be ignored for large b. For example, with three 64-bit counters, every 8 nanoseconds (OC-768) for N
equal to a million requires only 8 Mbit of 2.5 microseconds SRAM with 51.2 microseconds DRAM.
Note that in this case the value of b is 51.2/2.5 ≈ 21.
    The bottom line is that the naive method would have required 192 Mbit of SRAM compared to
8 Mbit, a factor of 24 savings in expensive SRAM. Overall, this provides roughly a factor of 24 savings
in cost since DRAM is roughly two orders of magnitude cheaper than SRAM.
    But this begs the question: How do the chip processing counters find the largest counter? Bhagwan
and Lin (2000) describe an implementation of a pipelined heap structure that can determine the largest
value at a fairly high expense in hardware complexity and space. Their heap structure requires pointers
of size log2 N for each counter just to identify the counter to be evicted. Unfortunately, log2 N addi-
tional bits per counter can be large (20 for N = 1 million) and can defeat the overall goal that was to
reduce the required SRAM bits from 64 to say 10.
    The need for a pointer per heap value seems hard to avoid. This is because the counters must be in
a fixed place to be updated when packets arrive, but values in a heap must keep moving to maintain
the heap property. On the other hand, when the largest value arrives at the top of the heap, one has to
correlate it to the counter index to reset the appropriate counter and to banish its contents to DRAM.
Notice also that all values in the heap, including pointers and values, must be in SRAM for speed.
    The following LR algorithm (Ramabhadran and Varghese, 2003) simplifies the largest count first
(LCF) algorithm of Shah et al. (2002a) and is easier to implement. Let j be the index of the counter
with the largest value among the counters incremented in the last cycle of b updates to SRAM. Ties may
be broken arbitrarily. If cj ≥ b, the algorithm updates counter cj to DRAM. If cj < b, the algorithm
updates any counter with value at least b to DRAM. If no such counter exists, LR(T ) updates counter
Cj to DRAM.
    It can be shown that LR (Ramabhadran and Varghese, 2003) is also conditionally optimal (within
the “pick-a-counter-to-flush” algorithmic framework) and produces SRAM counter width c, which is
equal to that of LCF. The maintaining of all counters above the threshold b can be done using a size-N
bitmap in which a 1 implies that the corresponding position has a counter no less than b.

16.3 A randomized counter scheme                 455
