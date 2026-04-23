# network-algorithmics-5-2-4-transparently-emulating-copy-semantics (chunk 000002)

linked together by a buffer aggregate, and the application programmer must deal with this new buffer
model chosen by the kernel.
    Thus a reasonable question is whether many of the benefits of fbufs can be realized without mod-
ifying the UNIX API. Theoretically, application software will continue to run, and one might get
performance without recoding applications.
    In a series of papers Brustoloni and Steenkiste (e.g., Ref. Brustoloni and Steenkiste, 1996) showed
that there is a clever mechanism, which they call TCOW (for transient copy-on-write), that makes
this possible. While preserving the API theoretically allows unmodified applications to enjoy better
performance, there is no experimental confirmation of this possibility. Thus in practice, it is likely that
applications have to be modified (perhaps in more intuitive ways) to take advantage of the underlying
kernel implementation changes. Nevertheless, the idea is simple and clever and worth pointing out.
    Recall that the standard API requires allowing an application to write or deallocate a buffer passed
to the kernel at any time. The fbuf design changes the API by making it illegal for an application to
do this. Instead, to preserve the API while doing only VM mappings, the operating system must deal
with these two potential threats, application writes and application deallocates, during the period the
buffer is being used by the kernel to send or retransmit a packet. In the Genie system (Brustoloni and
Steenkiste, 1996) VM mapping is used, as in fbufs, but these two threats are dealt with as follows.
   Countering Write Threats by Modifying the VM Fault Manager: First, when an application does a
Write, the buffer is marked specially, as Read Only. Thus if the application does a Write, the VM fault
manager is invoked. Normally, this should cause an exception. But, of course, if the OS is preserving
copy semantics, this should not be an error. Thus Genie modifies the exception handler as follows.
First, for each such page/buffer, Genie keeps track of whether there are outstanding sends (sends to
the network) using a simple counter that is incremented when the Send starts and decremented when
the Send completes. Second, the fault handler is modified to make a separate copy of the page for the
application (which incorporates the new Write) if there is an outstanding Send. Of course, this makes
performance suffer, but it does preserve the standard copy semantics of APIs such as UNIX. This
technique, called transient copy-on-write protection, is invoked only when needed—when the buffer is
also being read out by the network subsystem.
   Countering Deallocate Threats by Modifying the Pageout Daemon: In a standard VM system, there
is a process that is responsible for putting deallocated pages into a free list from which pages may be
written to disk. This pageout daemon can be modified not to deallocate a page when the page is being
used to send or receive packets.
    Interestingly these two ideas are both instances of principle P3c, shifting computation in space. The
work of checking for unexpected writes is moved to the VM fault handler, and the work of dealing with
deallocates is moved to the page deallocation routine.
    These two ideas are sufficient for sending a packet but not for receiving. On receiving, Genie needs
to depend, like fbufs, on hardware support5 in the adaptor to split a packet’s headers into one buffer and
the remaining data into a page-size buffer that can be swapped to the application’s buffer.

5 Hardware support for parsing in the adaptor is the simplest alternative proposed by the Genie system; there are a number of
more baroque mechanisms proposed as part of the Genie system to get around this hardware requirement, but they seem too
complicated and full of side effects to be useful in practice.

5.2 Reducing copying via local restructuring                        125
