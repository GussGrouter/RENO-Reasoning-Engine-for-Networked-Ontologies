# network-algorithmics-6-5-avoiding-system-calls-or-kernel-bypass (chunk 000002)

packet (for this application) should be written to. Thus we should consider carefully and separately
both descriptor memory as well as the actual buffer memory.
    We can deal with descriptor memory quite easily by recalling that the adaptor memory is memory
mapped. Suppose that the adaptor has 10,000 bytes of memory that is considered memory on the bus
and that the physical page size of the system is 1000 bytes. This means that the adaptor has 10 physical
pages. Suppose we allocate two physical pages to each of five high-performance applications (e.g.,
Web, FTP) that want to use the adaptor to transfer data. Suppose the Web application gets two physical
pages, 9 and 10. Then the kernel maps the physical pages 9 and 10 into the Web application’s page
table and the physical pages 3 and 4 into the FTP application’s page table.
    Now the Web application can write directly to physical pages 9 and 10 without any danger; if it
tries to write into pages 3 and 4, the virtual memory hardware will generate an exception. Thus we are
exploiting existing hardware (P4c) in the form of the TLB to protect access to pages. So now let us
assume that Page 10 is a sequence of free buffer descriptors written by the Web application; each buffer
descriptor describes a page of main memory (assume this can be done using just 32 bits) that will be
used to receive the next packet described for the Web application.
    For example, Page 10 could contain the sequence 18, 12 (see Fig. 6.8). This means that the Web
application has currently queued physical pages 18 and 12 for the next incoming packet and its succes-
sor. We assume that pages 18 and 12 are in main memory and are physically locked pages that were
assigned to the Web application by the kernel when the Web application first started.
    When a new packet arrives for the Web application, the adaptor will demultiplex the packet to the
descriptor Page 10 using a packet filter, and then it will write the data of the packet (using DMA (direct

168        Chapter 6 Transferring control
