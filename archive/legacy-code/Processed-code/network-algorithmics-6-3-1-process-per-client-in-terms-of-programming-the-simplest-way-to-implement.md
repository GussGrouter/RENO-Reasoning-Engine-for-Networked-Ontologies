# Network Algorithmics — 6.3.1 Process per client In terms of programming, the simplest way to implement a Web server is to structure the processing of (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 181
- Slice: from `6.3.1 Process per client In terms of programming, the simplest way to implement a Web server is to structure the processing of` up to next detected section heading

---

6.3.1 Process per client
In terms of programming, the simplest way to implement a Web server is to structure the processing of
each client as a separate process. In other words, every client is in a separate group by itself in Fig. 6.1.
In Chapter 2 we saw that the operating system scheduler juggles between processes, assigning a new
process to a CPU when a current process is blocked. Most modern operating systems also can take
into account multiple CPUs and schedule the CPUs such that all CPUs are doing useful work wherever
possible.
    Thus the Web server application need not do the juggling between clients; the operating system
does this automatically on the application’s behalf. For example, when Client 1 is blocked waiting for
the disk controller, the operating system may save all the context for the Client 1 process to memory
and allow the Client 2 process to run by restoring its context from memory.
    This simplicity, however, comes at a cost. First, as we have seen, process-context switching and
restoring is expensive. It requires reads and writes from memory to registers to save and restore con-
text. Recall that the context includes changing the page tables being used (because page tables are per
process); thus any virtual memory translations cached within the TLB (translation lookaside buffer)
need to be cached. Similarly, the contents of the data cache and the instruction cache are likely to rep-
resent the tastes and preferences of the previously resident process; thus much of it may be useless to
the new process. When all caches fail, the initial performance of the switched-in process can be very
poor.
    Further, spawning a new process when a new client comes in, as was done by some initial Web
servers, is also expensive.2 Fortunately, the overhead to create and destroy processes when clients come
and go can be avoided by precomputation and/or lazy process deletion (P2, shifting computation in
time). When a client finishes its request processing and the connection is terminated, rather than destroy
the process, the process can be returned to a pool of idle processes. The process can then be assigned
to the next new client that needs a process to shepherd its request through the server.
    A second issue is the problem of matchmaking between new arriving clients and processes in the
process pool. A naive way to do this is as follows. Each new client is handed to a well-known match-
making process, which then hands off each new client to some available process in the pool. However,
operating system designers have realized the importance of matchmaking. They have invented system


2 While some of these early schemes may seem primitive in terms of the techniques in this book, they were probably very simple
to program and maintain. It is difficult to quantify the trade-off between efficiency and ease of implementation and maintenance.

                                   6.3 Avoiding context-switching overhead in applications                                155



calls (for instance, the Accept call in UNIX) to do matchmaking at the cost of a system call invocation,
as opposed to requiring a process-context switch.
    When a process in the pool is done, it makes an Accept call and waits in line in a kernel data
structure. When a new client comes in, its socket is handed off to the idle process that is first in line.
Thus the kernel provides matchmaking services directly.


6.3.2 Thread per client
Even after removing the overheads of creating a process on demand and the overhead of matchmaking,
processes are an expensive solution. Since the rate of arrivals to popular Web servers can easily exceed
10 Gbps, it is not unusual for a Web server to have 50000 concurrent clients citegooglecarousel being
served at once.
     As we have seen, even if the processes are already created, switching between processes incurs TLB
and cache misses and requires effort to save and restore context. Further, each process requires memory
to store context. This can take away from the memory needed by the file cache.
     An intermediate stance is to use threads or lightweight processes. Note that threads generally trust
each other, as is appropriate for all the threads processing different clients in a Web server. Thus in
Fig. 6.5 we can replace the processing of each client with a separate thread per client, all within the
protection of a single process. Note that the threads share the same virtual memory. Thus TLB entries
do not have to be flushed between threads.
     Further, the fact that threads can share memory implies that all threads can use a common cache
to share file name translations and even files. Implementing a process per client, on the other hand,
implies that file caches can often not be shared efficiently across processes, because each process uses
a separate virtual memory space. Thus application caches for Web servers, as described in Chapter 5,
will suffer in performance because files common to many clients are replicated.3 Thus a classic Web
server, the Apache Web server, was implemented using a thread per client in Windows.
     However, when all is said and done, the overhead for switching between threads, while smaller than
that for switching between processes, is still considerable. Fundamentally, the operating system must
still save and restore per-thread context such as stacks and registers. Also, the memory required to store
per-thread or per-process state takes away from the file cache, which then leads to potentially higher
miss rates.
