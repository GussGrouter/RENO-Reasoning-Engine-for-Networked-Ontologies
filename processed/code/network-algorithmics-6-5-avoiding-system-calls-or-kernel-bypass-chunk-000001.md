# network-algorithmics-6-5-avoiding-system-calls-or-kernel-bypass (chunk 000001)

# Network Algorithmics — 6.5 Avoiding system calls or Kernel Bypass (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 193
- Slice: from `6.5 Avoiding system calls or Kernel Bypass` up to next detected section heading

---

6.5 Avoiding system calls or Kernel Bypass
For now, forget about the intervening discussion of select() and recall the discussion of user-level net-
working. We seem to have gotten the kernel out of the picture on the receipt or sending of a packet,
but sadly that is not quite the case. When an application wants to send data, it must somehow tell the
adaptor where the data is.
    When the application wants to receive data, it must specify buffers where the received packet data
should be written to. Today, in UNIX this is typically done using system calls, where the application
tells the kernel about data it wishes to send and buffers it wishes to receive to. Even if we implement
the protocol in user space, the kernel must service these system calls (which can be expensive; see
Chapter 2) for every packet sent and received.
    This appears to be required because there can be several applications sending and receiving data
from a common adaptor; since the adaptor is a shared resource, it seems unthinkable for an application
to write directly to the device registers of a network adaptor without kernel mediation to check for
malicious or erroneous use. Or is it?
    A simple analogy suggests that alternatives may be possible. In Fig. 6.7 we see that when an appli-
cation wants to set the value of a variable X equal to 10, it does not actually make a call to the kernel.
If this were the case, every read and write in a program would be slowed down very badly. Instead, the
hardware determines the virtual page of X, translates it to a physical page (say, 10) via the TLB, and
then allows direct access as long as the application has Page 10 mapped into its virtual memory.
    If Page 10 is not mapped into the application’s virtual memory, the hardware generates an exception
and causes the kernel to intervene to determine why there is a page access violation. Notice that the
kernel was involved in setting up the virtual memory for the application (only the kernel should be
allowed to do so, for reasons of security) and may be involved if the application violates its page
accesses that the kernel set up. However, the kernel is not involved in every access. Could we hope for
a similar approach for application access to adaptor memory to avoid wasted system calls (P1)?
    To see if this is possible, we need to examine more carefully what information an application sends
and receives from an adaptor. Clearly, we must prevent incorrect or malicious applications from dam-
aging other applications or the kernel itself. Fig. 6.8 shows an application that wishes to receive data
directly from the adaptor. Typically, an application that does so must queue a descriptor. A descriptor
is a small piece of information that describes the buffer in main memory where the data for the next

6.5 Avoiding system calls or Kernel Bypass           167

FIGURE 6.7
Reading and writing to memory is not mediated by the kernel.

FIGURE 6.8
Application device channels.
