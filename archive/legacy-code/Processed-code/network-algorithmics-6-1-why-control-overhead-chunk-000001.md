# network-algorithmics-6-1-why-control-overhead (chunk 000001)

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
