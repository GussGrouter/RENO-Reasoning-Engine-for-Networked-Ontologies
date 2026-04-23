8.4.6 Volumes and Pools
Historically, file systems were built upon a single disk or disk partition. Volumes and pools allow
file systems to be built upon multiple disks and can be configured using different RAID strategies
(see Chapter 9, Disks).

Figure 8.11 Volumes and pools
Volumes present multiple disks as one virtual disk, upon which the file system is built. When
built upon whole disks (and not slices or partitions), volumes isolate workloads, reducing performance issues of contention.

(PDF page break here carries a stray “8.5 Methodology” running header before the next paragraph;
content below continues §8.4.6.)

Volume management software includes the Logical Volume Manager (LVM) for Linux-based
systems. Volumes, or virtual disks, may also be provided by hardware RAID controllers.
Pooled storage includes multiple disks in a storage pool, from which multiple file systems can be
created. This is shown in Figure 8.11 with volumes for comparison. Pooled storage is more flexible than volume storage, as file systems can grow and shrink regardless of the backing devices.
This approach is used by modern file systems, including ZFS and btrfs, and is also possible using
LVM.
Pooled storage can use all disk devices for all file systems, improving performance. Workloads
are not isolated; in some cases, multiple pools may be used to separate workloads, given the
trade-off of some flexibility, as disk devices must be initially placed in one pool or another.
Note that pooled disks may be of different types and sizes, whereas volumes may be restricted to
uniform disks within a volume.
Additional performance considerations when using either software volume managers or pooled
storage include the following:
■

■

■

■

Stripe width: Matching this to the workload.
Observability: The virtual device utilization can be confusing; check the separate
physical devices.
CPU overhead: Especially when performing RAID parity computation. This has become
less of an issue with modern, faster CPUs. (Parity computation can also be offloaded to
hardware RAID controllers.)
Rebuilding: Also called resilvering, this is when an empty disk is added to a RAID group
(e.g., replacing a failed disk) and it is populated with the necessary data to join the group.
This can significantly affect performance as it consumes I/O resources and may last for
hours or even days.

Rebuilding is a worsening problem, as the capacity of storage devices increases faster than their
throughput, increasing rebuild time, and making the risk of a failure or medium errors during
rebuild greater. When possible, offline rebuilds of unmounted drives can improve rebuild times.
