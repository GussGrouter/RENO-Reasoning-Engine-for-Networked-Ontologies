7.4.2

USE Method

The USE method is for identifying bottlenecks and errors across all components early in a performance investigation, before deeper and more time-consuming strategies are followed.
Check system-wide for:
■

■

■

Utilization: How much memory is in use, and how much is available. Both physical
memory and virtual memory should be checked.
Saturation: The degree of page scanning, paging, swapping, and Linux OOM killer
sacrifices performed, as measures to relieve memory pressure.
Errors: Software or hardware errors.

You may want to check saturation first, as continual saturation is a sign of a memory issue. These
metrics are usually readily available from operating system tools, including vmstat(8) and sar(1)
for swapping statistics, and dmesg(1) for OOM killer sacrifices. For systems configured with a
separate disk swap device, any activity to the swap device is another a sign of memory pressure.
Linux also provides memory saturation statistics as part of pressure stall information (PSI).
Physical memory utilization can be reported differently by different tools, depending on
whether they account for unreferenced file system cache pages or inactive pages. A system may
report that it has only 10 Mbytes of available memory when it actually has 10 Gbytes of file
system cache that can be reclaimed by applications immediately when needed. Check the tool
documentation to see what is included.
Virtual memory utilization may also need to be checked, depending on whether the system performs overcommit. For systems that do not, memory allocations will fail once virtual memory is
exhausted—a type of memory error.
Memory errors can be caused by software, such as failed memory allocations or the Linux OOM
killer, or by hardware, such as ECC errors. Historically, memory allocation errors have been left
for the applications to report, although not all applications do (and, with Linux overcommit,
developers may not have felt it necessary). Hardware errors are also difficult to diagnose. Some
tools can report ECC-correctable errors (e.g., on Linux, dmidecode(8), edac-utils, ipmitool sel)
when ECC memory is used. These correctable errors can be used as a USE method error metric,
and can be a sign that uncorrectable errors may soon occur. With actual (uncorrectable)

7.4

Methodology

memory errors, you may experience unexplained, unreproducible crashes (including segfaults
and bus error signals) of arbitrary applications.
For environments that implement memory limits or quotas (resource controls), as in some cloud
computing environments, memory utilization and saturation may need to be measured differently. Your OS instance may be at its software memory limit and swapping, even though there is
plenty of physical memory available on the host. See Chapter 11, Cloud Computing.

