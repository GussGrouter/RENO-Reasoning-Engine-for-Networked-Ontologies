8.6.15

bpftrace

bpftrace is a BPF-based tracer that provides a high-level programming language, allowing the
creation of powerful one-liners and short scripts. It is well suited for custom file system analysis
based on clues from other tools.
bpftrace is explained in Chapter 15, BPF. This section shows some examples for file system
analysis: one-liners, syscall tracing, VFS tracing, and file system internals.

One-Liners
The following one-liners are useful and demonstrate different bpftrace capabilities.

Trace files opened via openat(2) with process name (printf comm + filename).

Count read syscalls by syscall variant (`sys_enter_*read*`).

Count write syscalls by syscall variant (`sys_enter_*write*`).

Histogram read() **request sizes** (`sys_enter_read`, `args->count`).

Histogram read() **returned bytes** on exit (`sys_exit_read`, `args->ret`).

Count read() errors by errno (`sys_exit_read` filter ret < 0).

Count VFS calls (`kprobe:vfs_*`), optionally filtered by PID.

Count ext4 / xfs tracepoint families.

Count ext4 file reads by **user stack + comm** (`kprobe:ext4_file_read_iter`).

Trace ZFS `spa_sync()` entry times (`kprobe:spa_sync`).

Count dcache references via `lookup_fast` by comm+pid.

(Full verbatim one-liners: see PDF / Chapter 15.)
