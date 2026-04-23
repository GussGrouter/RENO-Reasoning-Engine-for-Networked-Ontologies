4.3.2

/sys

Linux provides a sysfs file system, mounted on /sys, which was introduced with the 2.6 kernel
to provide a directory-based structure for kernel statistics. This differs from /proc, which has
evolved over time and had various system statistics mostly added to the top-level directory. sysfs
was originally designed to provide device driver statistics but has been extended to include any
statistic type.

143

144

Chapter 4 Observability Tools

For example, the following lists /sys files for CPU 0 (truncated):
$ find /sys/devices/system/cpu/cpu0 -type f
/sys/devices/system/cpu/cpu0/uevent
/sys/devices/system/cpu/cpu0/hotplug/target
/sys/devices/system/cpu/cpu0/hotplug/state
/sys/devices/system/cpu/cpu0/hotplug/fail
/sys/devices/system/cpu/cpu0/crash_notes_size
/sys/devices/system/cpu/cpu0/power/runtime_active_time
/sys/devices/system/cpu/cpu0/power/runtime_active_kids
/sys/devices/system/cpu/cpu0/power/pm_qos_resume_latency_us
/sys/devices/system/cpu/cpu0/power/runtime_usage
[...]
/sys/devices/system/cpu/cpu0/topology/die_id
/sys/devices/system/cpu/cpu0/topology/physical_package_id
/sys/devices/system/cpu/cpu0/topology/core_cpus_list
/sys/devices/system/cpu/cpu0/topology/die_cpus_list
/sys/devices/system/cpu/cpu0/topology/core_siblings
[...]

Many of the listed files provide information about the CPU hardware caches. The following output shows their contents (using grep(1) so that the file name is included with the output):
$ grep . /sys/devices/system/cpu/cpu0/cache/index*/level
/sys/devices/system/cpu/cpu0/cache/index0/level:1
/sys/devices/system/cpu/cpu0/cache/index1/level:1
/sys/devices/system/cpu/cpu0/cache/index2/level:2
/sys/devices/system/cpu/cpu0/cache/index3/level:3
$ grep . /sys/devices/system/cpu/cpu0/cache/index*/size
/sys/devices/system/cpu/cpu0/cache/index0/size:32K
/sys/devices/system/cpu/cpu0/cache/index1/size:32K
/sys/devices/system/cpu/cpu0/cache/index2/size:1024K
/sys/devices/system/cpu/cpu0/cache/index3/size:33792K

This shows that CPU 0 has access to two Level 1 caches, each 32 Kbytes, a Level 2 cache of 1
Mbyte, and a Level 3 cache of 33 Mbytes.
The /sys file system typically has tens of thousands of statistics in read-only files, as well as
many writeable files for changing kernel state. For example, CPUs can be set to online or offline
by writing “1” or “0” to a file named “online.” As with reading statistics, some state settings can
be made by using text strings at the command line (echo 1 > filename), rather than a binary
interface.

4.3 Observability Sources

