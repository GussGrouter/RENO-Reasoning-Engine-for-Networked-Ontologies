<!-- Extracted from systems-performance-ch4-scout-p171-220.txt (combined extract; Chapter 5 Applications) -->

■

Elimination of latency outliers: zero requests beyond 1,000 ms

■

■

A maximum throughput of at least 10,000 application requests per second per server of a
given size1
Average disk utilization under 50% for 10,000 application requests per second

Once a goal has been chosen, you can work on the limiters for that goal. For latency, the limiter
may be disk or network I/O; for throughput, it may be CPU usage. The strategies in this and
other chapters will help you identify them.
