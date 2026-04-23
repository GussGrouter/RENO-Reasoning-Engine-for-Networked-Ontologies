7.2.1 Virtual Memory
Virtual memory is an abstraction that provides each process and the kernel with its own large,
linear, and private address space. It simplifies software development, leaving physical memory
placement for the operating system to manage. It also supports multitasking (virtual address
spaces are separated by design) and oversubscription (in-use memory can extend beyond main
memory). Virtual memory was introduced in Chapter 3, Operating Systems, Section 3.2.8,
Virtual Memory. For historical background, see [Denning 70].
Figure 7.1 shows the role of virtual memory for a process, on a system with a swap device
(secondary storage). A page of memory is shown, as most virtual memory implementations are
page-based.

Figure 7.1 Process virtual memory
The process address space is mapped by the virtual memory subsystem to main memory and the
physical swap device. Pages of memory can be moved between them by the kernel as needed, a
process Linux calls swapping (and other OSes call anonymous paging). This allows the kernel to
oversubscribe main memory.
The kernel may impose a limit to oversubscription. A commonly used limit is the size of main
memory plus the physical swap devices. The kernel can fail allocations that try to exceed this
limit. Such “out of virtual memory” errors can be confusing at first glance, since virtual memory
itself is an abstract resource.
Linux also allows other behaviors, including placing no bounds on memory allocation. This is
termed overcommit and is described after the following sections on paging and demand paging,
which are necessary for overcommit to work.
