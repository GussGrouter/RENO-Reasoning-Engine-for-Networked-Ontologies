8.4

Architecture

This section introduces generic and specific file system architecture, beginning with the I/O
stack, VFS, file system caches and features, common file system types, volumes, and pools. Such
background is useful when determining which file system components to analyze and tune.
For deeper internals and other file system topics, refer to source code, if available, and external
documentation. Some of these are listed at the end of this chapter.

8.4.1

File System I/O Stack

Figure 8.6 depicts a general model of the file system I/O stack, focusing on the file system interface. Specific components, layers, and APIs depend on the operating system type, version, and
file systems used. A higher-level I/O stack figure is included in Chapter 3, Operating Systems,
and another showing the disk components in more detail is in Chapter 9, Disks.

Figure 8.6 Generic file system I/O stack
This shows the path of I/O from applications and system libraries to syscalls and through the
kernel. The path from system calls directly to the disk device subsystem is raw I/O. The path via
VFS and the file system is file system I/O, including direct I/O, which skips the file system cache.

8.4

