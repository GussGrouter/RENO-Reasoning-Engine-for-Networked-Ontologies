# network-algorithmics-16-3-a-randomized-counter-scheme (chunk 000003)

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
