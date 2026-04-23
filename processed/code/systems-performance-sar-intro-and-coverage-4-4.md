<!-- Extracted from systems-performance-ch4-scout-p171-220.txt (book PDF region ~171–220) -->

■

module: This usually refers to the kernel module that created the statistic, such as sd for
the SCSI disk driver, or zfs for the ZFS file system.
instance: Some modules exist as multiple instances, such as an sd module for each SCSI
disk. The instance is an enumeration.

■

name: This is a name for the group of statistics.

■

statistic: This is the individual statistic name.

Kstats are accessed using a binary kernel interface, and various libraries exist.
As an example Kstat, the following reads the “nproc” statistic using kstat(1M) and specifying the
full four-tuple:
$ kstat -p unix:0:system_misc:nproc
unix:0:system_misc:nproc

94

This statistic shows the currently running number of processes.
In comparison, the /proc/stat-style sources on Linux have inconsistent formatting and usually
