VFS Tracing
As the virtual file system (VFS) abstracts all file systems (and other devices), tracing its calls provides a single point from which to observe all file systems.

VFS Counts
Counting VFS calls provides a high-level overview of the operation types in use. Example:
`bpftrace -e 'kprobe:vfs_* { @[func] = count(); }'` attaches many probes and prints counts per
`vfs_*` function (book example includes thousands of `vfs_read` calls in the window).

VFS Latency
As with syscalls, VFS reads can be for file systems, sockets, and other targets. The book’s
`vfsreadlat.bt` program uses the **superblock `s_type->name`** (e.g. `ext4`, `sockfs`, `proc`) to
**split** `vfs_read()` latency histograms by backing “type,” surfacing that a single `vfs_read` path
serves multiple classes of object.

(Omitted in this processed extract: full per-type ASCII histograms and the full bpftrace source
listing — see PDF.)

The output (truncated in the book) also included latency histograms for sysfs, devpts, pipefs,
devtmpfs, tmpfs, and anon_inodefs.

You can extend this tool to include other operations, such as vfs_readv(), vfs_write(), vfs_
writev(), etc. To understand this code, begin with Section 15.2.4, Programming, which explains
the basics of timing vfs_read().
Note that this latency may or may not directly affect application performance, as mentioned
in Section 8.3.1, File System Latency. It depends on whether the latency is encountered during
an application request, or if it occurs during an asynchronous background task. To answer this,
you can include the user stack trace (ustack) as an additional histogram key, which may reveal
whether or not the vfs_read() call took place during an application request.

File System Internals
If needed, you can develop custom tools that show the behavior of file system internals. Start by
trying the tracepoints, if available.

(Omitted in this processed extract: long `bpftrace -l tracepoint:ext4:*` and `bpftrace -lv kprobe:ext4_*`
listings — see PDF.)

Each of these has arguments that can be listed using -lv. If the tracepoints are insufficient (or
not available for your file system type), consider using dynamic instrumentation with kprobes.

In this kernel version (5.3) there are 105 ext4 tracepoints and 538 possible ext4 kprobes.
