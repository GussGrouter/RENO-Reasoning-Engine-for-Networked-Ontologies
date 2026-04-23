Syscall Tracing
Syscalls are a great target for tracing and are the instrumentation source for many tracing tools.
However, some syscalls lack file system context, making them confusing to use. I’ll provide an
example of things working (openat(2) tracing) and not working (read(2) tracing), with suggested
remedies.

openat(2)
Tracing the open(2) family of syscalls shows files that are opened. Nowadays the openat(2)
variant is more commonly used.

(Omitted in this processed extract: bpftrace example run + `bpftrace -lv` struct dump — see PDF.)

This output caught the execution of sar(1) for archiving statistics, and the files it was opening.
bpftrace used the filename argument from the tracepoint; all arguments can be listed using -lv.

The arguments are the syscall number, file descriptor, filename, open flags, and open mode:
enough information for use by one-liners and tools, such as opensnoop(8).

read(2)
read(2) should be a useful tracing target for understanding file system read latency. However,
consider the tracepoint arguments: **only fd, buf, count**—no type bit for “file vs socket vs /proc.”

read(2) can be called for file systems, sockets, /proc, and other targets, and the arguments do not
differentiate between them.

(Omitted in this processed extract: example counts by process name — see PDF.)

While tracing, Java performed many read(2) syscalls, but are they from a file system, a socket, or
something else? (The sshd reads are probably socket I/O.)
What read(2) does provide is the file descriptor (FD) as an integer, but it is just a number and
does not show the FD type (and bpftrace is running in a restricted kernel mode: it can’t look up
FD information in /proc). There are at least four solutions to this:

Print the PID and FD from bpftrace, and later look up the FDs using lsof(8) or /proc to see
what they are.

A BPF helper (`get_fd_path()` in Gregg’s text as “upcoming”) can return the pathname for an FD.

Trace from VFS instead, where more data structures are available.

Trace file system functions directly, which exclude other I/O types—used by ext4dist(8) and ext4slower(8).

The following section on VFS Latency Tracing shows the VFS-based solution.
