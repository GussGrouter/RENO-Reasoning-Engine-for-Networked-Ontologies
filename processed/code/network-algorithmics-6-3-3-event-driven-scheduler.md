# Network Algorithmics — 6.3.3 Event-driven scheduler (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 182
- Slice: from `6.3.3 Event-driven scheduler` up to next detected section heading

---

6.3.3 Event-driven scheduler
If a general-purpose operating system facility is too expensive, the simplest strategy is to avoid it com-
pletely. Thus while thread scheduling provides a facility for juggling between clients without further
programming, if it is too expensive, the application may benefit from doing the juggling itself. Effec-
tively, the application must implement its own internal scheduler that juggles the state of each client.
    For example, the application may have to implement a state machine that remembers that Client 1
is in Stage 2 (HTTP processing) while Client 2 is in Stage 3 (waiting for disk I/O) and Client 3 is in
Stage 4 (waiting for a socket buffer to clear up to send the next part of the response).


3 However, this replication will not cost much if a system such as I/O-Lite, described in Chapter 5, is used. The problem is that
historically many operating systems did not have such mechanisms to allow subsystems to share data.

156       Chapter 6 Transferring control




FIGURE 6.5
The two simplest alternatives for structuring a Web server: (1) the use of a single process (or thread) per client;
(2) a single process implementation that uses an event manager to tell the process of the status of I/O for each client.


    However, the kernel has an advantage over an application program because the kernel sees all I/O
completion events. For example, if Client 1 is blocked waiting for I/O, in a per-thread implementation,
when the disk controller interrupts the CPU to say that the data is now in memory, the kernel can now
attempt to schedule the Client 1 thread.
    Thus if the Web server application is to do its own scheduling between clients, the kernel must pass
information (P9) across the API to allow a single-threaded application to view the completion of all
I/O that it has initiated. Many operating systems provide such a facility, which we generically called
FindActive() in Fig. 6.1. For example, Windows NT 3.5 has an I/O completion port (IOCP) mechanism,
UNIX provides the select() system call, Linux provides the epoll() system call.
    The main idea is that the application stays in a loop invoking the FindActive() call. Assuming there
is always some work to do on behalf of some client, the call will return with a list of I/O descriptors
(e.g., file 1 data is now in memory, connection 5 has received data) with pending work. When the Web
server processes these active descriptors, it loops back to making another FindActive() call.
    If there is always some client that needs attention (typically true for a busy server), there is no
need to sleep and invoke the costs of context switching (e.g., scheduler overhead, TLB misses) when
juggling between clients. Of course, such juggling requires that the application keeps a state machine
that allows it to do its own context switching among the many concurrent requests. Such application-
specific internal scheduling is more efficient than invoking the general-purpose, external scheduler. This

                                   6.3 Avoiding context-switching overhead in applications                               157



is because the application knows the minimum set of context that must be saved when moving from
client to client.
    The Zeus server and the original Harvest/Squid proxy cache server use the single-process event-
driven model. Fig. 6.5 contrasts the multiprocess (and multithreaded) server architectures with an event-
driven architecture. The details of a generic event-driven implementation using a single process can be
found in Barile (2004), together with pointers to source code. Barile (2004) describes generic code
that is abstracted to work across platforms (a crucial requirement for today’s server environments),
including Windows and UNIX.
