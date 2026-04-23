# network-algorithmics-6-4-3-analysis-of-select (chunk 000001)

# Network Algorithmics — 6.4.3 Analysis of select() (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 189
- Slice: from `6.4.3 Analysis of select()` up to next detected section heading

---

6.4.3 Analysis of select()
We start by describing opportunities for optimization in the existing select() implementation and then
use our principles to suggest strategies to improve performance.

Obvious waste in select() implementation
Principle P1 seeks to remove obvious waste. In order to apply Principle P1, it helps to catalog the
sources of “obvious waste” in the select() implementations. With each source of waste, we also attach
a scapegoat that can be blamed for the waste.
1. Recreating interest on each call: The same bitmap is used for input and output. This overloading
   causes the application to rebuild the bitmaps from scratch, though it maybe interested in most of the
   same descriptors across consecutive calls to select(). For example, if only 10 bits change in a bitmap
   of size 6000 on each call, the application still has to walk through 6000 bits, to set each if needed.
   Blame this on either the interface (API) or on the lack of incremental computing in the
   application.
2. Rechecking state after resume: No information is passed from a protocol module (that wakes up a
   thread sleeping on a socket) to the select() call that is invoked when the thread resumes. For example,
   if the TCP module receives data on socket 9, on which thread 1 is sleeping, the TCP module will
   ensure that thread 1 is woken up. However, no information is passed to thread 1 as to who woke up
   thread 1; thus thread 1 must again check all selected sockets to determine that socket 9 indeed has
   data. Clearly, the TCP module knew this when it woke up thread 1.
   Blame the kernel implementation.
3. Kernel rechecks readiness for descriptors known not to be ready: The Web server application is
   typically interested in a socket until connection failure or termination. In that case, why repeat
   tests for readiness if no change in state has been observed? For example, assume that socket 9 is a
   connection to a remote client with a delay of 1 second to send and receive network packets. Assume
   that at time t, a request is sent to the client on socket 9 and the server is waiting for a response,
   which arrives at t + 1 seconds. Assume that in the interval from t to t + 1, the server thread calls
   select() 15,000 times. Each time select() is called the kernel makes an expensive check of socket 9
   to determine that no data has arrived. Instead, the kernel can infer this from the fact that the socket
   was checked at time t and no network packet has been received for this socket since time t. Thus
   15,000 expensive and useless checks can be avoided; when the packet finally arrives at time t + 1,
   the TCP module can pass information to reinstate checking of this socket.
   Blame the kernel implementation.

6.4 Scalable I/O Notification         163

4. Bitmaps linear with descriptor size: Both kernel and user have to scan bitmaps proportional to the
   size of possible descriptors, not to the amount of useful work returned. For example, if there are
   6000 possible descriptors a Web server may have to deal with at peak load, the bitmaps are of length
   6000. Suppose during some period there are 100 concurrent clients, of which only 10 are ready
   during each call to select(). Both kernel and application are scanning and copying bitmaps of size
   6000, though the application is only interested in 200 bits and only 10 bits are set when each select()
   returns.
   Blame the API.
