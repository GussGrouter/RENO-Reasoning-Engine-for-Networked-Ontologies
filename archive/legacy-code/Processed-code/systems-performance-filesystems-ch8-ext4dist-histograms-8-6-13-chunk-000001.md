8.6.13

ext4dist (xfs, zfs, btrfs, nfs)

ext4dist(8) is a BCC and bpftrace tool to instrument the ext4 file system and show the distribution of latencies as histograms for common operations: reads, writes, opens, and fsync. There are
versions for other file systems: xfsdist(8), zfsdist(8), btrfsdist(8), and nfsdist(8).

(Omitted in this processed extract: full ASCII histogram output — see PDF.)

Gregg interprets an example trace (10-second window): **bi-modal read latency**—one cluster near
0–15 μs (likely page-cache hits), another near 256–2048 μs (likely disk reads). Writes look fast due
to buffering; **fsync** carries the slower tail as data is flushed.

This tool and its companion ext4slower(8) (next section) show latencies that applications can
experience. Measuring latency down at the disk level is possible, and is shown in Chapter 9, but
the applications may not be blocking on disk I/O directly, making those measurements harder
to interpret. Where possible, I use the ext4dist(8)/ext4slower(8) tools first before disk I/O latency
tools. See Section 8.3.12 for differences between logical I/O to the file systems, as measured by
this tool, and physical I/O to the disks.

Options include **-m** (milliseconds), **-p PID**.

The output from this tool can be visualized as a latency heat map. For more information on slow
file system I/O, run ext4slower(8) and its variants.
