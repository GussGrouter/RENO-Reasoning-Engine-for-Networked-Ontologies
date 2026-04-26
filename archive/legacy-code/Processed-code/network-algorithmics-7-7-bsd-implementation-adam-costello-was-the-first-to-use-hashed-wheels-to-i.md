# Network Algorithmics — 7.7 BSD implementation Adam Costello was the first to use hashed wheels to implement (Costello and Varghese, 1998) the BSD (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 216
- Slice: from `7.7 BSD implementation Adam Costello was the first to use hashed wheels to implement (Costello and Varghese, 1998) the BSD` up to next detected section heading

---

7.7 BSD implementation
Adam Costello was the first to use hashed wheels to implement (Costello and Varghese, 1998) the BSD
UNIX callout and timer facilities. The earlier BSD kernels took time proportional to the number of
outstanding timers to set or cancel timers. The Costello implementation, which is based on Scheme 6,
takes constant time to start, stop, and maintain timers; this led to a highly scalable design that could
support thousands of outstanding timers without much overhead.
     In the original BSD implementation each callout was represented by a CALLOUT structure con-
taining a pointer to the function to be called (C_FUNC), a pointer to the function’s argument (C_ARG),
and a time (C_TIME) expressed in units of clock ticks. Outstanding callouts were kept in a linked list,
sorted by their expiration times. The C_TIME member of each callout structure was differential, not
absolute; the first callout in the list stores the number of ticks from now until expiration, and each sub-
sequent callout in the list stores the number of ticks between its own expiration and the expiration of
its predecessor.
     In BSD UNIX callouts are set and canceled using TIMEOUT() and UNTIMEOUT(), respectively.
TIMEOUT ( FUNC , ARG , TIME ) registers FUNC ( ARG ) to be called at the specified time. UNTIME -
OUT ( FUNC , ARG ) cancels the callout with matching function and argument. Because the CALLTODO
list was searched linearly, both operations originally took time proportional to the number of outstand-
ing callouts. Interrupts were locked out for the duration of the search.
     Adding new algorithms to an existing system can sometimes run into compatibility problems with
existing interfaces. For example, the Costello implementation was based on Scheme 6. Costello found,
however, that the TIMEOUT()/UNTIMEOUT() interface in BSD did not allow the passing of handles,
which was used in all the schemes we described above to quickly cancel a timer. The Costello im-
plementation used two solutions to this problem. For calls using the existing interface, a search for a
callout given a function pointer and argument is done using a hash table. A second solution was also
implemented: A new interface function was defined for removing a callout (UNSETCALLOUT()) that
takes a handle as its only argument. This allowed existing code to use the old interface and new appli-
cations to use the new interface. The performance difference between these two approaches was slight,
so the hash table approach was preferable.
     In the Costello implementation, the timer routines were guaranteed to lock out interrupts only for a
small, bounded amount of time. The Costello implementation also extended the SETITIMER() interface
to allow a process to have multiple outstanding timers, thereby reducing the need for users to maintain
their own timer packages. The changes to the BSD kernel were small (548 lines of code added, 80

190      Chapter 7 Maintaining timers



removed). Details can be found in (Costello and Varghese, 1998); the written report contains several
important implementation details that are not given here.
    The advent of multicore machines required changes to the Costello implementation. An early
change was that a single callwheel was replaced by a per-CPU callwheel to improve scalability and
performance (Motin and Italiano, 2018). Motin and Italiano (Motin and Italiano, 2018) have recently
introduced an updated version called Calloutng to address the following three drawbacks of the Costello
implementation. First, intervals are rounded to the next tick resulting in a loss of accuracy; second, the
CPU is woken up on every interrupt resulting in extra energy consumption; finally, one cannot defer and
coalesce callouts which leads to extra interrupts. They considered using a balanced tree but decided to
retain the wheel structure. The code was, however, updated to give more attention to accuracy, to allow
aggregation, to use a new hash function to index into the wheel, and to carefully consider CPU cache
affinity affects (Motin and Italiano, 2018).
