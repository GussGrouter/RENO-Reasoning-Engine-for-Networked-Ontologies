# Network Algorithmics — 6.1 Why control overhead? (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 174
- Slice: from `6.1 Why control overhead?` up to next detected section heading

---

6.1 Why control overhead?
Chapter 5 started with a review of the copying overhead involved in a Web server by showing the po-
tential copies (Fig. 5.1) involved in responding to a GET request at a server. By contrast, Fig. 6.1 shows
the potential control overhead involved in a large Web server that handles many clients. Note that in
comparison with Fig. 5.1 for Web copies, Fig. 6.1 ignores all aspects of data transfer. Thus Fig. 6.1 uses
a simplified architectural picture that concentrates on the control interplay between the network adaptor
and the CPU (via interrupts), between the application and the kernel (via system calls), and between
various application-level processes or threads (via scheduler invocations). The reader unfamiliar with
operating systems may wish to consult the review of operating systems in Chapter 2. For simplicity, the
picture shows only one CPU in the server (many servers are multiprocessors) and a single disk (some
servers use multiple disks and disks with multiple heads). Assume that the server can handle a large
number (say, thousands) of concurrent clients.
    For the purposes of understanding the possible control overhead involved in serving a GET request,
the relevant aspects of the story are slightly different from that in Chapter 5. First, assume the client
has sent a TCP SYN request to the server that arrives at the adaptor from which it is placed in memory.
The kernel is then informed of this arrival via an interrupt. The kernel notifies the Web server via the
unblocking of an earlier system call; the Web server application will accept this connection if it has
sufficient resources.
    In the second step of processing some server process parses the Web request. For example, assume
the request is GET File 1. In the third step the server needs to locate where the file is on disk, for
example, by navigating directory structures that may also be stored on disk. Once the file is located, in
the fourth step, the server process initiates a Read to the file system (another system call). If the file is
in the file cache, the read request can be satisfied quickly; failing a cache hit, the file subsystem initiates

148       Chapter 6 Transferring control




FIGURE 6.1
Control overhead involved in handling a GET request at a server.


a disk seek to read the data from disk. Finally, after the file is in an application buffer, the server sends
out the HTTP response by writing to the corresponding connection (another system call).
    So far the only control overhead appears to be that of system calls and interrupts. However, that is
because we have not examined closely the structure of the networking and application code.
    First, if the networking code is structured naively, with a single process per layer in the stack,
then the process scheduling overhead (on the order of hundreds of microseconds) for processing a
packet can easily be much larger than a single packet arrival time. This potential scheduling overhead
is shown in Fig. 6.1 with a dashed line to the TCP/IP code in the kernel. Fortunately, most networking
code is structured more monolithically, with minimal control overhead, although there are some clever
techniques that can do even better.
    Second, our description of Web processing has focused on a single client. Since we are assuming a
large Web server that is working concurrently on behalf of thousands of clients, it is unclear how the
Web server should be structured. At one extreme, if each client is a separate process (or thread) running
the Web server code, concurrency is maximized (because when client 1 is waiting for a disk read, client
2 could be sending out network packets) at the cost of high process scheduling overhead.
    On the other hand, if all clients are handled by a single event-driven process, then context-switching
overhead is minimized, but the single process must internally schedule the clients to maximize concur-
rency. In particular, it must know when file reads have completed and when network data has arrived.
    Many operating systems provide a system call for this purpose that we have generically called
FindActive() in Fig. 6.1. For example, in UNIX the specific name for this generic routine is the select()
system call. While even an empty system call is expensive because of the kernel-to-application bound-
ary crossing, an inefficient select() implementation can be even more expensive.
    Thus there are challenging questions as to how to structure both the networking and server code
in order to minimize scheduling overhead and maximize concurrency. For this reason, Fig. 6.1 shows

                               6.2 Avoiding scheduling overhead in networking code                   149



the clients partitioned into groups, each of which is implemented in a single process or thread. Note
that placing all clients in a single group yields the event-driven approach, while placing each client in a
separate group yields the process-per-client (or thread-per-client) approach.
    Thus an unoptimized implementation can incur considerable process-switching overhead (hun-
dreds of microseconds) if the application and networking code is poorly structured. Even if process-
structuring overhead is removed, system calls can cost tens of microseconds, and interrupts can cost
microseconds. To put these numbers in perspective, observe that on a 100-Gbps Ethernet link, a 40-byte
packet can arrive at a PC every 3.2 nanoseconds.
    Given that 100-Gbps links have already arrived, it is clear that careful attention has to be paid to
control overhead. Note that as we have seen in Chapter 2, as CPUs get faster, historically the control
overheads associated with context switching, system calls, and interrupts have not improved at the
same rate. Some progress has been made with more efficient operating systems such as Linux, but the
progress will not be sufficient to keep up with increasing link speeds.
    We now begin attacking the bottlenecks described in Fig. 6.1.
