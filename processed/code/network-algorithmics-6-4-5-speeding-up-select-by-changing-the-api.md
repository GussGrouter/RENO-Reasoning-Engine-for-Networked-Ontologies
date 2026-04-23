# Network Algorithmics — 6.4.5 Speeding up select() by changing the API (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 191
- Slice: from `6.4.5 Speeding up select() by changing the API` up to next detected section heading

---

6.4.5 Speeding up select() by changing the API
The technique described in Section 6.4.4 improves performance considerably by eliminating the first
three (and chief) sources of overhead in select(). However, it does so by maintaining extra state (P12)
in the form of three more sets of descriptors (i.e., H , I , and R) that are also maintained as bitmaps.
This, taken together with the selection set S passed in each call, requires the scanning and updating of
four separate bitmaps.
    In a situation where a large number of connections are present but only a few are active at any
instant, this fundamentally still requires paying some small overhead, proportional to the total number
of connections as opposed to the number of active connections. This is the fourth source of “waste”
enumerated earlier, and it appears unavoidable given the present API.
    Further, as we saw earlier, even the modified fast select() potentially checks a descriptor multiple
times for each event such as a packet arrival (if the application does not consume all the data at once).
Such additional checks are unavoidable because select() provides the state of each descriptor.
    If one looks closely at the interface, what the application fundamentally requires is to be notified
of the stream of events (e.g., file I/O completed, network packet arrived) that causes changes in state.
Event-based notifications appear, on the surface, to have some obvious drawbacks that may have pre-
vented them from being used in the past.


7 The reader may wonder whether it suffices to set I = S. The exercises explore some of the issues with this alternative imple-
mentation.

                                                                         6.4 Scalable I/O Notification     165



• Asynchronous notification: If the application is notified as soon as an event occurs, this can take
  excessive overhead and be difficult to program. For example, when an application is servicing socket
  5, a packet to socket 12 may arrive. Interrupting the application to inform it of the new packet may
  be a bad idea.
• Excessive event rate: The application is interested in the events that cause state change and not in the
  raw event stream. For a large Web transfer, several packets may arrive to a socket and the application
  may wish to get one notification for a batch, and not one for every packet. The overhead for each
  notification is in terms of communication costs (CPU) as well as storage for each notification.
   Principle P6 suggests designing efficient specialized routines to overcome bottlenecks. In this spirit,
Banga, Mogul, and Druschel (Banga et al., 1999) describe a new event-based API that avoids both these
problems.
• Synchronous inquiry: As in the original select() call, the application can inquire for pending events.
  For example, in the previous example, the application continues to service socket 5 and all other
  active sockets before asking for (and being told about) events such as packet arrival on socket 12.
• Coalescing of events: If a second event occurs for a descriptor while a first event has been queued
  for notification, the second notification is omitted. Thus there can be at most one outstanding event
  notification per descriptor.
    The use of this new API is straightforward and roughly follows the style in which applications use
the old select() API. The application stays in a loop in which it asks synchronously for the next set of
events and goes to sleep if there are none. When the call returns, the application goes through each event
notification and invokes the appropriate read or write handlers. Implicitly, the setting up of a connection
registers interest in the corresponding descriptor, while disconnection removes the descriptor from the
interest list.
    The implementation is as follows. Associated with each thread is a set of descriptors in which it
is interested. Each descriptor (e.g., socket) keeps a reverse mapping list of all threads interested in the
descriptor. On I/O activity (e.g., data arrival on a socket), the I/O module uses its reverse mapping list
to identify all potentially interested threads. If the descriptor is in the thread’s interest set, a notification
event is added to a queue of pending events for that thread.
    A simple per-thread bitmap, one bit per descriptor, is used to record the fact that an event is pending
in the queue and is used to avoid multiple event notifications per descriptor. Finally, when the applica-
tion asks for the next set of events, these are returned from the pending queue.8
    Linux epoll() API: Event mechanisms like select() require the server to re-declare its interest set
every time it wishes to retrieve events, since the kernel does not remember the interest sets from previ-
ous calls. In Linux, our prior discussion of (Banga et al., 1999) culminated in the epoll() (epoll(7)) API
which actually uses three separate system calls to avoid the problems of select(). First, the epoll_create
system call instructs the kernel to create an event data structure that can be used to track events on a
number of descriptors. Thereafter, the epoll_ctl call is used to modify interest sets, while the epoll_wait
call is used to retrieve events. The intellectual connection between the work in Banga et al. (1999) and
epoll() is described in (Gammo et al., 2004).


8 This simple description glosses over some tricky race conditions and overflow conditions.

166      Chapter 6 Transferring control



    As we have seen, a drawback of select() is that it does work proportional to the size of the interest
set, rather than the number of events returned, which causes poor scaling. The epoll API, of course,
avoids this issue. As described in Gammo et al. (2004), if the server has many idle connections, perfor-
mance degrades badly when using select() but not when using epoll(). The advent of multicore CPUs
complicated the design of epoll() since many applications scale by using multi-threading. This was not
supported by early implementations of epoll() but was fixed later.
    There are other subtleties. Imagine a socket descriptor shared across multiple operating system
threads or processes. When an event happens all of the threads/processes must be woken up. This is
sometimes called the “thundering herd” (epoll(7), 2022) problem. This is avoided by having a flag that
ensures that the kernel wakes up just one of the waiting threads/processes.
