# Network Algorithmics — 5.2.3 Fbufs: optimizing page remapping (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 146
- Slice: from `5.2.3 Fbufs: optimizing page remapping` up to next detected section heading

---

5.2.3 Fbufs: optimizing page remapping
Even ignoring the aspect of protecting against application writes, Fig. 5.4 implies that a large buffer can
be transferred from application to kernel (or vice versa) with a Write to the page table. This simplistic
view of page remapping is somewhat naive and misleading.
    Fig. 5.4 shows a concrete example of page remapping. Suppose the operating system wishes to
make a fast copy of data of Process 1 (say, the application) in VP 10 to some virtual page (e.g., VP 8)
in the page table of Process 2’s (say, the kernel). Naively, this seems to require only changing the page
table entry corresponding to VP 8 in Process 2 to point to the packet data to which that VP table entry
10 in Process 1 already points. However, there are several additional pieces of overhead that are glossed
over by this simple description.
• Multiple-level page tables: Most modern systems use multiple levels of page table mappings because
  it takes too much page table memory to map from, say, 20 bits of a VP. Thus the real mapping may
  require changing mappings in at least a first- and a second-level page table. For portability, there
  are also both machine-independent and machine-dependent tables. Thus there are several Writes
  involved, not just one.
• Acquiring locks and modifying page table entries: Page tables are shared resources and thus must
  be protected using locks that must be acquired and released.
• Flushing translation look-aside buffers (TLBs): As we said earlier, to save translation time, com-
  monly used page table mappings are cached in the TLB. When a new VP location for VP 8 is
  written, any TLB entries for VP 8 must be found and flushed (i.e., removed) or corrected.

120        Chapter 5 Copying data



• Allocating VM in destination domain: While we have assumed that VM location 8 was the location
  for the destination page, some computation must be done to find a free page table entry in the
  destination process before the copy can take place.
• Locking the corresponding pages: Physical pages can be swapped out to disk to make room for other
  VPs currently on disk. To prevent pages from being swapped out, pages have to be locked, which is
  additional overhead.
    All these overheads are exacerbated in multiprocessor and multicore systems. The net result is that
while the page table mapping can seem very good (the mapping seems to take a constant time, indepen-
dent of the size of the packet data), the constant factors (see Q4 in the discussion of caveats) are actually
a big overhead. This was experimentally demonstrated by experiments performed by Druschel and Pe-
terson (1993) in the early 1990s. In the decade that followed, if anything, page mapping overheads have
only increased.
    Druschel and Peterson, however, did not stop with the experiments but invented an operating system
facility called fbufs (short for “fast buffers”), which actually removes most or all of the four sources of
page remapping overhead. Their idea can be described as follows in terms of the principles used in this
book.

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



    To implement the fbuf idea the operating system could take some number of physical pages
P1 , . . . , Pk and premap them onto the page tables of the Ethernet driver, the TCP/IP code, and the
Web application. The same operation could be performed with a different set of physical pages for
Ethernet, OSI, and FTP. Thus we are using principle P2a to precompute mappings. Reserving physical
pages for each path could be wasteful because traffic is bursty; instead, a better idea is to lazily establish
(P2b) such mappings when a path becomes busy.
    Lazy establishment avoids the overheads of updating multiple levels of page tables, acquiring locks,
flushing TLBs, and allocating destination VM after the first few data packets arrive and are sent. Instead,
all this work is done once, when the transfer first starts. To make fbufs work, it is crucial that when a
packet arrives, the lowest-level driver (or even the adaptor itself) be able to quickly figure out what the
complete path the packet will be mapped to when receiving a packet from the network. This function,
called early demultiplexing, is described in detail in Chapter 8. Intuitively, in Fig. 5.5 this is done by
examining all the packet headers to determine (for instance) that a packet with an Ethernet, IP, and
HTTP header belongs to Path 1.
    The driver (or the adaptor) will then have a list of free buffers for that path, which will be used
by the adaptor to write the packet to; when the adaptor is done it will pass the buffer descriptor to the
next application in the path. Note that a buffer descriptor is only a pointer to a shared page, not the
page itself. When the last application in the path finishes with the page, it passes it back to the first
application in the path, where it again becomes a free buffer, and so on.
    At this point, the reader may wonder why paths are unidirectional. Paths are made unidirectional
