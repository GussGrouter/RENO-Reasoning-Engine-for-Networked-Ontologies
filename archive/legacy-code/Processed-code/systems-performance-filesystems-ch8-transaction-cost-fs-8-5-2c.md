Transaction Cost
Another way to present file system latency is as the total time spent waiting on the file system
during an application transaction (e.g., a database query):
percent time in file system = 100 * total blocking file system latency/application
transaction time

This allows the cost of file system operations to be quantified in terms of application performance, and performance improvements to be predicted. The metric may be presented as the
average either for all transactions during an interval, or for individual transactions.
Figure 8.12 shows the time spent on an application thread that is servicing a transaction. This
transaction issues a single file system read; the application blocks and waits for its completion,
transitioning to off-CPU. The total blocking time in this case is the time for the single file system
read. If multiple blocking I/O were called during a transaction, the total time is their sum.

Figure 8.12 Application and file system latency
As a specific example, an application transaction takes 200 ms, during which it waits for a total
of 180 ms on multiple file system I/O. The time that the application was blocked by the file
system is 90% (100 * 180 ms/200 ms). Eliminating file system latency may improve performance
by up to 10x.
As another example, if an application transaction takes 200 ms, during which only 2 ms was
spent in the file system, the file system—and the entire disk I/O stack—is contributing only 1%
to the transaction runtime. This result is incredibly useful, as it can steer the performance investigation to the real source of latency.
If the application were issuing I/O as non-blocking, the application can continue to execute
on-CPU while the file system responds. In this case, the blocking file system latency measures
only the time the application was blocked off-CPU.

