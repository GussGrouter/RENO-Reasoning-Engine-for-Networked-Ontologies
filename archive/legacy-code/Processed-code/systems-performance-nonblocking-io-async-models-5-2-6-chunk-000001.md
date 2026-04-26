■

A single global mutex lock for all data structures. While this solution is simple, concurrent
access will encounter contention for the lock and latency while waiting for it. Multiple
threads that need the lock will serialize—execute in sequence, rather than concurrently.
A mutex lock for every data structure. While this reduces contention to only the times it is
really needed—concurrent access to the same data structure—there are storage overheads
for the lock, and CPU overheads for the creation and destruction of the lock for every data
structure.

A hash table of locks is an in-between solution and is suitable when lock contention is expected
to be light. A fixed number of locks is created, and a hashing algorithm is used to select which
lock is used for which data structure. This avoids the creation and destruction cost with the data
structure and also avoids the problem of having only a single lock.
The example hash table shown in Figure 5.2 has four entries, called buckets, each of which
contains its own lock.

Figure 5.2

Example hash table

This example also shows one approach for solving hash collisions, where two or more input data
structures hash to the same bucket. Here, a chain of data structures is created to store them all
under the same bucket, where they will be found again by the hashing function. These hash
chains can be a performance problem if they become too long and are walked serially, because
they are protected by only one lock that can begin to have long hold times. The hash function
and table size can be selected with the goal of uniformly spreading data structures over many
buckets, to keep hash chain length to a minimum. Hash chain length should be checked for
production workloads, in case the hashing algorithm is not working as intended and is instead
creating long hash chains that perform poorly.
Ideally, the number of hash table buckets should be equal to or greater than the CPU count, for the
potential of maximum parallelism. The hashing algorithm may be as simple as taking low-order
bits4 of the data structure address and using this as an index into a power-of-two-size array of
locks. Such simple algorithms are also fast, allowing data structures to be located quickly.
4

Or middle bits. The lowest-order bits for addresses to an array of structs may have too many collisions.

