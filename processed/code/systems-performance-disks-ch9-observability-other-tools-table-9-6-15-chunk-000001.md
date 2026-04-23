9.6.15       Other Tools
Disk tools included in other chapters of this book and in BPF Performance Tools [Gregg 19] are
listed in Table 9.6.


Table 9.6     Other disk observability tools
Section          Tool             Description
7.5.1            vmstat           Virtual memory statistics including swapping
7.5.3            swapon           Swap device usage
[Gregg 19]       seeksize         Show requested I/O seek distances
[Gregg 19]       biopattern       Identify random/sequential disk access patterns
[Gregg 19]       bioerr           Trace disk errors
[Gregg 19]       mdflush          Trace md flush requests
[Gregg 19]       iosched          Summarize I/O scheduler latency
[Gregg 19]       scsilatency      Show SCSI command latency distributions
[Gregg 19]       scsiresult       Show SCSI command result codes
[Gregg 19]       nvmelatency      Summarize NVME driver command latency



Other Linux disk observability tools and sources include the following:

    ■   /proc/diskstats: High-level per-disk statistics
    ■   seekwatcher: Visualizes disk access patterns [Mason 08]

The disks vendors may have additional tools that access firmware statistics, or by installing a
debug version of the firmware.


