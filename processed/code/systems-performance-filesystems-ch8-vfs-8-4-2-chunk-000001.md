8.4.2

Architecture

VFS

VFS (the virtual file system interface) provides a common interface for different file system
types. Its location is shown in Figure 8.7.

Figure 8.7 Virtual file system interface
VFS originated in SunOS and has become the standard abstraction for file systems.
The terminology used by the Linux VFS interface can be a little confusing, since it reuses the
terms inodes and superblocks to refer to VFS objects—terms that originated from Unix file system
on-disk data structures. The terms used for Linux on-disk data structures are usually prefixed
with their file system type, for example, ext4_inode and ext4_super_block. The VFS inodes and
VFS superblocks are in memory only.
The VFS interface can also serve as a common location for measuring the performance of any
file system. Doing this may be possible using operating system–supplied statistics, or static or
dynamic instrumentation.

