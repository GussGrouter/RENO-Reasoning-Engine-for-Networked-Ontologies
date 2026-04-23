# network-algorithmics-5-2-3-fbufs-optimizing-page-remapping (chunk 000002)

Fbufs
The main idea in fbufs is to realize that if an application is sending a lot of data packets to the network
through the kernel, then a buffer will probably be reused multiple times, and thus the operating system
can precompute (P2a) all the page mapping information for the buffer ahead of time and then avoid
much of the page mapping overhead during the actual data transfer. Alternatively, the mappings can be
computed lazily (P2b) when the data transfer is first started (causing high overhead for the first few
received packets) but can be cached (P11a) for the subsequent packets. In this version page remapping
overheads are eliminated in the common case.
    The simplest way to do this would be to use what is called shared memory. Map a number of pages
P1 , . . . , Pn into the VM tables of the kernel as well as all sending applications A1 , . . . , Ak . However,
this is a bad idea, because we now can have (say) application A1 reading the packets sent by application
A2 .3 This would violate security and fault-isolation goals.
    A more secure notion would be to reserve (or lazily establish) mapped shared pages for each
application-to-kernel transfer and vice versa. For example, there could be one set of buffers (pages)
for FTP, one set for HTTP, and so on. More generally, some operating systems define multiple se-
curity subsystems besides kernel and application. Thus the fbuf designers call a path a sequence of
security domains. For our simple examples described earlier, it suffices to think of a path as either ker-
nel, application or application, kernel (e.g., FTP, kernel or kernel, HTTP). We will see why paths are
unidirectional—that is, why each application needs two paths in both directions—in a minute.
    Fig. 5.5 shows a more complex example of paths, where the Ethernet software is implemented as a
kernel-level driver, the TCP/IP stack is implemented as a user-level security domain, and, finally, the
Web application is implemented at the application layer. Each security domain has its own set of page
tables. The receiving paths are Ethernet, TCP/IP, Web and Ethernet, OSI, FTP.

3 It is worth knowing that the VM hardware normally enforces this security constraint by making sure that any accesses by A
                                                                                                                              2
can access only physical pages mapped into the page tables of A2 .

5.2 Reducing copying via local restructuring                    121

FIGURE 5.5
Premapping or lazily establishing buffer pages into the page tables of each domain in a path avoids the expense of
page remapping in the real-time path, after the initial setup.
