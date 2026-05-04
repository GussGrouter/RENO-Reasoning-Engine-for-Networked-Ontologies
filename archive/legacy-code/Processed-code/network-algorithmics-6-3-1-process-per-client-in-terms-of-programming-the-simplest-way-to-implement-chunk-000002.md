# network-algorithmics-6-3-1-process-per-client-in-terms-of-programming-the-simplest-way-to-implement (chunk 000002)

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
