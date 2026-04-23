# network-algorithmics-2-4-3-system-calls-io (chunk 000001)

# Network Algorithmics — operating systems: I/O via system calls (2.4.3) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 64 -l 81 -layout
- Slice: from `2.4.3 Simple I/O via system calls` up to (excluding) `2.5 Summary`

---

2.4.3 Simple I/O via system calls
Having an application programmer be aware of the variety and complexity of each I/O device would
be intolerable. Thus operating systems provide the programmer with the abstraction of the devices as a
piece of memory (Fig. 2.14) that can be read and written.
     The code that maps from a simple I/O interface call to the actual physical Read (with all parameters
filled in) to the device is called a device driver. If abstraction were the only concern, the device driver
code could be installed in a library of commonly available code that can be “checked out” by each
application. However, since devices such as disks must be shared by all applications, if applications
directly control the disk, an erroneous process could crash the disk. Instead, secure operating system
design requires that only the buggy application fail.
     Thus it makes sense for the I/O calls to be handled by device drivers that are in a secure portion of
the operating system that cannot be affected by buggy processes. This secure portion, called the kernel,
provides a core of essential services, including I/O and page table updates, that applications cannot be
trusted to perform directly.
     Thus when a browser such as Netscape wants to make a disk access to read a Web page, it must make
a so-called system call across the application–kernel boundary. System calls are a protected form of a
function call. The hardware instruction is said to “trap” to a more privileged level (kernel mode), which
allows access to operating system internals. When the function call returns after the I/O completes, the
application code runs at normal privilege levels. A system call is more expensive than a function call
because of the hardware privilege escalation and the extra sanitizing checks for incorrect parameter
values. A simple system call may take a few microseconds on modern machines.
     The relevance to networking is that when a browser wishes to send a message over the network (e.g.,
Process 2 in Fig. 2.14), it must do a system call to activate TCP processing. A few microseconds for
a system call may seem small, but it is really very high overhead on a fast Pentium. Can applications
speed up networking by bypassing the system call? If so, does OS protection get tossed out of the
window? Answers to these tantalizing questions are postponed to Chapter 6.

---

## PDF page 72
