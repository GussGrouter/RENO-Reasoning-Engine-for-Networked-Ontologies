While caches improve read performance, their storage is often used as buffers to improve write
performance.

5.2

Application Performance Techniques

5.2.3 Buffering
To improve write performance, data may be coalesced in a buffer before being sent to the next
level. This increases the I/O size and efficiency of the operation. Depending on the type of
writes, it may also increase write latency, as the first write to a buffer waits for subsequent writes
before being sent.
A ring buffer (or circular buffer) is a type of fixed buffer that can be used for continuous transfer
between components, which act upon the buffer asynchronously. It may be implemented using
start and end pointers, which can be moved by each component as data is appended or removed.

5.2.4

Polling

Polling is a technique in which the system waits for an event to occur by checking the status of
the event in a loop, with pauses between checks. There are some potential performance problems
with polling when there is little work to do:
■

Costly CPU overhead of repeated checks

■

High latency between the occurrence of the event and the next polled check

Where this is a performance problem, applications may be able to change their behavior to listen
for the event to occur, which immediately notifies the application and executes the desired
routine.

poll() System Call
There is a poll(2) syscall to check for the status of file descriptors, which serves a similar function
to polling, although it is event-based so it doesn’t suffer the performance cost of polling.
The poll(2) interface supports multiple file descriptors as an array, which requires the application
to scan the array when events occur to find the related file descriptors. This scanning is O(n)
(see Section 5.1.4, Big O Notation), whose overhead can become a performance problem at scale.
An alternative on Linux is epoll(2), which can avoid the scan and therefore be O(1). On BSD, the
equivalent is kqueue(2).

5.2.5 Concurrency and Parallelism
Time-sharing systems (including all derived from Unix) provide program concurrency: the ability
to load and begin executing multiple runnable programs. While their runtimes may overlap,
they do not necessarily execute on-CPU at the same instant. Each of these programs may be an
application process.
To take advantage of a multiprocessor system, an application must execute on multiple CPUs