because the first process on each path is assumed to be a writer and the remaining processes are as-
sumed to be readers. This can be enforced during the premapping by setting a write-allowed bit for
the first application in its page table entry, and a read-only bit in the page table entries of all the other
applications. Clearly, this is asymmetric in both directions and requires unidirectional paths. But this
does ensure some level of protection.
    This is shown in Fig. 5.6 with just two domains in a path. Note that the writer writes packets into
buffers described by a queue of free fbufs and then puts the written descriptor onto a queue of written
fbufs that are read by the next application (only one is shown in Fig. 5.6).

122        Chapter 5 Copying data




FIGURE 5.6
The single writer optimization.


    So far, it is possible that premapped page 8 in the first application on a path is mapped to page 10
in the second application. This is painful because when the second application reads a descriptor for
page 8, it must somehow know that it corresponds to its own VP 10. Instead, the designers used the
principle of avoiding unnecessary generality (P7) and insisted that the fbuf get mapped to the same VP
in all applications on the path. This can be done by reserving some number of initial pages in the VM
of all processes to be fbuf pages.
    At this point, we may feel that we are finished, but there are still a few thorny problems. To achieve
protection, we allowed only a single writer and had multiple readers. However, that means that pages
are immutable; only the writer can touch them. But what about adding headers when one goes down
the stack. The solution to this problem is shown in Fig. 5.7, where a packet is really an aggregate data
structure with pointers to individual fbufs so that headers can be added by adding an ordinary buffer or
an fbuf to the aggregate.
    This is not as big a deal as it sounds because the commonly used UNIX mbufs (see Chapter 9) are
also composites of buffers strung together.4
    So far, the fbuf scheme has used the underlying VM mapping ideas in Fig. 5.3 except that it has
made them more efficient by amortizing the mapping costs over (hopefully) a large number of packet
transfers. Page table updates are removed in the common case. This can be done in ordinary operating
systems. In fact, after the fbufs paper, Thadani and Khalidi (1995) extended the idea and implemented
it in Sun’s Solaris operating system. But this begs the question: How are standard copy semantics
preserved? What if the application does a Write? A standard operating system such as UNIX cannot
depend on COW as in Fig. 5.3.
    The ultimate answer in fbufs is that standard copy semantics are not preserved. The API is changed.
Application writers must be careful not to write to an fbuf when it has been handed to the kernel until
the fbuf is returned by the kernel in a free list. To protect against buggy or malicious code, the kernel


4 To be precise, UNIX mbufs are strung together in a linear topology, while buffer aggregates form a more general tree topology,
but the performance costs due to chaining and indexing are similar.

                                               5.2 Reducing copying via local restructuring           123




FIGURE 5.7
Using aggregate objects to allow adding layers to add headers while allowing only a single writer.



can briefly toggle the write-enable bit when an fbuf is transferred from the application to the kernel; the
bit is set again when the fbuf is given back. If the application does a Write when it does not have write
permission, an exception is generated and the application crashes, leaving other processes unaffected.
    Since the toggling of the write-enable bits requires some of the overhead that fbufs worked hard to
avoid, the fbuf facility also allows another form of fbufs, called volatile. Observe that if the writer is a
trusted entity (such as the kernel), then there is no point enforcing write protection. If the kernel has a
bug that causes it to make unexpected writes, the whole system will crash anyway.
    Changing the API in this way sounds dramatic. Does this mean that the huge amount of existing
UNIX application software (which uses the networking stack) must be rewritten? Since this is infea-
sible, there are several ways out. First, the existing API can be augmented with new system calls. For
example, the Solaris extensions in Thadani and Khalidi (1995) add a uf_write() call in addition to the
standard write() call. Applications interested in performance can be rewritten using these new calls.
    Second, the extensions can be used in implementing common I/O substrates (such as the UNIX
stdio library) that are a part of several applications. Applications that are linked to this library do not
need to be changed and yet can potentially benefit in performance.
    Eventually, the pragmatic consideration is not whether the API changes but how hard it is to modify
applications to benefit from the API changes. The experiences described in Thadani and Khalidi (1995)
and Pai et al. (1999b) for a number of applications indicate that the changes required in an application
to migrate to an fbuf-like API are small and localized.
