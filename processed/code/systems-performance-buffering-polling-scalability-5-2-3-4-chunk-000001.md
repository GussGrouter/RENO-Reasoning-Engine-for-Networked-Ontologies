pushed to service more users or data objects than they ever have before, at which point algorithms such as O(n^2) may begin to be pathological. The fix may be for the developer to use a
more efficient algorithm or to partition the population differently.
Big O notation does ignore some constant computation costs incurred for each algorithm. For
cases where n (the input data size) is small, these costs may dominate.

5.2 Application Performance Techniques
This section describes some commonly used techniques by which application performance can
be improved: selecting an I/O size, caching, buffering, polling, concurrency and parallelism,
non-blocking I/O, and processor binding. Refer to the application documentation to see which
of these are used, and for any additional application-specific features.

5.2.1 Selecting an I/O Size
Costs associated with performing I/O can include initializing buffers, making a system call,
mode or context switching, allocating kernel metadata, checking process privileges and limits,
mapping addresses to devices, executing kernel and driver code to deliver the I/O, and, finally,
freeing metadata and buffers. “Initialization tax” is paid for small and large I/O alike. For efficiency, the more data transferred by each I/O, the better.
Increasing the I/O size is a common strategy used by applications to improve throughput. It’s
usually much more efficient to transfer 128 Kbytes as a single I/O than as 128 × 1 Kbyte I/O,
considering any fixed per-I/O costs. Rotational disk I/O, in particular, has historically had a high
per-I/O cost due to seek time.
There’s a downside when the application doesn’t need larger I/O sizes. A database performing
8 Kbyte random reads may run more slowly with a 128 Kbyte disk I/O size, as 120 Kbytes of data
transfer is wasted. This introduces I/O latency, which can be lowered by selecting a smaller I/O
size that more closely matches what the application is requesting. Unnecessarily larger I/O sizes
can also waste cache space.

5.2.2

Caching

The operating system uses caches to improve file system read performance and memory allocation
performance; applications often use caches for a similar reason. Instead of always performing
an expensive operation, the results of commonly performed operations may be stored in a local
cache for future use. An example is the database buffer cache, which stores data from commonly
performed database queries.
A common task when deploying applications is to determine which caches are provided, or can
be enabled, and then to configure their sizes to suit the system.
