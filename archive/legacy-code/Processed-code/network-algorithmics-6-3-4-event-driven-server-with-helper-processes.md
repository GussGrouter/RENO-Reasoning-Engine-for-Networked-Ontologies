# Network Algorithmics — 6.3.4 Event-driven server with helper processes (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 184
- Slice: from `6.3.4 Event-driven server with helper processes` up to next detected section heading

---

6.3.4 Event-driven server with helper processes
In principle, an event-driven server can extract as much concurrency from a stream of client operations
as a multiprocess or multithreaded server. Unfortunately, many operating systems, such as UNIX, do
not provide suitable support for nonblocking disk operations.
     For example, if an event-driven server is not to waste opportunities to do useful work, then when
it issues a read() to a file that is not in cache, we wish the read() to return immediately saying it is
unavailable so that the read() is nonblocking. This allows the server to move on to other clients. Later,
when the disk I/O completes, the application can find out using the next invocation of the FindActive()
call. On the other hand, if the read() call is blocking, then the server main loop would be stuck waiting
for the milliseconds required for disk I/O to complete.
     The difficulty is that many operating systems, such as Solaris and UNIX, allow nonblocking read()
and write() operations on network connections but may block when used on disk files. These operating
systems do allow other asynchronous system calls for disk I/O, but these are not integrated with the
select() call (i.e., the UNIX equivalent of FindActive()). Thus in such operating systems one must
choose between the loss of concurrency incurred by blocking on disk I/O and going beyond the single-
process model.
     The Flash Web server (Pai et al., 1999a) goes beyond the single-process model to maximize concur-
rency. When a file is to be read, the main server process first tests if the file is already in memory using
either a standard system call4 or by locking down the file cache pages so that the server process always
knows which files are in the cache.5 If the file is not in memory, the main server process instructs a
helper process to perform the potentially blocking disk read. When the helper is done, it communicates
to the main server process via some form of interprocess communication such as a pipe.
     Note that unlike the multiprocess model, helpers are needed only for each concurrent disk operation
and not for each concurrent client request. In some sense, this model exploits a degree of freedom (P13)
by observing that there are interesting alternatives between a single process and a process per client.
     Besides file reads, helper processes can also be used to do directory lookups to locate the file on
disk. While Flash maintains a cache that maps between directory path names and disk files, if there is
a cache miss, then there is a need to search through on-disk directory structures. Since such directory
lookups can also block, these are also relegated to helper processes. Increasing the pathname cache


4 The original Flash Web server uses UNIX’s mincore() command.
5 If the virtual memory system could swap out cached files under the nose of the server, the server may think a file is in cache
when it really is not.

158       Chapter 6 Transferring control




FIGURE 6.6
Two other proposals for Web architectures besides the two shown in Fig. 6.5: (3) event-driven plus helper processes;
(4) staged event-driven architecture.



does increase memory consumption, but the reduced cache miss rate may reduce the number of helper
processes required and so decrease memory overall.
    Clearly, helper processes should be prespawned to avoid the latency of creating a process each
time a helper process is invoked. How many helper processes should be spawned? Too few can cause
concurrency loss, and too many results in wasted memory. The solution in Flash (Pai et al., 1999a) is
to dynamically spawn and destroy helper processes according to load.
