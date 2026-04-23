# network-algorithmics-6-4-2-problems-with-implementations-of-select (chunk 000001)

# Network Algorithmics — 6.4.2 Problems with implementations of select() (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 187
- Slice: from `6.4.2 Problems with implementations of select()` up to next detected section heading

---

6.4.2 Problems with implementations of select()
Assuming that ufalloc() overhead can easily be minimized by changing the kernel implementation, it is
important to improve the remaining bottleneck caused by the select() implementation in an event-driven
server. Because the causes of the problem are more complex, this section starts by reviewing the use
and implementation of select() in order to understand the various sources of overhead.

Parameters
Select() is called as follows:
• Input: An application calls select() with three bitmaps (sets) of descriptors (one for descriptors it
  wishes to read from, one for those it wishes to write to, and one for those it wishes to hear exceptions
  from), a timeout value, and a parameter called nfds that is the highest-numbered file descriptor in

6 While the reader familiar with algorithms will immediately think of a heap, a better solution, which exploits typical computer
architectures, is explored in Exercise 3.

6.4 Scalable I/O Notification           161

any of the three sets plus 1. The purpose of nfds is to save the kernel time by restricting the scope of
  its search for the bits that have value 1 in the three bitmaps.
• Interim: The application is blocked if there is no descriptor ready.
• Output: When something of interest occurs, the call returns with number of ready descriptors (passed
  by value as an integer) and the specific lists of descriptors of each category (passed by reference, by
  overwriting input bitmaps).

Usage in a Web server
Having understood the parameters of the select() call, it is important to understand how select() could
be used by an event-driven Web server. A plausible use of select() is as follows (Banga and Mogul,
1998). The server application thread stays in a loop with three major components:
• Initialize: The application first zeroes out bitmaps and sets bits for descriptors of interest for read
  and write. For example, the server application may be interested in reading from file descriptors and
  writing and reading from network sockets open to clients.
• Call: The application then calls select() with bitmaps it built in the previous step, and it blocks if no
  descriptor is ready at the point of call; if a timeout occurs, the application does exception processing.
• Respond: After the call returns, the application linearly walks through returned bitmaps and invokes
  appropriate read and write handlers for descriptors corresponding to set bit positions.
    Note that the costs of building the bitmaps in Step 1 and scanning the bitmaps in Step 3 are charged
to the user, though they are directly attributable to the costs of preparing for and responding to a select()
call.
