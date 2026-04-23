# network-algorithmics-15-6-exercises-1-fcvc-flow-control-protocol-the-fcvc-flow-control-protocol-of (chunk 000002)

2. Load balancing with variable-sized packets: Load balancing within a router is typically at the
   granularity of cells. However, load balancing across routers is often at the granularity of (variable-
   sized) packets. Thus simple round-robin striping may not balance load equally because all the large
   packets may be sent on one link and the small ones on another. Modify the load-balancing algorithm
   without sequence numbers (using ideas suggested by the deficit round-robin (DRR) algorithm de-
   scribed in Chapter 14) to balance the load evenly, even while striping variable-sized packets. Extend
   the fault-tolerance machinery to also handle this case.
3. Concurrent compaction and search: In many lookup applications, routers must use available on-
   chip SRAM efficiently and may have to compact memory periodically to avoid filling up memory
   with unusably small amounts of free space. Imagine a sequence of N trie nodes of size-4 words
   that are laid out contiguously in SRAM memory, after which there is a hole of size-2 words. As
   a fundamental operation in compaction, the update algorithm needs to move the sequence of N
   nodes two words to the right to fill the hole. Unfortunately, moving a node two steps to the right can
   overwrite itself and its neighbor. Find a technique for doing compaction for updating with minimal
   disruption to a concurrent search process. Assume that, when a node X is moved, there is at most one
   other node Y that points to X and that the update process has a fast technique for finding Y given X
   (see Chapter 11). Use this method to find a way to compact a sequence of trie nodes arbitrarily laid
   out in memory into a configuration where all the free space is at one end of memory and there are
   no “holes” between nodes. Of course, the catch is that the algorithm should work without locking
   out a concurrent search process for more than one write operation every K search operations, as in
   the bridge binary search example.

This page intentionally left blank

PART

Endgame
                                                                                    4
              Daring ideas are like chessmen moved forward. They may be beaten, but they may start a winning
                                                                                                       game.
                                                                                                   —Goethe

We didn’t lose the game; we just ran out of time.
                                                                                           —Vince Lombardi

The last part of the book applies network algorithmics to the emerging fields of security and measure-
ment. As the Internet matures, we believe that good abstractions for security and measurement will be
key to well-engineered networks. While the problems (e.g., detecting a denial-of-service (DoS) attack at
a high-speed router) seem hard, some remarkable ideas have been proposed. The final chapter reaches
closure by distilling the underlying unities behind the many different techniques surveyed in this book
and by surveying the future of network algorithmics.

This page intentionally left blank

CHAPTER

Measuring network traffic
                                                                                                   16
                                      Not everything that is counted counts, and not everything that counts can be counted.
                                                                                                          —Albert Einstein
