Service thread pool: A pool of threads services network requests, where each thread
services one client connection at a time.
CPU thread pool: One thread is created per CPU. This is commonly used by longduration batch processing, such as video encoding.
Staged event-driven architecture (SEDA): Application requests are decomposed into
stages that may be processed by pools of one or more threads.

2

The official Microsoft documentation warns about problems that fibers can pose: e.g., thread-local storage is
shared between fibers, so programmers must switch to fiber-local storage, and any routine that exits a thread will
exit all fibers on that thread. The documentation states: “In general, fibers do not provide advantages over a welldesigned multithreaded application” [Microsoft 18].
3

With some exceptions, such as using sendfile(2) to avoid I/O syscalls, and Linux io_uring, which allows userspace to schedule I/O by writing and reading from io_uring queues (these are summarized in Section 5.2.6,
Non-Blocking I/O).

5.2

Application Performance Techniques

