<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs) -->

6.5.2

USE Method

The USE method can be used to identify bottlenecks and errors across all components early in a
performance investigation, before trying deeper and more time-consuming strategies.
For each CPU, check for:
■

Utilization: The time the CPU was busy (not in the idle thread)

■

Saturation: The degree to which runnable threads are queued waiting their turn on-CPU

■

Errors: CPU errors, including correctable errors

245

246

Chapter 6 CPUs

You can check errors first since they are typically quick to check and the easiest to interpret. Some
processors and operating systems will sense an increase in correctable errors (error-correction
code, ECC) and will offline a CPU as a precaution, before an uncorrectable error causes a CPU
failure. Checking for these errors can be a matter of checking that all CPUs are still online.
Utilization is usually readily available from operating system tools as percent busy. This metric
should be examined per CPU, to check for scalability issues. High CPU and core utilization can
be understood by using profiling and cycle analysis.
For environments that implement CPU limits or quotas (resource controls; e.g., Linux tasksets
and cgroups), as is common in cloud computing environments, CPU utilization should be measured in terms of the imposed limit, in addition to the physical limit. Your system may exhaust
its CPU quota well before the physical CPUs reach 100% utilization, encountering saturation
earlier than expected.
Saturation metrics are commonly provided system-wide, including as part of load averages. This
metric quantifies the degree to which the CPUs are overloaded, or a CPU quota, if present, is
used up.
You can follow a similar process for checking the health of GPUs and other accelerators, if in use,
depending on available metrics.

