# network-algorithmics-7-7-bsd-implementation-adam-costello-was-the-first-to-use-hashed-wheels-to-i (chunk 000002)

removed). Details can be found in (Costello and Varghese, 1998); the written report contains several
important implementation details that are not given here.
    The advent of multicore machines required changes to the Costello implementation. An early
change was that a single callwheel was replaced by a per-CPU callwheel to improve scalability and
performance (Motin and Italiano, 2018). Motin and Italiano (Motin and Italiano, 2018) have recently
introduced an updated version called Calloutng to address the following three drawbacks of the Costello
implementation. First, intervals are rounded to the next tick resulting in a loss of accuracy; second, the
CPU is woken up on every interrupt resulting in extra energy consumption; finally, one cannot defer and
coalesce callouts which leads to extra interrupts. They considered using a balanced tree but decided to
retain the wheel structure. The code was, however, updated to give more attention to accuracy, to allow
aggregation, to use a new hash function to index into the wheel, and to carefully consider CPU cache
affinity affects (Motin and Italiano, 2018).
