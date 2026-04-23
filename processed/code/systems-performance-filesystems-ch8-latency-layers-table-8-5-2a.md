8.5.2 Latency Analysis (continued)

operation latency = time (operation completion) - time (operation request)

These times can be measured from one of four layers, summarized in Table 8.4 in the book/PDF.

**Application** — Closest measure of end-user effect of file system latency; can determine whether latency occurs on the application’s primary path or asynchronously. Technique varies between applications and versions.

**Syscall interface** — Well-documented; commonly observable via operating system tools and static tracing. Syscalls cover all file system types, including non-storage file systems (statistics, sockets), which can be confusing unless filtered. Multiple syscalls may implement the same logical file operation (e.g., read(2), pread64(2), preadv(2), preadv2(2)); each variant may need to be measured.

**VFS** — Standard interface for file system operations (e.g., vfs_write()); one logical call site per operation type. Traces all file system types, including non-storage types, unless filtered.

**Top of file system** — Targets the storage file system type being analyzed; may expose internal FS context. Specific to each implementation and often version-sensitive (though some stacks expose a stable internal interface mapped from VFS).

(Omitted in this processed extract: the original Table 8.4 Pros/Cons grid — see PDF.)
